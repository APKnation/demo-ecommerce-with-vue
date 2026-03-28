<template>
  <div class="min-h-screen bg-section">

    <!-- Cart Header -->
    <div class="bg-white shadow-sm border-b border-neutral-200">
      <div class="container py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-600 rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4 8H5.4M7 13l2.293 2.293c.63.63.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
            </div>
            <h1 class="text-3xl font-bold text-gradient">Shopping Cart</h1>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-neutral-500">{{ totalItems?.value || 0 }} item{{ (totalItems?.value || 0) !== 1 ? 's' : '' }}</span>
            <span class="text-neutral-400">•</span>
            <span class="font-semibold text-neutral-700">Tsh {{ (totalPrice?.value || 0).toLocaleString() }}</span>
            <button
              v-if="totalItems?.value > 0"
              @click="clearCart"
              class="ml-4 px-4 py-2 bg-red-500 text-white text-sm font-medium rounded-lg hover:bg-red-600 transition-colors duration-300"
            >
              Clear Cart
            </button>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Content -->
    <div class="container py-8">
      <!-- Empty State -->
      <div v-if="totalItems?.value === 0" class="text-center py-16">
        <div class="card card-elevated p-8 max-w-md mx-auto">
          <div class="w-24 h-24 mx-auto bg-gradient-to-br from-orange-100 to-orange-200 rounded-full flex items-center justify-center mb-6">
            <svg class="w-12 h-12 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4 8H5.4M7 13l2.293 2.293c.63.63.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
          </div>
          <h2 class="text-2xl font-bold text-neutral-800 mb-4">Your cart is empty</h2>
          <p class="text-neutral-600 mb-6">Start shopping to add some amazing products to your cart!</p>
          <router-link to="/" class="btn btn-primary">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4 8H5.4M7 13l2.293 2.293c.63.63.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            Continue Shopping
          </router-link>
        </div>
      </div>
      
      <!-- Cart Items -->
      <div v-else-if="isLoading" class="flex justify-center items-center py-12">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-orange-500"></div>
        <span class="ml-4 text-gray-600">Loading cart...</span>
      </div>
      
      <!-- Cart Items -->
      <div v-else class="space-y-6">
        <!-- Cart Items List -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
          <div class="divide-y divide-gray-200">
            <div
              v-for="(item, index) in (unifiedCart?.cartItems?.value || [])"
              :key="index"
              class="p-6 hover:bg-gradient-to-r from-orange-50 to-yellow-50 transition-colors duration-300 group"
            >
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-4">
                  <img
                    :src="getImageUrl(item.image || item.product?.image)"
                    :alt="item.name || item.product?.title"
                    class="w-20 h-20 object-cover rounded-lg shadow-md group-hover:scale-110 transition-transform duration-300"
                    @error="handleImageError"
                  >
                  <div>
                    <h3 class="text-lg font-semibold text-gray-900 group-hover:text-orange-600 transition-colors duration-300">
                      {{ item.name || item.product?.title }}
                    </h3>
                    <p class="text-sm text-gray-600">{{ item.category || item.product?.category?.name }}</p>
                    <p class="text-lg font-bold text-blue-600">Tsh {{ Number(item.price || item.product?.price).toLocaleString() }}</p>
                  </div>
                </div>
                
                <!-- Quantity Controls -->
                <div class="flex items-center space-x-3">
                  <button
                    @click="updateQuantity(index, -1)"
                    class="w-8 h-8 bg-red-500 text-white rounded-lg hover:bg-red-600 transition-colors duration-300 flex items-center justify-center"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 12H4"></path>
                    </svg>
                  </button>
                  <span class="px-3 font-semibold text-gray-700">{{ item.quantity }}</span>
                  <button
                    @click="updateQuantity(index, 1)"
                    class="w-8 h-8 bg-green-500 text-white rounded-lg hover:bg-green-600 transition-colors duration-300 flex items-center justify-center"
                  >
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6v6m0 6v6m0 6V6"></path>
                    </svg>
                  </button>
                </div>
                
                <!-- Item Total & Remove -->
                <div class="text-right">
                  <p class="text-lg font-bold text-gray-800 mb-2">Tsh {{ (Number(item.price || item.product?.price) * item.quantity).toLocaleString() }}</p>
                  <button
                    @click="removeFromCart(index)"
                    class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors duration-300 flex items-center"
                  >
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 01-2.828 0H5a2 2 0 00-2.828 0l5.694 11.656a1 1 0 00.707.707 1.707z"></path>
                    </svg>
                    Remove
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Cart Summary - Enhanced Visibility -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 sticky bottom-4">
          <div class="space-y-4">
            <div class="flex justify-between items-center pb-4 border-b border-gray-200">
              <h2 class="text-2xl font-bold text-gray-800">Order Summary</h2>
              <div class="text-right">
                <p class="text-sm text-gray-500 mb-1">Subtotal</p>
                <p class="text-3xl font-bold text-orange-600">Tsh {{ totalPrice.toLocaleString() }}</p>
              </div>
            </div>
            
            <!-- Checkout buttons - always visible and prominent -->
            <div class="space-y-3">
              <!-- Main checkout button - always visible -->
              <router-link
                to="/place-order"
                class="w-full relative overflow-hidden bg-gradient-to-r from-green-500 to-green-600 text-white font-bold py-4 rounded-xl hover:from-green-600 hover:to-green-700 transition-all duration-300 transform hover:scale-105 shadow-xl text-center flex items-center justify-center"
              >
                <span class="relative z-10 flex items-center justify-center">
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 9"></path>
                  </svg>
                  Proceed to Checkout • Tsh {{ (totalPrice?.value || 0).toLocaleString() }}
                </span>
                <div class="absolute inset-0 bg-gradient-to-r from-green-600 to-green-700 opacity-0 hover:opacity-100 transition-opacity duration-300"></div>
              </router-link>
              
              <!-- Secondary actions row -->
              <div class="flex flex-col sm:flex-row gap-3">
                <!-- Login prompt for guests -->
                <router-link
                  v-if="!isAuthenticated"
                  to="/login"
                  class="flex-1 bg-blue-500 text-white font-semibold py-3 rounded-xl hover:bg-blue-600 transition-colors duration-300 text-center flex items-center justify-center"
                >
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1"></path>
                  </svg>
                  Login for Better Checkout
                </router-link>
                
                <!-- Continue shopping -->
                <router-link
                  to="/"
                  class="flex-1 bg-orange-500 text-white font-semibold py-3 rounded-xl hover:bg-orange-600 transition-colors duration-300 text-center flex items-center justify-center"
                >
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l2.293 2.293c.63.63.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                  </svg>
                  Continue Shopping
                </router-link>
              </div>
              
              <!-- Clear cart button -->
              <button
                @click="clearCart"
                class="w-full bg-gray-200 text-gray-700 font-semibold py-3 rounded-xl hover:bg-gray-300 transition-colors duration-300"
              >
                <svg class="w-4 h-4 mr-2 inline" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 01-2.828 0H5a2 2 0 00-2.828 0l5.694 11.656a1 1 0 00.707.707 1.707z"></path>
                </svg>
                Clear Cart
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
import { useUnifiedCart } from '../composables/useUnifiedCart'
import Swal from 'sweetalert2'

