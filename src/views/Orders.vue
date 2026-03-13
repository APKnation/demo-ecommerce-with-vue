<template>
  <div>
    <h1 class="text-3xl font-bold mb-8">Order History</h1>
    
    <div v-if="orders.length === 0" class="text-center py-12">
      <div class="mb-8">
        <svg class="w-24 h-24 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
        </svg>
        <p class="text-gray-500 text-lg mb-4">You haven't placed any orders yet</p>
        <router-link to="/" class="btn btn-primary">
          Start Shopping
        </router-link>
      </div>
    </div>
    
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

    // Load orders from localStorage
    const loadOrders = () => {
      orders.value = JSON.parse(localStorage.getItem('orders')) || []
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
      if (confirm('Are you sure you want to cancel this order?')) {
        const orderIndex = orders.value.findIndex(order => order.id === orderId)
        if (orderIndex !== -1) {
          orders.value[orderIndex].status = 'Cancelled'
          localStorage.setItem('orders', JSON.stringify(orders.value))
          showNotification('Order cancelled successfully')
        }
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
      orders,
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
