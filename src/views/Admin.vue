<template>
  <div>
    <!-- Admin Header with Profile -->
    <div class="bg-gradient-to-r from-primary-600 to-secondary-600 text-white rounded-lg shadow-xl p-8 mb-8">
    <div class="flex items-center justify-between">
      <div class="flex items-center space-x-4">
        <!-- Profile Image -->
        <div class="relative">
          <img 
            src="/images/IMG-20240518-WA0002.jpg" 
            alt="Admin Profile" 
            class="w-16 h-16 rounded-full object-cover border-3 border-white shadow-lg"
          >
          <div class="absolute bottom-0 right-0 w-4 h-4 bg-success-500 rounded-full border-2 border-white"></div>
        </div>
        <div>
          <h1 class="text-4xl font-bold mb-2">Admin Dashboard</h1>
          <p class="text-primary-100">Manage your e-commerce store</p>
        </div>
      </div>
      <div class="text-right">
        <div class="text-3xl font-bold">{{ products.length }}</div>
        <div class="text-sm text-primary-100">Total Products</div>
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
  </div>
    
    <div class="grid grid-cols-1 xl:grid-cols-3 gap-8">
      <!-- Add Product Section -->
      <div class="xl:col-span-2">
        <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
          <div class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-4">
            <h2 class="text-xl font-semibold flex items-center">
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
                    <option value="laptops">Laptops</option>
                    <option value="phones">Smartphones</option>
                    <option value="accessories">Accessories</option>
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
    
    <!-- Manage Products Section -->
    <div class="mt-8">
      <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
        <div class="bg-gradient-to-r from-gray-700 to-gray-800 text-white px-6 py-4">
          <h2 class="text-xl font-semibold flex items-center">
            Manage Products
          </h2>
        </div>
        
        <div v-if="products.length === 0" class="p-12 text-center">
          <p class="text-gray-500 text-lg">No products available.</p>
          <p class="text-gray-400 mt-2">Add your first product using the form above.</p>
        </div>
        
        <div v-else class="relative overflow-x-auto bg-neutral-50 shadow-xs rounded-lg border border-neutral-200">
          <!-- Table Header with Search and Filter -->
          <div class="p-4 flex items-center justify-between space-x-4">
            <label for="input-group-1" class="sr-only">Search</label>
            <div class="relative">
              <div class="absolute inset-y-0 start-0 flex items-center ps-3 pointer-events-none">
                <svg class="w-4 h-4 text-neutral-500" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                  <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="m21 21-3.5-3.5M17 10a7 7 0 1 1-14 0 7 7 0 0 1 14 0Z"/>
                </svg>
              </div>
              <input 
                type="text" 
                id="input-group-1" 
                class="block w-full max-w-96 ps-9 pe-3 py-2 bg-white border border-neutral-300 text-neutral-900 text-sm rounded-lg focus:ring-primary-500 focus:border-primary-500 shadow-xs placeholder:text-neutral-500" 
                placeholder="Search products..."
                v-model="searchQuery"
              >
            </div>
            <button 
              @click="toggleFilterDropdown" 
              class="shrink-0 inline-flex items-center justify-center text-neutral-700 bg-white border border-neutral-300 hover:bg-neutral-100 hover:text-neutral-900 focus:ring-4 focus:ring-neutral-300 shadow-xs font-medium leading-5 rounded-lg text-sm px-3 py-2 focus:outline-none" 
              type="button"
            >
              <svg class="w-4 h-4 me-1.5 -ms-0.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                <path stroke="currentColor" stroke-linecap="round" stroke-width="2" d="M18.796 4H5.204a1 1 0 0 0-.753 1.659l5.302 6.058a1 1 0 0 1 .247.659v4.874a.5.5 0 0 0 .2.4l3 2.25a.5.5 0 0 0 .8-.4v-7.124a1 1 0 0 1 .247-.659l5.302-6.059c.566-.646.106-1.658-.753-1.658Z"/>
              </svg>
              Filter by
              <svg class="w-4 h-4 ms-1.5 -me-0.5" aria-hidden="true" xmlns="http://www.w3.org/2000/svg" width="24" height="24" fill="none" viewBox="0 0 24 24">
                <path stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="m19 9-7 7-7-7"/>
              </svg>
            </button>
            <!-- Dropdown menu -->
            <div v-if="filterDropdownOpen" class="z-10 absolute top-full right-0 mt-2 bg-white border border-neutral-300 rounded-lg shadow-lg w-32">
              <ul class="p-2 text-sm text-neutral-700 font-medium" aria-labelledby="dropdownDefaultButton">
                <li>
                  <button @click="setFilter('category')" class="inline-flex items-center w-full p-2 hover:bg-neutral-100 hover:text-neutral-900 rounded">
                    Category
                  </button>
                </li>
                <li>
                  <button @click="setFilter('price')" class="inline-flex items-center w-full p-2 hover:bg-neutral-100 hover:text-neutral-900 rounded">
                    Price
                  </button>
                </li>
                <li>
                  <button @click="setFilter('all')" class="inline-flex items-center w-full p-2 hover:bg-neutral-100 hover:text-neutral-900 rounded">
                    All
                  </button>
                </li>
              </ul>
            </div>
          </div>
          
          <!-- Table -->
          <table class="w-full text-sm text-left rtl:text-right text-neutral-700">
            <thead class="text-sm text-neutral-700 bg-neutral-100 border-b border-t border-neutral-300">
              <tr>
                <th scope="col" class="p-4">
                  <div class="flex items-center">
                    <input 
                      id="table-checkbox-all" 
                      type="checkbox" 
                      value="" 
                      class="w-4 h-4 border border-neutral-300 rounded bg-neutral-50 focus:ring-2 focus:ring-primary-500"
                      @change="toggleSelectAll"
                    >
                    <label for="table-checkbox-all" class="sr-only">Table checkbox</label>
                  </div>
                </th>
                <th scope="col" class="px-6 py-3 font-medium">
                  Product name
                </th>
                <th scope="col" class="px-6 py-3 font-medium">
                  Category
                </th>
                <th scope="col" class="px-6 py-3 font-medium">
                  Price
                </th>
                <th scope="col" class="px-6 py-3 font-medium">
                  Status
                </th>
                <th scope="col" class="px-6 py-3 font-medium">
                  Action
                </th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(product, index) in filteredProducts" :key="index" class="bg-white border-b border-neutral-200 hover:bg-neutral-50">
                <td class="w-4 p-4">
                  <div class="flex items-center">
                    <input 
                      :id="`table-checkbox-${index}`" 
                      type="checkbox" 
                      value="" 
                      class="w-4 h-4 border border-neutral-300 rounded bg-neutral-50 focus:ring-2 focus:ring-primary-500"
                      v-model="selectedProducts"
                      :value="index"
                    >
                    <label :for="`table-checkbox-${index}`" class="sr-only">Table checkbox</label>
                  </div>
                </td>
                <th scope="row" class="px-6 py-4 font-medium text-neutral-900 whitespace-nowrap">
                  <div class="flex items-center">
                    <img v-if="product.image" :src="product.image" :alt="product.name" class="w-10 h-10 rounded-lg object-cover mr-3">
                    <div>
                      <div class="text-sm font-medium text-neutral-900">{{ product.name }}</div>
                    </div>
                  </div>
                </th>
                <td class="px-6 py-4">
                  <span class="px-2 py-1 text-xs rounded-full bg-primary-100 text-primary-800">
                    {{ product.category }}
                  </span>
                </td>
                <td class="px-6 py-4">
                  Tsh {{ product.price.toLocaleString() }}
                </td>
                <td class="px-6 py-4">
                  <span class="px-2 py-1 text-xs rounded-full bg-success-100 text-success-800">
                    Active
                  </span>
                </td>
                <td class="px-6 py-4">
                  <div class="flex items-center space-x-2">
                    <button
                      @click="viewProduct(product)"
                      class="font-medium text-primary-600 hover:underline"
                      title="View Product"
                    >
                      View
                    </button>
                    <button
                      @click="editProduct(product)"
                      class="font-medium text-primary-600 hover:underline"
                      title="Edit Product"
                    >
                      Edit
                    </button>
                    <button
                      @click="removeProduct(index)"
                      class="font-medium text-error-600 hover:underline"
                      title="Delete Product"
                    >
                      Delete
                    </button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- Vue Notification Component -->
    <div v-if="showNotification" class="fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300 transform">
      {{ notification }}
    </div>

    <!-- Vue Confirm Dialog -->
    <div v-if="showConfirmDialog" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 transition-opacity duration-200">
      <div class="bg-white rounded-xl p-6 max-w-md w-full mx-4 transition-all duration-200 transform">
        <div class="text-center">
          <div class="mx-auto flex items-center justify-center h-12 w-12 rounded-full bg-red-100 mb-4">
            <span class="text-red-600 text-2xl">⚠️</span>
          </div>
          <h3 class="text-lg font-semibold text-gray-900 mb-2">Confirm Delete</h3>
          <p class="text-gray-600 mb-6">
            Are you sure you want to delete this product? This action cannot be undone.
          </p>
          <div class="flex space-x-3">
            <button
              @click="cancelDelete"
              class="flex-1 px-4 py-2 bg-gray-200 text-gray-800 rounded-lg hover:bg-gray-300 transition-colors"
            >
              Cancel
            </button>
            <button
              @click="executeDelete"
              class="flex-1 px-4 py-2 bg-red-600 text-white rounded-lg hover:bg-red-700 transition-colors"
            >
              Delete
            </button>
          </div>
        </div>
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
    const editingProduct = ref(null)
    const isEditing = ref(false)
    const viewingProduct = ref(null)
    const notification = ref('')
    const showNotification = ref(false)
    const showConfirmDialog = ref(false)
    const productToDelete = ref(null)
    
    // New table functionality
    const searchQuery = ref('')
    const filterDropdownOpen = ref(false)
    const selectedProducts = ref([])
    const currentFilter = ref('all')

    // Reactive notification system
    const showNotificationMessage = (message) => {
      notification.value = message
      showNotification.value = true
      setTimeout(() => {
        showNotification.value = false
        notification.value = ''
      }, 3000)
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
      
      showNotificationMessage('Product added successfully!')
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

    onMounted(() => {
      loadData()
    })

    return {
      products,
      orders,
      newProduct,
      editingProduct,
      isEditing,
      viewingProduct,
      notification,
      showNotification,
      showConfirmDialog,
      productToDelete,
      totalRevenue,
      pendingOrders,
      // New table functionality
      searchQuery,
      filterDropdownOpen,
      selectedProducts,
      currentFilter,
      filteredProducts,
      addProduct,
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
      // New table methods
      toggleFilterDropdown,
      setFilter,
      toggleSelectAll
    }
  }
}
</script>
