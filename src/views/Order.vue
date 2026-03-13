<template>
  <div>
    <div v-if="!order" class="text-center py-12">
      <div class="mb-8">
        <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
        </svg>
        <p class="text-gray-500 text-lg mb-4">Order not found</p>
        <router-link to="/orders" class="btn btn-primary">
          Back to Orders
        </router-link>
      </div>
    </div>
    
    <div v-else>
      <!-- Order Header -->
      <div class="card mb-6">
        <div class="flex justify-between items-start mb-4">
          <div>
            <h1 class="text-3xl font-bold mb-2">Order Details</h1>
            <p class="text-gray-600">Order ID: {{ order.id }}</p>
            <p class="text-gray-600">Placed on: {{ formatDate(order.date) }}</p>
          </div>
          <div class="text-right">
            <span :class="getStatusClass(order.status)" class="inline-block text-lg px-4 py-2 rounded-full">
              {{ order.status }}
            </span>
          </div>
        </div>
      </div>
      
      <!-- Order Summary -->
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-6 mb-6">
        <div class="lg:col-span-2">
          <!-- Order Items -->
          <div class="card">
            <h2 class="text-xl font-semibold mb-4">Order Items</h2>
            <div class="space-y-3">
              <div
                v-for="(item, index) in order.items"
                :key="index"
                class="flex justify-between items-center p-4 border rounded-lg"
              >
                <div class="flex-1">
                  <h3 class="font-semibold text-lg">{{ item.name }}</h3>
                  <p class="text-gray-600">Quantity: {{ item.quantity }}</p>
                  <p class="text-gray-600">Price per item: Tsh {{ item.price.toLocaleString() }}</p>
                </div>
                <div class="text-right">
                  <p class="text-xl font-bold">Tsh {{ (item.price * item.quantity).toLocaleString() }}</p>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Order Summary Sidebar -->
        <div>
          <div class="card">
            <h2 class="text-xl font-semibold mb-4">Order Summary</h2>
            <div class="space-y-3">
              <div class="flex justify-between">
                <span>Subtotal:</span>
                <span>Tsh {{ subtotal.toLocaleString() }}</span>
              </div>
              <div class="flex justify-between">
                <span>Shipping:</span>
                <span>Tsh {{ shipping.toLocaleString() }}</span>
              </div>
              <div class="flex justify-between">
                <span>Tax:</span>
                <span>Tsh {{ tax.toLocaleString() }}</span>
              </div>
              <div class="border-t pt-3">
                <div class="flex justify-between text-lg font-bold">
                  <span>Total:</span>
                  <span class="text-blue-600">Tsh {{ order.total.toLocaleString() }}</span>
                </div>
              </div>
            </div>
            
            <!-- Order Actions -->
            <div class="mt-6 space-y-3">
              <button
                v-if="order.status === 'Pending'"
                @click="cancelOrder"
                class="btn btn-danger w-full"
              >
                Cancel Order
              </button>
              <button
                v-if="order.status === 'Completed'"
                @click="reorder"
                class="btn btn-primary w-full"
              >
                Reorder Items
              </button>
              <router-link
                to="/orders"
                class="btn btn-secondary w-full text-center block"
              >
                Back to Orders
              </router-link>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, inject } from 'vue'
import { useRoute, useRouter } from 'vue-router'

export default {
  name: 'Order',
  props: {
    id: {
      type: String,
      required: true
    }
  },
  setup() {
    const route = useRoute()
    const router = useRouter()
    const orders = ref([])
    const cart = inject('cart', ref([]))
    const notification = inject('notification', ref(''))

    // Load orders from localStorage
    const loadOrders = () => {
      orders.value = JSON.parse(localStorage.getItem('orders')) || []
    }

    const order = computed(() => {
      return orders.value.find(o => o.id === route.params.id)
    })

    const subtotal = computed(() => {
      if (!order.value) return 0
      return order.value.items.reduce((total, item) => total + (item.price * item.quantity), 0)
    })

    const shipping = computed(() => {
      if (!order.value) return 0
      return order.value.total > 1000000 ? 0 : 10000 // Free shipping for orders over 1M
    })

    const tax = computed(() => {
      if (!order.value) return 0
      return Math.round(subtotal.value * 0.18) // 18% tax
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

    const cancelOrder = () => {
      if (confirm('Are you sure you want to cancel this order?')) {
        const orderIndex = orders.value.findIndex(o => o.id === route.params.id)
        if (orderIndex !== -1) {
          orders.value[orderIndex].status = 'Cancelled'
          localStorage.setItem('orders', JSON.stringify(orders.value))
          showNotification('Order cancelled successfully')
          router.push('/orders')
        }
      }
    }

    const reorder = () => {
      if (!order.value) return
      
      // Clear existing cart
      cart.value = []
      
      // Add items from order to cart
      order.value.items.forEach(item => {
        cart.value.push({ ...item })
      })
      
      // Save cart
      localStorage.setItem('cart', JSON.stringify(cart.value))
      
      showNotification('Items added to cart successfully')
      router.push('/cart')
    }

    const showNotification = (message) => {
      notification.value = message
      setTimeout(() => {
        notification.value = ''
      }, 3000)
    }

    loadOrders()

    return {
      order,
      subtotal,
      shipping,
      tax,
      formatDate,
      getStatusClass,
      cancelOrder,
      reorder
    }
  }
}
</script>
