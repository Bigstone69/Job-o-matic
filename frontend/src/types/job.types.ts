/**
 * TypeScript types for job-related API responses.
 *
 * These types match the Pydantic schemas from the backend.
 */

export enum EmploymentType {
  FULL_TIME = 'full_time',
  PART_TIME = 'part_time',
  CONTRACT = 'contract',
  TEMPORARY = 'temporary',
  INTERNSHIP = 'internship',
}

export enum RemotePolicy {
  REMOTE = 'remote',
  HYBRID = 'hybrid',
  ONSITE = 'onsite',
  UNKNOWN = 'unknown',
}

export interface Company {
  id: number
  name: string
  website?: string
  logo_url?: string
  industry?: string
  location?: string
}

export interface Job {
  id: number
  title: string
  company: Company
  location: string
  remote_policy: RemotePolicy
  salary_min?: number
  salary_max?: number
  salary_currency: string
  employment_type: EmploymentType
  source: string
  url: string
  posted_date?: string
  is_active: boolean
  created_at: string
}

export interface JobDetail extends Job {
  description: string
  benefits?: string[]
  requirements_parsed?: Record<string, any>
  source_id?: string
  updated_at: string
}

export interface JobSearchRequest {
  query: string
  location: string
  sources?: string[]
  employment_type?: EmploymentType[]
  remote_only?: boolean
  salary_min?: number
  max_results?: number
}

export interface JobSearchResponse {
  jobs: Job[]
  total: number
  page: number
  per_page: number
  search_query: string
  search_location: string
}

export interface CreateManualJobRequest {
  title: string
  company_name: string
  url: string
  location?: string
  description?: string
  employment_type?: EmploymentType
  remote_policy?: RemotePolicy
  salary_min?: number
  salary_max?: number
  salary_currency?: string
  posted_date?: string
}

export interface JobListParams {
  skip?: number
  limit?: number
  company_id?: number
  location?: string
  employment_type?: EmploymentType
  remote_policy?: RemotePolicy
  is_active?: boolean
}
