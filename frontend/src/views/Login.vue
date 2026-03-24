<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-orange-50 flex items-center justify-center px-4">
    <!-- Background Pattern -->
    <div class="absolute inset-0 bg-[url('/images/pattern.svg')] opacity-5"></div>
    
    <!-- Login Container -->
    <div class="relative w-full max-w-md">
      <!-- Logo/Brand Section -->
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-r from-orange-500 to-orange-600 rounded-2xl shadow-lg mb-4">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 11V7a4 4 0 00-8 0v4M5 9h14l1 12H4L5 9z"></path>
          </svg>
        </div>
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Welcome Back</h1>
        <p class="text-gray-600">Sign in with your phone number and password</p>
        <p class="text-sm text-gray-500 mt-1">For customers, authors, and admins</p>
      </div>

      <!-- Login Form -->
      <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
        <form @submit.prevent="handleLogin" class="space-y-6">
          <!-- Phone Number Field -->
          <div>
            <label for="phone" class="block text-sm font-semibold text-gray-800 mb-2">
              Phone Number
            </label>
            <input
              id="phone"
              v-model="form.phone"
              type="tel"
              required
              :disabled="isLoading"
              class="w-full px-3 py-3 border-2 border-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 disabled:opacity-50 disabled:cursor-not-allowed bg-white"
              pattern="[+]?[0-9]{10,15}"
              placeholder=" +255 123 456 789"
              title="Enter phone number with country code (e.g., +255123456789)"
              @input="validatePhoneInput"
              @keydown="preventNonNumeric"
            >
          </div>

          <!-- Password Field -->
          <div>
            <label for="password" class="block text-sm font-semibold text-gray-800 mb-2">
              Password
            </label>
            <div class="relative">
              <input
                id="password"
                v-model="form.password"
                :type="showPassword ? 'text' : 'password'"
                required
                :disabled="isLoading"
                class="w-full px-3 pr-10 py-3 border-2 border-blue-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed bg-white"
                minlength="8"
                title="Password must be at least 8 characters long"
              >
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <svg class="h-5 w-5 text-gray-400 hover:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path v-if="showPassword" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path>
                  <g v-else>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                  </g>
                </svg>
              </button>
            </div>
          </div>

          <!-- Remember Me & Forgot Password -->
          <div class="flex items-center justify-between">
            <label class="flex items-center">
              <input
                v-model="form.rememberMe"
                type="checkbox"
                class="w-4 h-4 text-orange-600 border-gray-300 rounded focus:ring-orange-500"
              >
              <span class="ml-2 text-sm text-gray-600">Remember me</span>
            </label>
            <a href="#" class="text-sm text-orange-600 hover:text-orange-700 font-medium">
              Forgot password?
            </a>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4">
            <div class="flex items-center">
              <svg class="w-5 h-5 text-red-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <span class="text-red-700 text-sm">{{ error }}</span>
            </div>
          </div>

          <!-- Success Message -->
          <div v-if="successMessage" class="bg-green-50 border border-green-200 rounded-lg p-4">
            <div class="flex items-center">
              <svg class="w-5 h-5 text-green-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <span class="text-green-700 text-sm">{{ successMessage }}</span>
            </div>
          </div>

          <!-- Login Button -->
          <button
            type="submit"
            :disabled="isLoading"
            class="w-full bg-gradient-to-r from-orange-500 to-orange-600 text-white font-semibold py-3 px-4 rounded-lg hover:from-orange-600 hover:to-orange-700 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-[1.02]"
          >
            <span v-if="isLoading" class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Signing in...
            </span>
            <span v-else>Sign In</span>
          </button>
        </form>

        <!-- Divider -->
        <div class="relative my-6">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-300"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-4 bg-white text-gray-500">New to KAFUKA Store?</span>
          </div>
        </div>

        <!-- Register Link -->
        <div class="text-center">
          <router-link
            to="/register"
            class="inline-flex items-center text-orange-600 hover:text-orange-700 font-medium"
          >
            Create an account
            <svg class="ml-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 8l4 4m0 0l-4 4m4-4H3"></path>
            </svg>
          </router-link>
        </div>
      </div>

      <!-- Back to Home -->
      <div class="text-center mt-6">
        <router-link
          to="/"
          class="inline-flex items-center text-gray-600 hover:text-gray-800 text-sm"
        >
          <svg class="mr-2 w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"></path>
          </svg>
          Back to Home
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth'

export default {
  name: 'Login',
  setup() {
    const router = useRouter()
    const { login, isLoading, error } = useAuth()
    
    const form = ref({
      phone: '',
      password: '',
      rememberMe: false
    })
    
    const showPassword = ref(false)
    const successMessage = ref('')

    // Phone number validation functions
    const preventNonNumeric = (event) => {
      // Allow: backspace, delete, tab, escape, enter, + sign, numbers
      const allowedKeys = ['Backspace', 'Delete', 'Tab', 'Escape', 'Enter', '+']
      const isNumber = /^[0-9]$/.test(event.key)
      
      if (!allowedKeys.includes(event.key) && !isNumber) {
        event.preventDefault()
      }
    }

    const validatePhoneInput = (event) => {
      // Remove any non-numeric characters except + at the beginning
      let value = event.target.value
      
      // Allow + only at the beginning
      if (value.includes('+')) {
        value = '+' + value.replace(/\D/g, '').replace(/^\+/, '')
      } else {
        value = value.replace(/\D/g, '')
      }
      
      // Update the form value
      form.value.phone = value
    }

    const handleLogin = async () => {
      successMessage.value = ''
      
      const result = await login({
        phone: form.value.phone, // Use phone number for login
        password: form.value.password
      })

      if (result.success) {
        successMessage.value = 'Login successful! Redirecting...'
        
        // Redirect after a short delay to show success message
        setTimeout(() => {
          // Check user role and redirect accordingly
          const userRole = result.data?.user?.role
          
          if (userRole === 'admin') {
            // Redirect admin to admin panel
            router.push('/admin')
          } else {
            // Redirect customer/author to intended page or home
            const redirect = router.currentRoute.value.query.redirect || '/'
            router.push(redirect)
          }
        }, 1000)
      }
    }

    return {
      form,
      showPassword,
      isLoading,
      error,
      successMessage,
      handleLogin,
      preventNonNumeric,
      validatePhoneInput
    }
  }
}
</script>