export default {
  name: 'Cart',
  setup() {
    const router = useRouter()
    const { isAuthenticated } = useAuth()
    const unifiedCart = useUnifiedCart()
    const isProcessing = ref(false)
    const isLoading = ref(false)
    const error = ref('')

    // Computed properties to handle both cart systems
    const totalItems = computed(() => unifiedCart.totalItems.value)

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

    // Computed properties to handle both cart systems
    const displayCart = computed(() => unifiedCart.cartItems.value)
    const displayTotalPrice = computed(() => unifiedCart.totalPrice.value)

    // Load cart based on authentication status
    const loadUserCart = async () => {
      try {
        isLoading.value = true
        await unifiedCart.loadCart()
      } catch (err) {
        error.value = err.message
        showNotificationMessage('Failed to load cart', 'error')
      } finally {
        isLoading.value = false
      }
    }

    // Unified remove from cart function
    const handleRemoveFromCart = async (itemId) => {
      try {
        await unifiedCart.removeFromCart(itemId)
        showNotificationMessage('Item removed from cart', 'success')
      } catch (err) {
        console.error('Error removing from cart:', err)
        showNotificationMessage('Error removing from cart', 'error')
      }
    }

    // Unified update quantity function
    const handleUpdateQuantity = async (itemId, newQuantity) => {
      try {
        await unifiedCart.updateQuantity(itemId, newQuantity)
      } catch (err) {
        console.error('Error updating quantity:', err)
        showNotificationMessage('Error updating quantity', 'error')
      }
    }

    const updateQuantity = (itemId, newQuantity) => {
      handleUpdateQuantity(itemId, newQuantity)
    }

    const removeFromCart = (itemId) => {
      handleRemoveFromCart(itemId)
    }

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

    const handleImageError = (event) => {
      event.target.src = 'http://localhost:8000/media/products/default-product.jpg'
    }

    // Load cart on mount
    onMounted(() => {
      loadUserCart()
    })

    const checkout = async () => {
      if (cart.value.length === 0) {
        showNotificationMessage('Your cart is empty')
        return
      }
      
      isProcessing.value = true
      try {
        const total = totalPrice.value
        
        // Get existing orders
        let orders = []
        try {
          const savedOrders = localStorage.getItem('orders')
          if (savedOrders) {
            orders = JSON.parse(savedOrders)
          }
        } catch (error) {
          console.error('Error reading existing orders:', error)
        }
        
        // Create new order
        const order = {
          id: 'ORD' + Date.now(),
          items: [...cart.value],
          total: total,
          date: new Date().toISOString(),
          status: 'Pending'
        }
        
        // Add order to list
        orders.push(order)
        
        // Save orders to localStorage
        localStorage.setItem('orders', JSON.stringify(orders))
        
        // Verify order was saved
        const verifyOrders = JSON.parse(localStorage.getItem('orders'))
        const wasSaved = verifyOrders.some(o => o.id === order.id)
        
        if (wasSaved) {
          showNotificationMessage('Order placed successfully! Thank you for your purchase.')
          
          // Clear the cart
          cart.value = []
          saveCart()
          
          // Navigate to orders page after delay
          setTimeout(() => {
            router.push('/orders')
          }, 1500)
        } else {
          showNotificationMessage('Error: Order could not be placed')
        }
      } catch (error) {
        console.error('Checkout error:', error)
        showNotificationMessage('Error processing checkout')
      } finally {
        isProcessing.value = false
      }
    }

    return {
      cart: unifiedCart.cartItems,
      totalPrice: unifiedCart.totalPrice,
      totalItems,
      isProcessing,
      isAuthenticated,
      isLoading,
      error,
      getImageUrl,
      handleImageError,
      updateQuantity: handleUpdateQuantity,
      removeFromCart: handleRemoveFromCart,
      clearCart: unifiedCart.clearCart,
      checkout
    }
  }
}
</script>
