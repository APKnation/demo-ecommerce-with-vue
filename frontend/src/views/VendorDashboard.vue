<template>
  <div class="min-h-screen bg-gradient-to-br from-purple-50 via-white to-pink-50">
    <!-- Header -->
    <div class="bg-white shadow-sm border-b border-purple-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-purple-500 to-pink-500 rounded-xl flex items-center justify-center shadow-lg">
              <span class="text-white text-xl font-bold">🏪</span>
            </div>
            <h1 class="text-3xl font-bold bg-gradient-to-r from-purple-600 to-pink-600 bg-clip-text text-transparent">Vendor Dashboard</h1>
          </div>
          <router-link to="/" class="text-purple-600 hover:text-purple-800">
            ← Back to Home
          </router-link>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <!-- Vendor Status Alert -->
      <div v-if="!user?.is_vendor_approved" class="bg-yellow-50 border border-yellow-200 rounded-xl p-6 mb-8">
        <div class="flex items-center">
          <span class="text-3xl mr-4">⏳</span>
          <div>
            <h3 class="text-lg font-bold text-yellow-800">Vendor Account Pending Approval</h3>
            <p class="text-yellow-700 mt-1">Your vendor account is waiting for admin approval. You'll be notified once approved.</p>
          </div>
        </div>
      </div>

      <!-- Welcome Section -->
      <div v-if="user?.is_vendor_approved" class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 mb-8">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold text-gray-800">Welcome back, {{ user?.username || 'Vendor' }}! 👋</h2>
            <p class="text-gray-600 mt-1">Manage your products and track your sales</p>
          </div>
          <div class="text-right">
            <p class="text-sm text-gray-500">Vendor since</p>
            <p class="text-lg font-bold text-purple-600">{{ formatDate(user?.date_joined) }}</p>
          </div>
        </div>
      </div>

      <!-- Stats Grid -->
      <div v-if="user?.is_vendor_approved" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div class="bg-white rounded-xl shadow-md border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Total Products</p>
              <p class="text-3xl font-bold text-purple-600">{{ vendorStats.totalProducts }}</p>
            </div>
            <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
              <span class="text-2xl">📦</span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-md border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Active Products</p>
              <p class="text-3xl font-bold text-green-600">{{ vendorStats.activeProducts }}</p>
            </div>
            <div class="w-12 h-12 bg-green-100 rounded-xl flex items-center justify-center">
              <span class="text-2xl">✅</span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-md border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Total Sales</p>
              <p class="text-3xl font-bold text-blue-600">{{ vendorStats.totalSales }}</p>
            </div>
            <div class="w-12 h-12 bg-blue-100 rounded-xl flex items-center justify-center">
              <span class="text-2xl">💰</span>
            </div>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-md border border-gray-200 p-6">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">Revenue</p>
              <p class="text-3xl font-bold text-pink-600">Tsh {{ vendorStats.totalRevenue.toLocaleString() }}</p>
            </div>
            <div class="w-12 h-12 bg-pink-100 rounded-xl flex items-center justify-center">
              <span class="text-2xl">💵</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Quick Actions -->
      <div v-if="user?.is_vendor_approved" class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
        <div class="bg-white rounded-xl shadow-md border border-gray-200 p-6">
          <h3 class="text-lg font-bold text-gray-800 mb-4">Quick Actions</h3>
          <div class="space-y-3">
            <router-link to="/product-register" class="flex items-center justify-between p-3 bg-purple-50 rounded-lg hover:bg-purple-100 transition-colors">
              <div class="flex items-center">
                <span class="text-2xl mr-3">➕</span>
                <span class="font-medium text-purple-800">Add New Product</span>
              </div>
              <span class="text-purple-600">→</span>
            </router-link>
            
            <router-link to="/admin?tab=products" class="flex items-center justify-between p-3 bg-blue-50 rounded-lg hover:bg-blue-100 transition-colors">
              <div class="flex items-center">
                <span class="text-2xl mr-3">📦</span>
                <span class="font-medium text-blue-800">Manage Products</span>
              </div>
              <span class="text-blue-600">→</span>
            </router-link>
            
            <button @click="refreshStats" class="flex items-center justify-between p-3 bg-green-50 rounded-lg hover:bg-green-100 transition-colors w-full">
              <div class="flex items-center">
                <span class="text-2xl mr-3">🔄</span>
                <span class="font-medium text-green-800">Refresh Stats</span>
              </div>
              <span class="text-green-600">→</span>
            </button>
          </div>
        </div>

        <div class="bg-white rounded-xl shadow-md border border-gray-200 p-6">
          <h3 class="text-lg font-bold text-gray-800 mb-4">Recent Activity</h3>
          <div class="space-y-3">
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div class="flex items-center">
                <span class="text-2xl mr-3">📈</span>
                <div>
                  <p class="font-medium text-gray-800">Sales Today</p>
                  <p class="text-sm text-gray-600">{{ vendorStats.salesToday }} orders</p>
                </div>
              </div>
              <span class="text-green-600 font-bold">+{{ vendorStats.salesGrowth }}%</span>
            </div>
            
            <div class="flex items-center justify-between p-3 bg-gray-50 rounded-lg">
              <div class="flex items-center">
                <span class="text-2xl mr-3">👥</span>
                <div>
                  <p class="font-medium text-gray-800">New Customers</p>
                  <p class="text-sm text-gray-600">{{ vendorStats.newCustomers }} this week</p>
                </div>
              </div>
              <span class="text-blue-600 font-bold">+{{ vendorStats.customerGrowth }}%</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Products Table -->
      <div v-if="user?.is_vendor_approved" class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
        <div class="bg-gradient-to-r from-purple-600 to-pink-600 text-white px-6 py-4">
          <h2 class="text-xl font-bold">Your Products</h2>
        </div>
        <div class="p-6">
          <div v-if="vendorProducts.length > 0" class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-gray-50 border-b border-gray-200">
                <tr>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Product</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Stock</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Sales</th>
                  <th class="px-4 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="product in vendorProducts" :key="product.id" class="hover:bg-gray-50">
                  <td class="px-4 py-4 whitespace-nowrap">
                    <div class="flex items-center">
                      <img :src="getProductImage(product)" :alt="product.title" class="w-10 h-10 object-cover rounded-lg mr-3">
                      <div>
                        <div class="text-sm font-medium text-gray-900">{{ product.title }}</div>
                        <div class="text-xs text-gray-500">{{ product.category }}</div>
                      </div>
                    </div>
                  </td>
                  <td class="px-4 py-4 whitespace-nowrap">
                    <span class="text-sm font-bold text-gray-900">Tsh {{ Number(product.price).toLocaleString() }}</span>
                  </td>
                  <td class="px-4 py-4 whitespace-nowrap">
                    <span :class="product.stock > 10 ? 'text-green-600' : product.stock > 0 ? 'text-yellow-600' : 'text-red-600'" class="text-sm font-bold">
                      {{ product.stock }} units
                    </span>
                  </td>
                  <td class="px-4 py-4 whitespace-nowrap">
                    <span :class="product.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" class="px-2 py-1 rounded-full text-xs font-medium">
                      {{ product.is_active ? 'Active' : 'Inactive' }}
                    </span>
                  </td>
                  <td class="px-4 py-4 whitespace-nowrap">
                    <span class="text-sm font-bold text-purple-600">{{ product.sales_count || 0 }}</span>
                  </td>
                  <td class="px-4 py-4 whitespace-nowrap">
                    <router-link :to="`/admin?tab=products&edit=${product.id}`" class="text-purple-600 hover:text-purple-800 text-sm font-medium">
                      Edit
                    </router-link>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
          
          <div v-else class="text-center py-12">
            <span class="text-6xl">📦</span>
            <h3 class="text-xl font-bold text-gray-800 mt-4">No products yet</h3>
            <p class="text-gray-600 mt-2">Start by adding your first product</p>
            <router-link to="/product-register" class="mt-4 inline-flex items-center px-4 py-2 bg-purple-600 text-white rounded-lg hover:bg-purple-700">
              <span class="mr-2">➕</span>
              Add Product
            </router-link>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useAuth } from '../composables/useAuth'

