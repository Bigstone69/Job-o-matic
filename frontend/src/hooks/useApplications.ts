/**
 * React Query hooks for application-related data fetching.
 *
 * Provides hooks for managing applications with caching and optimistic updates.
 */

import { useQuery, useMutation, useQueryClient, UseQueryOptions } from '@tanstack/react-query'
import {
  createApplication,
  listApplications,
  getApplicationStats,
  getApplication,
  updateApplication,
  updateApplicationStatus,
  deleteApplication,
  getApplicationHistory,
} from '../api/applications.api'
import {
  Application,
  ApplicationDetail,
  CreateApplicationRequest,
  UpdateApplicationRequest,
  UpdateStatusRequest,
  ApplicationStats,
  ApplicationListParams,
  StatusHistory,
} from '../types/application.types'

// Helper to create stable cache keys
const serializeKey = (obj: any): string => {
  if (!obj) return ''
  const sorted = Object.keys(obj)
    .sort()
    .reduce((result: any, key: string) => {
      const value = obj[key]
      if (value !== undefined && value !== null) {
        result[key] = Array.isArray(value) ? [...value].sort() : value
      }
      return result
    }, {})
  return JSON.stringify(sorted)
}

// Query keys for cache management
export const applicationKeys = {
  all: ['applications'] as const,
  lists: () => [...applicationKeys.all, 'list'] as const,
  list: (params?: ApplicationListParams) => [...applicationKeys.lists(), serializeKey(params)] as const,
  details: () => [...applicationKeys.all, 'detail'] as const,
  detail: (id: number) => [...applicationKeys.details(), id] as const,
  stats: () => [...applicationKeys.all, 'stats'] as const,
  history: (id: number) => [...applicationKeys.all, 'history', id] as const,
}

/**
 * Hook for listing applications with filters.
 */
export const useApplicationList = (
  params?: ApplicationListParams,
  options?: Omit<UseQueryOptions<Application[], Error>, 'queryKey' | 'queryFn'>
) => {
  return useQuery<Application[], Error>({
    queryKey: applicationKeys.list(params),
    queryFn: () => listApplications(params),
    staleTime: 2 * 60 * 1000, // 2 minutes
    ...options,
  })
}

/**
 * Hook for getting application statistics.
 */
export const useApplicationStats = (
  options?: Omit<UseQueryOptions<ApplicationStats, Error>, 'queryKey' | 'queryFn'>
) => {
  return useQuery<ApplicationStats, Error>({
    queryKey: applicationKeys.stats(),
    queryFn: getApplicationStats,
    staleTime: 1 * 60 * 1000, // 1 minute
    ...options,
  })
}

/**
 * Hook for getting detailed application information.
 */
export const useApplication = (
  applicationId: number,
  options?: Omit<UseQueryOptions<ApplicationDetail, Error>, 'queryKey' | 'queryFn'>
) => {
  return useQuery<ApplicationDetail, Error>({
    queryKey: applicationKeys.detail(applicationId),
    queryFn: () => getApplication(applicationId),
    enabled: Boolean(applicationId),
    staleTime: 5 * 60 * 1000, // 5 minutes
    ...options,
  })
}

/**
 * Hook for getting application status history.
 */
export const useApplicationHistory = (
  applicationId: number,
  options?: Omit<UseQueryOptions<StatusHistory[], Error>, 'queryKey' | 'queryFn'>
) => {
  return useQuery<StatusHistory[], Error>({
    queryKey: applicationKeys.history(applicationId),
    queryFn: () => getApplicationHistory(applicationId),
    enabled: Boolean(applicationId),
    staleTime: 5 * 60 * 1000, // 5 minutes
    ...options,
  })
}

/**
 * Hook for creating applications.
 */
export const useCreateApplication = () => {
  const queryClient = useQueryClient()

  return useMutation<ApplicationDetail, Error, CreateApplicationRequest>({
    mutationFn: createApplication,
    onSuccess: () => {
      // Invalidate lists and stats
      queryClient.invalidateQueries({ queryKey: applicationKeys.lists() })
      queryClient.invalidateQueries({ queryKey: applicationKeys.stats() })
    },
    onError: (error) => {
      console.error('Failed to create application:', error)
    },
  })
}

/**
 * Hook for updating applications.
 */
export const useUpdateApplication = () => {
  const queryClient = useQueryClient()

  return useMutation<
    ApplicationDetail,
    Error,
    { applicationId: number; request: UpdateApplicationRequest }
  >({
    mutationFn: ({ applicationId, request }) => updateApplication(applicationId, request),
    onSuccess: (data) => {
      // Update detail cache
      queryClient.setQueryData(applicationKeys.detail(data.id), data)
      // Invalidate lists
      queryClient.invalidateQueries({ queryKey: applicationKeys.lists() })
    },
    onError: (error) => {
      console.error('Failed to update application:', error)
    },
  })
}

/**
 * Hook for updating application status with optimistic updates.
 */
export const useUpdateStatus = () => {
  const queryClient = useQueryClient()

  return useMutation<
    ApplicationDetail,
    Error,
    { applicationId: number; request: UpdateStatusRequest },
    { previousApp: ApplicationDetail | undefined }
  >({
    mutationFn: ({ applicationId, request }) =>
      updateApplicationStatus(applicationId, request),
    onMutate: async ({ applicationId, request }) => {
      // Cancel outgoing refetches
      await queryClient.cancelQueries({ queryKey: applicationKeys.detail(applicationId) })

      // Snapshot previous value
      const previousApp = queryClient.getQueryData<ApplicationDetail>(
        applicationKeys.detail(applicationId)
      )

      // Optimistically update
      if (previousApp) {
        queryClient.setQueryData<ApplicationDetail>(
          applicationKeys.detail(applicationId),
          {
            ...previousApp,
            status: request.status,
          }
        )
      }

      return { previousApp }
    },
    onError: (error, { applicationId }, context) => {
      // Rollback on error
      if (context?.previousApp) {
        queryClient.setQueryData(
          applicationKeys.detail(applicationId),
          context.previousApp
        )
      }
      console.error('Failed to update status:', error)
    },
    onSuccess: (data) => {
      // Update caches
      queryClient.setQueryData(applicationKeys.detail(data.id), data)
      queryClient.invalidateQueries({ queryKey: applicationKeys.lists() })
      queryClient.invalidateQueries({ queryKey: applicationKeys.stats() })
      queryClient.invalidateQueries({ queryKey: applicationKeys.history(data.id) })
    },
  })
}

/**
 * Hook for deleting applications.
 */
export const useDeleteApplication = () => {
  const queryClient = useQueryClient()

  return useMutation<void, Error, number>({
    mutationFn: deleteApplication,
    onSuccess: () => {
      // Invalidate all application queries
      queryClient.invalidateQueries({ queryKey: applicationKeys.all })
    },
    onError: (error) => {
      console.error('Failed to delete application:', error)
    },
  })
}
