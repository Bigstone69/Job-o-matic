import { Link } from 'react-router-dom'
import { Briefcase, Search, FileText, BarChart } from 'lucide-react'

export default function HomePage() {
  const features = [
    {
      name: 'Intelligent Job Search',
      description: 'Search across multiple job boards with AI-powered matching and filtering.',
      icon: Search,
    },
    {
      name: 'Application Tracking',
      description: 'Track all your applications with status updates and timeline visualization.',
      icon: Briefcase,
    },
    {
      name: 'AI Cover Letters',
      description: 'Generate tailored cover letters using Claude or local Ollama models.',
      icon: FileText,
    },
    {
      name: 'Analytics Dashboard',
      description: 'Visualize your application progress with comprehensive analytics.',
      icon: BarChart,
    },
  ]

  return (
    <div>
      {/* Hero Section */}
      <div className="text-center">
        <h1 className="text-4xl font-bold tracking-tight text-gray-900 dark:text-white sm:text-6xl">
          Enterprise-Grade Job Application Management
        </h1>
        <p className="mt-6 text-lg leading-8 text-gray-600 dark:text-gray-400">
          Streamline your job search with AI-powered assistance, comprehensive tracking, and
          intelligent insights. Built with MCP integration for seamless Claude Desktop experience.
        </p>
        <div className="mt-10 flex items-center justify-center gap-x-6">
          <Link
            to="/dashboard"
            className="btn btn-primary"
          >
            Get Started
          </Link>
          <Link
            to="/jobs"
            className="btn btn-secondary"
          >
            Browse Jobs
          </Link>
        </div>
      </div>

      {/* Features Grid */}
      <div className="mt-20">
        <div className="grid grid-cols-1 gap-8 sm:grid-cols-2 lg:grid-cols-4">
          {features.map((feature) => {
            const Icon = feature.icon
            return (
              <div
                key={feature.name}
                className="card"
              >
                <div className="flex h-12 w-12 items-center justify-center rounded-lg bg-primary-100 dark:bg-primary-900">
                  <Icon className="h-6 w-6 text-primary-600 dark:text-primary-300" />
                </div>
                <h3 className="mt-4 text-lg font-semibold text-gray-900 dark:text-white">
                  {feature.name}
                </h3>
                <p className="mt-2 text-sm text-gray-600 dark:text-gray-400">
                  {feature.description}
                </p>
              </div>
            )
          })}
        </div>
      </div>

      {/* Status Section */}
      <div className="mt-20 rounded-lg bg-primary-50 p-8 dark:bg-primary-900/20">
        <div className="text-center">
          <h2 className="text-2xl font-bold text-gray-900 dark:text-white">
            Development Status
          </h2>
          <p className="mt-4 text-lg text-gray-600 dark:text-gray-400">
            Phase 1: Foundation & Setup - <span className="font-semibold text-primary-600 dark:text-primary-400">In Progress</span>
          </p>
          <p className="mt-2 text-sm text-gray-500 dark:text-gray-500">
            Backend: FastAPI + PostgreSQL + SQLAlchemy ✓ | Frontend: React + Vite + TypeScript ✓
          </p>
        </div>
      </div>
    </div>
  )
}
