/**
 * React Query hooks for job-related data fetching.
 *
 * Provides hooks for searching, listing, and managing jobs with caching.
 */

import { useQuery, useMutation, useQueryClient, UseQueryOptions } from '@tanstack/react-query'
import {
  searchJobs,
  listJobs,
  getJob,
  createManualJob,
  deleteJob,
} from '../api/jobs.api'
import {
  Job,
  JobDetail,
  JobSearchRequest,
  JobSearchResponse,
  CreateManualJobRequest,
  JobListParams,
} from '../types/job.types'

// Helper to create stable cache keys from objects
const serializeKey = (obj: any): string => {
  if (!obj) return ''
  // Sort keys to ensure stable serialization
  const sorted = Object.keys(obj)
    .sort()
    .reduce((result: any, key: string) => {
      const value = obj[key]
      if (value !== undefined && value !== null) {
        // Create shallow copy of arrays before sorting to avoid mutation
        result[key] = Array.isArray(value) ? [...value].sort() : value
      }
      return result
    }, {})
  return JSON.stringify(sorted)
}

// Query keys for cache management
export const jobKeys = {
  all: ['jobs'] as const,
  lists: () => [...jobKeys.all, 'list'] as const,
  list: (params?: JobListParams) => [...jobKeys.lists(), serializeKey(params)] as const,
  searches: () => [...jobKeys.all, 'search'] as const,
  search: (request: JobSearchRequest) => [...jobKeys.searches(), serializeKey(request)] as const,
  details: () => [...jobKeys.all, 'detail'] as const,
  detail: (id: number) => [...jobKeys.details(), id] as const,
}

/**
 * Hook for searching jobs across multiple platforms.
 *
 * @param request - Search parameters
 * @param options - React Query options
 */
export const useJobSearch = (
  request: JobSearchRequest,
  options?: Omit<UseQueryOptions<JobSearchResponse, Error>, 'queryKey' | 'queryFn'>
) => {
  return useQuery<JobSearchResponse, Error>({
    queryKey: jobKeys.search(request),
    queryFn: () => searchJobs(request),
    // Only run query when query and location are provided
    enabled: Boolean(request.query && request.location),
    // Cache for 5 minutes
    staleTime: 5 * 60 * 1000,
    ...options,
  })
}

/**
 * Hook for listing saved jobs with filters.
 *
 * @param params - Filter parameters
 * @param options - React Query options
 */
export const useJobList = (
  params?: JobListParams,
  options?: Omit<UseQueryOptions<Job[], Error>, 'queryKey' | 'queryFn'>
) => {
  return useQuery<Job[], Error>({
    queryKey: jobKeys.list(params),
    queryFn: () => listJobs(params),
    // Cache for 2 minutes
    staleTime: 2 * 60 * 1000,
    ...options,
  })
}

/**
 * Hook for getting detailed job information.
 *
 * @param jobId - Job ID
 * @param options - React Query options
 */
export const useJob = (
  jobId: number,
  options?: Omit<UseQueryOptions<JobDetail, Error>, 'queryKey' | 'queryFn'>
) => {
  return useQuery<JobDetail, Error>({
    queryKey: jobKeys.detail(jobId),
    queryFn: () => getJob(jobId),
    enabled: Boolean(jobId),
    // Cache for 5 minutes
    staleTime: 5 * 60 * 1000,
    ...options,
  })
}

/**
 * Hook for creating manual job entries.
 */
export const useCreateJob = () => {
  const queryClient = useQueryClient()

  return useMutation<JobDetail, Error, CreateManualJobRequest>({
    mutationFn: createManualJob,
    onSuccess: () => {
      // Invalidate job lists to refetch with new job
      queryClient.invalidateQueries({ queryKey: jobKeys.lists() })
    },
    onError: (error) => {
      console.error('Failed to create job:', error)
    },
  })
}

/**
 * Hook for deleting jobs.
 */
export const useDeleteJob = () => {
  const queryClient = useQueryClient()

  return useMutation<void, Error, number>({
    mutationFn: deleteJob,
    onSuccess: () => {
      // Invalidate all job queries to refetch
      queryClient.invalidateQueries({ queryKey: jobKeys.all })
    },
    onError: (error) => {
      console.error('Failed to delete job:', error)
    },
  })
}

/**
 * Hook for manually triggering job search.
 * Useful for search forms where you want to control when the search runs.
 */
export const useJobSearchMutation = () => {
  const queryClient = useQueryClient()

  return useMutation<JobSearchResponse, Error, JobSearchRequest>({
    mutationFn: searchJobs,
    onSuccess: (data, request) => {
      // Cache the search results
      queryClient.setQueryData(jobKeys.search(request), data)
    },
    onError: (error) => {
      console.error('Job search failed:', error)
    },
  })
}
