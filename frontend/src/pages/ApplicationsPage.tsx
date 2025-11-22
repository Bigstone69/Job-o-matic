/**
 * ApplicationsPage - Main page for managing job applications.
 */

import { useState } from 'react'
import {
  useApplicationList,
  useApplicationStats,
  useDeleteApplication,
} from '../hooks/useApplications'
import { ApplicationStatus, Application, ApplicationDetail } from '../types/application.types'
import ApplicationList from '../components/ApplicationList'
import StatusUpdateModal from '../components/StatusUpdateModal'

// Status filter options
const statusFilters = [
  { value: null, label: 'All Applications' },
  { value: ApplicationStatus.DRAFT, label: 'Draft' },
  { value: ApplicationStatus.SUBMITTED, label: 'Submitted' },
  { value: ApplicationStatus.SCREENING, label: 'Screening' },
  { value: ApplicationStatus.INTERVIEW, label: 'Interview' },
  { value: ApplicationStatus.TECHNICAL, label: 'Technical' },
  { value: ApplicationStatus.OFFER, label: 'Offer' },
  { value: ApplicationStatus.ACCEPTED, label: 'Accepted' },
  { value: ApplicationStatus.REJECTED, label: 'Rejected' },
  { value: ApplicationStatus.WITHDRAWN, label: 'Withdrawn' },
]

export default function ApplicationsPage() {
  const [selectedStatus, setSelectedStatus] = useState<ApplicationStatus | null>(null)
  const [selectedApplication, setSelectedApplication] = useState<ApplicationDetail | null>(null)
  const [isStatusModalOpen, setIsStatusModalOpen] = useState(false)
  const [applicationToDelete, setApplicationToDelete] = useState<number | null>(null)

  // Fetch data
  const { data: stats, isLoading: statsLoading } = useApplicationStats()
  const {
    data: applications,
    isLoading: applicationsLoading,
    error,
    refetch,
  } = useApplicationList({
    status: selectedStatus || undefined,
    is_active: true,
  })

  const deleteApplicationMutation = useDeleteApplication()

  // Handlers
  const handleStatusUpdate = (application: Application) => {
    // Cast to ApplicationDetail - the modal will need full details
    // In production, consider fetching full details here
    setSelectedApplication(application as unknown as ApplicationDetail)
    setIsStatusModalOpen(true)
  }

  const handleStatusUpdateSuccess = () => {
    refetch()
  }

  const handleDeleteClick = (application: Application) => {
    setApplicationToDelete(application.id)
  }

  const handleDeleteConfirm = async () => {
    if (applicationToDelete) {
      try {
        await deleteApplicationMutation.mutateAsync(applicationToDelete)
        setApplicationToDelete(null)
        refetch()
      } catch (error) {
        console.error('Failed to delete application:', error)
      }
    }
  }

  const handleDeleteCancel = () => {
    setApplicationToDelete(null)
  }

  return (
    <div className="min-h-screen bg-gray-50 dark:bg-gray-900">
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
        {/* Header */}
        <div className="mb-8">
          <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
            My Applications
          </h1>
          <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
            Track and manage your job applications
          </p>
        </div>

        {/* Stats Dashboard */}
        {statsLoading ? (
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
            {[...Array(4)].map((_, i) => (
              <div
                key={i}
                className="bg-white dark:bg-gray-800 rounded-lg shadow p-6 animate-pulse"
              >
                <div className="h-4 bg-gray-200 dark:bg-gray-700 rounded w-1/2 mb-2" />
                <div className="h-8 bg-gray-200 dark:bg-gray-700 rounded w-1/4" />
              </div>
            ))}
          </div>
        ) : stats ? (
          <div className="grid grid-cols-1 md:grid-cols-4 gap-4 mb-8">
            <StatCard
              title="Total Applications"
              value={stats.total}
              icon={
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"
                  />
                </svg>
              }
              color="blue"
            />
            <StatCard
              title="Active"
              value={stats.active}
              icon={
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M13 10V3L4 14h7v7l9-11h-7z"
                  />
                </svg>
              }
              color="green"
            />
            <StatCard
              title="In Interview"
              value={
                (stats.by_status[ApplicationStatus.INTERVIEW] || 0) +
                (stats.by_status[ApplicationStatus.TECHNICAL] || 0)
              }
              icon={
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"
                  />
                </svg>
              }
              color="purple"
            />
            <StatCard
              title="Recent (7d)"
              value={stats.recent_applications}
              icon={
                <svg className="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"
                  />
                </svg>
              }
              color="yellow"
            />
          </div>
        ) : null}

        {/* Filters */}
        <div className="mb-6">
          <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-4">
            <label
              htmlFor="status-filter"
              className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
            >
              Filter by Status
            </label>
            <select
              id="status-filter"
              value={selectedStatus || ''}
              onChange={(e) =>
                setSelectedStatus((e.target.value as ApplicationStatus) || null)
              }
              className="w-full md:w-64 px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md shadow-sm focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:text-white"
            >
              {statusFilters.map((filter) => (
                <option key={filter.label} value={filter.value || ''}>
                  {filter.label}
                </option>
              ))}
            </select>
          </div>
        </div>

        {/* Applications List */}
        {error ? (
          <div className="bg-red-50 dark:bg-red-900/20 border border-red-200 dark:border-red-800 rounded-lg p-6 text-center">
            <svg
              className="w-12 h-12 text-red-500 mx-auto mb-4"
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
            <h3 className="text-lg font-semibold text-red-800 dark:text-red-300 mb-2">
              Failed to load applications
            </h3>
            <p className="text-sm text-red-600 dark:text-red-400 mb-4">
              {error.message || 'An unexpected error occurred'}
            </p>
            <button
              onClick={() => refetch()}
              className="px-4 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-red-500"
            >
              Try Again
            </button>
          </div>
        ) : (
          <ApplicationList
            applications={applications || []}
            loading={applicationsLoading}
            error={error}
            onStatusClick={handleStatusUpdate}
            onDelete={handleDeleteClick}
          />
        )}

        {/* Status Update Modal */}
        {selectedApplication && (
          <StatusUpdateModal
            application={selectedApplication}
            isOpen={isStatusModalOpen}
            onClose={() => setIsStatusModalOpen(false)}
            onSuccess={handleStatusUpdateSuccess}
          />
        )}

        {/* Delete Confirmation Modal */}
        {applicationToDelete && (
          <DeleteConfirmationModal
            isOpen={true}
            isDeleting={deleteApplicationMutation.isPending}
            onConfirm={handleDeleteConfirm}
            onCancel={handleDeleteCancel}
          />
        )}
      </div>
    </div>
  )
}

