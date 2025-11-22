/**
 * ApplicationStatusBadge component - displays application status with color coding.
 */

import { ApplicationStatus } from '../types/application.types'

interface ApplicationStatusBadgeProps {
  status: ApplicationStatus
  size?: 'sm' | 'md' | 'lg'
}

export default function ApplicationStatusBadge({
  status,
  size = 'md',
}: ApplicationStatusBadgeProps) {
  // Get color classes for each status
  const getStatusColor = (status: ApplicationStatus): string => {
    const colorMap: Record<ApplicationStatus, string> = {
      [ApplicationStatus.DRAFT]: 'bg-gray-100 text-gray-800 dark:bg-gray-700 dark:text-gray-300',
      [ApplicationStatus.SUBMITTED]: 'bg-blue-100 text-blue-800 dark:bg-blue-900 dark:text-blue-300',
      [ApplicationStatus.SCREENING]: 'bg-yellow-100 text-yellow-800 dark:bg-yellow-900 dark:text-yellow-300',
      [ApplicationStatus.INTERVIEW]: 'bg-purple-100 text-purple-800 dark:bg-purple-900 dark:text-purple-300',
      [ApplicationStatus.TECHNICAL]: 'bg-indigo-100 text-indigo-800 dark:bg-indigo-900 dark:text-indigo-300',
      [ApplicationStatus.OFFER]: 'bg-green-100 text-green-800 dark:bg-green-900 dark:text-green-300',
      [ApplicationStatus.ACCEPTED]: 'bg-emerald-100 text-emerald-800 dark:bg-emerald-900 dark:text-emerald-300',
      [ApplicationStatus.REJECTED]: 'bg-red-100 text-red-800 dark:bg-red-900 dark:text-red-300',
      [ApplicationStatus.WITHDRAWN]: 'bg-gray-100 text-gray-600 dark:bg-gray-700 dark:text-gray-400',
    }
    return colorMap[status] || 'bg-gray-100 text-gray-800'
  }

  // Format status text
  const getStatusText = (status: ApplicationStatus): string => {
    const textMap: Record<ApplicationStatus, string> = {
      [ApplicationStatus.DRAFT]: 'Draft',
      [ApplicationStatus.SUBMITTED]: 'Submitted',
      [ApplicationStatus.SCREENING]: 'Screening',
      [ApplicationStatus.INTERVIEW]: 'Interview',
      [ApplicationStatus.TECHNICAL]: 'Technical',
      [ApplicationStatus.OFFER]: 'Offer',
      [ApplicationStatus.ACCEPTED]: 'Accepted',
      [ApplicationStatus.REJECTED]: 'Rejected',
      [ApplicationStatus.WITHDRAWN]: 'Withdrawn',
    }
    return textMap[status] || status
  }

  // Get icon for each status
  const getStatusIcon = (status: ApplicationStatus): JSX.Element | null => {
    const iconClass = size === 'sm' ? 'w-3 h-3' : size === 'lg' ? 'w-5 h-5' : 'w-4 h-4'

    switch (status) {
      case ApplicationStatus.DRAFT:
        return (
          <svg className={iconClass} fill="currentColor" viewBox="0 0 20 20">
            <path d="M13.586 3.586a2 2 0 112.828 2.828l-.793.793-2.828-2.828.793-.793zM11.379 5.793L3 14.172V17h2.828l8.38-8.379-2.83-2.828z" />
          </svg>
        )
      case ApplicationStatus.SUBMITTED:
        return (
          <svg className={iconClass} fill="currentColor" viewBox="0 0 20 20">
            <path d="M2.003 5.884L10 9.882l7.997-3.998A2 2 0 0016 4H4a2 2 0 00-1.997 1.884z" />
            <path d="M18 8.118l-8 4-8-4V14a2 2 0 002 2h12a2 2 0 002-2V8.118z" />
          </svg>
        )
      case ApplicationStatus.SCREENING:
      case ApplicationStatus.INTERVIEW:
      case ApplicationStatus.TECHNICAL:
        return (
          <svg className={iconClass} fill="currentColor" viewBox="0 0 20 20">
            <path
              fillRule="evenodd"
              d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z"
              clipRule="evenodd"
            />
          </svg>
        )
      case ApplicationStatus.OFFER:
        return (
          <svg className={iconClass} fill="currentColor" viewBox="0 0 20 20">
            <path d="M9 2a1 1 0 000 2h2a1 1 0 100-2H9z" />
            <path
              fillRule="evenodd"
              d="M4 5a2 2 0 012-2 3 3 0 003 3h2a3 3 0 003-3 2 2 0 012 2v11a2 2 0 01-2 2H6a2 2 0 01-2-2V5zm9.707 5.707a1 1 0 00-1.414-1.414L9 12.586l-1.293-1.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
        )
      case ApplicationStatus.ACCEPTED:
        return (
          <svg className={iconClass} fill="currentColor" viewBox="0 0 20 20">
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-9.293a1 1 0 00-1.414-1.414L9 10.586 7.707 9.293a1 1 0 00-1.414 1.414l2 2a1 1 0 001.414 0l4-4z"
              clipRule="evenodd"
            />
          </svg>
        )
      case ApplicationStatus.REJECTED:
        return (
          <svg className={iconClass} fill="currentColor" viewBox="0 0 20 20">
            <path
              fillRule="evenodd"
              d="M10 18a8 8 0 100-16 8 8 0 000 16zM8.707 7.293a1 1 0 00-1.414 1.414L8.586 10l-1.293 1.293a1 1 0 101.414 1.414L10 11.414l1.293 1.293a1 1 0 001.414-1.414L11.414 10l1.293-1.293a1 1 0 00-1.414-1.414L10 8.586 8.707 7.293z"
              clipRule="evenodd"
            />
          </svg>
        )
      case ApplicationStatus.WITHDRAWN:
        return (
          <svg className={iconClass} fill="currentColor" viewBox="0 0 20 20">
            <path
              fillRule="evenodd"
              d="M9 2a1 1 0 00-.894.553L7.382 4H4a1 1 0 000 2v10a2 2 0 002 2h8a2 2 0 002-2V6a1 1 0 100-2h-3.382l-.724-1.447A1 1 0 0011 2H9zM7 8a1 1 0 012 0v6a1 1 0 11-2 0V8zm5-1a1 1 0 00-1 1v6a1 1 0 102 0V8a1 1 0 00-1-1z"
              clipRule="evenodd"
            />
          </svg>
        )
      default:
        return null
    }
  }

  // Size-specific padding and text size
  const sizeClasses = {
    sm: 'px-2 py-0.5 text-xs',
    md: 'px-2.5 py-1 text-sm',
    lg: 'px-3 py-1.5 text-base',
  }

  return (
    <span
      className={`inline-flex items-center gap-1 rounded-full font-medium ${getStatusColor(
        status
      )} ${sizeClasses[size]}`}
    >
      {getStatusIcon(status)}
      {getStatusText(status)}
    </span>
  )
}
