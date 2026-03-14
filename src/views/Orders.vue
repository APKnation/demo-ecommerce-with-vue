<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-100">
    <!-- Vue Notification Component -->
    <div v-if="showLocalNotification" class="fixed top-4 right-4 bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-3 rounded-xl shadow-2xl z-50 transition-all duration-300 transform hover:scale-105">
      <div class="flex items-center">
        <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        {{ localNotification }}
      </div>
    </div>

    <!-- Orders Header -->
    <div class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2 2v10a2 2 0 002 2h6a2 2 0 002-2V9a2 2 0 00-2-2H9z"></path>
              </svg>
            </div>
            <h1 class="text-3xl font-bold bg-gradient-to-r from-blue-600 to-blue-700 bg-clip-text text-transparent">Order History</h1>
          </div>
          <div class="flex items-center space-x-2">
            <span class="text-gray-500">{{ orders.length }} order{{ orders.length !== 1 ? 's' : '' }}</span>
            <span class="text-gray-400">•</span>
            <span class="font-semibold text-gray-700">Tsh {{ totalSpent.toLocaleString() }}</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Loading State -->
      <div v-if="isLoading" class="text-center py-16">
        <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md mx-auto">
          <div class="w-16 h-16 mx-auto bg-gradient-to-br from-blue-100 to-blue-200 rounded-full flex items-center justify-center mb-6">
            <svg class="w-8 h-8 text-blue-500 animate-spin" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 4v2.618A2 2 0 002 2.618V9a2 2 0 002-2V4.382A2 2 0 002 2.618L6.618 9.382A2 2 0 019.382 12H20a2 2 0 002 2v2.618A2 2 0 002 2.618L17.382 19.618A2 2 0 011.618 20H9a2 2 0 00-2-2V9a2 2 0 00-2-2H4.382z"></path>
            </svg>
          </div>
          <h2 class="text-2xl font-bold text-gray-800 mb-4">Loading your orders...</h2>
          <p class="text-gray-600">Please wait while we fetch your order history.</p>
        </div>
      </div>
      
      <!-- Empty State -->
      <div v-else-if="orders.length === 0" class="text-center py-16">
        <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md mx-auto">
          <div class="w-24 h-24 mx-auto bg-gradient-to-br from-blue-100 to-blue-200 rounded-full flex items-center justify-center mb-6">
            <svg class="w-12 h-12 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2 2v10a2 2 0 002 2h6a2 2 0 002-2V9a2 2 0 00-2-2H9z"></path>
            </svg>
          </div>
          <h2 class="text-2xl font-bold text-gray-800 mb-4">No Orders Found</h2>
          <p class="text-gray-600 mb-6">You haven't placed any orders yet. Start shopping to create your first order!</p>
          
          <!-- Order Benefits -->
          <div class="bg-blue-50 rounded-xl p-6 mb-6">
            <h3 class="text-lg font-semibold text-blue-800 mb-4">Why Shop With Us?</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <span class="text-gray-700">Fast and secure checkout</span>
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-gradient-to-br from-green-500 to-green-600 rounded-lg flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <span class="text-gray-700">Order tracking and history</span>
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <span class="text-gray-700">Easy reordering of past purchases</span>
              </div>
            </div>
          </div>
          
          <!-- Action Buttons -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link to="/" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 transform hover:scale-105 shadow-lg">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
              Start Shopping
            </router-link>
            <router-link to="/cart" class="inline-flex items-center px-6 py-3 bg-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-300 transition-colors duration-300">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
              View Cart
            </router-link>
          </div>
        </div>
      </div>
      
      <!-- Orders Content -->
      <div v-else class="space-y-6">
        <!-- Order Statistics -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
            <div class="text-center">
              <div class="w-12 h-12 mx-auto bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2 2v10a2 2 0 002 2h6a2 2 0 002-2V9a2 2 0 00-2-2H9z"></path>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Orders</h3>
              <p class="text-3xl font-bold text-blue-600">{{ orders.length }}</p>
            </div>
          </div>
          
          <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
            <div class="text-center">
              <div class="w-12 h-12 mx-auto bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 1.343-1.343A5.002 5.002 0 013.657 6.66l-6.314 6.314a5.002 5.002 0 016.657 3.343A5.002 5.002 0 013.657 6.66z"></path>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Spent</h3>
              <p class="text-3xl font-bold text-green-600">Tsh {{ totalSpent.toLocaleString() }}</p>
            </div>
          </div>
          
          <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
            <div class="text-center">
              <div class="w-12 h-12 mx-auto bg-gradient-to-br from-yellow-500 to-orange-600 rounded-xl flex items-center justify-center mb-4">
                <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m0 0l-6-6"></path>
                </svg>
              </div>
              <h3 class="text-lg font-semibold text-gray-600 mb-2">Pending Orders</h3>
              <p class="text-3xl font-bold text-yellow-600">{{ pendingOrders }}</p>
            </div>
          </div>
        </div>
      
        <!-- Orders List -->
        <div class="space-y-6">
          <div
            v-for="order in sortedOrders"
            :key="order.id"
            class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden hover:shadow-xl transition-all duration-300 group"
          >
            <!-- Order Header -->
            <div class="p-6 bg-gradient-to-r from-gray-50 to-blue-50 border-b border-gray-200">
              <div class="flex justify-between items-center">
                <div>
                  <h3 class="text-xl font-bold text-gray-800">Order {{ order.id }}</h3>
                  <p class="text-sm text-gray-600 flex items-center">
                    <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m4 0h4M0 4v14a2 2 0 002 2h4a2 2 0 002-2V7a2 2 0 00-2-2H8z"></path>
                    </svg>
                    {{ formatDate(order.date) }}
                  </p>
                </div>
                <div class="text-right">
                  <p class="text-2xl font-bold text-blue-600">Tsh {{ (order?.total || 0).toLocaleString() }}</p>
                  <span :class="getStatusClass(order?.status || 'Unknown')" class="inline-block text-sm px-4 py-2 rounded-full font-semibold">
                    {{ order?.status || 'Unknown' }}
                  </span>
                </div>
              </div>
            </div>
            
            <!-- Order Items -->
            <div class="p-6">
              <div class="flex justify-between items-center mb-4">
                <h4 class="font-semibold text-gray-700">Order Items ({{ order?.items?.length || 0 }})</h4>
                <button
                  @click="toggleOrderDetails(order.id)"
                  class="text-blue-600 hover:text-blue-800 text-sm font-medium bg-blue-50 hover:bg-blue-100 px-4 py-2 rounded-lg transition-colors duration-300"
                >
                  {{ expandedOrders.includes(order.id) ? 'Hide Details' : 'Show Details' }}
                </button>
              </div>
              
              <!-- Expandable Order Details -->
              <div v-show="expandedOrders.includes(order.id)" class="space-y-2">
                <div
                  v-for="(item, index) in (order?.items || [])"
                  :key="index"
                  class="flex justify-between items-center p-3 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors duration-300"
                >
                  <div class="flex items-center space-x-3">
                    <img
                      :src="item.image"
                      :alt="item.name"
                      class="w-16 h-16 object-cover rounded-lg shadow-md"
                    >
                    <div>
                      <span class="font-medium text-gray-800">{{ item?.name || 'Unknown item' }}</span>
                      <span class="text-gray-600 ml-2">x{{ item?.quantity || 0 }}</span>
                    </div>
                  </div>
                  <div class="text-right">
                    <p class="font-semibold text-gray-700">Tsh {{ ((item?.price || 0) * (item?.quantity || 0)).toLocaleString() }}</p>
                  </div>
                </div>
              </div>
            </div>
            
            <!-- Order Actions -->
            <div class="flex justify-end space-x-3 p-6 bg-gray-50 border-t border-gray-200">
              <button
                v-if="order.status === 'Pending'"
                @click="cancelOrder(order.id)"
                class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors duration-300 flex items-center"
              >
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 01-2.828 0H5a2 2 0 00-2 828 0l5.694 11.656a1 1 0 00.707.707 1.707z"></path>
                </svg>
                Cancel Order
              </button>
              <button
                @click="reorder(order.items)"
                class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-4 py-2 rounded-lg hover:from-blue-600 hover:to-blue-700 transition-all duration-300 transform hover:scale-105 flex items-center"
              >
                <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                Reorder Items
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, inject, onMounted } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'Orders',
  setup() {
    const router = useRouter()
    const orders = ref([])
    const cart = inject('cart', ref([]))
    const notification = inject('notification', ref(''))
    const localNotification = ref('')
    const showLocalNotification = ref(false)
    const isLoading = ref(true)
    const expandedOrders = ref([])

    // Vue notification system
    const showNotificationMessage = (message) => {
      localNotification.value = message
      showLocalNotification.value = true
      setTimeout(() => {
        showLocalNotification.value = false
        localNotification.value = ''
      }, 3000)
    }

    // Load orders from localStorage
    const loadOrders = async () => {
      isLoading.value = true
      try {
        const savedOrders = localStorage.getItem('orders')
        if (savedOrders) {
          orders.value = JSON.parse(savedOrders)
        } else {
          orders.value = []
        }
      } catch (error) {
        console.error('Error loading orders:', error)
        orders.value = []
      } finally {
        isLoading.value = false
      }
    }

    const totalSpent = computed(() => {
      return orders.value.reduce((total, order) => total + (order?.total || 0), 0)
    })

    const pendingOrders = computed(() => {
      return orders.value.filter(order => order?.status === 'Pending').length
    })

    const sortedOrders = computed(() => {
      return [...orders.value].sort((a, b) => new Date(b?.date || 0) - new Date(a?.date || 0))
    })

    const formatDate = (dateString) => {
      if (!dateString) return 'Unknown date'
      try {
        const date = new Date(dateString)
        if (isNaN(date.getTime())) return 'Invalid date'
        return date.toLocaleDateString('en-US', {
          year: 'numeric',
          month: 'long',
          day: 'numeric',
          hour: '2-digit',
          minute: '2-digit'
        })
      } catch (error) {
        return 'Invalid date'
      }
    }

    const getStatusClass = (status) => {
      switch(status) {
        case 'Pending':
          return 'bg-yellow-100 text-yellow-800'
        case 'Processing':
          return 'bg-blue-100 text-blue-800'
        case 'Completed':
          return 'bg-green-100 text-green-800'
        case 'Cancelled':
          return 'bg-red-100 text-red-800'
        default:
          return 'bg-gray-100 text-gray-800'
      }
    }

    const cancelOrder = (orderId) => {
      const orderIndex = orders.value.findIndex(order => order.id === orderId)
      if (orderIndex !== -1) {
        orders.value[orderIndex].status = 'Cancelled'
        localStorage.setItem('orders', JSON.stringify(orders.value))
        showNotificationMessage('Order cancelled successfully')
      }
    }

    const reorder = (items) => {
      if (!items || !Array.isArray(items)) {
        showNotificationMessage('No items to reorder')
        return
      }
      
      // Clear existing cart
      cart.value = []
      
      // Add items from order to cart
      items.forEach(item => {
        if (item && item.name) {
          cart.value.push({ ...item })
        }
      })
      
      // Save cart
      localStorage.setItem('cart', JSON.stringify(cart.value))
      
      showNotificationMessage('Items added to cart successfully')
      router.push('/cart')
    }

    const toggleOrderDetails = (orderId) => {
      const index = expandedOrders.value.indexOf(orderId)
      if (index > -1) {
        expandedOrders.value.push(orderId)
      } else {
        expandedOrders.value.splice(index, 1)
      }
    }

    // Load orders on mount
    onMounted(() => {
      loadOrders()
    })

    return {
      orders,
      isLoading,
      localNotification,
      showLocalNotification,
      expandedOrders,
      totalSpent,
      pendingOrders,
      sortedOrders,
      formatDate,
      getStatusClass,
      cancelOrder,
      reorder,
      toggleOrderDetails
    }
  }
}
</script>
