/**
 * TypeScript types for application-related API responses.
 *
 * These types match the Pydantic schemas from the backend.
 */

import { Job } from './job.types'

export enum ApplicationStatus {
  DRAFT = 'draft',
  SUBMITTED = 'submitted',
  SCREENING = 'screening',
  INTERVIEW = 'interview',
  TECHNICAL = 'technical',
  OFFER = 'offer',
  ACCEPTED = 'accepted',
  REJECTED = 'rejected',
  WITHDRAWN = 'withdrawn',
}

export interface StatusHistory {
  id: number
  old_status: ApplicationStatus | null
  new_status: ApplicationStatus
  notes?: string
  created_at: string
}

export interface Application {
  id: number
  job: Job
  status: ApplicationStatus
  applied_date?: string
  interview_date?: string
  offer_deadline?: string
  is_active: boolean
  created_at: string
  updated_at: string
}

export interface ApplicationDetail extends Application {
  notes?: string
  resume_version?: string
  cover_letter_id?: number
  salary_offered?: number
  status_history: StatusHistory[]
}

export interface CreateApplicationRequest {
  job_id: number
  status?: ApplicationStatus
  notes?: string
  resume_version?: string
  cover_letter_id?: number
  applied_date?: string
  interview_date?: string
  offer_deadline?: string
  salary_offered?: number
}

export interface UpdateApplicationRequest {
  notes?: string
  resume_version?: string
  cover_letter_id?: number
  applied_date?: string
  interview_date?: string
  offer_deadline?: string
  salary_offered?: number
}

export interface UpdateStatusRequest {
  status: ApplicationStatus
  notes?: string
}

export interface ApplicationStats {
  total: number
  active: number
  by_status: Record<string, number>
  recent_applications: number
}

export interface ApplicationListParams {
  status?: ApplicationStatus
  company_id?: number
  is_active?: boolean
  skip?: number
  limit?: number
}
