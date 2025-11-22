/**
 * Job API service.
 *
 * Provides methods for interacting with job-related endpoints.
 */

import apiClient from './client'
import {
  Job,
  JobDetail,
  JobSearchRequest,
  JobSearchResponse,
  CreateManualJobRequest,
  JobListParams,
} from '../types/job.types'

/**
 * Search for jobs across multiple platforms.
 */
export const searchJobs = async (
  request: JobSearchRequest
): Promise<JobSearchResponse> => {
  const response = await apiClient.post<JobSearchResponse>(
    '/api/v1/jobs/search',
    request
  )
  return response.data
}

/**
 * List saved jobs with optional filters.
 */
export const listJobs = async (params?: JobListParams): Promise<Job[]> => {
  const response = await apiClient.get<Job[]>('/api/v1/jobs', {
    params,
  })
  return response.data
}

/**
 * Get detailed information about a specific job.
 */
export const getJob = async (jobId: number): Promise<JobDetail> => {
  const response = await apiClient.get<JobDetail>(`/api/v1/jobs/${jobId}`)
  return response.data
}

/**
 * Create a manual job entry.
 */
export const createManualJob = async (
  request: CreateManualJobRequest
): Promise<JobDetail> => {
  const response = await apiClient.post<JobDetail>('/api/v1/jobs', request)
  return response.data
}

/**
 * Delete a job entry (soft delete).
 */
export const deleteJob = async (jobId: number): Promise<void> => {
  await apiClient.delete(`/api/v1/jobs/${jobId}`)
}

/**
 * Health check - verify API is running.
 */
export const healthCheck = async (): Promise<{ status: string; service: string }> => {
  const response = await apiClient.get<{ status: string; service: string }>('/health')
  return response.data
}
