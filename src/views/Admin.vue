<template>
  <!-- Admin Header -->
  <div class="bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg shadow-xl p-8 mb-8">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-4xl font-bold mb-2">Admin Dashboard</h1>
        <p class="text-blue-100">Manage your e-commerce store</p>
      </div>
      <div class="text-right">
        <div class="text-3xl font-bold">{{ products.length }}</div>
        <div class="text-sm text-blue-100">Total Products</div>
      </div>
    </div>
  </div>
    
    <div class="grid grid-cols-1 xl:grid-cols-3 gap-8">
      <!-- Add Product Section -->
      <div class="xl:col-span-2">
        <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
          <div class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-4">
            <h2 class="text-xl font-semibold flex items-center">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v16m8-8H4"></path>
              </svg>
              Add New Product
            </h2>
          </div>
          <div class="p-6">
            <form @submit.prevent="addProduct" class="space-y-6">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Product Name</label>
                  <input
                    v-model="newProduct.name"
                    type="text"
                    required
                    placeholder="Enter product name"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                  >
                </div>
                
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Price (Tsh)</label>
                  <input
                    v-model.number="newProduct.price"
                    type="number"
                    required
                    min="0"
                    placeholder="0"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                  >
                </div>
              </div>
              
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Category</label>
                  <select
                    v-model="newProduct.category"
                    required
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                  >
                    <option value="">Select Category</option>
                    <option value="laptops">💻 Laptops</option>
                    <option value="phones">📱 Smartphones</option>
                    <option value="accessories">⌚ Accessories</option>
                  </select>
                </div>
                
                <div>
                  <label class="block text-sm font-semibold text-gray-700 mb-2">Image URL</label>
                  <input
                    v-model="newProduct.image"
                    type="text"
                    required
                    placeholder="/images/product.jpg"
                    class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
                  >
                </div>
              </div>
              
              <button type="submit" class="w-full bg-gradient-to-r from-blue-500 to-blue-600 text-white font-semibold py-3 px-6 rounded-lg hover:from-blue-600 hover:to-blue-700 transition-all duration-200 shadow-lg">
                Add Product
              </button>
            </form>
          </div>
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
                <svg class="w-6 h-6 text-blue-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 7l-8-4-8 4M16 7l-4 4m0 0l-4-4m4 4V3m0 0v4m0 0l4 4m-4-4h8m-8 0v8m0 0h8m-8 0l4 4m0-4l-4 4"></path>
                </svg>
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
                <svg class="w-6 h-6 text-green-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                </svg>
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
                <svg class="w-6 h-6 text-yellow-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3-.895 3-2-1.343-2-3-2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1l-2.599-1.599M5 13h14"></path>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Manage Products Section -->
    <div class="mt-8">
      <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
        <div class="bg-gradient-to-r from-gray-700 to-gray-800 text-white px-6 py-4">
          <h2 class="text-xl font-semibold flex items-center">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10"></path>
            </svg>
            Manage Products
          </h2>
        </div>
        
        <div v-if="products.length === 0" class="p-12 text-center">
          <svg class="w-16 h-16 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 00-.293.707V17"></path>
          </svg>
          <p class="text-gray-500 text-lg">No products available.</p>
          <p class="text-gray-400 mt-2">Add your first product using the form above.</p>
        </div>
        
        <div v-else class="overflow-x-auto">
          <table class="w-full">
            <thead class="bg-gray-50 border-b border-gray-200">
              <tr>
                <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Product</th>
                <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
                <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
                <th class="px-6 py-4 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                <th class="px-6 py-4 text-center text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="(product, index) in products" :key="index" class="hover:bg-gray-50 transition-colors">
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="flex items-center">
                    <img v-if="product.image" :src="product.image" :alt="product.name" class="w-10 h-10 rounded-lg object-cover mr-3">
                    <div>
                      <div class="text-sm font-medium text-gray-900">{{ product.name }}</div>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="px-2 py-1 text-xs rounded-full bg-blue-100 text-blue-800">
                    {{ product.category }}
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <div class="text-sm text-gray-900 font-semibold">Tsh {{ product.price.toLocaleString() }}</div>
                </td>
                <td class="px-6 py-4 whitespace-nowrap">
                  <span class="px-2 py-1 text-xs rounded-full bg-green-100 text-green-800">
                    Active
                  </span>
                </td>
                <td class="px-6 py-4 whitespace-nowrap text-center">
                  <button
                    @click="removeProduct(index)"
                    class="text-red-600 hover:text-red-900 font-medium text-sm transition-colors"
                  >
                    Remove
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'

export default {
  name: 'Admin',
  setup() {
    const products = ref([])
    const orders = ref([])
    const newProduct = ref({
      name: '',
      price: 0,
      category: '',
      image: ''
    })

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

    const addProduct = () => {
      products.value.push({ ...newProduct.value })
      saveProducts()
      
      // Reset form
      newProduct.value = {
        name: '',
        price: 0,
        category: '',
        image: ''
      }
      
      alert('Product added successfully!')
    }

    const totalRevenue = computed(() => {
      return orders.value.reduce((total, order) => total + order.total, 0)
    })

    const pendingOrders = computed(() => {
      return orders.value.filter(order => order.status === 'Pending').length
    })

    onMounted(() => {
      loadData()
    })

    return {
      products,
      orders,
      newProduct,
      totalRevenue,
      pendingOrders,
      addProduct
    }
  }
}
</script>
