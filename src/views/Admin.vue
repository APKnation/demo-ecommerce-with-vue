<template>
  <div>
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
    <div v-if="isEditing" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-96 overflow-y-auto">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold text-gray-900">Edit Product</h2>
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
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
              >
            </div>
            
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Price (Tsh)</label>
              <input
                v-model.number="editingProduct.price"
                type="number"
                required
                min="0"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
              >
            </div>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Category</label>
              <select
                v-model="editingProduct.category"
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
                v-model="editingProduct.image"
                type="text"
                required
                placeholder="/images/product.jpg"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all"
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
                  <div class="flex items-center justify-center space-x-2">
                    <button
                      @click="viewProduct(product)"
                      class="text-blue-600 hover:text-blue-900 font-medium text-sm transition-colors px-3 py-2 bg-blue-50 rounded"
                      title="View Product"
                    >
                      View
                    </button>
                    <button
                      @click="editProduct(product)"
                      class="text-yellow-600 hover:text-yellow-900 font-medium text-sm transition-colors px-3 py-2 bg-yellow-50 rounded"
                      title="Edit Product"
                    >
                      Edit
                    </button>
                    <button
                      @click="removeProduct(index)"
                      class="text-red-600 hover:text-red-900 font-medium text-sm transition-colors px-3 py-2 bg-red-50 rounded"
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

    // View product functions
    const viewProduct = (product) => {
      viewingProduct.value = { ...product, addedDate: new Date().toISOString() }
    }

    const closeViewModal = () => {
      viewingProduct.value = null
    }

    // Edit product functions
    const editProduct = (product) => {
      editingProduct.value = { ...product }
      isEditing.value = true
      closeViewModal()
    }

    const closeEditModal = () => {
      editingProduct.value = null
      isEditing.value = false
    }

    const updateProduct = () => {
      const index = products.value.findIndex(p => p.name === editingProduct.value.name)
      if (index !== -1) {
        products.value[index] = { ...editingProduct.value }
        saveProducts()
        closeEditModal()
        showNotificationMessage('Product updated successfully!')
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
      formatDate
    }
  }
}
</script>
