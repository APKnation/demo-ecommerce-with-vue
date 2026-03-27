<template>
  <div class="min-h-screen bg-gradient-to-br from-blue-50 via-white to-orange-50 flex items-center justify-center px-4">
    <!-- Background Pattern -->
    <div class="absolute inset-0 bg-[url('/images/pattern.svg')] opacity-5"></div>
    
    <!-- Register Container -->
    <div class="relative w-full max-w-md">
      <!-- Logo/Brand Section -->
      <div class="text-center mb-8">
        <div class="inline-flex items-center justify-center w-16 h-16 bg-gradient-to-r from-orange-500 to-orange-600 rounded-2xl shadow-lg mb-4">
          <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z"></path>
          </svg>
        </div>
        <h1 class="text-3xl font-bold text-gray-900 mb-2">Create Account</h1>
        <p class="text-gray-600">Join KAFUKA Store today</p>
      </div>

      <!-- Register Form -->
      <div class="bg-white rounded-2xl shadow-xl p-8 border border-gray-100">
        <form @submit.prevent="handleRegister" class="space-y-6">
          <!-- Name Fields -->
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label for="firstName" class="block text-sm font-medium text-gray-700 mb-2">
                First Name
              </label>
              <input
                id="firstName"
                v-model="form.firstName"
                type="text"
                required
                :disabled="isLoading"
                class="w-full px-3 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
            </div>
            <div>
              <label for="lastName" class="block text-sm font-medium text-gray-700 mb-2">
                Last Name
              </label>
              <input
                id="lastName"
                v-model="form.lastName"
                type="text"
                required
                :disabled="isLoading"
                class="w-full px-3 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
            </div>
          </div>

          <!-- Email Field -->
          <div>
            <label for="email" class="block text-sm font-medium text-gray-700 mb-2">
              Email Address
            </label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 12a4 4 0 10-8 0 4 4 0 008 0zm0 0v1.5a2.5 2.5 0 005 0V12a9 9 0 10-9 9m4.5-1.206a8.959 8.959 0 01-4.5 1.207"></path>
                </svg>
              </div>
              <input
                id="email"
                v-model="form.email"
                type="email"
                required
                :disabled="isLoading"
                class="w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
            </div>
          </div>

          <!-- Username Field -->
          <div>
            <label for="username" class="block text-sm font-medium text-gray-700 mb-2">
              Username
            </label>
            <div class="relative">
              <div class="absolute inset-y-0 left-0 pl-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M16 7a4 4 0 11-8 0 4 4 0 018 0zM12 14a7 7 0 00-7 7h14a7 7 0 00-7-7z"></path>
                </svg>
              </div>
              <input
                id="username"
                v-model="form.username"
                type="text"
                required
                :disabled="isLoading"
                class="w-full pl-10 pr-3 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
            </div>
          </div>

          <!-- Phone Field -->
          <div>
            <label for="phone" class="block text-sm font-semibold text-gray-800 mb-2">
              Phone Number
            </label>
            <input
              id="phone"
              v-model="form.phone"
              type="tel"
              :disabled="isLoading"
              class="w-full px-3 py-3 border-2 border-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 disabled:opacity-50 disabled:cursor-not-allowed bg-white"
              pattern="[+]?[0-9]{10,15}"
              placeholder="📞 +255 123 456 789"
              title="Enter phone number with country code (e.g., +255123456789)"
              @input="validatePhoneInput"
              @keydown="preventNonNumeric"
            >
          </div>

          <!-- Role Selection -->
          <div>
            <label for="role" class="block text-sm font-semibold text-gray-800 mb-2">
              Account Type
            </label>
            <div class="relative">
              <select
                id="role"
                v-model="form.role"
                required
                :disabled="isLoading"
                class="w-full px-3 py-3 border-2 border-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 disabled:opacity-50 disabled:cursor-not-allowed bg-white appearance-none cursor-pointer"
              >
                <option value="">Select account type...</option>
                <option value="customer">Customer - Buy products</option>
                <option value="vendor">Vendor - Sell products</option>
              </select>
              <div class="absolute inset-y-0 right-0 pr-3 flex items-center pointer-events-none">
                <svg class="h-5 w-5 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
                </svg>
              </div>
            </div>
            <p class="mt-2 text-xs text-gray-600">
              <span v-if="form.role === 'vendor'" class="text-orange-600 font-medium">
                📦 Vendors can add and sell products (requires admin approval)
              </span>
              <span v-else-if="form.role === 'customer'" class="text-blue-600 font-medium">
                🛍️ Customers can browse and purchase products
              </span>
              <span v-else class="text-gray-500">
                Choose how you want to use KAFUKA Store
              </span>
            </p>
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

          <!-- Confirm Password Field -->
          <div>
            <label for="confirmPassword" class="block text-sm font-semibold text-gray-800 mb-2">
              Confirm Password
            </label>
            <div class="relative">
              <input
                id="confirmPassword"
                v-model="form.confirmPassword"
                :type="showConfirmPassword ? 'text' : 'password'"
                required
                :disabled="isLoading"
                class="w-full px-3 pr-10 py-3 border-2 border-blue-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 disabled:opacity-50 disabled:cursor-not-allowed bg-white"
                minlength="8"
                title="Please confirm your password"
              >
              <button
                type="button"
                @click="showConfirmPassword = !showConfirmPassword"
                class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <svg class="h-5 w-5 text-gray-400 hover:text-gray-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path v-if="showConfirmPassword" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13.875 18.825A10.05 10.05 0 0112 19c-4.478 0-8.268-2.943-9.543-7a9.97 9.97 0 011.563-3.029m5.858.908a3 3 0 114.243 4.243M9.878 9.878l4.242 4.242M9.88 9.88l-3.29-3.29m7.532 7.532l3.29 3.29M3 3l3.59 3.59m0 0A9.953 9.953 0 0112 5c4.478 0 8.268 2.943 9.543 7a10.025 10.025 0 01-4.132 5.411m0 0L21 21"></path>
                  <g v-else>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                  </g>
                </svg>
              </button>
            </div>
          </div>
          <div v-if="form.confirmPassword && !passwordsMatch" class="mt-1 text-xs text-red-600">
              Passwords do not match
            </div>

          <!-- Terms and Conditions -->
          <div>
            <label class="flex items-start">
              <input
                v-model="form.agreeTerms"
                type="checkbox"
                required
                :disabled="isLoading"
                class="w-4 h-4 text-orange-600 border-gray-300 rounded focus:ring-orange-500 mt-1"
              >
              <span class="ml-2 text-sm text-gray-600">
                I agree to the 
                <a href="#" class="text-orange-600 hover:text-orange-700 font-medium">Terms of Service</a>
                and 
                <a href="#" class="text-orange-600 hover:text-orange-700 font-medium">Privacy Policy</a>
              </span>
            </label>
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

          <!-- Register Button -->
          <button
            type="submit"
            :disabled="isLoading || !isFormValid"
            class="w-full bg-gradient-to-r from-orange-500 to-orange-600 text-white font-semibold py-3 px-4 rounded-lg hover:from-orange-600 hover:to-orange-700 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2 disabled:opacity-50 disabled:cursor-not-allowed transition-all duration-200 transform hover:scale-[1.02]"
          >
            <span v-if="isLoading" class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Creating account...
            </span>
            <span v-else>Create Account</span>
          </button>
        </form>

        <!-- Divider -->
        <div class="relative my-6">
          <div class="absolute inset-0 flex items-center">
            <div class="w-full border-t border-gray-300"></div>
          </div>
          <div class="relative flex justify-center text-sm">
            <span class="px-4 bg-white text-gray-500">Already have an account?</span>
          </div>
        </div>

        <!-- Login Link -->
        <div class="text-center">
          <router-link
            to="/login"
            class="inline-flex items-center text-orange-600 hover:text-orange-700 font-medium"
          >
            Sign in instead
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
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth'

