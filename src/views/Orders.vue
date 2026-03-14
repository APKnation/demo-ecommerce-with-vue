<template>
  <div>
    <!-- Vue Notification Component -->
    <div v-if="showLocalNotification" class="fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300 transform">
      {{ localNotification }}
    </div>

    <h1 class="text-3xl font-bold mb-8">Order History</h1>
    
    <!-- Loading State -->
    <div v-if="isLoading" class="text-center py-12">
      <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
      <p class="text-gray-500 mt-4">Loading orders...</p>
    </div>
    
    <!-- Empty State -->
    <div v-else-if="orders.length === 0" class="text-center py-12">
      <div class="mb-8">
        <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
        </svg>
        <h2 class="text-2xl font-bold text-gray-700 mb-4">No Orders Found</h2>
        <p class="text-gray-500 text-lg mb-6">You haven't placed any orders yet. Start shopping to create your first order!</p>
        
        <!-- Order Benefits -->
        <div class="bg-blue-50 rounded-lg p-6 mb-6 max-w-md mx-auto">
          <h3 class="text-lg font-semibold text-blue-800 mb-3">Why Shop With Us?</h3>
          <div class="text-left space-y-2">
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
              </svg>
              <span class="text-gray-700">Fast and secure checkout</span>
            </div>
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
              </svg>
              <span class="text-gray-700">Order tracking and history</span>
            </div>
            <div class="flex items-center space-x-2">
              <svg class="w-5 h-5 text-blue-600" fill="currentColor" viewBox="0 0 20 20">
                <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
              </svg>
              <span class="text-gray-700">Easy reordering of past purchases</span>
            </div>
          </div>
        </div>
        
        <!-- Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-4 justify-center">
          <router-link to="/" class="btn btn-primary flex items-center justify-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            Start Shopping
          </router-link>
          <router-link to="/cart" class="btn btn-secondary flex items-center justify-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            View Cart
          </router-link>
        </div>
      </div>
    </div>
    
    <!-- Orders Content -->
    <div v-else>
      <!-- Order Statistics -->
      <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
        <div class="card text-center">
          <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Orders</h3>
          <p class="text-3xl font-bold text-blue-600">{{ orders.length }}</p>
        </div>
        
        <div class="card text-center">
          <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Spent</h3>
          <p class="text-3xl font-bold text-green-600">Tsh {{ totalSpent.toLocaleString() }}</p>
        </div>
        
        <div class="card text-center">
          <h3 class="text-lg font-semibold text-gray-600 mb-2">Pending Orders</h3>
          <p class="text-3xl font-bold text-yellow-600">{{ pendingOrders }}</p>
        </div>
      </div>
      
      <!-- Orders List -->
      <div class="space-y-6">
        <div
          v-for="order in sortedOrders"
          :key="order.id"
          class="card hover:shadow-lg transition-shadow duration-300"
        >
          <div class="flex justify-between items-start mb-4">
            <div>
              <h3 class="text-xl font-semibold">Order {{ order.id }}</h3>
              <p class="text-gray-600">{{ formatDate(order.date) }}</p>
            </div>
            <div class="text-right">
              <p class="text-2xl font-bold text-blue-600">Tsh {{ order.total.toLocaleString() }}</p>
              <span :class="getStatusClass(order.status)" class="inline-block text-sm px-3 py-1 rounded-full mt-2">
                {{ order.status }}
              </span>
            </div>
          </div>
          
          <!-- Order Items -->
          <div class="border-t pt-4">
            <h4 class="font-semibold mb-3">Order Items:</h4>
            <div class="space-y-2">
              <div
                v-for="(item, index) in order.items"
                :key="index"
                class="flex justify-between items-center p-3 bg-gray-50 rounded"
              >
                <div>
                  <span class="font-medium">{{ item.name }}</span>
                  <span class="text-gray-600 ml-2">x{{ item.quantity }}</span>
                </div>
                <span class="font-semibold">Tsh {{ (item.price * item.quantity).toLocaleString() }}</span>
              </div>
            </div>
          </div>
          
          <!-- Order Actions -->
          <div class="flex justify-end space-x-3 mt-6 pt-4 border-t">
            <router-link
              :to="`/order/${order.id}`"
              class="btn btn-secondary"
            >
              View Details
            </router-link>
            <button
              v-if="order.status === 'Pending'"
              @click="cancelOrder(order.id)"
              class="btn btn-danger"
            >
              Cancel Order
            </button>
            <button
              @click="reorder(order.items)"
              class="btn btn-primary"
            >
              Reorder
            </button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, inject } from 'vue'
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
        orders.value = JSON.parse(localStorage.getItem('orders')) || []
        showNotificationMessage('Orders loaded successfully')
      } catch (error) {
        showNotificationMessage('Error loading orders')
      } finally {
        isLoading.value = false
      }
    }

    const totalSpent = computed(() => {
      return orders.value.reduce((total, order) => total + order.total, 0)
    })

    const pendingOrders = computed(() => {
      return orders.value.filter(order => order.status === 'Pending').length
    })

    const sortedOrders = computed(() => {
      return [...orders.value].sort((a, b) => new Date(b.date) - new Date(a.date))
    })

    const formatDate = (dateString) => {
      const date = new Date(dateString)
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
      })
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
      // Clear existing cart
      cart.value = []
      
      // Add items from order to cart
      items.forEach(item => {
        cart.value.push({ ...item })
      })
      
      // Save cart
      localStorage.setItem('cart', JSON.stringify(cart.value))
      
      showNotificationMessage('Items added to cart successfully')
      router.push('/cart')
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
      totalSpent,
      pendingOrders,
      sortedOrders,
      formatDate,
      getStatusClass,
      cancelOrder,
      reorder
    }
  }
}
</script>
