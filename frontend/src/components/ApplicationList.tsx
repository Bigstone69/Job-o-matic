/**
 * ApplicationList component - renders a list of applications.
 */

import { Application } from '../types/application.types'
import ApplicationCard from './ApplicationCard'

interface ApplicationListProps {
  applications: Application[]
  loading?: boolean
  error?: Error | null
  onApplicationClick?: (application: Application) => void
  onStatusClick?: (application: Application) => void
  onDelete?: (application: Application) => void
  emptyMessage?: string
}

export default function ApplicationList({
  applications,
  loading = false,
  error = null,
  onApplicationClick,
  onStatusClick,
  onDelete,
  emptyMessage = 'No applications found',
}: ApplicationListProps) {
  // Loading state
  if (loading) {
    return (
      <div className="space-y-4">
        {[1, 2, 3].map((i) => (
          <div
            key={i}
            className="bg-white dark:bg-gray-800 rounded-lg shadow-md p-6 animate-pulse"
          >
            <div className="flex items-start justify-between">
              <div className="flex-1 space-y-3">
                <div className="h-6 bg-gray-200 dark:bg-gray-700 rounded w-3/4" />
                <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-1/2" />
                <div className="h-3 bg-gray-200 dark:bg-gray-700 rounded w-1/3" />
              </div>
            </div>
            <div className="mt-4">
              <div className="h-6 bg-gray-200 dark:bg-gray-700 rounded w-24" />
            </div>
            <div className="mt-4 space-y-2">
              <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-40" />
              <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-36" />
            </div>
          </div>
        ))}
      </div>
    )
  }

  // Error state
  if (error) {
    return (
      <div className="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-6 text-center">
        <svg
          className="w-12 h-12 text-red-500 dark:text-red-400 mx-auto mb-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"
          />
        </svg>
        <h3 className="text-lg font-semibold text-red-900 dark:text-red-200 mb-2">
          Error Loading Applications
        </h3>
        <p className="text-red-700 dark:text-red-300">
          {error.message || 'An unexpected error occurred'}
        </p>
      </div>
    )
  }

  // Empty state
  if (applications.length === 0) {
    return (
      <div className="bg-gray-50 dark:bg-gray-800 border border-gray-200 dark:border-gray-700 rounded-lg p-12 text-center">
        <svg
          className="w-16 h-16 text-gray-400 dark:text-gray-500 mx-auto mb-4"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
          />
        </svg>
        <h3 className="text-lg font-semibold text-gray-900 dark:text-white mb-2">
          {emptyMessage}
        </h3>
        <p className="text-gray-600 dark:text-gray-400">
          Start applying to jobs to track your applications here
        </p>
      </div>
    )
  }

  // Applications list
  return (
    <div className="space-y-4">
      {applications.map((application) => (
        <ApplicationCard
          key={application.id}
          application={application}
          onClick={onApplicationClick}
          onStatusClick={onStatusClick}
          onDelete={onDelete}
        />
      ))}
    </div>
  )
}
