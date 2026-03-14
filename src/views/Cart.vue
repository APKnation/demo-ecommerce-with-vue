<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-100">

    <!-- Cart Header -->
    <div class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-600 rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
            </div>
            <h1 class="text-3xl font-bold bg-gradient-to-r from-orange-600 to-orange-700 bg-clip-text text-transparent">Shopping Cart</h1>
          </div>
          <div class="flex items-center space-x-2">
            <span class="text-gray-500">{{ cart.length }} item{{ cart.length !== 1 ? 's' : '' }}</span>
            <span class="text-gray-400">•</span>
            <span class="font-semibold text-gray-700">Tsh {{ totalPrice.toLocaleString() }}</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Empty State -->
      <div v-if="cart.length === 0" class="text-center py-16">
        <div class="bg-white rounded-2xl shadow-xl p-8 max-w-md mx-auto">
          <div class="w-24 h-24 mx-auto bg-gradient-to-br from-orange-100 to-orange-200 rounded-full flex items-center justify-center mb-6">
            <svg class="w-12 h-12 text-orange-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
          </div>
          <h2 class="text-2xl font-bold text-gray-800 mb-4">Your cart is empty</h2>
          <p class="text-gray-600 mb-6">Start shopping to add some amazing products to your cart!</p>
          <router-link to="/" class="inline-flex items-center px-6 py-3 bg-gradient-to-r from-orange-500 to-orange-600 text-white font-semibold rounded-xl hover:from-orange-600 hover:to-orange-700 transition-all duration-300 transform hover:scale-105 shadow-lg">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            Continue Shopping
          </router-link>
        </div>
      </div>
      
      <!-- Cart Items -->
      <div v-else class="space-y-6">
        <!-- Cart Items List -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
          <div class="divide-y divide-gray-200">
            <div
              v-for="(item, index) in cart"
              :key="index"
              class="p-6 hover:bg-gradient-to-r from-orange-50 to-yellow-50 transition-colors duration-300 group"
            >
              <div class="flex items-center justify-between">
                <div class="flex items-center space-x-4">
                  <img
                    :src="item.image"
                    :alt="item.name"
                    class="w-20 h-20 object-cover rounded-xl shadow-md group-hover:scale-110 transition-transform duration-300"
                  >
                  <div>
                    <h3 class="text-xl font-bold text-gray-800 mb-1">{{ item.name }}</h3>
                    <p class="text-sm text-gray-500">{{ item.category }}</p>
                    <p class="text-lg font-semibold text-orange-600">Tsh {{ item.price.toLocaleString() }}</p>
                  </div>
                </div>
                
                <!-- Quantity Controls -->
                <div class="flex items-center space-x-3">
                  <div class="flex items-center bg-gray-100 rounded-lg p-1">
                    <button
                      @click="updateQuantity(index, -1)"
                      class="w-8 h-8 bg-red-500 text-white rounded-lg hover:bg-red-600 transition-colors duration-300 flex items-center justify-center"
                    >
                      <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 6L9 17l-5-5L4 6z"></path>
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
                </div>
                
                <!-- Item Total & Remove -->
                <div class="text-right">
                  <p class="text-lg font-bold text-gray-800 mb-2">Tsh {{ (item.price * item.quantity).toLocaleString() }}</p>
                  <button
                    @click="removeFromCart(index)"
                    class="bg-red-500 text-white px-4 py-2 rounded-lg hover:bg-red-600 transition-colors duration-300 flex items-center"
                  >
                    <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 01-2.828 0H5a2 2 0 00-2 828 0l5.694 11.656a1 1 0 00.707.707 1.707z"></path>
                    </svg>
                    Remove
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Cart Summary -->
        <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6">
          <div class="space-y-4">
            <div class="flex justify-between items-center pb-4 border-b border-gray-200">
              <h2 class="text-2xl font-bold text-gray-800">Order Summary</h2>
              <div class="text-right">
                <p class="text-sm text-gray-500 mb-1">Subtotal</p>
                <p class="text-3xl font-bold text-orange-600">Tsh {{ totalPrice.toLocaleString() }}</p>
              </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <button
                @click="checkout"
                :disabled="isProcessing"
                class="relative overflow-hidden bg-gradient-to-r from-orange-500 to-orange-600 text-white font-bold py-4 rounded-xl hover:from-orange-600 hover:to-orange-700 transition-all duration-300 transform hover:scale-105 disabled:opacity-50 disabled:cursor-not-allowed disabled:transform-none shadow-xl"
              >
                <span class="relative z-10 flex items-center justify-center">
                  <svg v-if="!isProcessing" class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 9"></path>
                  </svg>
                  <svg v-if="isProcessing" class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                    <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                    <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V8c4 10.09 4.91 12 6h4"></path>
                  </svg>
                  <span v-if="!isProcessing">Place Order</span>
                  <span v-else>Processing...</span>
                </span>
                <div class="absolute inset-0 bg-gradient-to-r from-orange-600 to-orange-700 opacity-0 hover:opacity-100 transition-opacity duration-300"></div>
              </button>
              
              <button
                @click="clearCart"
                class="bg-gray-200 text-gray-700 font-semibold py-4 rounded-xl hover:bg-gray-300 transition-colors duration-300"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 01-2.828 0H5a2 2 0 00-2 828 0l5.694 11.656a1 1 0 00.707.707 1.707z"></path>
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
import { ref, computed, inject } from 'vue'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

export default {
  name: 'Cart',
  setup() {
    const router = useRouter()
    const cart = inject('cart', ref([]))
    const isProcessing = ref(false)

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

    const totalPrice = computed(() => {
      return cart.value.reduce((total, item) => total + (item.price * item.quantity), 0)
    })

    const updateQuantity = (index, change) => {
      cart.value[index].quantity += change
      
      if (cart.value[index].quantity <= 0) {
        removeFromCart(index)
      } else {
        saveCart()
      }
    }

    const removeFromCart = (index) => {
      const itemName = cart.value[index].name
      cart.value.splice(index, 1)
      saveCart()
      showNotificationMessage(`${itemName} removed from cart`)
    }

    const clearCart = () => {
      cart.value = []
      saveCart()
      showNotificationMessage('Cart cleared successfully')
    }

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

    const saveCart = () => {
      localStorage.setItem('cart', JSON.stringify(cart.value))
    }

    return {
      cart,
      totalPrice,
      isProcessing,
      updateQuantity,
      removeFromCart,
      clearCart,
      checkout
    }
  }
}
</script>
