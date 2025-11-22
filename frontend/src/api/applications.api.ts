/**
 * Application API service.
 *
 * Provides methods for interacting with application-related endpoints.
 */

import apiClient from './client'
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

/**
 * Create a new application.
 */
export const createApplication = async (
  request: CreateApplicationRequest
): Promise<ApplicationDetail> => {
  const response = await apiClient.post<ApplicationDetail>(
    '/api/v1/applications',
    request
  )
  return response.data
}

/**
 * List applications with optional filters.
 */
export const listApplications = async (
  params?: ApplicationListParams
): Promise<Application[]> => {
  const response = await apiClient.get<Application[]>('/api/v1/applications', {
    params,
  })
  return response.data
}

/**
 * Get application statistics.
 */
export const getApplicationStats = async (): Promise<ApplicationStats> => {
  const response = await apiClient.get<ApplicationStats>(
    '/api/v1/applications/stats'
  )
  return response.data
}

/**
 * Get detailed information about a specific application.
 */
export const getApplication = async (
  applicationId: number
): Promise<ApplicationDetail> => {
  const response = await apiClient.get<ApplicationDetail>(
    `/api/v1/applications/${applicationId}`
  )
  return response.data
}

/**
 * Update application details.
 */
export const updateApplication = async (
  applicationId: number,
  request: UpdateApplicationRequest
): Promise<ApplicationDetail> => {
  const response = await apiClient.put<ApplicationDetail>(
    `/api/v1/applications/${applicationId}`,
    request
  )
  return response.data
}

/**
 * Update application status.
 */
export const updateApplicationStatus = async (
  applicationId: number,
  request: UpdateStatusRequest
): Promise<ApplicationDetail> => {
  const response = await apiClient.patch<ApplicationDetail>(
    `/api/v1/applications/${applicationId}/status`,
    request
  )
  return response.data
}

/**
 * Delete an application (soft delete).
 */
export const deleteApplication = async (applicationId: number): Promise<void> => {
  await apiClient.delete(`/api/v1/applications/${applicationId}`)
}

/**
 * Get status history for an application.
 */
export const getApplicationHistory = async (
  applicationId: number
): Promise<StatusHistory[]> => {
  const response = await apiClient.get<StatusHistory[]>(
    `/api/v1/applications/${applicationId}/history`
  )
  return response.data
}
