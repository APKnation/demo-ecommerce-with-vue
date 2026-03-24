<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-4xl mx-auto px-4">
      <div class="bg-white rounded-lg shadow-lg p-6">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">Checkout</h1>
        
        <!-- Cart Items Summary -->
        <div class="mb-8">
          <h2 class="text-lg font-semibold text-gray-900 mb-4">Order Summary</h2>
          <div class="bg-gray-50 rounded-lg p-4">
            <div v-if="cartItems.length === 0" class="text-center py-4">
              <p class="text-gray-500">Your cart is empty</p>
            </div>
            <div v-else>
              <div v-for="item in cartItems" :key="item.id" class="flex justify-between items-center py-2 border-b border-gray-200 last:border-0">
                <div class="flex-1">
                  <h3 class="font-medium text-gray-900">{{ item.product.title }}</h3>
                  <p class="text-sm text-gray-500">Quantity: {{ item.quantity }}</p>
                </div>
                <div class="text-right">
                  <p class="font-medium text-gray-900">Tsh {{ (item.quantity * item.product.price).toLocaleString() }}</p>
                  <p class="text-sm text-gray-500">Tsh {{ item.product.price.toLocaleString() }} each</p>
                </div>
              </div>
              <div class="mt-4 pt-4 border-t border-gray-200">
                <div class="flex justify-between items-center">
                  <span class="text-lg font-semibold text-gray-900">Total:</span>
                  <span class="text-lg font-bold text-orange-600">Tsh {{ totalAmount.toLocaleString() }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>

        <!-- Shipping Address Form -->
        <div class="mb-8">
          <h2 class="text-lg font-semibold text-gray-900 mb-4">Shipping Address</h2>
          <form @submit.prevent="handleCheckout" class="space-y-6">
            <div>
              <label for="shipping_address" class="block text-sm font-medium text-gray-700 mb-2">
                Shipping Address *
              </label>
              <textarea
                id="shipping_address"
                v-model="shippingAddress"
                required
                rows="4"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500"
                placeholder="Enter your complete shipping address including street, city, and postal code"
              ></textarea>
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

            <!-- Action Buttons -->
            <div class="flex justify-between space-x-4">
              <router-link
                to="/cart"
                class="px-6 py-3 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-orange-500"
              >
                Back to Cart
              </router-link>
              <button
                type="submit"
                :disabled="isLoading || cartItems.length === 0"
                class="px-6 py-3 bg-orange-600 text-white rounded-lg hover:bg-orange-700 focus:outline-none focus:ring-2 focus:ring-orange-500 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="isLoading">Processing Order...</span>
                <span v-else>Complete Order</span>
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '../composables/useAuth'
import { useAuthenticatedCart } from '../composables/useAuthenticatedCart'

export default {
  name: 'Checkout',
  setup() {
    const router = useRouter()
    const { user, isAuthenticated } = useAuth()
    const { cartItems, totalPrice, loadCart, isLoading: cartLoading } = useAuthenticatedCart()
    
    const shippingAddress = ref('')
    const isLoading = ref(false)
    const error = ref('')
    const successMessage = ref('')

    // Calculate total amount
    const totalAmount = computed(() => {
      return cartItems.value.reduce((total, item) => {
        return total + (item.quantity * item.product.price)
      }, 0)
    })

    // Load cart from backend
    const loadUserCart = async () => {
      if (!isAuthenticated.value) {
        router.push('/login')
        return
      }

      try {
        await loadCart()
      } catch (err) {
        error.value = err.message
      }
    }

    // Handle checkout
    const handleCheckout = async () => {
      if (cartItems.value.length === 0) {
        error.value = 'Your cart is empty'
        return
      }

      if (!shippingAddress.value.trim()) {
        error.value = 'Please enter a shipping address'
        return
      }

      isLoading.value = true
      error.value = ''
      successMessage.value = ''

      try {
        const token = localStorage.getItem('token')
        const response = await fetch('http://localhost:8000/api/orders/create/', {
          method: 'POST',
          headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json',
          },
          body: JSON.stringify({
            shipping_address: shippingAddress.value
          })
        })

        const data = await response.json()

        if (!response.ok) {
          throw new Error(data.error || data.shipping_address?.[0] || 'Failed to create order')
        }

        successMessage.value = `Order ${data.order_number} created successfully! Redirecting to orders...`
        
        // Redirect to orders page after a short delay
        setTimeout(() => {
          router.push('/orders')
        }, 2000)

      } catch (err) {
        error.value = err.message
      } finally {
        isLoading.value = false
      }
    }

    onMounted(() => {
      if (!isAuthenticated.value) {
        router.push('/login')
        return
      }
      loadUserCart()
    })

    return {
      cartItems,
      shippingAddress,
      isLoading,
      error,
      successMessage,
      totalAmount,
      handleCheckout
    }
  }
}
</script>