const API_BASE_URL = 'http://localhost:8000/api'

export default {
  name: 'VendorDashboard',
  setup() {
    const { user } = useAuth()
    const vendorProducts = ref([])
    const vendorStats = ref({
      totalProducts: 0,
      activeProducts: 0,
      totalSales: 0,
      totalRevenue: 0,
      salesToday: 0,
      salesGrowth: 0,
      newCustomers: 0,
      customerGrowth: 0
    })
    const isLoading = ref(false)

    // Load vendor products
    const loadVendorProducts = async () => {
      if (!user.value?.id) return
      
      try {
        const token = localStorage.getItem('token')
        const response = await fetch(`${API_BASE_URL}/products/?vendor=${user.value.id}`, {
          headers: {
            'Authorization': `Token ${token}`
          }
        })
        
        if (response.ok) {
          const products = await response.json()
          vendorProducts.value = products
          updateStats(products)
        }
      } catch (error) {
        console.error('Error loading vendor products:', error)
      }
    }

    // Update vendor statistics
    const updateStats = (products) => {
      vendorStats.value = {
        totalProducts: products.length,
        activeProducts: products.filter(p => p.is_active).length,
        totalSales: products.reduce((sum, p) => sum + (p.sales_count || 0), 0),
        totalRevenue: products.reduce((sum, p) => sum + ((p.sales_count || 0) * Number(p.price || 0)), 0),
        salesToday: Math.floor(Math.random() * 10), // Mock data
        salesGrowth: Math.floor(Math.random() * 20), // Mock data
        newCustomers: Math.floor(Math.random() * 5), // Mock data
        customerGrowth: Math.floor(Math.random() * 15) // Mock data
      }
    }

    // Refresh stats
    const refreshStats = async () => {
      isLoading.value = true
      await loadVendorProducts()
      isLoading.value = false
    }

    // Get product image
    const getProductImage = (product) => {
      if (product.image) {
        return `http://localhost:8000${product.image}`
      }
      return 'http://localhost:8000/media/products/default-product.jpg'
    }

    // Format date
    const formatDate = (dateString) => {
      if (!dateString) return 'Unknown'
      return new Date(dateString).toLocaleDateString()
    }

    onMounted(() => {
      loadVendorProducts()
    })

    return {
      user,
      vendorProducts,
      vendorStats,
      isLoading,
      refreshStats,
      getProductImage,
      formatDate
    }
  }
}
</script>
