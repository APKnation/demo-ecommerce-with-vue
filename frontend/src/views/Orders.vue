<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-100">

    <!-- Orders Header -->
    <div class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center shadow-lg">
              <span class="text-white text-xl font-bold">📋</span>
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
            <span class="text-blue-500 animate-spin text-2xl">⏳</span>
          </div>
          <h2 class="text-2xl font-bold text-gray-800 mb-4">Loading your orders...</h2>
          <p class="text-gray-600">Please wait while we fetch your order history.</p>
        </div>
      </div>
      
      <!-- Error State -->
      <div v-else-if="error" class="text-center py-16">
        <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md mx-auto">
          <div class="w-16 h-16 mx-auto bg-gradient-to-br from-red-100 to-red-200 rounded-full flex items-center justify-center mb-6">
            <span class="text-red-500 text-2xl">⚠️</span>
          </div>
          <h2 class="text-2xl font-bold text-gray-800 mb-4">Error Loading Orders</h2>
          <p class="text-gray-600 mb-6">{{ error }}</p>
          <button @click="loadOrders" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 transform hover:scale-105 shadow-lg">
            <span class="text-blue-500 text-xl">🔄</span>
            Try Again
          </button>
        </div>
      </div>
      
      <!-- Empty State -->
      <div v-else-if="orders.length === 0" class="text-center py-16">
        <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md mx-auto">
          <div class="w-24 h-24 mx-auto bg-gradient-to-br from-blue-100 to-blue-200 rounded-full flex items-center justify-center mb-6">
            <span class="text-blue-500 text-xl">📋</span>
          </div>
          <h2 class="text-2xl font-bold text-gray-800 mb-4">No Orders Found</h2>
          <p class="text-gray-600 mb-6">You haven't placed any orders yet. Start shopping to create your first order!</p>
          
          <!-- Order Benefits -->
          <div class="bg-blue-50 rounded-xl p-6 mb-6">
            <h3 class="text-lg font-semibold text-blue-800 mb-4">Why Shop With Us?</h3>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-gradient-to-br from-blue-500 to-blue-600 rounded-lg flex items-center justify-center">
                  <span class="text-white text-xl">🛍</span>
                </div>
                <span class="text-gray-700">Fast and secure checkout</span>
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-gradient-to-br from-green-500 to-green-600 rounded-lg flex items-center justify-center">
                  <span class="text-white text-xl">💰</span>
                </div>
                <span class="text-gray-700">Order tracking and history</span>
              </div>
              <div class="flex items-center space-x-3">
                <div class="w-8 h-8 bg-gradient-to-br from-purple-500 to-purple-600 rounded-lg flex items-center justify-center">
                  <span class="text-white text-xl">📝</span>
                </div>
                <span class="text-gray-700">Easy reordering of past purchases</span>
              </div>
            </div>
          </div>
          
          <!-- Action Buttons -->
          <div class="flex flex-col sm:flex-row gap-4 justify-center">
            <router-link to="/" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-blue-500 to-blue-600 text-white font-semibold rounded-xl hover:from-blue-600 hover:to-blue-700 transition-all duration-300 transform hover:scale-105 shadow-lg">
              <span class="text-blue-500 text-xl mr-2">🛍</span>
              Start Shopping
            </router-link>
            <router-link to="/cart" class="inline-flex items-center px-6 py-3 bg-gray-200 text-gray-700 font-semibold rounded-xl hover:bg-gray-300 transition-colors duration-300">
              <span class="text-gray-500 text-xl mr-2">🛒</span>
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
                <span class="text-blue-500 text-xl">📋</span>
              </div>
              <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Orders</h3>
              <p class="text-3xl font-bold text-blue-600">{{ orders.length }}</p>
            </div>
          </div>
          
          <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
            <div class="text-center">
              <div class="w-12 h-12 mx-auto bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center mb-4">
                <span class="text-green-500 text-xl">💰</span>
              </div>
              <h3 class="text-lg font-semibold text-gray-600 mb-2">Total Spent</h3>
              <p class="text-3xl font-bold text-green-600">Tsh {{ totalSpent.toLocaleString() }}</p>
            </div>
          </div>
          
          <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 hover:shadow-xl transition-shadow duration-300">
            <div class="text-center">
              <div class="w-12 h-12 mx-auto bg-gradient-to-br from-yellow-500 to-orange-600 rounded-xl flex items-center justify-center mb-4">
                <span class="text-yellow-500 text-xl">⏰</span>
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
              <div class="flex justify-between items-start">
                <div>
                  <h3 class="text-xl font-bold text-gray-900 mb-2">
                    Order #{{ order?.order_number || order?.id || 'Unknown' }}
                  </h3>
                  <p class="text-sm text-gray-600 mb-1">
                    Placed on {{ formatDate(order?.created_at || order?.date) }}
                  </p>
                  <p class="text-sm text-gray-600">
                    Status: <span :class="getStatusClass(order?.status)">{{ order?.status || 'Unknown' }}</span>
                  </p>
                </div>
                <div class="text-right">
                  <p class="text-2xl font-bold text-blue-600">Tsh {{ Number(order?.total_amount || order?.total || 0).toLocaleString() }}</p>
                  <p class="text-sm text-gray-500">{{ order?.items?.length || 0 }} items</p>
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
                <div v-if="order.items && order.items.length > 0">
                  <div
                    v-for="(item, index) in order.items"
                    :key="index"
                    class="flex justify-between items-center p-3 bg-gray-50 rounded-xl hover:bg-gray-100 transition-colors duration-300"
                  >
                    <div class="flex items-center space-x-3">
                      <img
                        :src="getProductImageWithFallback(item.product)"
                        :alt="item.product?.title || item.product?.name || 'Unknown item'"
                        class="w-16 h-16 object-cover rounded-lg shadow-md"
                        @error="handleImageError"
                      >
                      <div>
                        <!-- Debug: Show actual data structure -->
                        <div class="text-xs text-gray-500 mb-1">DEBUG: {{ JSON.stringify(item) }}</div>
                        <span class="font-medium text-gray-800">{{ item.product?.title || item.product?.name || 'Unknown item' }}</span>
                        <span class="text-gray-600 ml-2">x{{ item.quantity || 0 }}</span>
                      </div>
                    </div>
                    <div class="text-right">
                      <span class="font-semibold text-gray-700">Tsh {{ Number(item.price || 0).toLocaleString() }}</span>
                    </div>
                  </div>
                </div>
                <div v-else class="text-center p-4 text-gray-500">
                  <p>No items found for this order</p>
                </div>
              </div>
            </div>
            
            <!-- Order Actions -->
            <div class="flex justify-end space-x-3 p-6 bg-gray-50 border-t border-gray-200">
              <!-- Status Update Buttons -->
              <div v-if="order.status === 'Pending'" class="flex space-x-2">
                <button
                  @click="markOrderAsPaid(order.id)"
                  class="bg-blue-500 text-white px-3 py-1 rounded text-sm hover:bg-blue-600 transition-colors"
                >
                  Mark Paid
                </button>
                <button
                  @click="cancelOrder(order.id)"
                  class="bg-red-500 text-white px-3 py-1 rounded text-sm hover:bg-red-600 transition-colors"
                >
                  Cancel
                </button>
              </div>
              <div v-else-if="order.status === 'Paid'" class="flex space-x-2">
                <button
                  @click="markOrderAsShipped(order.id)"
                  class="bg-purple-500 text-white px-3 py-1 rounded text-sm hover:bg-purple-600 transition-colors"
                >
                  Mark Shipped
                </button>
              </div>
              <div v-else-if="order.status === 'Shipped'" class="flex space-x-2">
                <button
                  @click="markOrderAsDelivered(order.id)"
                  class="bg-green-500 text-white px-3 py-1 rounded text-sm hover:bg-green-600 transition-colors"
                >
                  Mark Delivered
                </button>
              </div>
              
              <!-- Reorder Button -->
              <button
                @click="reorder(order.items)"
                class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-4 py-2 rounded-lg hover:from-blue-600 hover:to-blue-700 transition-all duration-300 transform hover:scale-105 flex items-center"
              >
                <span class="text-white text-xl">🛒</span>
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
import { useAuth } from '../composables/useAuth'
import { useOrderManagement } from '../composables/useOrderManagement'
import Swal from 'sweetalert2'

