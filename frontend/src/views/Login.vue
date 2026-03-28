<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-orange-50 flex items-center justify-center px-4">
    <!-- Background Pattern -->
    <div class="absolute inset-0 bg-[url('/images/pattern.svg')] opacity-5"></div>
    
    <!-- Login Container -->
    <div class="relative w-full max-w-md">
      <!-- Logo/Brand Section -->
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-r from-orange-500 to-orange-600 rounded-2xl shadow-lg mb-4">
          <span class="text-lg">📝</span>
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
                placeholder="Enter your password"
              >
              <button
                type="button"
                @click="showPassword = !showPassword"
                class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <span class="text-lg">📝</span>
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
              <span class="text-lg">📝</span>
              <span class="text-red-700 text-sm">{{ error }}</span>
            </div>
          </div>

          <!-- Success Message -->
          <div v-if="successMessage" class="bg-green-50 border border-green-200 rounded-lg p-4">
            <div class="flex items-center">
              <span class="text-lg">📝</span>
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
              <span class="text-lg">📝</span>
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
            <span class="text-lg">📝</span>
          </router-link>
        </div>
      </div>

      <!-- Back to Home -->
      <div class="text-center mt-6">
        <router-link
          to="/"
          class="inline-flex items-center text-gray-600 hover:text-gray-800 text-sm"
        >
          <span class="text-lg">📝</span>
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
