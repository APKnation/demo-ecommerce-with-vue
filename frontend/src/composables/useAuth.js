import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'

const API_BASE_URL = 'http://localhost:8000/api'

export function useAuth() {
  const router = useRouter()
  const user = ref(null)
  const token = ref(localStorage.getItem('token'))
  const isLoading = ref(false)
  const error = ref(null)

  // Check if user is authenticated
  const isAuthenticated = computed(() => !!token.value && !!user.value)

  // Set authentication data
  const setAuth = (authToken, userData) => {
    token.value = authToken
    user.value = userData
    localStorage.setItem('token', authToken)
    localStorage.setItem('user', JSON.stringify(userData))
  }

  // Clear authentication data
  const clearAuth = () => {
    token.value = null
    user.value = null
    localStorage.removeItem('token')
    localStorage.removeItem('user')
  }

  // Load user from localStorage on init
  const loadUser = () => {
    const savedUser = localStorage.getItem('user')
    if (savedUser && token.value) {
      try {
        user.value = JSON.parse(savedUser)
      } catch (e) {
        clearAuth()
      }
    }
  }

  // Register user
  const register = async (userData) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${API_BASE_URL}/accounts/register/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(userData)
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || 'Registration failed')
      }

      return { success: true, data }
    } catch (err) {
      error.value = err.message
      return { success: false, error: err.message }
    } finally {
      isLoading.value = false
    }
  }

  // Login user
  const login = async (credentials) => {
    isLoading.value = true
    error.value = null
    
    try {
      const response = await fetch(`${API_BASE_URL}/accounts/login/`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials)
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.non_field_errors?.[0] || data.message || 'Login failed')
      }

      setAuth(data.token, data.user)
      return { success: true, data }
    } catch (err) {
      error.value = err.message
      return { success: false, error: err.message }
    } finally {
      isLoading.value = false
    }
  }

  // Logout user
  const logout = async () => {
    if (token.value) {
      try {
        await fetch(`${API_BASE_URL}/accounts/logout/`, {
          method: 'POST',
          headers: {
            'Authorization': `Token ${token.value}`,
            'Content-Type': 'application/json',
          }
        })
      } catch (err) {
        console.error('Logout error:', err)
      }
    }
    
    clearAuth()
    router.push('/login')
  }

  // Get user profile
  const getProfile = async () => {
    if (!token.value) return { success: false, error: 'No token' }

    try {
      const response = await fetch(`${API_BASE_URL}/accounts/profile/`, {
        headers: {
          'Authorization': `Token ${token.value}`,
          'Content-Type': 'application/json',
        }
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || 'Failed to get profile')
      }

      user.value = data
      localStorage.setItem('user', JSON.stringify(data))
      return { success: true, data }
    } catch (err) {
      error.value = err.message
      if (response.status === 401) {
        clearAuth()
        router.push('/login')
      }
      return { success: false, error: err.message }
    }
  }

  // Update user profile
  const updateProfile = async (profileData) => {
    if (!token.value) return { success: false, error: 'No token' }

    try {
      const response = await fetch(`${API_BASE_URL}/accounts/profile/`, {
        method: 'PUT',
        headers: {
          'Authorization': `Token ${token.value}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(profileData)
      })

      const data = await response.json()

      if (!response.ok) {
        throw new Error(data.message || 'Failed to update profile')
      }

      user.value = data
      localStorage.setItem('user', JSON.stringify(data))
      return { success: true, data }
    } catch (err) {
      error.value = err.message
      return { success: false, error: err.message }
    }
  }

  // Initialize auth state
  loadUser()

  return {
    user,
    token,
    isLoading,
    error,
    isAuthenticated,
    register,
    login,
    logout,
    getProfile,
    updateProfile,
    clearAuth
  }
}
