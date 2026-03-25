<template>
  <div class="min-h-screen bg-gradient-to-br from-green-50 via-white to-green-100">
    <!-- Header -->
    <div class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center shadow-lg">
              <span class="text-white text-xl font-bold">✅</span>
            </div>
            <h1 class="text-3xl font-bold bg-gradient-to-r from-green-600 to-green-700 bg-clip-text text-transparent">Order Success!</h1>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Success Message -->
      <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden mb-8">
        <div class="p-8 text-center">
          <div class="w-20 h-20 mx-auto bg-gradient-to-br from-green-100 to-green-200 rounded-full flex items-center justify-center mb-6">
            <span class="text-green-600 text-4xl">🎉</span>
          </div>
          
          <h2 class="text-3xl font-bold text-gray-800 mb-4">Order Placed Successfully!</h2>
          <p class="text-xl text-gray-600 mb-2">Thank you for your purchase</p>
          <p class="text-lg text-gray-500 mb-6">Order #{{ orderNumber }}</p>
          
          <div class="bg-green-50 rounded-xl p-6 mb-6">
            <h3 class="text-lg font-semibold text-green-800 mb-4">What happens next?</h3>
            <div class="grid grid-cols-1 md:grid-cols-3 gap-4 text-left">
              <div class="flex items-start space-x-3">
                <span class="text-green-600 text-xl">📧</span>
                <div>
                  <p class="font-medium text-green-800">Confirmation Email</p>
                  <p class="text-sm text-green-600">We've sent a confirmation to your email</p>
                </div>
              </div>
              <div class="flex items-start space-x-3">
                <span class="text-green-600 text-xl">📦</span>
                <div>
                  <p class="font-medium text-green-800">Order Processing</p>
                  <p class="text-sm text-green-600">We'll prepare your items for shipping</p>
                </div>
              </div>
              <div class="flex items-start space-x-3">
                <span class="text-green-600 text-xl">🚚</span>
                <div>
                  <p class="font-medium text-green-800">Delivery</p>
                  <p class="text-sm text-green-600">Estimated 3-5 business days</p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Order Details -->
      <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden mb-8">
        <div class="p-6 bg-gradient-to-r from-blue-50 to-blue-100 border-b border-gray-200">
          <h3 class="text-xl font-bold text-gray-800">Order Details</h3>
        </div>
        <div class="p-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-6">
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Order Number</label>
              <p class="text-gray-900 font-medium">{{ orderNumber }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Order Date</label>
              <p class="text-gray-900 font-medium">{{ formatDate(new Date()) }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Payment Method</label>
              <p class="text-gray-900 font-medium">{{ paymentMethod || 'Cash on Delivery' }}</p>
            </div>
            <div>
              <label class="block text-sm font-medium text-gray-700 mb-1">Status</label>
              <span class="inline-flex px-3 py-1 rounded-full text-xs font-medium bg-yellow-100 text-yellow-800">
                Pending
              </span>
            </div>
          </div>

          <!-- Order Items -->
          <div v-if="orderItems.length > 0" class="mb-6">
            <h4 class="font-semibold text-gray-800 mb-4">Order Items</h4>
            <div class="space-y-3">
              <div v-for="(item, index) in orderItems" :key="index" class="flex justify-between items-center p-4 bg-gray-50 rounded-xl">
                <div class="flex items-center space-x-4">
                  <img 
                    :src="getProductImage(item.product || item)" 
                    :alt="item.product?.title || item.name || 'Product'" 
                    class="w-16 h-16 object-cover rounded-lg"
                  >
                  <div>
                    <h5 class="font-medium text-gray-800">{{ item.product?.title || item.name || 'Unknown Product' }}</h5>
                    <p class="text-sm text-gray-600">Quantity: {{ item.quantity }}</p>
                  </div>
                </div>
                <div class="text-right">
                  <p class="font-bold text-gray-700">Tsh {{ (item.quantity * Number(item.price || item.product?.price || 0)).toLocaleString() }}</p>
                </div>
              </div>
            </div>
          </div>

          <!-- Order Total -->
          <div class="border-t pt-4">
            <div class="flex justify-between items-center mb-2">
              <span class="text-gray-600">Subtotal</span>
              <span class="font-medium">Tsh {{ totalAmount.toLocaleString() }}</span>
            </div>
            <div class="flex justify-between items-center mb-2">
              <span class="text-gray-600">Shipping</span>
              <span class="font-medium">Tsh 0</span>
            </div>
            <div class="flex justify-between items-center mb-2">
              <span class="text-gray-600">Tax</span>
              <span class="font-medium">Tsh 0</span>
            </div>
            <div class="flex justify-between items-center pt-2 border-t">
              <span class="text-lg font-bold text-gray-800">Total</span>
              <span class="text-lg font-bold text-green-600">Tsh {{ totalAmount.toLocaleString() }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Action Buttons -->
      <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6">
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <router-link
            to="/orders"
            class="flex items-center justify-center px-6 py-3 bg-blue-600 text-white font-medium rounded-xl hover:bg-blue-700 transition-colors duration-300"
          >
            <span class="mr-2">📋</span>
            Track Order
          </router-link>
          
          <router-link
            to="/"
            class="flex items-center justify-center px-6 py-3 bg-green-600 text-white font-medium rounded-xl hover:bg-green-700 transition-colors duration-300"
          >
            <span class="mr-2">🛍️</span>
            Continue Shopping
          </router-link>
          
          <router-link
            to="/user-dashboard"
            class="flex items-center justify-center px-6 py-3 bg-purple-600 text-white font-medium rounded-xl hover:bg-purple-700 transition-colors duration-300"
          >
            <span class="mr-2">👤</span>
            My Dashboard
          </router-link>
        </div>
      </div>

      <!-- Customer Support -->
      <div class="mt-8 text-center">
        <div class="bg-blue-50 rounded-xl p-6 inline-block">
          <h4 class="text-lg font-semibold text-blue-800 mb-2">Need Help?</h4>
          <p class="text-blue-600 mb-4">Our customer support team is here to help</p>
          <div class="flex justify-center space-x-4">
            <a href="#" class="text-blue-600 hover:text-blue-800">
              <span class="mr-1">📞</span> Call Us
            </a>
            <a href="#" class="text-blue-600 hover:text-blue-800">
              <span class="mr-1">✉️</span> Email Us
            </a>
            <a href="#" class="text-blue-600 hover:text-blue-800">
              <span class="mr-1">💬</span> Live Chat
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'

export default {
  name: 'OrderSuccess',
  setup() {
    const route = useRoute()
    const router = useRouter()
    
    const orderNumber = ref(route.query.order || `ORD-${Math.random().toString(36).substr(2, 9).toUpperCase()}`)
    const paymentMethod = ref(route.query.payment || 'Cash on Delivery')
    const totalAmount = ref(Number(route.query.total) || 0)
    const orderItems = ref([])
    
    const getProductImage = (item) => {
      if (item.product?.image) return item.product.image
      if (item.image) return item.image
      return '/images/placeholder.jpg'
    }

    const formatDate = (date) => {
      return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'long',
        day: 'numeric'
      })
    }

    const loadOrderData = () => {
      // Try to get order data from localStorage (for guest orders)
      const recentOrder = localStorage.getItem('recentOrder')
      if (recentOrder) {
        try {
          const orderData = JSON.parse(recentOrder)
          orderItems.value = orderData.items || []
          totalAmount.value = orderData.total || totalAmount.value
          paymentMethod.value = orderData.paymentMethod || paymentMethod.value
          localStorage.removeItem('recentOrder') // Clean up
        } catch (error) {
          console.error('Error parsing order data:', error)
        }
      }
    }

    onMounted(() => {
      loadOrderData()
    })

    return {
      orderNumber,
      paymentMethod,
      totalAmount,
      orderItems,
      getProductImage,
      formatDate
    }
  }
}
</script>
