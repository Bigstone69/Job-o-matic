/**
 * Axios API client configuration.
 *
 * Configures axios instance with base URL, headers, and interceptors.
 */

import axios, { AxiosError, AxiosResponse } from 'axios'

// Get API base URL from environment or use default
const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || 'http://localhost:8000'

// Create axios instance with default config
export const apiClient = axios.create({
  baseURL: API_BASE_URL,
  timeout: 30000, // 30 seconds
  headers: {
    'Content-Type': 'application/json',
  },
})

// Request interceptor - add auth token if available
apiClient.interceptors.request.use(
  (config) => {
    // TODO: Add authentication token when auth is implemented
    // const token = localStorage.getItem('auth_token')
    // if (token) {
    //   config.headers.Authorization = `Bearer ${token}`
    // }
    return config
  },
  (error) => {
    console.error('Request error:', error)
    return Promise.reject(error)
  }
)

// Response interceptor - handle common errors
apiClient.interceptors.response.use(
  (response: AxiosResponse) => {
    return response
  },
  (error: AxiosError) => {
    if (error.response) {
      // Server responded with error status
      const status = error.response.status
      const data = error.response.data as any

      switch (status) {
        case 400:
          console.error('Bad request:', data.detail || data.message)
          break
        case 401:
          console.error('Unauthorized - redirecting to login')
          // TODO: Redirect to login when auth is implemented
          break
        case 403:
          console.error('Forbidden:', data.detail || data.message)
          break
        case 404:
          console.error('Not found:', data.detail || data.message)
          break
        case 500:
          console.error('Server error:', data.detail || data.message)
          break
        default:
          console.error('API error:', data.detail || data.message || error.message)
      }
    } else if (error.request) {
      // Request made but no response received
      console.error('Network error - no response received')
    } else {
      // Error setting up the request
      console.error('Request setup error:', error.message)
    }

    return Promise.reject(error)
  }
)

export default apiClient