export default {
  name: 'Register',
  setup() {
    const router = useRouter()
    const { register, isLoading, error } = useAuth()
    
    const form = ref({
      firstName: '',
      lastName: '',
      email: '',
      username: '',
      phone: '',
      role: '', // Add role selection
      password: '',
      confirmPassword: '',
      agreeTerms: false
    })
    
    const showPassword = ref(false)
    const showConfirmPassword = ref(false)
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

    const passwordsMatch = computed(() => {
      return form.value.password === form.value.confirmPassword
    })

    const isFormValid = computed(() => {
      return (
        form.value.firstName &&
        form.value.lastName &&
        form.value.email &&
        form.value.username &&
        form.value.role && // Add role validation
        form.value.password &&
        form.value.confirmPassword &&
        passwordsMatch.value &&
        form.value.agreeTerms
      )
    })

    const handleRegister = async () => {
      if (!isFormValid.value) return
      
      successMessage.value = ''
      
      const result = await register({
        first_name: form.value.firstName,
        last_name: form.value.lastName,
        email: form.value.email,
        username: form.value.username,
        phone: form.value.phone,
        role: form.value.role, // Include role selection
        password: form.value.password,
        password_confirm: form.value.confirmPassword
      })

      if (result.success) {
        successMessage.value = 'Account created successfully! Please login to continue.'
        
        // Redirect to login after a short delay
        setTimeout(() => {
          router.push('/login')
        }, 2000)
      }
    }

    return {
      form,
      showPassword,
      showConfirmPassword,
      isLoading,
      error,
      successMessage,
      passwordsMatch,
      isFormValid,
      handleRegister,
      preventNonNumeric,
      validatePhoneInput
    }
  }
}
</script>
