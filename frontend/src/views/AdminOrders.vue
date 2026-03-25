<template>
  <div class="min-h-screen bg-gray-100">
    <!-- Admin Header -->
    <div class="bg-gradient-to-r from-blue-600 to-blue-800 text-white shadow-lg">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex items-center justify-between py-6">
          <div class="flex items-center space-x-4">
            <div class="w-12 h-12 bg-white/20 rounded-xl flex items-center justify-center">
              <svg class="w-7 h-7 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2 2v10a2 2 0 002 2h6a2 2 0 002-2V9a2 2 0 00-2-2H9z"></path>
              </svg>
            </div>
            <div>
              <h1 class="text-2xl font-bold">Admin Order Management</h1>
              <p class="text-blue-200 text-sm">Manage all store orders</p>
            </div>
          </div>
          <div class="flex items-center space-x-4">
            <router-link to="/admin" class="text-blue-200 hover:text-white">
              ← Back to Dashboard
            </router-link>
            <span class="text-blue-200">|</span>
            <span class="text-blue-200">{{ currentUser?.username }}</span>
            <button @click="logout" class="bg-red-500 hover:bg-red-600 text-white px-4 py-2 rounded-lg transition-colors">
              Logout
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Stats Cards -->
      <div class="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
        <div v-for="stat in orderStats" :key="stat.label" class="bg-white rounded-xl shadow-md p-6">
          <p class="text-sm font-medium text-gray-600">{{ stat.label }}</p>
          <p class="text-3xl font-bold mt-2" :class="stat.color">{{ stat.value }}</p>
        </div>
      </div>

      <!-- Filter & Search -->
      <div class="bg-white rounded-xl shadow-md p-4 mb-6 flex flex-wrap gap-4 items-center justify-between">
        <div class="flex gap-4">
          <select v-model="statusFilter" class="border rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-500">
            <option value="all">All Orders</option>
            <option value="Pending">Pending</option>
            <option value="Confirmed">Confirmed</option>
            <option value="Completed">Completed</option>
            <option value="Cancelled">Cancelled</option>
          </select>
          <input v-model="searchQuery" type="text" placeholder="Search orders..." class="border rounded-lg px-3 py-2 w-64">
        </div>
        <div class="text-sm text-gray-600">
          Showing {{ filteredOrders.length }} of {{ allOrders.length }} orders
        </div>
      </div>

      <!-- Orders Table -->
      <div class="bg-white rounded-xl shadow-md overflow-hidden">
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Order #</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Customer</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Items</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Amount</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Status</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="order in filteredOrders" :key="order.id" class="hover:bg-gray-50">
                <td class="px-6 py-4 text-sm font-medium text-gray-900">{{ order.order_number || order.id }}</td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ order.customer?.username || 'Unknown' }}</td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ order.items?.length || 0 }} items</td>
                <td class="px-6 py-4 text-sm text-gray-900 font-semibold">Tsh {{ Number(order.total_amount || order.total).toLocaleString() }}</td>
                <td class="px-6 py-4">
                  <span :class="getStatusClass(order.status)">{{ order.status }}</span>
                </td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ formatDate(order.created_at || order.date) }}</td>
                <td class="px-6 py-4 text-sm">
                  <div class="flex flex-wrap gap-2">
                    <button @click="viewOrder(order)" class="bg-gray-500 hover:bg-gray-600 text-white px-3 py-1 rounded text-xs">View</button>
                    <button v-if="order.status === 'Pending'" @click="updateStatus(order.id, 'Confirmed')" class="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded text-xs">Confirm</button>
                    <button v-if="order.status === 'Confirmed'" @click="updateStatus(order.id, 'Completed')" class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-xs">Complete</button>
                    <button v-if="['Pending', 'Confirmed'].includes(order.status)" @click="updateStatus(order.id, 'Cancelled')" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-xs">Cancel</button>
                    <button @click="deleteOrder(order.id)" class="bg-gray-700 hover:bg-gray-800 text-white px-3 py-1 rounded text-xs">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Order Details Modal -->
    <div v-if="selectedOrder" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-bold">Order #{{ selectedOrder.order_number || selectedOrder.id }}</h3>
          <button @click="selectedOrder = null" class="text-gray-500 hover:text-gray-700">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <div class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-sm text-gray-600">Customer</p>
              <p class="font-medium">{{ selectedOrder.customer?.username || 'Unknown' }}</p>
              <p class="text-sm text-gray-500">{{ selectedOrder.customer?.email }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-600">Status</p>
              <span :class="getStatusClass(selectedOrder.status)">{{ selectedOrder.status }}</span>
            </div>
          </div>
          <div>
            <p class="text-sm text-gray-600 mb-2">Order Items</p>
            <div class="bg-gray-50 rounded-lg p-4 space-y-2">
              <div v-for="item in selectedOrder.items" :key="item.id" class="flex justify-between items-center py-2 border-b last:border-0">
                <div class="flex items-center space-x-3">
                  <img v-if="item.product?.image" :src="item.product.image" class="w-12 h-12 object-cover rounded" />
                  <div>
                    <p class="font-medium">{{ item.product?.title || item.name }}</p>
                    <p class="text-sm text-gray-500">Qty: {{ item.quantity }} × Tsh {{ Number(item.price).toLocaleString() }}</p>
                  </div>
                </div>
                <span class="font-semibold">Tsh {{ Number(item.price * item.quantity).toLocaleString() }}</span>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center pt-4 border-t">
            <div>
              <p class="text-sm text-gray-600">Order Date</p>
              <p class="font-medium">{{ formatDate(selectedOrder.created_at) }}</p>
            </div>
            <div class="text-right">
              <p class="text-sm text-gray-600">Total Amount</p>
              <p class="text-2xl font-bold text-blue-600">Tsh {{ Number(selectedOrder.total_amount || selectedOrder.total).toLocaleString() }}</p>
            </div>
          </div>
          <div class="flex justify-end space-x-3 pt-4">
            <button @click="selectedOrder = null" class="px-4 py-2 border rounded-lg hover:bg-gray-50">Close</button>
            <button v-if="selectedOrder.status === 'Pending'" @click="updateStatus(selectedOrder.id, 'Confirmed'); selectedOrder = null" class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600">Confirm Order</button>
            <button v-if="selectedOrder.status === 'Confirmed'" @click="updateStatus(selectedOrder.id, 'Completed'); selectedOrder = null" class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">Complete Order</button>
            <button v-if="['Pending', 'Confirmed'].includes(selectedOrder.status)" @click="updateStatus(selectedOrder.id, 'Cancelled'); selectedOrder = null" class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600">Cancel Order</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

export default {
  name: 'AdminOrders',
  setup() {
    const router = useRouter()
    const allOrders = ref([])
    const currentUser = ref(null)
    const statusFilter = ref('all')
    const searchQuery = ref('')
    const selectedOrder = ref(null)
    
    const API_BASE_URL = 'http://localhost:8000/api'
    const getToken = () => localStorage.getItem('token')

    const orderStats = computed(() => [
      { label: 'Total Orders', value: allOrders.value.length, color: 'text-gray-900' },
      { label: 'Pending', value: allOrders.value.filter(o => o.status === 'Pending').length, color: 'text-yellow-600' },
      { label: 'Confirmed', value: allOrders.value.filter(o => o.status === 'Confirmed').length, color: 'text-blue-600' },
      { label: 'Completed', value: allOrders.value.filter(o => o.status === 'Completed').length, color: 'text-green-600' }
    ])

    const filteredOrders = computed(() => {
      let filtered = allOrders.value
      if (statusFilter.value !== 'all') {
        filtered = filtered.filter(o => o.status === statusFilter.value)
      }
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        filtered = filtered.filter(o => 
          (o.order_number || '').toString().toLowerCase().includes(query) ||
          (o.customer?.username || '').toLowerCase().includes(query)
        )
      }
      return filtered.sort((a, b) => new Date(b.created_at || b.date) - new Date(a.created_at || a.date))
    })

    const loadOrders = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/orders/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) {
          allOrders.value = await response.json()
        }
      } catch (error) {
        console.error('Failed to load orders:', error)
      }
    }

    const updateStatus = async (orderId, status) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 
            'Authorization': `Token ${getToken()}`, 
            'Content-Type': 'application/json' 
          },
          body: JSON.stringify({ status })
        })
        if (response.ok) {
          const updated = await response.json()
          const index = allOrders.value.findIndex(o => o.id === orderId)
          if (index !== -1) allOrders.value[index] = updated
          Swal.fire({ icon: 'success', title: 'Success!', text: `Order ${status.toLowerCase()}!`, timer: 2000, showConfirmButton: false })
        }
      } catch (error) {
        Swal.fire({ icon: 'error', title: 'Error', text: 'Failed to update order' })
      }
    }

    const deleteOrder = async (orderId) => {
      const result = await Swal.fire({
        title: 'Delete Order?',
        text: 'This action cannot be undone!',
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#ef4444',
        confirmButtonText: 'Yes, delete it!'
      })
      if (!result.isConfirmed) return
      
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'DELETE',
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) {
          allOrders.value = allOrders.value.filter(o => o.id !== orderId)
          Swal.fire({ icon: 'success', title: 'Deleted!', text: 'Order has been deleted.', timer: 2000, showConfirmButton: false })
        }
      } catch (error) {
        Swal.fire({ icon: 'error', title: 'Error', text: 'Failed to delete order' })
      }
    }

    const viewOrder = (order) => {
      selectedOrder.value = order
    }

    const getStatusClass = (status) => {
      const classes = {
        'Pending': 'bg-yellow-100 text-yellow-800 px-2 py-1 rounded-full text-xs font-medium',
        'Confirmed': 'bg-blue-100 text-blue-800 px-2 py-1 rounded-full text-xs font-medium',
        'Completed': 'bg-green-100 text-green-800 px-2 py-1 rounded-full text-xs font-medium',
        'Cancelled': 'bg-red-100 text-red-800 px-2 py-1 rounded-full text-xs font-medium'
      }
      return classes[status] || 'bg-gray-100 text-gray-800 px-2 py-1 rounded-full text-xs font-medium'
    }

    const formatDate = (dateString) => {
      if (!dateString) return 'N/A'
      return new Date(dateString).toLocaleDateString('en-US', { year: 'numeric', month: 'short', day: 'numeric', hour: '2-digit', minute: '2-digit' })
    }

    const logout = () => {
      localStorage.removeItem('token')
      localStorage.removeItem('user')
      router.push('/login')
    }

    onMounted(() => {
      const userData = localStorage.getItem('user')
      if (userData) currentUser.value = JSON.parse(userData)
      loadOrders()
    })

    return {
      allOrders,
      currentUser,
      statusFilter,
      searchQuery,
      selectedOrder,
      orderStats,
      filteredOrders,
      updateStatus,
      deleteOrder,
      viewOrder,
      getStatusClass,
      formatDate,
      logout
    }
  }
}
</script>