// StatCard Component
interface StatCardProps {
  title: string
  value: number
  icon: React.ReactNode
  color: 'blue' | 'green' | 'purple' | 'yellow'
}

function StatCard({ title, value, icon, color }: StatCardProps) {
  const colorClasses = {
    blue: 'bg-blue-100 text-blue-600 dark:bg-blue-900/20 dark:text-blue-400',
    green: 'bg-green-100 text-green-600 dark:bg-green-900/20 dark:text-green-400',
    purple: 'bg-purple-100 text-purple-600 dark:bg-purple-900/20 dark:text-purple-400',
    yellow: 'bg-yellow-100 text-yellow-600 dark:bg-yellow-900/20 dark:text-yellow-400',
  }

  return (
    <div className="bg-white dark:bg-gray-800 rounded-lg shadow p-6">
      <div className="flex items-center justify-between mb-2">
        <div className={`p-2 rounded-lg ${colorClasses[color]}`}>{icon}</div>
      </div>
      <h3 className="text-sm font-medium text-gray-600 dark:text-gray-400">{title}</h3>
      <p className="text-3xl font-bold text-gray-900 dark:text-white mt-2">{value}</p>
    </div>
  )
}

// Delete Confirmation Modal
interface DeleteConfirmationModalProps {
  isOpen: boolean
  isDeleting: boolean
  onConfirm: () => void
  onCancel: () => void
}

function DeleteConfirmationModal({
  isOpen,
  isDeleting,
  onConfirm,
  onCancel,
}: DeleteConfirmationModalProps) {
  if (!isOpen) return null

  return (
    <div className="fixed inset-0 z-50 overflow-y-auto">
      {/* Backdrop */}
      <div
        className="fixed inset-0 bg-black bg-opacity-50 transition-opacity"
        onClick={!isDeleting ? onCancel : undefined}
      />

      {/* Modal */}
      <div className="flex min-h-full items-center justify-center p-4">
        <div className="relative bg-white dark:bg-gray-800 rounded-lg shadow-xl max-w-md w-full p-6">
          {/* Icon */}
          <div className="flex items-center justify-center w-12 h-12 mx-auto bg-red-100 dark:bg-red-900/20 rounded-full mb-4">
            <svg
              className="w-6 h-6 text-red-600 dark:text-red-400"
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
          </div>

          {/* Content */}
          <h3 className="text-lg font-semibold text-gray-900 dark:text-white text-center mb-2">
            Delete Application
          </h3>
          <p className="text-sm text-gray-600 dark:text-gray-400 text-center mb-6">
            Are you sure you want to delete this application? This action cannot be undone.
          </p>

          {/* Actions */}
          <div className="flex gap-3 justify-end">
            <button
              type="button"
              onClick={onCancel}
              disabled={isDeleting}
              className="px-4 py-2 text-sm font-medium text-gray-700 dark:text-gray-300 bg-white dark:bg-gray-700 border border-gray-300 dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              Cancel
            </button>
            <button
              type="button"
              onClick={onConfirm}
              disabled={isDeleting}
              className="px-4 py-2 text-sm font-medium text-white bg-red-600 border border-transparent rounded-md hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-red-500 disabled:opacity-50 disabled:cursor-not-allowed flex items-center gap-2"
            >
              {isDeleting ? (
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
                  Deleting...
                </>
              ) : (
                'Delete'
              )}
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}
