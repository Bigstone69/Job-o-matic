/**
 * StatusUpdateModal component - modal for updating application status.
 */

import { useState, useEffect, FormEvent } from 'react'
import { ApplicationStatus, ApplicationDetail } from '../types/application.types'
import { useUpdateStatus } from '../hooks/useApplications'
import ApplicationStatusBadge from './ApplicationStatusBadge'

interface StatusUpdateModalProps {
  application: ApplicationDetail
  isOpen: boolean
  onClose: () => void
  onSuccess?: () => void
}

// Status options with labels
const statusOptions = [
  { value: ApplicationStatus.DRAFT, label: 'Draft' },
  { value: ApplicationStatus.SUBMITTED, label: 'Submitted' },
  { value: ApplicationStatus.SCREENING, label: 'Screening' },
  { value: ApplicationStatus.INTERVIEW, label: 'Interview' },
  { value: ApplicationStatus.TECHNICAL, label: 'Technical Assessment' },
  { value: ApplicationStatus.OFFER, label: 'Offer' },
  { value: ApplicationStatus.ACCEPTED, label: 'Accepted' },
  { value: ApplicationStatus.REJECTED, label: 'Rejected' },
  { value: ApplicationStatus.WITHDRAWN, label: 'Withdrawn' },
]

export default function StatusUpdateModal({
  application,
  isOpen,
  onClose,
  onSuccess,
}: StatusUpdateModalProps) {
  const [selectedStatus, setSelectedStatus] = useState<ApplicationStatus>(application.status)
  const [notes, setNotes] = useState('')
  const updateStatusMutation = useUpdateStatus()

  // Reset form when modal opens
  useEffect(() => {
    if (isOpen) {
      setSelectedStatus(application.status)
      setNotes('')
    }
  }, [isOpen, application.status])

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault()

    if (selectedStatus === application.status) {
      // No change
      onClose()
      return
    }

    try {
      await updateStatusMutation.mutateAsync({
        applicationId: application.id,
        request: {
          status: selectedStatus,
          notes: notes.trim() || undefined,
        },
      })

      onSuccess?.()
      onClose()
    } catch (error) {
      // Error is logged by the mutation
      console.error('Failed to update status:', error)
    }
  }

  const handleCancel = () => {
    if (!updateStatusMutation.isPending) {
      onClose()
    }
  }

  if (!isOpen) return null

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto">
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black bg-opacity-50 transition-opacity"
        onClick={handleCancel}
      />

      {/* Modal */}
      <div className="flex min-h-full items-center justify-center p-4">
        <div className="relative bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-md w-full p-6">
          {/* Header */}
          <div className="mb-4">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              Update Application Status
            </h3>
            <p className="mt-1 text-sm text-gray-500 dark:text-gray-400">
              {application.job.title} at {application.job.company.name}
            </p>
          </div>

          {/* Current Status */}
          <div className="mb-4 p-3 bg-gray-50 dark:bg-gray-700 rounded-md">
            <div className="text-sm text-gray-600 dark:text-gray-300 mb-1">
              Current Status:
            </div>
            <ApplicationStatusBadge status={application.status} size="md" />
          </div>

          {/* Form */}
          <form onSubmit={handleSubmit}>
            {/* Status Dropdown */}
            <div className="mb-4">
              <label
                htmlFor="status"
                className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
              >
                New Status
              </label>
              <select
                id="status"
                value={selectedStatus}
                onChange={(e) => setSelectedStatus(e.target.value as ApplicationStatus)}
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
                disabled={updateStatusMutation.isPending}
              >
                {statusOptions.map((option) => (
                  <option key={option.value} value={option.value}>
                    {option.label}
                  </option>
                ))}
              </select>
            </div>

            {/* Preview New Status */}
            {selectedStatus !== application.status && (
              <div className="mb-4 p-3 bg-blue-50 dark:bg-blue-900/20 rounded-md border border-blue-200 dark:border-blue-800">
                <div className="flex items-center gap-2">
                  <ApplicationStatusBadge status={application.status} size="sm" />
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
                  <ApplicationStatusBadge status={selectedStatus} size="sm" />
                </div>
              </div>
            )}

            {/* Notes */}
            <div className="mb-4">
              <label
                htmlFor="notes"
                className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-1"
              >
                Notes (optional)
              </label>
              <textarea
                id="notes"
                value={notes}
                onChange={(e) => setNotes(e.target.value)}
                rows={3}
                maxLength={500}
                placeholder="Add notes about this status change..."
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white resize-none"
                disabled={updateStatusMutation.isPending}
              />
              <div className="mt-1 text-xs text-gray-500 dark:text-gray-400 text-right">
                {notes.length}/500
              </div>
            </div>

            {/* Error Display */}
            {updateStatusMutation.isError && (
              <div className="mb-4 p-3 bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-md">
                <p className="text-sm text-red-800 dark:text-red-300">
                  Failed to update status. Please try again.
                </p>
              </div>
            )}

            {/* Actions */}
            <div className="flex gap-3 justify-end">
              <button
                type="button"
                onClick={handleCancel}
                disabled={updateStatusMutation.isPending}
                className="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                Cancel
              </button>
              <button
                type="submit"
                disabled={
                  updateStatusMutation.isPending || selectedStatus === application.status
                }
                className="px-4 py-2 text-sm font-medium text-white bg-blue-600 border border-transparent rounded-md hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
              >
                {updateStatusMutation.isPending ? (
                  <>
                    <svg
                      className="animate-spin h-4 w-4"
                      xmlns="http://www.w3.org/2000/svg"
                      fill="none"
                      viewBox="0 0 24 24"
                    >
                      <circle
                        className="opacity-25"
                        cx="12"
                        cy="12"
                        r="10"
                        stroke="currentColor"
                        strokeWidth="4"
                      />
                      <path
                        className="opacity-75"
                        fill="currentColor"
                        d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                      />
                    </svg>
                    Updating...
                  </>
                ) : (
                  'Update Status'
                )}
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  )
}
