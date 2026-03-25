<template>
  <div>
    <!-- Admin Header -->
    <div class="bg-gradient-to-r from-primary-600 to-secondary-600 text-white rounded-lg shadow-xl p-8 mb-8">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-4xl font-bold mb-2">Admin Dashboard</h1>
        <p class="text-primary-100">Manage your e-commerce store</p>
      </div>
      <div class="text-right">
        <div class="text-3xl font-bold">{{ products.length }}</div>
        <div class="text-sm text-primary-100">Total Products</div>
      </div>
    </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="mt-8 flex space-x-1 bg-white rounded-lg p-1 shadow-md">
      <button 
        v-for="tab in tabs" 
        :key="tab.id"
        @click="tab.route ? $router.push(tab.route) : activeTab = tab.id"
        :class="[
          'px-6 py-3 rounded-md font-medium transition-all text-sm',
          (activeTab === tab.id && !tab.route) || $route.path === tab.route
            ? 'bg-blue-600 text-white shadow-md' 
            : 'text-gray-600 hover:bg-gray-100'
        ]"
      >
        {{ tab.name }}
        <span v-if="tab.badge" class="ml-2 bg-red-500 text-white text-xs px-2 py-0.5 rounded-full">
          {{ tab.badge }}
        </span>
      </button>
    </div>

    <!-- Dashboard Stats Section -->
    <div v-if="activeTab === 'dashboard'" class="mt-8 grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
      <div v-for="stat in dashboardStats" :key="stat.label" 
           class="bg-white rounded-xl shadow-lg p-6">
        <div class="flex items-center justify-between">
          <div>
            <p class="text-sm font-medium text-gray-600">{{ stat.label }}</p>
            <p class="text-2xl font-bold text-gray-900 mt-1">{{ stat.value }}</p>
          </div>
          <div :class="`w-12 h-12 ${stat.bgColor} rounded-xl flex items-center justify-center`">
            <svg class="w-6 h-6" :class="stat.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="stat.icon"></path>
            </svg>
          </div>
        </div>
      </div>
    </div>

    <!-- View Product Modal -->
    <div v-if="viewingProduct" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-96 overflow-y-auto">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold text-gray-900">Product Details</h2>
          <button @click="closeViewModal" class="text-gray-500 hover:text-gray-700 font-medium">
            Close
          </button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <img v-if="viewingProduct.image" :src="viewingProduct.image" :alt="viewingProduct.name" 
                 class="w-full h-64 object-cover rounded-lg">
            <div v-else class="w-full h-64 bg-gray-200 rounded-lg flex items-center justify-center">
              <span class="text-gray-400">No Image</span>
            </div>
          </div>
          
          <div class="space-y-4">
            <div>
              <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ viewingProduct.name }}</h3>
              <span class="px-3 py-1 text-sm rounded-full bg-blue-100 text-blue-800">
                {{ viewingProduct.category }}
              </span>
            </div>
            
            <div class="text-2xl font-bold text-blue-600">
              Tsh {{ viewingProduct.price.toLocaleString() }}
            </div>
            
            <div class="text-sm text-gray-600">
              <p><strong>Status:</strong> <span class="px-2 py-1 rounded-full bg-green-100 text-green-800">Active</span></p>
              <p><strong>Added:</strong> {{ formatDate(viewingProduct.addedDate) }}</p>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end space-x-3 mt-6 pt-4 border-t">
          <button @click="closeViewModal" class="btn btn-secondary">
            Close
          </button>
          <button @click="editProduct(viewingProduct)" class="btn btn-primary">
            Edit Product
          </button>
        </div>
      </div>
    </div>

    <!-- Edit Product Modal -->
    <div v-if="isEditing && editingProduct" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-96 overflow-y-auto">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold text-gray-900 mb-4">Edit Product</h2>
          <div class="flex items-center space-x-2">
            <div class="flex items-center">
              <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
              <span class="text-sm text-green-600 font-medium">Editing Mode</span>
            </div>
            <button @click="closeEditModal" class="text-gray-500 hover:text-gray-700 font-medium">
            Cancel
          </button>
        </div>
        
        <form @submit.prevent="updateProduct" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Product Name</label>
              <input
                v-model="editingProduct.name"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
            
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Price (Tsh)</label>
              <input
                v-model.number="editingProduct.price"
                type="number"
                required
                min="0"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Category</label>
              <select
                v-model="editingProduct.category"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
                <option value="">Select Category</option>
                <option value="laptops">Laptops</option>
                <option value="phones">Smartphones</option>
                <option value="accessories">Accessories</option>
              </select>
            </div>
            
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Image URL</label>
              <input
                v-model="editingProduct.image"
                type="text"
                required
                placeholder="/images/product.jpg"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
          </div>
          
          <div class="flex space-x-3">
            <button type="button" @click="closeEditModal" class="btn btn-secondary">
              Cancel
            </button>
            <button type="submit" class="btn btn-primary">
              Update Product
            </button>
          </div>
        </form>
      </div>
    </div>
    
    <!-- Orders Management Section -->
    <div v-if="activeTab === 'orders'" class="mt-8">
      <div class="bg-white rounded-xl shadow-lg p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">Order Management</h2>
          <div class="flex gap-4">
            <select v-model="orderStatusFilter" class="border rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-500">
              <option value="all">All Orders</option>
              <option value="Pending">Pending</option>
              <option value="Confirmed">Confirmed</option>
              <option value="Completed">Completed</option>
              <option value="Cancelled">Cancelled</option>
            </select>
          </div>
        </div>
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
              <tr v-for="order in filteredOrdersList" :key="order.id">
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
                    <button @click="viewOrderDetails(order)" class="bg-gray-500 hover:bg-gray-600 text-white px-3 py-1 rounded text-xs">View</button>
                    <button v-if="order.status === 'Pending'" @click="confirmOrder(order.id)" class="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded text-xs">Confirm</button>
                    <button v-if="order.status === 'Confirmed'" @click="completeOrder(order.id)" class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-xs">Complete</button>
                    <button v-if="['Pending', 'Confirmed'].includes(order.status)" @click="cancelOrder(order.id)" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-xs">Cancel</button>
                    <button v-if="order.status !== 'Cancelled'" @click="deleteOrder(order.id)" class="bg-gray-700 hover:bg-gray-800 text-white px-3 py-1 rounded text-xs">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    
    <!-- Users Management Section -->
    <div v-if="activeTab === 'users'" class="mt-8">
      <div class="bg-white rounded-xl shadow-lg p-6">
        <h2 class="text-2xl font-bold mb-4">User Management</h2>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">User</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Role</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Phone</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Joined</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="user in allUsers" :key="user.id">
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center text-sm font-medium">{{ user.username?.charAt(0).toUpperCase() }}</div>
                    <div class="ml-3">
                      <p class="text-sm font-medium text-gray-900">{{ user.username }}</p>
                      <p class="text-sm text-gray-500">{{ user.first_name }} {{ user.last_name }}</p>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4"><span :class="getRoleClass(user.role)">{{ user.role }}</span></td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ user.phone }}</td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ formatDate(user.created_at) }}</td>
                <td class="px-6 py-4 text-sm">
                  <button v-if="user.id !== currentUser?.id" @click="deleteUser(user.id)" class="bg-red-500 text-white px-3 py-1 rounded text-xs">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    
    <!-- Products Tab (existing content wrapped) -->
    <div v-if="activeTab === 'products'" class="mt-8 grid grid-cols-1 xl:grid-cols-3 gap-8">
      <!-- Add Product Section -->
      <div class="xl:col-span-2">
        <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
          <div class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-4">
            <h2 class="text-xl font-semibold flex items-center">
              Add New Product
            </h2>
          </div>
          <form @submit.prevent="addProduct" class="p-6">
            <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Product Name</label>
                <input
                  v-model="newProduct.name"
                  type="text"
                  required
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="Enter product name"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Price (Tsh)</label>
                <input
                  v-model.number="newProduct.price"
                  type="number"
                  required
                  min="0"
                  step="0.01"
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="Enter price"
                />
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
                <select
                  v-model="newProduct.category"
                  required
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                >
                  <option value="">Select category</option>
                  <option value="Electronics">Electronics</option>
                  <option value="Phones">Phones</option>
                  <option value="Laptops">Laptops</option>
                  <option value="Accessories">Accessories</option>
                  <option value="Other">Other</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Image URL</label>
                <input
                  v-model="newProduct.image"
                  type="url"
                  class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  placeholder="Enter image URL (optional)"
                />
              </div>
            </div>
            <div class="mt-6">
              <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
              <textarea
                v-model="newProduct.description"
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Enter product description"
              ></textarea>
            </div>
            <div class="mt-6 flex justify-end space-x-3">
              <button
                type="button"
                @click="resetProductForm"
                class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
              >
                Reset
              </button>
              <button
                type="submit"
                :disabled="isAddingProduct"
                class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="isAddingProduct">Adding...</span>
                <span v-else>Add Product</span>
              </button>
            </div>
          </form>
        </div>
      </div>
      
      <!-- Statistics Section -->
      <div class="space-y-6">
        <!-- Stats Cards -->
        <div class="grid grid-cols-1 gap-4">
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Total Products</p>
                <p class="text-3xl font-bold text-blue-600 mt-1">{{ products.length }}</p>
              </div>
              <div class="bg-blue-100 p-3 rounded-lg">
                <span class="text-blue-600 font-bold text-xl">📦</span>
              </div>
            </div>
          </div>
          
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Total Orders</p>
                <p class="text-3xl font-bold text-green-600 mt-1">{{ orders.length }}</p>
              </div>
              <div class="bg-green-100 p-3 rounded-lg">
                <span class="text-green-600 font-bold text-xl">📋</span>
              </div>
            </div>
          </div>
          
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Total Revenue</p>
                <p class="text-3xl font-bold text-yellow-600 mt-1">Tsh {{ totalRevenue.toLocaleString() }}</p>
              </div>
              <div class="bg-yellow-100 p-3 rounded-lg">
                <span class="text-yellow-600 font-bold text-xl">💰</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    </div>
    
    <!-- Order Details Modal -->
    <div v-if="selectedOrder" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-bold">Order Details #{{ selectedOrder.order_number || selectedOrder.id }}</h3>
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
            </div>
            <div>
              <p class="text-sm text-gray-600">Status</p>
              <span :class="getStatusClass(selectedOrder.status)">{{ selectedOrder.status }}</span>
            </div>
          </div>
          <div>
            <p class="text-sm text-gray-600 mb-2">Items</p>
            <div class="bg-gray-50 rounded-lg p-4 space-y-2">
              <div v-for="item in selectedOrder.items" :key="item.id" class="flex justify-between items-center py-2 border-b last:border-0">
                <div class="flex items-center space-x-3">
                  <img v-if="item.product?.image || item.image" :src="item.product?.image || item.image" class="w-12 h-12 object-cover rounded" />
                  <div>
                    <p class="font-medium">{{ item.product?.title || item.name }}</p>
                    <p class="text-sm text-gray-500">Qty: {{ item.quantity }}</p>
                  </div>
                </div>
                <span class="font-semibold">Tsh {{ Number(item.price).toLocaleString() }}</span>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center pt-4 border-t">
            <div>
              <p class="text-sm text-gray-600">Order Date</p>
              <p class="font-medium">{{ formatDate(selectedOrder.created_at || selectedOrder.date) }}</p>
            </div>
            <div class="text-right">
              <p class="text-sm text-gray-600">Total Amount</p>
              <p class="text-2xl font-bold text-blue-600">
                Tsh {{ Number(selectedOrder.total_amount || selectedOrder.total).toLocaleString() }}
              </p>
            </div>
          </div>
          <div class="flex justify-end space-x-3 pt-4">
            <button @click="selectedOrder = null" class="px-4 py-2 border rounded-lg hover:bg-gray-50">Close</button>
            <button v-if="selectedOrder.status === 'Pending'" @click="confirmOrder(selectedOrder.id); selectedOrder = null" class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600">Confirm</button>
            <button v-if="selectedOrder.status === 'Confirmed'" @click="completeOrder(selectedOrder.id); selectedOrder = null" class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">Complete</button>
            <button v-if="['Pending', 'Confirmed'].includes(selectedOrder.status)" @click="cancelOrder(selectedOrder.id); selectedOrder = null" class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600">Cancel</button>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, inject, onMounted } from 'vue'
