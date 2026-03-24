<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4">
      <div class="bg-white rounded-lg shadow-lg p-6">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">My Profile</h1>
        
        <!-- Profile Information -->
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h2 class="text-lg font-semibold text-gray-900 mb-4">Personal Information</h2>
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">First Name</label>
                <input
                  v-model="profile.first_name"
                  type="text"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500"
                  :disabled="isLoading"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Last Name</label>
                <input
                  v-model="profile.last_name"
                  type="text"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500"
                  :disabled="isLoading"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Email</label>
                <input
                  v-model="profile.email"
                  type="email"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500"
                  :disabled="isLoading"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Phone</label>
                <input
                  v-model="profile.phone"
                  type="tel"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500"
                  :disabled="isLoading"
                />
              </div>
            </div>
          </div>
          
          <div>
            <h2 class="text-lg font-semibold text-gray-900 mb-4">Account Information</h2>
            <div class="space-y-4">
              <div>
                <label class="block text-sm font-medium text-gray-700">Username</label>
                <input
                  v-model="profile.username"
                  type="text"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500"
                  :disabled="isLoading"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Role</label>
                <input
                  :value="profile.role"
                  type="text"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm bg-gray-50"
                  disabled
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700">Member Since</label>
                <input
                  :value="formatDate(profile.date_joined)"
                  type="text"
                  class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm bg-gray-50"
                  disabled
                />
              </div>
            </div>
          </div>
        </div>
        
        <!-- Address -->
        <div class="mt-6">
          <h2 class="text-lg font-semibold text-gray-900 mb-4">Address</h2>
          <div>
            <label class="block text-sm font-medium text-gray-700">Shipping Address</label>
            <textarea
              v-model="profile.address"
              rows="3"
              class="mt-1 block w-full px-3 py-2 border border-gray-300 rounded-md shadow-sm focus:outline-none focus:ring-orange-500 focus:border-orange-500"
              :disabled="isLoading"
              placeholder="Enter your shipping address"
            ></textarea>
          </div>
        </div>
        
        <!-- Messages -->
        <div v-if="error" class="mt-6 bg-red-50 border border-red-200 rounded-lg p-4">
          <div class="flex items-center">
            <svg class="w-5 h-5 text-red-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <span class="text-red-700 text-sm">{{ error }}</span>
          </div>
        </div>
        
        <div v-if="successMessage" class="mt-6 bg-green-50 border border-green-200 rounded-lg p-4">
          <div class="flex items-center">
            <svg class="w-5 h-5 text-green-400 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
            </svg>
            <span class="text-green-700 text-sm">{{ successMessage }}</span>
          </div>
        </div>
        
        <!-- Actions -->
        <div class="mt-6 flex justify-end space-x-4">
          <router-link
            to="/"
            class="px-4 py-2 border border-gray-300 rounded-md text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-orange-500"
          >
            Back to Home
          </router-link>
          <button
            @click="updateProfile"
            :disabled="isLoading"
            class="px-4 py-2 bg-orange-600 text-white rounded-md hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-orange-500 disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="isLoading">Updating...</span>
            <span v-else>Update Profile</span>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth'

export default {
  name: 'Profile',
  setup() {
    const router = useRouter()
    const { user, isAuthenticated, updateProfile: updateAuthProfile } = useAuth()
    
    const profile = ref({
      username: '',
      email: '',
      first_name: '',
      last_name: '',
      phone: '',
      address: '',
      role: '',
      date_joined: ''
    })
    
    const isLoading = ref(false)
    const error = ref('')
    const successMessage = ref('')

    // Load profile data
    const loadProfile = () => {
      if (user.value) {
        profile.value = { ...user.value }
      }
    }

    // Update profile
    const updateProfile = async () => {
      isLoading.value = true
      error.value = ''
      successMessage.value = ''

      try {
        const result = await updateAuthProfile(profile.value)
        
        if (result.success) {
          successMessage.value = 'Profile updated successfully!'
        } else {
          error.value = result.error || 'Failed to update profile'
        }
      } catch (err) {
        error.value = err.message || 'An error occurred while updating profile'
      } finally {
        isLoading.value = false
      }
    }

    // Format date
    const formatDate = (dateString) => {
      if (!dateString) return ''
      return new Date(dateString).toLocaleDateString()
    }

    onMounted(() => {
      if (!isAuthenticated.value) {
        router.push('/login')
        return
      }
      loadProfile()
    })

    return {
      profile,
      isLoading,
      error,
      successMessage,
      updateProfile,
      formatDate
    }
  }
}
</script>
