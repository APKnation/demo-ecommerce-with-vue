<template>
  <div>
    <!-- Vue Notification Component -->
    <transition name="notification" appear>
      <div v-if="showLocalNotification" class="fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50">
        {{ localNotification }}
      </div>
    </transition>

    <h1 class="text-3xl font-bold mb-8">Shopping Cart</h1>
    
    <div v-if="cart.length === 0" class="text-center py-12">
      <div class="mb-8">
        <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
        </svg>
        <p class="text-gray-500 text-lg mb-4">Your cart is empty</p>
        <router-link to="/" class="btn btn-primary">
          Continue Shopping
        </router-link>
      </div>
    </div>
    
    <div v-else>
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
            <span v-else>Proceed to Checkout</span>
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
        
        // Save order to localStorage
        const orders = JSON.parse(localStorage.getItem('orders')) || []
        const order = {
          id: 'ORD' + Date.now(),
          items: [...cart.value],
          total: total,
          date: new Date().toISOString(),
          status: 'Pending'
        }
        orders.push(order)
        localStorage.setItem('orders', JSON.stringify(orders))

        showNotificationMessage('Order placed successfully! Thank you for your purchase.')
        
        // Clear the cart
        cart.value = []
        saveCart()
        
        // Navigate to orders page
        setTimeout(() => {
          router.push('/orders')
        }, 1500)
      } catch (error) {
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

<style scoped>
.notification-enter-active {
  animation: slideIn 0.3s ease-out;
}

.notification-leave-active {
  animation: slideOut 0.3s ease-in;
}

@keyframes slideIn {
  from {
    transform: translateX(100%);
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}

@keyframes slideOut {
  from {
    transform: translateX(0);
    opacity: 1;
  }
  to {
    transform: translateX(100%);
    opacity: 0;
  }
}
</style>
