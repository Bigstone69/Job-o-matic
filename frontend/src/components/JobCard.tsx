/**
 * JobCard component - displays a single job listing.
 */

import { Job, EmploymentType, RemotePolicy } from '../types/job.types'

interface JobCardProps {
  job: Job
  onClick?: (job: Job) => void
}

export default function JobCard({ job, onClick }: JobCardProps) {
  // Format salary range
  const formatSalary = () => {
    if (!job.salary_min && !job.salary_max) return null

    const format = (amount: number) => {
      return new Intl.NumberFormat('en-US', {
        style: 'currency',
        currency: job.salary_currency || 'USD',
        maximumFractionDigits: 0,
      }).format(amount)
    }

    if (job.salary_min && job.salary_max) {
      return `${format(job.salary_min)} - ${format(job.salary_max)}`
    } else if (job.salary_min) {
      return `${format(job.salary_min)}+`
    } else if (job.salary_max) {
      return `Up to ${format(job.salary_max)}`
    }
    return null
  }

  // Format employment type for display
  const formatEmploymentType = (type: EmploymentType): string => {
    const typeMap: Record<EmploymentType, string> = {
      [EmploymentType.FULL_TIME]: 'Full-time',
      [EmploymentType.PART_TIME]: 'Part-time',
      [EmploymentType.CONTRACT]: 'Contract',
      [EmploymentType.TEMPORARY]: 'Temporary',
      [EmploymentType.INTERNSHIP]: 'Internship',
    }
    return typeMap[type] || type
  }

  // Format remote policy for display
  const formatRemotePolicy = (policy: RemotePolicy): string => {
    const policyMap: Record<RemotePolicy, string> = {
      [RemotePolicy.REMOTE]: 'Remote',
      [RemotePolicy.HYBRID]: 'Hybrid',
      [RemotePolicy.ONSITE]: 'On-site',
      [RemotePolicy.UNKNOWN]: '',
    }
    return policyMap[policy] || ''
  }

  // Get badge color for remote policy
  const getRemoteBadgeColor = (policy: RemotePolicy): string => {
    const colorMap: Record<RemotePolicy, string> = {
      [RemotePolicy.REMOTE]: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300',
      [RemotePolicy.HYBRID]: 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300',
      [RemotePolicy.ONSITE]: 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300',
      [RemotePolicy.UNKNOWN]: 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300',
    }
    return colorMap[policy] || ''
  }

  // Format posted date
  const formatPostedDate = () => {
    if (!job.posted_date) return null

    const date = new Date(job.posted_date)
    const now = new Date()
    const diffTime = Math.abs(now.getTime() - date.getTime())
    const diffDays = Math.ceil(diffTime / (1000 * 60 * 60 * 24))

    if (diffDays === 0) return 'Posted today'
    if (diffDays === 1) return 'Posted yesterday'
    if (diffDays < 7) return `Posted ${diffDays} days ago`
    if (diffDays < 30) return `Posted ${Math.floor(diffDays / 7)} weeks ago`
    return date.toLocaleDateString()
  }

  const salary = formatSalary()
  const remoteText = formatRemotePolicy(job.remote_policy)
  const postedText = formatPostedDate()

  return (
    <div
      className={`bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow ${
        onClick ? 'cursor-pointer' : ''
      }`}
      onClick={() => onClick?.(job)}
    >
      {/* Header: Company logo and basic info */}
      <div className="flex items-start gap-4">
        {job.company.logo_url ? (
          <img
            src={job.company.logo_url}
            alt={`${job.company.name} logo`}
            className="w-12 h-12 rounded object-contain"
          />
        ) : (
          <div className="w-12 h-12 rounded bg-gray-200 dark:bg-gray-700 flex items-center justify-center">
            <span className="text-gray-500 dark:text-gray-400 text-xl font-semibold">
              {job.company.name.charAt(0).toUpperCase()}
            </span>
          </div>
        )}

        <div className="flex-1 min-w-0">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white truncate">
            {job.title}
          </h3>
          <p className="text-gray-600 dark:text-gray-300 font-medium">
            {job.company.name}
          </p>
          <p className="text-sm text-gray-500 dark:text-gray-400">
            {job.location}
          </p>
        </div>
      </div>

      {/* Badges and metadata */}
      <div className="mt-4 flex flex-wrap gap-2">
        {remoteText && (
          <span
            className={`px-2 py-1 rounded-full text-xs font-medium ${getRemoteBadgeColor(
              job.remote_policy
            )}`}
          >
            {remoteText}
          </span>
        )}
        <span className="px-2 py-1 rounded-full text-xs font-medium bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300">
          {formatEmploymentType(job.employment_type)}
        </span>
        <span className="px-2 py-1 rounded-full text-xs font-medium bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-300">
          {job.source}
        </span>
      </div>

      {/* Salary and posted date */}
      <div className="mt-4 flex items-center justify-between text-sm">
        {salary && (
          <span className="text-gray-900 dark:text-white font-semibold">
            {salary}
          </span>
        )}
        {postedText && (
          <span className="text-gray-500 dark:text-gray-400">{postedText}</span>
        )}
      </div>
    </div>
  )
}
