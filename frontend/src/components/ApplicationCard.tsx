/**
 * ApplicationCard component - displays a single application.
 */

import { Application } from '../types/application.types'
import ApplicationStatusBadge from './ApplicationStatusBadge'

interface ApplicationCardProps {
  application: Application
  onStatusClick?: (application: Application) => void
  onClick?: (application: Application) => void
  onDelete?: (application: Application) => void
}

export default function ApplicationCard({
  application,
  onStatusClick,
  onClick,
  onDelete,
}: ApplicationCardProps) {
  const formatDate = (dateString?: string): string => {
    if (!dateString) return 'Not set'

    const date = new Date(dateString)
    const now = new Date()
    const diffTime = now.getTime() - date.getTime()
    const diffDays = Math.floor(diffTime / (1000 * 60 * 60 * 24))

    if (diffDays === 0) return 'Today'
    if (diffDays === 1) return 'Yesterday'
    if (diffDays < 7) return `${diffDays} days ago`
    if (diffDays < 30) return `${Math.floor(diffDays / 7)} weeks ago`
    return date.toLocaleDateString()
  }

  const handleCardClick = () => {
    if (onClick) {
      onClick(application)
    }
  }

  const handleStatusClick = (e: React.MouseEvent) => {
    e.stopPropagation()
    if (onStatusClick) {
      onStatusClick(application)
    }
  }

  const handleDeleteClick = (e: React.MouseEvent) => {
    e.stopPropagation()
    if (onDelete) {
      onDelete(application)
    }
  }

  return (
    <div
      className={`bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 hover:shadow-lg transition-shadow ${
        onClick ? 'cursor-pointer' : ''
      }`}
      onClick={handleCardClick}
    >
      {/* Header: Job info */}
      <div className="flex items-start justify-between">
        <div className="flex-1 min-w-0">
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white truncate">
            {application.job.title}
          </h3>
          <p className="text-gray-600 dark:text-gray-300 font-medium">
            {application.job.company.name}
          </p>
          <p className="text-sm text-gray-500 dark:text-gray-400">
            {application.job.location}
          </p>
        </div>

        {/* Actions */}
        <div className="flex items-center gap-2 ml-4">
          {onDelete && (
            <button
              onClick={handleDeleteClick}
              className="text-gray-400 hover:text-red-600 dark:hover:text-red-400 transition-colors"
              title="Delete application"
            >
              <svg className="w-5 h-5" fill="currentColor" viewBox="0 0 20 20">
                <path
                  fillRule="evenodd"
                  d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
                  clipRule="evenodd"
                />
              </svg>
            </button>
          )}
        </div>
      </div>

      {/* Status Badge */}
      <div className="mt-4">
        <div
          onClick={onStatusClick ? handleStatusClick : undefined}
          className={onStatusClick ? 'cursor-pointer inline-block' : 'inline-block'}
        >
          <ApplicationStatusBadge status={application.status} size="md" />
        </div>
      </div>

      {/* Dates */}
      <div className="mt-4 space-y-2">
        {application.applied_date && (
          <div className="flex items-center gap-2 text-sm">
            <svg
              className="w-4 h-4 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z"
              />
            </svg>
            <span className="text-gray-600 dark:text-gray-400">
              Applied: {formatDate(application.applied_date)}
            </span>
          </div>
        )}

        {application.interview_date && (
          <div className="flex items-center gap-2 text-sm">
            <svg
              className="w-4 h-4 text-gray-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
              />
            </svg>
            <span className="text-gray-600 dark:text-gray-400">
              Interview: {formatDate(application.interview_date)}
            </span>
          </div>
        )}

        {application.offer_deadline && (
          <div className="flex items-center gap-2 text-sm">
            <svg
              className="w-4 h-4 text-red-400"
              fill="none"
              stroke="currentColor"
              viewBox="0 0 24 24"
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                strokeWidth={2}
                d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"
              />
            </svg>
            <span className="text-red-600 dark:text-red-400 font-medium">
              Offer deadline: {formatDate(application.offer_deadline)}
            </span>
          </div>
        )}
      </div>

      {/* Footer: Updated time */}
      <div className="mt-4 pt-4 border-t border-gray-200 dark:border-gray-700">
        <p className="text-xs text-gray-500 dark:text-gray-400">
          Last updated {formatDate(application.updated_at)}
        </p>
      </div>
    </div>
  )
}