import Swal from 'sweetalert2'

export default {
  name: 'Admin',
  setup() {
    const products = ref([])
    const orders = ref([])
    const allOrders = ref([])
    const allUsers = ref([])
    const stats = ref({})
    const currentUser = ref(null)
    const activeTab = ref('dashboard')
    const orderStatusFilter = ref('all')
    const selectedOrder = ref(null)
    const API_BASE_URL = 'http://localhost:8000/api'
    
    const getToken = () => localStorage.getItem('token')
    
    const tabs = computed(() => [
      { id: 'dashboard', name: 'Dashboard' },
      { id: 'orders', name: 'Orders', badge: stats.value.pending_orders, route: '/admin/orders' },
      { id: 'users', name: 'Users' },
      { id: 'products', name: 'Products' }
    ])
    
    const dashboardStats = computed(() => [
      { label: 'Total Users', value: stats.value.total_users || 0, bgColor: 'bg-blue-100', iconColor: 'text-blue-600', icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z' },
      { label: 'Total Orders', value: stats.value.total_orders || 0, bgColor: 'bg-green-100', iconColor: 'text-green-600', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2 2v10a2 2 0 002 2h6a2 2 0 002-2V9a2 2 0 00-2-2H9z' },
      { label: 'Total Products', value: stats.value.total_products || 0, bgColor: 'bg-orange-100', iconColor: 'text-orange-600', icon: 'M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4' },
      { label: 'Total Revenue', value: `Tsh ${Number(stats.value.total_revenue || 0).toLocaleString()}`, bgColor: 'bg-purple-100', iconColor: 'text-purple-600', icon: 'M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z' }
    ])

    const filteredOrdersList = computed(() => {
      if (orderStatusFilter.value === 'all') return allOrders.value
      return allOrders.value.filter(order => order.status === orderStatusFilter.value)
    })

    const newProduct = ref({
      name: '',
      price: 0,
      category: '',
      image: '',
      description: ''
    })
    const isAddingProduct = ref(false)
    const editingProduct = ref(null)
    const isEditing = ref(false)
    const viewingProduct = ref(null)
    const productToDelete = ref(null)
    
    // New table functionality
    const searchQuery = ref('')
    const filterDropdownOpen = ref(false)
    const selectedProducts = ref([])
    const currentFilter = ref('all')

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

    // Vue confirm dialog
    const confirmDelete = (index) => {
      productToDelete.value = index
      showConfirmDialog.value = true
    }

    const cancelDelete = () => {
      productToDelete.value = null
      showConfirmDialog.value = false
    }

    const executeDelete = () => {
      if (productToDelete.value !== null) {
        const productName = products.value[productToDelete.value].name
        products.value.splice(productToDelete.value, 1)
        saveProducts()
        showNotificationMessage(`${productName} removed successfully!`)
        cancelDelete()
      }
    }

    // Product Management Functions
    const addProduct = async () => {
      isAddingProduct.value = true
      try {
        const response = await fetch(`${API_BASE_URL}/products/`, {
          method: 'POST',
          headers: {
            'Authorization': `Token ${getToken()}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({
            title: newProduct.value.name,
            price: newProduct.value.price,
            category: newProduct.value.category,
            image: newProduct.value.image,
            description: newProduct.value.description
          })
        })
        
        if (response.ok) {
          const newProductData = await response.json()
          products.value.push(newProductData)
          showNotificationMessage('Product added successfully!')
          resetProductForm()
          loadData() // Refresh products list
        } else {
          const error = await response.json()
          showNotificationMessage('Failed to add product: ' + JSON.stringify(error), 'error')
        }
      } catch (error) {
        showNotificationMessage('Failed to add product', 'error')
      } finally {
        isAddingProduct.value = false
      }
    }

    const resetProductForm = () => {
      newProduct.value = {
        name: '',
        price: 0,
        category: '',
        image: '',
        description: ''
      }
    }

    // Load data from localStorage
    const loadData = () => {
      const savedProducts = localStorage.getItem('adminProducts')
      if (savedProducts) {
        products.value = JSON.parse(savedProducts)
      } else {
        // Load default products
        products.value = [
          { name: 'Mac Book', price: 1000000, category: 'laptops', image: '/images/w.jpg' },
          { name: 'HP-Brand', price: 150000, category: 'laptops', image: '/images/j.jpg' },
          { name: 'Dell', price: 200000, category: 'laptops', image: '/images/k.jpg' },
          { name: 'Apple', price: 1000000, category: 'phones', image: '/images/d.jpg' },
          { name: 'HP-Elite', price: 1500000, category: 'laptops', image: '/images/a.jpg' },
          { name: 'Sony', price: 200000, category: 'accessories', image: '/images/f.jpg' },
          { name: 'Infinix', price: 400000, category: 'phones', image: '/images/g.jpg' },
          { name: 'iPhone', price: 1500000, category: 'phones', image: '/images/p.jpg' },
          { name: 'Samsung', price: 3000000, category: 'phones', image: '/images/l.jpg' }
        ]
        saveProducts()
      }
      
      orders.value = JSON.parse(localStorage.getItem('orders')) || []
    }

    const saveProducts = () => {
      localStorage.setItem('adminProducts', JSON.stringify(products.value))
    }

    const totalRevenue = computed(() => {
      return orders.value.reduce((total, order) => total + order.total, 0)
    })

    const pendingOrders = computed(() => {
      return orders.value.filter(order => order.status === 'Pending').length
    })

    // Filtered products based on search and filter
    const filteredProducts = computed(() => {
      let filtered = products.value

      // Apply search filter
      if (searchQuery.value) {
        filtered = filtered.filter(product => 
          product.name.toLowerCase().includes(searchQuery.value.toLowerCase()) ||
          product.category.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
      }

      // Apply category filter
      if (currentFilter.value === 'category') {
        filtered = filtered.sort((a, b) => a.category.localeCompare(b.category))
      } else if (currentFilter.value === 'price') {
        filtered = filtered.sort((a, b) => a.price - b.price)
      }

      return filtered
    })

    // View product functions
    const viewProduct = (product) => {
      viewingProduct.value = { ...product, addedDate: new Date().toISOString() }
    }

    const closeViewModal = () => {
      viewingProduct.value = null
    }

    // Edit product functions
    const editProduct = (product) => {
      editingProduct.value = JSON.parse(JSON.stringify(product))
      isEditing.value = true
      closeViewModal()
    }

    const closeEditModal = () => {
      editingProduct.value = null
      isEditing.value = false
    }

    const updateProduct = () => {
      if (!editingProduct.value || !editingProduct.value.name) {
        showNotificationMessage('No product to update')
        return
      }
      
      const index = products.value.findIndex(p => p.name === editingProduct.value.name)
      if (index !== -1) {
        products.value[index] = JSON.parse(JSON.stringify(editingProduct.value))
        saveProducts()
        closeEditModal()
        showNotificationMessage('Product updated successfully!')
      } else {
        showNotificationMessage('Product not found')
      }
    }

    // Enhanced remove product function with Vue confirm
    const removeProduct = (index) => {
      confirmDelete(index)
    }

    // Format date function
    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    // New table functionality methods
    const toggleFilterDropdown = () => {
      filterDropdownOpen.value = !filterDropdownOpen.value
    }

    const setFilter = (filter) => {
      currentFilter.value = filter
      filterDropdownOpen.value = false
    }

    const toggleSelectAll = (event) => {
      if (event.target.checked) {
        selectedProducts.value = filteredProducts.value.map((_, index) => index)
      } else {
        selectedProducts.value = []
      }
    }

    // Admin Dashboard API Functions
    const loadDashboardStats = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/dashboard-stats/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) stats.value = await response.json()
      } catch (error) { console.error('Failed to load stats:', error) }
    }

    const loadAllOrders = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/orders/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) allOrders.value = await response.json()
      } catch (error) { console.error('Failed to load orders:', error) }
    }

    const loadAllUsers = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/users/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) allUsers.value = await response.json()
      } catch (error) { console.error('Failed to load users:', error) }
    }

    const confirmOrder = async (orderId) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 'Authorization': `Token ${getToken()}`, 'Content-Type': 'application/json' },
          body: JSON.stringify({ status: 'Confirmed' })
        })
        if (response.ok) {
          showNotificationMessage('Order confirmed successfully!')
          loadAllOrders()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to confirm order', 'error') }
    }

    const cancelOrder = async (orderId) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 'Authorization': `Token ${getToken()}`, 'Content-Type': 'application/json' },
          body: JSON.stringify({ status: 'Cancelled' })
        })
        if (response.ok) {
          showNotificationMessage('Order cancelled successfully!')
          loadAllOrders()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to cancel order', 'error') }
    }

    const completeOrder = async (orderId) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 'Authorization': `Token ${getToken()}`, 'Content-Type': 'application/json' },
          body: JSON.stringify({ status: 'Completed' })
        })
        if (response.ok) {
          showNotificationMessage('Order completed successfully!')
          loadAllOrders()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to complete order', 'error') }
    }

    const deleteOrder = async (orderId) => {
      if (!confirm('Are you sure you want to delete this order?')) return
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'DELETE',
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) {
          showNotificationMessage('Order deleted successfully!')
          allOrders.value = allOrders.value.filter(o => o.id !== orderId)
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to delete order', 'error') }
    }

    const viewOrderDetails = (order) => {
      selectedOrder.value = order
    }

    const deleteUser = async (userId) => {
      if (!confirm('Are you sure you want to delete this user?')) return
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/users/${userId}/`, {
          method: 'DELETE',
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) {
          showNotificationMessage('User deleted successfully!')
          loadAllUsers()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to delete user', 'error') }
    }

    const getStatusClass = (status) => {
      const classes = { 'Pending': 'bg-yellow-100 text-yellow-800', 'Confirmed': 'bg-blue-100 text-blue-800', 'Completed': 'bg-green-100 text-green-800', 'Cancelled': 'bg-red-100 text-red-800' }
      return classes[status] || 'bg-gray-100 text-gray-800'
    }

    const getRoleClass = (role) => {
      const classes = { 'admin': 'bg-red-100 text-red-800', 'author': 'bg-blue-100 text-blue-800', 'customer': 'bg-green-100 text-green-800' }
      return classes[role] || 'bg-gray-100 text-gray-800'
    }

    onMounted(() => {
      loadData()
      loadDashboardStats()
      loadAllOrders()
      loadAllUsers()
      const userData = localStorage.getItem('user')
      if (userData) currentUser.value = JSON.parse(userData)
    })

    return {
      products,
      orders,
      newProduct,
      editingProduct,
      isEditing,
      viewingProduct,
      productToDelete,
      searchQuery,
      filterDropdownOpen,
      selectedProducts,
      currentFilter,
      totalRevenue,
      filteredProducts,
      saveProducts,
      addProduct,
      resetProductForm,
      isAddingProduct,
      viewProduct,
      closeViewModal,
      editProduct,
      closeEditModal,
      updateProduct,
      removeProduct,
      confirmDelete,
      cancelDelete,
      executeDelete,
      formatDate,
      toggleFilterDropdown,
      setFilter,
      toggleSelectAll,
      // Admin Dashboard
      activeTab,
      tabs,
      dashboardStats,
      allOrders,
      allUsers,
      stats,
      currentUser,
      loadDashboardStats,
      loadAllOrders,
      loadAllUsers,
      confirmOrder,
      cancelOrder,
      completeOrder,
      deleteOrder,
      viewOrderDetails,
      selectedOrder,
      orderStatusFilter,
      filteredOrdersList,
      deleteUser,
      getStatusClass,
      getRoleClass
    }
  }
}
</script>
