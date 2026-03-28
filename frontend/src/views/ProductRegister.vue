<template>
  <div class="min-h-screen bg-gray-50 py-8">
    <div class="max-w-3xl mx-auto px-4">
      <div class="bg-white rounded-lg shadow-lg p-6">
        <h1 class="text-2xl font-bold text-gray-900 mb-6">
      {{ isEditMode ? 'Edit Product' : 'Register New Product' }}
    </h1>
        
        <form @submit.prevent="handleSubmit" class="space-y-6">
          <!-- Product Title -->
          <div>
            <label for="title" class="block text-sm font-medium text-gray-700 mb-2">
              Product Title *
            </label>
            <input
              id="title"
              v-model="form.title"
              type="text"
              required
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Enter product title"
            >
          </div>

          <!-- Product Description -->
          <div>
            <label for="description" class="block text-sm font-medium text-gray-700 mb-2">
              Description *
            </label>
            <textarea
              id="description"
              v-model="form.description"
              required
              rows="4"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              placeholder="Enter product description"
            ></textarea>
          </div>

          <!-- Price and Stock -->
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label for="price" class="block text-sm font-medium text-gray-700 mb-2">
                Price ($) *
              </label>
              <input
                id="price"
                v-model.number="form.price"
                type="number"
                step="0.01"
                min="0"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="0.00"
              >
            </div>
            
            <div>
              <label for="stock" class="block text-sm font-medium text-gray-700 mb-2">
                Stock Quantity *
              </label>
              <input
                id="stock"
                v-model.number="form.stock"
                type="number"
                min="0"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="0"
              >
            </div>
          </div>

          <!-- Category and Condition -->
          <div class="grid grid-cols-2 gap-4">
            <div>
              <label for="category" class="block text-sm font-medium text-gray-700 mb-2">
                Category
              </label>
              <select
                id="category"
                v-model.number="form.category_id"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="">Select Category</option>
                <option v-for="category in categories" :key="category.id" :value="category.id">
                  {{ category.name }}
                </option>
              </select>
            </div>
            
            <div>
              <label for="condition" class="block text-sm font-medium text-gray-700 mb-2">
                Condition *
              </label>
              <select
                id="condition"
                v-model="form.condition"
                required
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
              >
                <option value="new">New</option>
                <option value="used">Used</option>
                <option value="refurbished">Refurbished</option>
              </select>
            </div>
          </div>

          <!-- Product Image -->
          <div>
            <label for="image" class="block text-sm font-medium text-gray-700 mb-2">
              Product Image
            </label>
            <input
              id="image"
              type="file"
              accept="image/*"
              @change="handleImageChange"
              class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            >
            <p class="text-sm text-gray-500 mt-1">Optional: Upload product image</p>
          </div>

          <!-- Active Status -->
          <div class="flex items-center">
            <input
              id="is_active"
              v-model="form.is_active"
              type="checkbox"
              class="w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500"
            >
            <label for="is_active" class="ml-2 text-sm text-gray-700">
              Make product active immediately
            </label>
          </div>

          <!-- Error Message -->
          <div v-if="error" class="bg-red-50 border border-red-200 rounded-lg p-4">
            <div class="flex items-center">
              <span class="text-lg">📝</span>
              <span class="text-red-700 text-sm">{{ error }}</span>
            </div>
          </div>

          <!-- Success Message -->
          <div v-if="successMessage" class="bg-green-50 border border-green-200 rounded-lg p-4">
            <div class="flex items-center">
              <span class="text-lg">📝</span>
              <span class="text-green-700 text-sm">{{ successMessage }}</span>
            </div>
          </div>

          <!-- Submit Button -->
          <div class="flex justify-end space-x-4">
            <router-link
              to="/admin"
              class="px-4 py-2 border border-gray-300 rounded-lg text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              Cancel
            </router-link>
            <button
              type="submit"
              :disabled="isLoading"
              class="px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none focus:ring-2 focus:ring-blue-500 disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="isLoading">{{ isEditMode ? 'Updating...' : 'Registering...' }}</span>
              <span v-else>{{ isEditMode ? 'Update Product' : 'Register Product' }}</span>
            </button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRouter, useRoute } from 'vue-router'

