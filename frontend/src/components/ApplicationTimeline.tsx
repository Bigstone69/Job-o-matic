/**
 * ApplicationTimeline component - displays status history timeline.
 */

import { StatusHistory } from '../types/application.types'
import ApplicationStatusBadge from './ApplicationStatusBadge'

interface ApplicationTimelineProps {
  statusHistory: StatusHistory[]
}

export default function ApplicationTimeline({ statusHistory }: ApplicationTimelineProps) {
  const formatDate = (dateString: string): string => {
    const date = new Date(dateString)
    return date.toLocaleString('en-US', {
      month: 'short',
      day: 'numeric',
      year: 'numeric',
      hour: '2-digit',
      minute: '2-digit',
    })
  }

  if (statusHistory.length === 0) {
    return (
      <div className="text-center py-8 text-gray-500 dark:text-gray-400">
        No history available
      </div>
    )
  }

  return (
    <div className="flow-root">
      <ul className="-mb-8">
        {statusHistory.map((entry, index) => (
          <li key={entry.id}>
            <div className="relative pb-8">
              {/* Vertical line connecting timeline items */}
              {index !== statusHistory.length - 1 && (
                <span
                  className="absolute top-4 left-4 -ml-px h-full w-0.5 bg-gray-200 dark:bg-gray-700"
                  aria-hidden="true"
                />
              )}

              <div className="relative flex space-x-3">
                {/* Timeline dot/icon */}
                <div>
                  <span className="h-8 w-8 rounded-full bg-white dark:bg-gray-800 border-2 border-gray-300 dark:border-gray-600 flex items-center justify-center ring-8 ring-white dark:ring-gray-900">
                    <svg
                      className="h-4 w-4 text-gray-500 dark:text-gray-400"
                      fill="currentColor"
                      viewBox="0 0 20 20"
                    >
                      <path
                        fillRule="evenodd"
                        d="M10 18a8 8 0 100-16 8 8 0 000 16zm1-12a1 1 0 10-2 0v4a1 1 0 00.293.707l2.828 2.829a1 1 0 101.415-1.415L11 9.586V6z"
                        clipRule="evenodd"
                      />
                    </svg>
                  </span>
                </div>

                {/* Content */}
                <div className="flex-1 min-w-0">
                  <div className="flex items-center gap-2 mb-1">
                    {entry.old_status && (
                      <>
                        <ApplicationStatusBadge status={entry.old_status} size="sm" />
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
                            d="M13 7l5 5m0 0l-5 5m5-5H6"
                          />
                        </svg>
                      </>
                    )}
                    <ApplicationStatusBadge status={entry.new_status} size="sm" />
                  </div>

                  <div className="text-sm text-gray-500 dark:text-gray-400">
                    {formatDate(entry.created_at)}
                  </div>

                  {entry.notes && (
                    <div className="mt-2 text-sm text-gray-700 dark:text-gray-300 bg-gray-50 dark:bg-gray-800 rounded-md p-3">
                      {entry.notes}
                    </div>
                  )}
                </div>
              </div>
            </div>
          </li>
        ))}
      </ul>
    </div>
  )
}
