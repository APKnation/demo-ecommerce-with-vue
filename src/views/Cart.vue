<template>
  <div>
    <!-- Vue Notification Component -->
    <div v-if="showLocalNotification" class="fixed top-4 right-4 bg-success-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300 transform">
      {{ localNotification }}
    </div>

    <h1 class="text-3xl font-bold mb-8 text-neutral-900">Shopping Cart</h1>
    
    <div v-if="cart.length === 0" class="text-center py-12">
      <div class="mb-8">
        <svg class="w-24 h-24 mx-auto text-neutral-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
        </svg>
        <p class="text-neutral-500 text-lg mb-4">Your cart is empty</p>
        <router-link to="/" class="inline-flex items-center px-4 py-2 bg-primary-600 text-white rounded-lg hover:bg-primary-700 transition-colors">
          Continue Shopping
        </router-link>
      </div>
    </div>
    
    <div v-else>
      <!-- Cart Header with Explanation -->
      <div class="mb-6 p-4 bg-blue-50 rounded-lg">
        <div class="flex items-start space-x-3">
          <svg class="w-5 h-5 text-blue-600 mt-0.5" fill="currentColor" viewBox="0 0 20 20">
            <path fill-rule="evenodd" d="M18 10a8 8 0 11-16 0 8 8 0 0116 0zm-7-4a1 1 0 11-2 0 1 1 0 012 0zM9 9a1 1 0 000 2v3a1 1 0 001 1h6a1 1 0 001-1V9a1 1 0 00-1-1H9z" clip-rule="evenodd"></path>
          </svg>
          <div>
            <h3 class="font-semibold text-blue-800 mb-1">Direct Checkout Process</h3>
            <p class="text-sm text-blue-700">Clicking "Place Order" will immediately process your order and save it to your order history. No additional payment steps required.</p>
          </div>
        </div>
      </div>
      
      <!-- Cart Items -->
      <div class="space-y-4 mb-8">
        <div
          v-for="(item, index) in cart"
          :key="index"
          class="card flex items-center justify-between"
        >
          <div class="flex-1">
            <h3 class="text-lg font-semibold">{{ item.name }}</h3>
            <p class="text-gray-600">Tsh {{ item.price.toLocaleString() }} each</p>
          </div>
          
          <div class="flex items-center space-x-4">
            <!-- Quantity Controls -->
            <div class="flex items-center space-x-2">
              <button
                @click="updateQuantity(index, -1)"
                class="btn btn-secondary px-3 py-1"
              >
                -
              </button>
              <span class="px-4 py-1 font-semibold">{{ item.quantity }}</span>
              <button
                @click="updateQuantity(index, 1)"
                class="btn btn-secondary px-3 py-1"
              >
                +
              </button>
            </div>
            
            <!-- Item Total -->
            <div class="text-right">
              <p class="font-semibold">Tsh {{ (item.price * item.quantity).toLocaleString() }}</p>
            </div>
            
            <!-- Remove Button -->
            <button
              @click="removeFromCart(index)"
              class="btn btn-danger"
            >
              Remove
            </button>
          </div>
        </div>
      </div>
      
      <!-- Cart Summary -->
      <div class="bg-white rounded-lg shadow-md p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">Order Summary</h2>
          <div class="text-right">
            <p class="text-lg">Total: <span class="font-bold text-blue-600">Tsh {{ totalPrice.toLocaleString() }}</span></p>
          </div>
        </div>
        
        <div class="flex space-x-4">
          <button
            @click="checkout"
            :disabled="isProcessing"
            class="btn btn-primary flex-grow disabled:opacity-50 disabled:cursor-not-allowed"
          >
            <span v-if="isProcessing" class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V8C4 10.09 4.91 12 6 12h4"></path>
              </svg>
              Processing...
            </span>
            <span v-else>Place Order</span>
          </button>
          <button
            @click="clearCart"
            class="btn btn-danger"
          >
            Clear Cart
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, inject } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'Cart',
  setup() {
    const router = useRouter()
    const cart = inject('cart', ref([]))
    const notification = inject('notification', ref(''))
    const localNotification = ref('')
    const showLocalNotification = ref(false)
    const isProcessing = ref(false)

    // Vue notification system
    const showNotificationMessage = (message) => {
      localNotification.value = message
      showLocalNotification.value = true
      setTimeout(() => {
        showLocalNotification.value = false
        localNotification.value = ''
      }, 3000)
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
      localNotification,
      showLocalNotification,
      updateQuantity,
      removeFromCart,
      clearCart,
      checkout
    }
  }
}
</script>
