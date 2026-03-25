<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-100">
    <!-- Header -->
    <div class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center shadow-lg">
              <span class="text-white text-xl font-bold">👤</span>
            </div>
            <h1 class="text-3xl font-bold bg-gradient-to-r from-purple-600 to-purple-700 bg-clip-text text-transparent">User Dashboard</h1>
          </div>
          <router-link to="/" class="text-purple-600 hover:text-purple-800">
            ← Back to Home
          </router-link>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Welcome Section -->
      <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 mb-8">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-gray-800">Welcome back, {{ user?.username || 'User' }}! 👋</h2>
            <p class="text-gray-600 mt-1">Manage your account and track your orders</p>
          </div>
          <div class="text-right">
            <p class="text-sm text-gray-500">Member since</p>
            <p class="font-semibold text-gray-700">{{ formatDate(user?.date_joined) }}</p>
          </div>
        </div>
      </div>

      <!-- Quick Stats -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="text-center">
            <div class="w-12 h-12 mx-auto bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-4">
              <span class="text-white text-xl">📦</span>
            </div>
            <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Orders</h3>
            <p class="text-3xl font-bold text-blue-600">{{ orderStats.totalOrders }}</p>
          </div>
        </div>
        
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="text-center">
            <div class="w-12 h-12 mx-auto bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center mb-4">
              <span class="text-green-500 text-xl">💰</span>
            </div>
            <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Spent</h3>
            <p class="text-3xl font-bold text-green-600">Tsh {{ orderStats.totalSpent.toLocaleString() }}</p>
          </div>
        </div>
        
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="text-center">
            <div class="w-12 h-12 mx-auto bg-gradient-to-br from-yellow-500 to-orange-600 rounded-xl flex items-center justify-center mb-4">
              <span class="text-yellow-500 text-xl">⏰</span>
            </div>
            <h3 class="text-lg font-semibold text-gray-600 mb-2">Pending Orders</h3>
            <p class="text-3xl font-bold text-yellow-600">{{ orderStats.pendingOrders }}</p>
          </div>
        </div>
        
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="text-center">
            <div class="w-12 h-12 mx-auto bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center mb-4">
              <span class="text-purple-500 text-xl">🎯</span>
            </div>
            <h3 class="text-lg font-semibold text-gray-600 mb-2">Completed</h3>
            <p class="text-3xl font-bold text-purple-600">{{ orderStats.completedOrders }}</p>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 mb-8">
        <!-- Recent Orders -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
          <div class="p-6 bg-gradient-to-r from-blue-50 to-blue-100 border-b border-gray-200">
            <div class="flex items-center justify-between">
              <h3 class="text-xl font-bold text-gray-800">Recent Orders</h3>
              <router-link to="/orders" class="text-blue-600 hover:text-blue-800 text-sm font-medium">
                View All →
              </router-link>
            </div>
          </div>
          <div class="p-6">
            <div v-if="recentOrders.length > 0" class="space-y-4">
              <div v-for="order in recentOrders" :key="order.id" class="flex justify-between items-center p-4 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors duration-300">
                <div>
                  <p class="font-semibold text-gray-800">{{ order.order_number || `Order #${order.id}` }}</p>
                  <p class="text-sm text-gray-600">{{ formatDate(order.created_at) }}</p>
                </div>
                <div class="text-right">
                  <p :class="getStatusClass(order.status)" class="px-3 py-1 rounded-full text-xs font-medium mb-2">
                    {{ order.status }}
                  </p>
                  <p class="font-bold text-gray-700">Tsh {{ Number(order.total_amount || order.total || 0).toLocaleString() }}</p>
                </div>
              </div>
            </div>
            <div v-else class="text-center py-8 text-gray-500">
              <span class="text-4xl mb-4 block">📦</span>
              <p>No orders yet</p>
              <router-link to="/" class="text-blue-600 hover:text-blue-800 mt-2 inline-block">
                Start Shopping →
              </router-link>
            </div>
          </div>
        </div>

        <!-- Quick Actions -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
          <div class="p-6 bg-gradient-to-r from-purple-50 to-purple-100 border-b border-gray-200">
            <h3 class="text-xl font-bold text-gray-800">Quick Actions</h3>
          </div>
          <div class="p-6">
            <div class="grid grid-cols-2 gap-4">
              <router-link
                to="/cart"
                class="flex flex-col items-center p-4 bg-blue-50 rounded-xl hover:bg-blue-100 transition-colors duration-300"
              >
                <span class="text-3xl mb-2">🛒</span>
                <span class="text-sm font-medium text-blue-800">View Cart</span>
              </router-link>
              
              <router-link
                to="/orders"
                class="flex flex-col items-center p-4 bg-green-50 rounded-xl hover:bg-green-100 transition-colors duration-300"
              >
                <span class="text-3xl mb-2">📋</span>
                <span class="text-sm font-medium text-green-800">My Orders</span>
              </router-link>
              
              <router-link
                to="/place-order"
                class="flex flex-col items-center p-4 bg-purple-50 rounded-xl hover:bg-purple-100 transition-colors duration-300"
              >
                <span class="text-3xl mb-2">🚀</span>
                <span class="text-sm font-medium text-purple-800">Place Order</span>
              </router-link>
              
              <button
                @click="handleLogout"
                class="flex flex-col items-center p-4 bg-red-50 rounded-xl hover:bg-red-100 transition-colors duration-300"
              >
                <span class="text-3xl mb-2">🚪</span>
                <span class="text-sm font-medium text-red-800">Logout</span>
              </button>
            </div>
          </div>
        </div>
      </div>

      <!-- Account Settings -->
      <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
        <div class="p-6 bg-gradient-to-r from-gray-50 to-gray-100 border-b border-gray-200">
          <h3 class="text-xl font-bold text-gray-800">Account Information</h3>
        </div>
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Username</label>
              <p class="text-gray-900 font-medium">{{ user?.username || 'N/A' }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Email</label>
              <p class="text-gray-900 font-medium">{{ user?.email || 'N/A' }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">First Name</label>
              <p class="text-gray-900 font-medium">{{ user?.first_name || 'Not set' }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Last Name</label>
              <p class="text-gray-900 font-medium">{{ user?.last_name || 'Not set' }}</p>
            </div>
          </div>
          
          <div class="mt-6 pt-6 border-t border-gray-200">
            <router-link to="/profile" class="inline-flex items-center px-4 py-2 bg-purple-600 text-white font-medium rounded-lg hover:bg-purple-700 transition-colors duration-300">
              Edit Profile →
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth'
import { useOrderManagement } from '../composables/useOrderManagement'
import Swal from 'sweetalert2'

export default {
  name: 'UserDashboard',
  setup() {
    const router = useRouter()
    const { user, logout } = useAuth()
    const orderManagement = useOrderManagement()
    
    const isLoading = ref(true)
    const recentOrders = ref([])
    
    // Computed properties for stats
    const orderStats = computed(() => {
      const orders = orderManagement.orders.value
      return {
        totalOrders: orders.length,
        totalSpent: orders.reduce((total, order) => total + (Number(order.total_amount || order.total || 0)), 0),
        pendingOrders: orders.filter(order => order.status === 'Pending').length,
        completedOrders: orders.filter(order => order.status === 'Delivered').length
      }
    })

    // Methods
    const formatDate = (dateString) => {
      if (!dateString) return 'Unknown'
      return new Date(dateString).toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric'
      })
    }

    const getStatusClass = (status) => {
      const statusClasses = {
        'Pending': 'bg-yellow-100 text-yellow-800',
        'Paid': 'bg-blue-100 text-blue-800',
        'Shipped': 'bg-purple-100 text-purple-800',
        'Delivered': 'bg-green-100 text-green-800',
        'Cancelled': 'bg-red-100 text-red-800'
      }
      return statusClasses[status] || 'bg-gray-100 text-gray-800'
    }

    const loadDashboardData = async () => {
      try {
        await orderManagement.loadOrderHistory()
        // Get recent orders (last 5)
        recentOrders.value = orderManagement.sortedOrders.value.slice(0, 5)
      } catch (error) {
        console.error('Error loading dashboard data:', error)
      } finally {
        isLoading.value = false
      }
    }

    const handleLogout = async () => {
      try {
        const result = await Swal.fire({
          title: 'Logout',
          text: 'Are you sure you want to logout?',
          icon: 'warning',
          showCancelButton: true,
          confirmButtonColor: '#3085d6',
          cancelButtonColor: '#d33',
          confirmButtonText: 'Yes, logout'
        })

        if (result.isConfirmed) {
          await logout()
          await Swal.fire('Logged Out', 'You have been logged out successfully', 'success')
          router.push('/')
        }
      } catch (error) {
        console.error('Logout error:', error)
        Swal.fire('Error', 'Failed to logout', 'error')
      }
    }

    onMounted(() => {
      loadDashboardData()
    })

    return {
      user,
      isLoading,
      recentOrders,
      orderStats,
      formatDate,
      getStatusClass,
      handleLogout
    }
  }
}
</script>
