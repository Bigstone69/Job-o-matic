export default function DashboardPage() {
  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 dark:text-white">Dashboard</h1>
      <p className="mt-2 text-gray-600 dark:text-gray-400">
        Analytics and insights for your job applications.
      </p>
      <div className="mt-8 grid grid-cols-1 gap-6 sm:grid-cols-2 lg:grid-cols-4">
        {/* Stats cards - to be implemented */}
        <div className="card">
          <p className="text-sm text-gray-500 dark:text-gray-400">Total Applications</p>
          <p className="mt-2 text-3xl font-semibold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="card">
          <p className="text-sm text-gray-500 dark:text-gray-400">Active</p>
          <p className="mt-2 text-3xl font-semibold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="card">
          <p className="text-sm text-gray-500 dark:text-gray-400">Interviews</p>
          <p className="mt-2 text-3xl font-semibold text-gray-900 dark:text-white">0</p>
        </div>
        <div className="card">
          <p className="text-sm text-gray-500 dark:text-gray-400">Offers</p>
          <p className="mt-2 text-3xl font-semibold text-gray-900 dark:text-white">0</p>
        </div>
      </div>
    </div>
  )
}