export default {
  name: 'ProductRegister',
  setup() {
    const router = useRouter()
    const route = useRoute()
    
    // Check if we're in edit mode
    const isEditMode = ref(!!route.params.id)
    const productId = ref(route.params.id || null)
    
    const form = ref({
      title: '',
      description: '',
      price: 0,
      stock: 1,
      condition: 'new',
      category_id: null,
      image: null,
      is_active: true
    })
    
    const categories = ref([])
    const isLoading = ref(false)
    const error = ref('')
    const successMessage = ref('')

    // Load categories
    const loadCategories = async () => {
      try {
        const response = await fetch('http://localhost:8000/api/products/categories/')
        if (response.ok) {
          categories.value = await response.json()
        }
      } catch (err) {
        console.error('Error loading categories:', err)
      }
    }

    // Handle image change
    const handleImageChange = (event) => {
      form.value.image = event.target.files[0]
    }

    // Load product data for edit mode
    const loadProduct = async () => {
      if (!isEditMode.value || !productId.value) return
      
      try {
        const token = localStorage.getItem('token')
        const response = await fetch(`http://localhost:8000/api/products/${productId.value}/`, {
          headers: {
            'Authorization': `Token ${token}`
          }
        })
        
        if (response.ok) {
          const product = await response.json()
          form.value = {
            title: product.title,
            description: product.description,
            price: parseFloat(product.price),
            stock: product.stock || 1,
            condition: product.condition,
            category_id: product.category?.id || null,
            image: null,
            is_active: product.is_active
          }
        } else {
          error.value = 'Failed to load product data'
        }
      } catch (err) {
        error.value = 'Error loading product: ' + err.message
      }
    }

    // Handle form submission
    const handleSubmit = async () => {
      isLoading.value = true
      error.value = ''
      successMessage.value = ''
      
      try {
        // Get auth token
        const token = localStorage.getItem('token')
        if (!token) {
          throw new Error('You must be logged in to register a product')
        }
        
        // Use FormData for file upload
        const formData = new FormData()
        
        // Add all form fields
        formData.append('title', form.value.title)
        formData.append('description', form.value.description)
        formData.append('price', form.value.price)
        formData.append('stock', form.value.stock)
        formData.append('condition', form.value.condition)
        formData.append('is_active', form.value.is_active)
        
        // Add category if selected
        if (form.value.category_id) {
          formData.append('category', form.value.category_id)
        }
        
        // Add image if selected
        if (form.value.image) {
          formData.append('image', form.value.image)
        }
        
        // Determine URL and method based on edit mode
        const url = isEditMode.value 
          ? `http://localhost:8000/api/products/${productId.value}/manage/`
          : 'http://localhost:8000/api/products/create/'
        const method = isEditMode.value ? 'PUT' : 'POST'
        
        const response = await fetch(url, {
          method: method,
          headers: {
            'Authorization': `Token ${token}`
            // Don't set Content-Type for FormData - browser sets it automatically with boundary
          },
          body: formData
        })
        
        const data = await response.json()
        
        if (!response.ok) {
          throw new Error(data.error || JSON.stringify(data) || 'Failed to register product')
        }
        
        successMessage.value = isEditMode.value ? 'Product updated successfully! Redirecting...' : 'Product registered successfully! Redirecting...'
        
        // Redirect after a short delay
        setTimeout(() => {
          router.push('/admin')
        }, 2000)
        
      } catch (err) {
        error.value = err.message
      } finally {
        isLoading.value = false
      }
    }

    onMounted(() => {
      loadCategories()
      if (isEditMode.value) {
        loadProduct()
      }
    })

    return {
      form,
      categories,
      isLoading,
      error,
      successMessage,
      isEditMode,
      handleImageChange,
      handleSubmit
    }
  }
}
</script>
