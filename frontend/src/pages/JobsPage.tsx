/**
 * JobsPage - Main job search and listing page.
 *
 * Provides job search functionality with filters and displays results.
 */

import { useState } from 'react'
import { useNavigate } from 'react-router-dom'
import SearchBar, { SearchParams } from '../components/SearchBar'
import JobList from '../components/JobList'
import JobFilters, { FilterValues } from '../components/JobFilters'
import { useJobSearchMutation } from '../hooks/useJobs'
import { Job, JobSearchRequest } from '../types/job.types'

export default function JobsPage() {
  const navigate = useNavigate()
  const [searchResults, setSearchResults] = useState<Job[]>([])
  const [currentSearch, setCurrentSearch] = useState<SearchParams | null>(null)
  const [filters, setFilters] = useState<FilterValues>({
    employment_types: [],
    remote_policies: [],
    sources: [],
  })

  // Use mutation for manual search control
  const searchMutation = useJobSearchMutation()

  const handleSearch = async (params: SearchParams) => {
    setCurrentSearch(params)

    // Build search request
    const request: JobSearchRequest = {
      query: params.query,
      location: params.location,
      remote_only: params.remote_only,
      max_results: 50,
      // Apply filters
      employment_type: filters.employment_types.length > 0 ? filters.employment_types : undefined,
      salary_min: filters.salary_min,
      sources: filters.sources.length > 0 ? filters.sources : undefined,
    }

    // Execute search
    const result = await searchMutation.mutateAsync(request)

    // Apply remote policy filters (client-side for now)
    let filteredJobs = result.jobs
    if (filters.remote_policies.length > 0) {
      filteredJobs = filteredJobs.filter((job) =>
        filters.remote_policies.includes(job.remote_policy)
      )
    }

    setSearchResults(filteredJobs)
  }

  const handleFilterChange = (newFilters: FilterValues) => {
    setFilters(newFilters)
    // Re-run search with new filters if there's an active search
    if (currentSearch) {
      handleSearch(currentSearch)
    }
  }

  const handleResetFilters = () => {
    setFilters({
      employment_types: [],
      remote_policies: [],
      sources: [],
    })
    // Re-run search without filters if there's an active search
    if (currentSearch) {
      handleSearch(currentSearch)
    }
  }

  const handleJobClick = (job: Job) => {
    // Navigate to job detail page (to be implemented)
    // For now, open job URL in new tab
    window.open(job.url, '_blank', 'noopener,noreferrer')
  }

  return (
    <div className="max-w-7xl mx-auto">
      {/* Header */}
      <div className="mb-8">
        <h1 className="text-3xl font-bold text-gray-900 dark:text-white">
          Job Search
        </h1>
        <p className="mt-2 text-gray-600 dark:text-gray-400">
          Search for jobs across multiple platforms
        </p>
      </div>

      {/* Search Bar */}
      <div className="mb-6">
        <SearchBar
          onSearch={handleSearch}
          loading={searchMutation.isPending}
        />
      </div>

      {/* Results Section */}
      {(searchResults.length > 0 || searchMutation.isPending || searchMutation.isError) && (
        <div>
          {/* Results Header with Filters */}
          <div className="flex items-center justify-between mb-6">
            <div>
              <h2 className="text-xl font-semibold text-gray-900 dark:text-white">
                Search Results
              </h2>
              {!searchMutation.isPending && (
                <p className="text-sm text-gray-600 dark:text-gray-400">
                  {searchResults.length} job{searchResults.length !== 1 ? 's' : ''} found
                  {currentSearch && (
                    <span>
                      {' '}
                      for "{currentSearch.query}" in {currentSearch.location}
                    </span>
                  )}
                </p>
              )}
            </div>

            {/* Filters */}
            <JobFilters
              onFilterChange={handleFilterChange}
              onReset={handleResetFilters}
            />
          </div>

          {/* Job List */}
          <JobList
            jobs={searchResults}
            loading={searchMutation.isPending}
            error={searchMutation.error}
            onJobClick={handleJobClick}
            emptyMessage="No jobs found matching your criteria"
          />
        </div>
      )}

      {/* Initial State - No Search Yet */}
      {!currentSearch && !searchMutation.isPending && searchResults.length === 0 && (
        <div className="bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-gray-800 dark:to-gray-900 rounded-lg p-12 text-center">
          <svg
            className="w-20 h-20 text-blue-400 dark:text-blue-500 mx-auto mb-6"
            fill="none"
            stroke="currentColor"
            viewBox="0 0 24 24"
          >
            <path
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth={1.5}
              d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"
            />
          </svg>
          <h3 className="text-2xl font-bold text-gray-900 dark:text-white mb-2">
            Start Your Job Search
          </h3>
          <p className="text-gray-600 dark:text-gray-400 mb-6 max-w-md mx-auto">
            Enter a job title and location to search across LinkedIn, Indeed, Glassdoor,
            and more
          </p>
          <div className="flex flex-wrap justify-center gap-2">
            <span className="px-3 py-1 bg-white dark:bg-gray-700 rounded-full text-sm text-gray-700 dark:text-gray-300">
              Try: "Software Engineer"
            </span>
            <span className="px-3 py-1 bg-white dark:bg-gray-700 rounded-full text-sm text-gray-700 dark:text-gray-300">
              "Product Manager"
            </span>
            <span className="px-3 py-1 bg-white dark:bg-gray-700 rounded-full text-sm text-gray-700 dark:text-gray-300">
              "Data Analyst"
            </span>
          </div>
        </div>
      )}
    </div>
  )
}
