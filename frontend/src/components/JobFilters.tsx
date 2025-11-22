/**
 * JobFilters component - advanced filtering controls for job listings.
 */

import { useState } from 'react'
import { EmploymentType, RemotePolicy } from '../types/job.types'

export interface FilterValues {
  employment_types: EmploymentType[]
  remote_policies: RemotePolicy[]
  salary_min?: number
  sources: string[]
}

interface JobFiltersProps {
  onFilterChange: (filters: FilterValues) => void
  onReset: () => void
}

export default function JobFilters({ onFilterChange, onReset }: JobFiltersProps) {
  const [isOpen, setIsOpen] = useState(false)
  const [employmentTypes, setEmploymentTypes] = useState<EmploymentType[]>([])
  const [remotePolicies, setRemotePolicies] = useState<RemotePolicy[]>([])
  const [salaryMin, setSalaryMin] = useState<string>('')
  const [sources, setSources] = useState<string[]>([])

  const handleApplyFilters = () => {
    onFilterChange({
      employment_types: employmentTypes,
      remote_policies: remotePolicies,
      salary_min: salaryMin ? parseInt(salaryMin) : undefined,
      sources,
    })
    setIsOpen(false)
  }

  const handleReset = () => {
    setEmploymentTypes([])
    setRemotePolicies([])
    setSalaryMin('')
    setSources([])
    onReset()
  }

  const toggleEmploymentType = (type: EmploymentType) => {
    setEmploymentTypes((prev) =>
      prev.includes(type) ? prev.filter((t) => t !== type) : [...prev, type]
    )
  }

  const toggleRemotePolicy = (policy: RemotePolicy) => {
    setRemotePolicies((prev) =>
      prev.includes(policy) ? prev.filter((p) => p !== policy) : [...prev, policy]
    )
  }

  const toggleSource = (source: string) => {
    setSources((prev) =>
      prev.includes(source) ? prev.filter((s) => s !== source) : [...prev, source]
    )
  }

  const activeFiltersCount =
    employmentTypes.length +
    remotePolicies.length +
    (salaryMin ? 1 : 0) +
    sources.length

  return (
    <div className="relative">
      {/* Filter Toggle Button */}
      <button
        onClick={() => setIsOpen(!isOpen)}
        className="flex items-center gap-2 px-4 py-2 bg-white dark:bg-gray-800 border border-gray-300 dark:border-gray-600 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
      >
        <svg
          className="w-5 h-5 text-gray-600 dark:text-gray-400"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth={2}
            d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"
          />
        </svg>
        <span className="text-sm font-medium text-gray-700 dark:text-gray-300">
          Filters
        </span>
        {activeFiltersCount > 0 && (
          <span className="bg-blue-600 text-white text-xs font-bold px-2 py-0.5 rounded-full">
            {activeFiltersCount}
          </span>
        )}
      </button>

      {/* Filter Panel */}
      {isOpen && (
        <div className="absolute right-0 mt-2 w-80 bg-white dark:bg-gray-800 rounded-lg shadow-lg border border-gray-200 dark:border-gray-700 z-10">
          <div className="p-4 border-b border-gray-200 dark:border-gray-700">
            <h3 className="text-lg font-semibold text-gray-900 dark:text-white">
              Filter Jobs
            </h3>
          </div>

          <div className="p-4 space-y-6 max-h-96 overflow-y-auto">
            {/* Employment Type */}
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Employment Type
              </label>
              <div className="space-y-2">
                {Object.values(EmploymentType).map((type) => (
                  <label key={type} className="flex items-center cursor-pointer">
                    <input
                      type="checkbox"
                      checked={employmentTypes.includes(type)}
                      onChange={() => toggleEmploymentType(type)}
                      className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                    />
                    <span className="ml-2 text-sm text-gray-700 dark:text-gray-300 capitalize">
                      {type.replace('_', '-')}
                    </span>
                  </label>
                ))}
              </div>
            </div>

            {/* Remote Policy */}
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Work Location
              </label>
              <div className="space-y-2">
                {[RemotePolicy.REMOTE, RemotePolicy.HYBRID, RemotePolicy.ONSITE].map(
                  (policy) => (
                    <label key={policy} className="flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        checked={remotePolicies.includes(policy)}
                        onChange={() => toggleRemotePolicy(policy)}
                        className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                      />
                      <span className="ml-2 text-sm text-gray-700 dark:text-gray-300 capitalize">
                        {policy}
                      </span>
                    </label>
                  )
                )}
              </div>
            </div>

            {/* Minimum Salary */}
            <div>
              <label
                htmlFor="salary_min"
                className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2"
              >
                Minimum Salary (USD)
              </label>
              <input
                type="number"
                id="salary_min"
                value={salaryMin}
                onChange={(e) => setSalaryMin(e.target.value)}
                placeholder="e.g., 100000"
                className="w-full px-3 py-2 border border-gray-300 dark:border-gray-600 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent dark:bg-gray-700 dark:text-white"
              />
            </div>

            {/* Job Sources */}
            <div>
              <label className="block text-sm font-medium text-gray-700 dark:text-gray-300 mb-2">
                Job Sources
              </label>
              <div className="space-y-2">
                {['linkedin', 'indeed', 'glassdoor', 'zip_recruiter'].map(
                  (source) => (
                    <label key={source} className="flex items-center cursor-pointer">
                      <input
                        type="checkbox"
                        checked={sources.includes(source)}
                        onChange={() => toggleSource(source)}
                        className="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
                      />
                      <span className="ml-2 text-sm text-gray-700 dark:text-gray-300 capitalize">
                        {source.replace('_', ' ')}
                      </span>
                    </label>
                  )
                )}
              </div>
            </div>
          </div>

          {/* Actions */}
          <div className="p-4 border-t border-gray-200 dark:border-gray-700 flex gap-2">
            <button
              onClick={handleReset}
              className="flex-1 px-4 py-2 border border-gray-300 dark:border-gray-600 text-gray-700 dark:text-gray-300 rounded-md hover:bg-gray-50 dark:hover:bg-gray-700 transition-colors"
            >
              Reset
            </button>
            <button
              onClick={handleApplyFilters}
              className="flex-1 px-4 py-2 bg-blue-600 hover:bg-blue-700 text-white font-medium rounded-md transition-colors"
            >
              Apply Filters
            </button>
          </div>
        </div>
      )}
    </div>
  )
}