export default {
  name: 'Orders',
  setup() {
    const router = useRouter()
    const { isAuthenticated } = useAuth()
    const orderManagement = useOrderManagement()
    const cart = inject('cart', ref([]))
    const isLoading = ref(true)
    const error = ref('')
    const expandedOrders = ref([])

    // SweetAlert notification system
    const showNotificationMessage = (message, type = 'success') => {
      Swal.fire({
        icon: type === 'success' ? 'success' : type === 'error' ? 'error' : 'info',
        title: type === 'success' ? 'Success!' : type === 'error' ? 'Error!' : 'Notification',
        text: message,
        position: 'top-end',
        timer: 3000,
        toast: true,
        showConfirmButton: false,
        showCancelButton: false,
        customClass: {
          popup: 'swal2-popup'
        }
      })
    }

    // Load orders using order management
    const loadOrders = async () => {
      try {
        await orderManagement.loadOrderHistory()
      } catch (err) {
        console.error('Failed to load orders:', err)
        error.value = 'Failed to load orders'
      } finally {
        isLoading.value = false
      }
    }

    // Computed properties from order management
    const orders = computed(() => orderManagement.orders.value)
    const totalSpent = computed(() => orderManagement.totalSpent.value)
    const pendingOrders = computed(() => orderManagement.pendingOrders.value)
    const sortedOrders = computed(() => orderManagement.sortedOrders.value)

    const formatDate = (dateString) => {
      return orderManagement.formatDate(dateString)
    }

    const getStatusClass = (status) => {
      return orderManagement.getStatusClass(status)
    }

    // Order status management functions
    const updateOrderStatus = async (orderId, newStatus) => {
      try {
        const result = await orderManagement.updateOrderStatus(orderId, newStatus)
        showNotificationMessage(`Order status updated to ${newStatus}`, 'success')
        return result
      } catch (err) {
        showNotificationMessage('Failed to update order status', 'error')
        throw err
      }
    }

    const markOrderAsPaid = async (orderId) => {
      return updateOrderStatus(orderId, 'PAID')
    }

    const markOrderAsShipped = async (orderId) => {
      return updateOrderStatus(orderId, 'SHIPPED')
    }

    const markOrderAsDelivered = async (orderId) => {
      return updateOrderStatus(orderId, 'DELIVERED')
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
      console.log('toggleOrderDetails called with orderId:', orderId)
      console.log('Current expandedOrders:', expandedOrders.value)
      
      const index = expandedOrders.value.indexOf(orderId)
      if (index > -1) {
        // Order is expanded, so collapse it (remove from expanded list)
        expandedOrders.value.splice(index, 1)
        console.log('Collapsed order:', orderId, 'New expandedOrders:', expandedOrders.value)
      } else {
        // Order is collapsed, so expand it (add to expanded list)
        expandedOrders.value.push(orderId)
        console.log('Expanded order:', orderId, 'New expandedOrders:', expandedOrders.value)
      }
    }

    // Load orders on mount
    onMounted(() => {
      loadOrders()
    })

    // Image handling functions
    const getImageUrl = (imagePath) => {
      if (!imagePath) {
        return 'http://localhost:8000/media/products/default-product.jpg'
      }
      
      // If it's already a full URL, return as is
      if (imagePath.startsWith('http')) {
        return imagePath
      }
      
      // If it starts with /media/, it's already correct
      if (imagePath.startsWith('/media/')) {
        return `http://localhost:8000${imagePath}`
      }
      
      // If it's just a filename, construct full URL
      return `http://localhost:8000/media/products/${imagePath}`
    }

    const getProductImageWithFallback = (product) => {
      // If product has an image, use it
      if (product?.image) {
        return getImageUrl(product.image)
      }
      
      // If product has images array with items, use first one
      if (product?.images && product.images.length > 0) {
        return getImageUrl(product.images[0])
      }
      
      // Use category-based placeholder images
      const categoryName = product?.category?.name?.toLowerCase()
      const categoryImages = {
        'laptops': '/images/laptop-placeholder.jpg',
        'phones': '/images/phone-placeholder.jpg',
        'accessories': '/images/accessory-placeholder.jpg',
        'electronics': '/images/electronics-placeholder.jpg'
      }
      
      if (categoryName && categoryImages[categoryName]) {
        return categoryImages[categoryName]
      }
      
      // Final fallback
      return '/images/placeholder.jpg'
    }

    // Handle image loading errors
    const handleImageError = (event) => {
      event.target.src = 'http://localhost:8000/media/products/default-product.jpg'
    }

    return {
      orders,
      isLoading,
      error,
      expandedOrders,
      totalSpent,
      pendingOrders,
      sortedOrders,
      formatDate,
      getStatusClass,
      cancelOrder,
      reorder,
      toggleOrderDetails,
      getImageUrl,
      getProductImageWithFallback,
      handleImageError,
      updateOrderStatus,
      markOrderAsPaid,
      markOrderAsShipped,
      markOrderAsDelivered,
      loadOrders
    }
  }
}
</script>
