<template>
  <div>
    <!-- Vue Notification Component -->
    <div v-if="showNotification" class="fixed top-4 right-4 bg-success-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300 transform">
      {{ notification }}
    </div>

   <!-- Hero Section with Premium Design -->
    <section class="relative min-h-screen hero-gradient overflow-hidden rounded-3xl mx-4 mt-4 bg-gradient-to-br from-slate-900 via-blue-900 to-purple-900">
      <!-- Hero Content -->
<div class="relative z-10 min-h-screen flex items-center px-4 sm:px-6 lg:px-8">
  <div class="max-w-7xl mx-auto w-full">
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 lg:gap-16 items-center">
      
      <!-- Left Content -->
      <div class="space-y-6 lg:space-y-8 text-center lg:text-left">
        
        <!-- Badge -->
        <div class="inline-flex items-center justify-center px-6 py-4 bg-gradient-to-r from-orange-500 via-orange-600 to-orange-700 text-white rounded-full text-lg font-bold shadow-xl shadow-orange-500/30 transform hover:scale-105 transition-all duration-300">
          <div class="w-3 h-3 bg-white rounded-full mr-2 sm:mr-4 animate-pulse"></div>
          <span class="tracking-wide text-sm sm:text-base lg:text-lg">WELCOME TO KAFUKA STORE</span>
        </div>
        
        <!-- Main Title -->
        <div class="space-y-6">
          <h2 class="text-4xl md:text-6xl lg:text-7xl font-bold text-white/95 leading-tight italic">
            Your Smart
            <br>
            Electronics
            <br>
            <span class="bg-gradient-to-r from-orange-400 via-orange-500 to-orange-600 bg-clip-text text-transparent drop-shadow-lg italic">
              Shopping Cart
            </span>
          </h2>

          <!-- ✅ UPDATED DESCRIPTION -->
          <p class="text-xl md:text-2xl text-gray-300 leading-relaxed max-w-xl font-light italic">
            Shop the latest electronics including smartphones, laptops, accessories, and home gadgets—all in one place. 
            Add items to your cart, compare options, and enjoy a fast, secure checkout with reliable delivery.
          </p>
        </div>
        
        <!-- Call-to-Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-6 pt-4">
          <router-link to="/cart" class="relative inline-flex items-center justify-center px-12 py-5 bg-gradient-to-r from-orange-500 to-orange-600 text-white font-bold text-lg rounded-2xl hover:from-orange-600 hover:to-orange-700 transition-all duration-300 transform hover:scale-105 shadow-2xl shadow-orange-500/30 hover:shadow-orange-600/40">
            <span class="relative z-10">Browse Products</span>
            <div class="absolute inset-0 bg-gradient-to-r from-orange-600 to-orange-700 rounded-2xl opacity-0 hover:opacity-100 transition-opacity duration-300"></div>
          </router-link>
          
          <router-link to="/admin" class="relative inline-flex items-center justify-center px-12 py-5 bg-white/10 backdrop-blur-md text-white font-bold text-lg rounded-2xl hover:bg-white/20 transition-all duration-300 transform hover:scale-105 border-2 border-white/30 hover:border-white/50 shadow-xl">
            <span class="relative z-10">Admin Panel</span>
          </router-link>
        </div>
      </div>
      
      <!-- Right Content - Product Showcase -->
      <div class="relative scale-110 lg:scale-125">
        
        <!-- Glow Effect -->
        <div class="absolute inset-0 bg-gradient-to-r from-orange-500/20 to-purple-500/20 rounded-3xl blur-3xl transform scale-110"></div>
        
        <!-- Product Image -->
        <div class="relative z-10 group">
          <img 
            src="/images/w.jpg" 
            alt="Electronics Products" 
            class="w-full h-auto max-w-2xl mx-auto rounded-3xl shadow-2xl transform transition-all duration-500 group-hover:scale-105 group-hover:rotate-1"
          >
          
          <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent rounded-3xl"></div>
        </div>
        
        <!-- Floating Features -->
        <div class="absolute -top-16 left-1/2 transform -translate-x-1/2 flex gap-4">
          
          <!-- Fast Delivery -->
          <div class="bg-white/90 backdrop-blur-sm rounded-2xl shadow-xl p-4 transform hover:scale-110 transition-all duration-300 border">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 bg-orange-500 rounded-xl flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <div>
                <div class="font-bold text-gray-900 text-sm">Fast</div>
                <div class="text-gray-600 text-xs">Delivery</div>
              </div>
            </div>
          </div>
          
          <!-- Quality -->
          <div class="bg-white/90 backdrop-blur-sm rounded-2xl shadow-xl p-4 transform hover:scale-110 transition-all duration-300 border">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 bg-blue-500 rounded-xl flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                </svg>
              </div>
              <div>
                <div class="font-bold text-gray-900 text-sm">Premium</div>
                <div class="text-gray-600 text-xs">Quality</div>
              </div>
            </div>
          </div>
          
          <!-- Service -->
          <div class="bg-white/90 backdrop-blur-sm rounded-2xl shadow-xl p-4 transform hover:scale-110 transition-all duration-300 border">
            <div class="flex items-center space-x-3">
              <div class="w-10 h-10 bg-purple-500 rounded-xl flex items-center justify-center">
                <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                </svg>
              </div>
              <div>
                <div class="font-bold text-gray-900 text-sm">Trusted</div>
                <div class="text-gray-600 text-xs">Service</div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Decorative Elements -->
        <div class="absolute -top-10 right-10 w-20 h-20 bg-orange-400/20 rounded-full blur-2xl animate-pulse"></div>
        <div class="absolute -bottom-10 left-10 w-16 h-16 bg-blue-400/20 rounded-full blur-2xl animate-pulse"></div>
      </div>
    </div>
  </div>

  </div>
    </section>

    <!-- Search and Filter Section - Separate from Hero -->
    <section class="mb-8 mt-8 relative z-20">
      <div class="bg-white/95 backdrop-blur-md rounded-xl shadow-xl p-6 border-2 border-orange-200">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
          <!-- Search Bar -->
          <div class="md:col-span-2">
            <div class="flex">
              <input
                v-model="searchTerm"
                type="text"
                placeholder="Search products..."
                class="flex-grow px-4 py-3 border-2 border-orange-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500"
                @input="filterProducts"
              >
              <button
                @click="filterProducts"
                class="px-6 py-3 bg-orange-500 text-white rounded-r-lg hover:bg-orange-600 transition-colors focus:outline-none focus:ring-2 focus:ring-orange-500"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
                </svg>
              </button>
            </div>
          </div>
          
          <!-- Category Filter -->
          <select
            v-model="categoryFilter"
            class="w-full px-4 py-3 bg-white border-2 border-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 shadow-sm hover:shadow-md transition-all duration-200 appearance-none cursor-pointer bg-gradient-to-r from-orange-50 to-white hover:from-orange-100 hover:to-white"
            @change="filterProducts"
          >
            <option value="" class="text-gray-500">📂 All Categories</option>
            <option value="laptops">💻 Laptops</option>
            <option value="phones">📱 Smartphones</option>
            <option value="accessories">🎧 Accessories</option>
          </select>
          
          <!-- Price Filter -->
          <select
            v-model="priceFilter"
            class="w-full px-4 py-3 bg-white border-2 border-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500 shadow-sm hover:shadow-md transition-all duration-200 appearance-none cursor-pointer bg-gradient-to-r from-orange-50 to-white hover:from-orange-100 hover:to-white"
            @change="filterProducts"
          >
            <option value="" class="text-gray-500">💵 All Prices</option>
            <option value="0-200000">💰 Under Tsh 200,000</option>
            <option value="200000-1000000">💰 Tsh 200,000 - 1,000,000</option>
            <option value="1000000+">💰 Above Tsh 1,000,000</option>
          </select>
        </div>
        
        <!-- Sort Filter -->
        <div class="mt-4">
          <select
            v-model="sortFilter"
            class="w-full px-4 py-3 bg-white border-2 border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-blue-500 shadow-sm hover:shadow-md transition-all duration-200 appearance-none cursor-pointer bg-gradient-to-r from-gray-50 to-white hover:from-blue-50 hover:to-white"
            @change="filterProducts"
          >
            <option value="" class="text-gray-500">🔽 Sort By</option>
            <option value="name-asc">📝 Name (A-Z)</option>
            <option value="name-desc">📝 Name (Z-A)</option>
            <option value="price-asc">💰 Price (Low to High)</option>
            <option value="price-desc">💰 Price (High to Low)</option>
          </select>
        </div>
        
        <!-- Action Buttons -->
        <div class="flex gap-3 mt-4">
          <button 
            @click="addAllToCompare"
            class="btn btn-secondary flex items-center gap-2 bg-gradient-to-r from-blue-500 to-blue-600 hover:from-blue-600 hover:to-blue-700 text-white shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300 px-6 py-3 rounded-xl border-2 border-blue-400 hover:border-blue-500 focus:outline-none focus:ring-2 focus:ring-blue-300"
            :disabled="filteredProducts.length === 0"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002-2v2a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2H9z"></path>
            </svg>
            <span class="font-semibold">Select All ({{ filteredProducts.length }})</span>
          </button>
          <button 
            class="btn btn-ghost text-error-600 hover:text-error-700 hover:bg-red-50 px-6 py-3 rounded-xl border-2 border-transparent hover:border-red-200 transition-all duration-300 transform hover:scale-105 focus:outline-none focus:ring-2 focus:ring-red-300"
          >
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
            </svg>
            Clear Filters
          </button>
        </div>
      </div>
    </section>

    <!-- Product Listing -->
    <section>
      <!-- Loading State -->
      <div v-if="isLoading" class="text-center py-12">
        <div class="inline-block animate-spin rounded-full h-8 w-8 border-b-2 border-blue-600"></div>
        <p class="text-gray-500 mt-4">Loading products...</p>
      </div>
      
      <!-- Empty State -->
      <div v-else-if="filteredProducts.length === 0" class="text-center py-12">
        <div class="mb-8">
          <svg class="w-16 h-16 mx-auto text-gray-300 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M20 13V6a2 2 0 00-2-2H6a2 2 0 00-2 2v7m16 0v5a2 2 0 01-2 2H6a2 2 0 01-2-2v-5m16 0h-2.586a1 1 0 00-.707.293l-2.414 2.414a1 1 0 00-.293.707V17"></path>
          </svg>
          <p class="text-gray-500 text-lg">No products found matching your criteria.</p>
        </div>
      </div>
      
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-4 sm:gap-4 lg:gap-6">
        <div
          v-for="product in filteredProducts"
          :key="product.id || product.name"
          class="card bg-white rounded-xl shadow-md hover:shadow-2xl hover:bg-gradient-to-br from-orange-50 via-yellow-50 to-orange-100 transition-all duration-300 transform hover:scale-105 hover:-translate-y-2 hover:rotate-1 group border-2 border-transparent hover:border-orange-300"
        >
          <div class="relative overflow-hidden rounded-t-lg">
            <img
              :src="product.image || product.images?.[0] || `/images/${getProductImage(product.title || product.name)}`"
              :alt="product.title || product.name"
              class="w-full h-48 object-cover rounded-t-lg mb-4 group-hover:scale-110 transition-transform duration-500"
              @error="handleImageError"
            >
            <!-- Image Overlay Effect -->
            <div class="absolute inset-0 bg-gradient-to-t from-transparent via-transparent to-orange-200/30 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-t-lg"></div>
          </div>
          <div class="p-3 sm:p-4 lg:p-6">
            <h3 class="text-lg sm:text-xl lg:text-2xl font-semibold mb-2 sm:mb-3 text-gray-800 group-hover:text-orange-600 transition-colors duration-300">{{ product.title || product.name }}</h3>
            <p class="text-sm sm:text-base text-gray-600 mb-2 sm:mb-3 group-hover:text-orange-500 transition-colors duration-300">{{ product.category?.name || product.category }}</p>
            <div class="flex items-center justify-between mb-4">
              <p class="text-lg sm:text-xl lg:text-2xl font-bold text-blue-600 group-hover:text-orange-500 transition-colors duration-300">Tsh {{ Number(product.price).toLocaleString() }}</p>
              <div class="w-6 sm:w-8 h-6 sm:h-8 lg:w-8 lg:h-8 bg-gradient-to-br from-green-400 to-green-500 rounded-full flex items-center justify-center group-hover:from-green-500 group-hover:to-green-600 transition-all duration-300">
                <svg class="w-3 sm:w-4 sm:h-4 lg:w-4 lg:h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 9"></path>
                </svg>
              </div>
            </div>
          </div>
        
        <div class="flex flex-wrap gap-1 justify-between px-2">
          <button
            @click="addToCart(product.title || product.name, Number(product.price))"
            class="relative group btn-primary bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 text-white shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300 px-4 py-2 rounded-lg border-2 border-orange-400 hover:border-orange-500 focus:outline-none focus:ring-4 focus:ring-orange-300 overflow-hidden"
          >
            <!-- Background Animation -->
            <div class="absolute inset-0 bg-gradient-to-r from-orange-600 to-orange-700 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
            
            <span class="relative z-10 flex items-center justify-center">
              <!-- Enhanced Cart Icon -->
              <svg class="w-4 h-4 mr-2 transform group-hover:rotate-12 transition-transform duration-300" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
              <span class="font-bold text-xs sm:text-xs lg:text-sm uppercase">Add to Cart</span>
            </span>
          </button>
          
          <button
            @click="likeProduct(product)"
            class="relative group btn-danger bg-gradient-to-br from-red-500 via-pink-500 to-pink-600 hover:from-red-600 hover:via-pink-600 hover:to-pink-700 text-white shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-300 px-3 py-2 rounded-lg border-2 border-pink-400 hover:border-pink-500 focus:outline-none focus:ring-4 focus:ring-pink-300 overflow-hidden"
          >
            <!-- Heart Animation Background -->
            <div class="absolute inset-0 bg-gradient-to-br from-pink-600 to-red-600 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-lg"></div>
            
            <span class="relative z-10 flex items-center justify-center">
              <!-- Animated Heart Icon -->
              <svg class="w-4 h-4 transform group-hover:scale-110 transition-all duration-300" fill="currentColor" viewBox="0 0 24 24">
                <!-- Enhanced Heart Path -->
                <path class="group-hover:fill-pink-200 transition-colors duration-300" stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </span>
          </button>
        </div>
      </div>
    </div>
  <!-- ... -->
    </section>
  </div>
  
  <!-- Extra spacing to push content up -->
  <div class="mb-16"></div>
</template>

<script>
import { ref, computed, inject, onMounted } from 'vue'
import { useAuth } from '../composables/useAuth'
import { useAuthenticatedCart } from '../composables/useAuthenticatedCart'

export default {
  name: 'Home',
  setup() {
    const { isAuthenticated } = useAuth()
    const { addToCart: addToAuthenticatedCart } = useAuthenticatedCart()
    const searchTerm = ref('')
    const categoryFilter = ref('')
    const priceFilter = ref('')
    const sortFilter = ref('')
    const products = ref([])
    const isLoading = ref(true)
    const notification = ref('')
    const showNotification = ref(false)
    const showNotificationMessage = (message) => {
      notification.value = message
      showNotification.value = true
      setTimeout(() => {
        showNotification.value = false
        notification.value = ''
      }, 3000)
    }

    // Show green notification for green button
    const showGreenNotification = (product) => {
      showNotificationMessage(`Green action triggered for ${product.name}! 🟢`, 'success')
    }

    // Like product function (not wishlist)
    const likeProduct = (product) => {
      // Simple like without notification
    }
    
    // Load products from backend API
    const loadProducts = async () => {
      isLoading.value = true
      try {
        const response = await fetch('http://localhost:8000/api/products/')
        if (response.ok) {
          const data = await response.json()
          products.value = data
        } else {
          // Fallback to localStorage products if API fails
          const savedProducts = localStorage.getItem('adminProducts')
          if (savedProducts) {
            products.value = JSON.parse(savedProducts)
          } else {
            // Default products with IDs
            products.value = [
              { id: 1, name: 'Mac Book', price: 1000000, category: 'laptops', image: '/images/w.jpg' },
              { id: 2, name: 'HP-Brand', price: 150000, category: 'laptops', image: '/images/j.jpg' },
              { id: 3, name: 'Dell', price: 200000, category: 'laptops', image: '/images/k.jpg' },
              { id: 4, name: 'Apple', price: 1000000, category: 'phones', image: '/images/d.jpg' },
              { id: 5, name: 'HP-Elite', price: 1500000, category: 'laptops', image: '/images/a.jpg' },
              { id: 6, name: 'Sony', price: 200000, category: 'accessories', image: '/images/f.jpg' },
              { id: 7, name: 'Infinix', price: 400000, category: 'phones', image: '/images/g.jpg' },
              { id: 8, name: 'iPhone', price: 1500000, category: 'phones', image: '/images/p.jpg' },
              { id: 9, name: 'Samsung', price: 3000000, category: 'phones', image: '/images/l.jpg' }
            ]
          }
        }
        showNotificationMessage('Welcome to Kafuka Electronics Store!', 'info', true)
      } catch (error) {
        showNotificationMessage('Error loading products')
      } finally {
        isLoading.value = false
      }
    }

    // Load products on mount
    onMounted(() => {
      loadProducts()
    })

    // Inject parent data and methods
    const cart = inject('cart', ref([]))
    const guestAddToCart = inject('addToCart')

    // Unified addToCart function for both authenticated and guest users
    const addToCart = async (productName, productPrice) => {
      if (isAuthenticated.value) {
        try {
          // For authenticated users, find the product and add to backend cart
          const product = products.value.find(p => p.title === productName || p.name === productName)
          if (product && product.id) {
            await addToAuthenticatedCart(product.id, 1)
            showNotificationMessage(`${product.title || product.name} added to cart!`, 'success')
          } else {
            showNotificationMessage('Product not found or missing ID', 'error')
          }
        } catch (error) {
          showNotificationMessage('Failed to add to cart', 'error')
        }
      } else {
        // For guest users, use the existing localStorage cart
        if (guestAddToCart) {
          guestAddToCart({ name: productName, price: productPrice })
        }
      }
    }

    // Cart total computed property
    const cartTotal = computed(() => {
      return cart.value.reduce((total, item) => total + (item.price * item.quantity), 0)
    })

    // Filter and sort products
    const filteredProducts = computed(() => {
      let filtered = products.value.filter(product => {
        // Search filter
        const productTitle = product.title || product.name || ''
        const matchesSearch = productTitle.toLowerCase().includes(searchTerm.value.toLowerCase())
        
        // Category filter
        const categoryName = product.category?.name || product.category || ''
        const matchesCategory = !categoryFilter.value || categoryName === categoryFilter.value
        
        // Price filter
        const productPrice = Number(product.price)
        let matchesPrice = true
        if (priceFilter.value === '0-200000') {
          matchesPrice = productPrice <= 200000
        } else if (priceFilter.value === '200000-1000000') {
          matchesPrice = productPrice > 200000 && productPrice <= 1000000
        } else if (priceFilter.value === '1000000+') {
          matchesPrice = productPrice > 1000000
        }
        
        return matchesSearch && matchesCategory && matchesPrice
      })

      // Sort products
      if (sortFilter.value) {
        filtered.sort((a, b) => {
          const titleA = a.title || a.name || ''
          const titleB = b.title || b.name || ''
          const priceA = Number(a.price)
          const priceB = Number(b.price)
          
          switch(sortFilter.value) {
            case 'name-asc':
              return titleA.localeCompare(titleB)
            case 'name-desc':
              return titleB.localeCompare(titleA)
            case 'price-asc':
              return priceA - priceB
            case 'price-desc':
              return priceB - priceA
            default:
              return 0
          }
        })
      }

      return filtered
    })

    // Check if product is in compare list
    const isInCompare = (productName) => {
      return compareList.value.some(item => item.name === productName)
    }

    // Filter products function
    const filterProducts = () => {
      // This function is reactive due to computed property
    }

    // Add all filtered products to comparison
    const addAllToCompare = () => {
      const maxProducts = 4 // Maximum comparison limit
      const availableSlots = maxProducts - compareList.value.length
      const productsToAdd = filteredProducts.value.slice(0, availableSlots)
      
      productsToAdd.forEach(product => {
        if (!isInCompareList(product)) {
          addToCompare(product)
        }
      })
      
      if (productsToAdd.length < filteredProducts.value.length) {
        showNotification(`Added ${productsToAdd.length} products to comparison. Maximum ${maxProducts} products allowed.`, 'warning')
      } else {
        showNotification(`Added all ${productsToAdd.length} products to comparison!`, 'success')
      }
    }

    // Helper function to map product names to image files
    const getProductImage = (productName) => {
      const imageMap = {
        'Mac Book': 'w.jpg',
        'HP-Brand': 'j.jpg', 
        'Dell': 'k.jpg',
        'Apple iPhone': 'd.jpg',
        'iPhone': 'd.jpg',
        'HP-Elite': 'a.jpg',
        'Sony Headphones': 'f.jpg',
        'Sony': 'f.jpg',
        'Infinix Smartphone': 'g.jpg',
        'Infinix': 'g.jpg',
        'iPhone Pro': 'p.jpg',
        'Samsung Galaxy': 'l.jpg',
        'Samsung': 'l.jpg'
      }
      
      // Find matching image by checking if product name contains any key
      for (const [key, image] of Object.entries(imageMap)) {
        if (productName.toLowerCase().includes(key.toLowerCase())) {
          return image
        }
      }
      
      // Default fallback images
      const defaultImages = ['Computer.jpeg', 'iPhone.jpg', 'watch1.jpeg']
      return defaultImages[Math.floor(Math.random() * defaultImages.length)]
    }

    // Handle image loading errors
    const handleImageError = (event) => {
      event.target.src = '/images/Computer.jpeg'
    }

    return {
      searchTerm,
      categoryFilter,
      priceFilter,
      sortFilter,
      products,
      isLoading,
      notification,
      showNotification,
      cart,
      cartTotal,
      addToCart,
      filteredProducts,
      filterProducts,
      likeProduct,
      getProductImage,
      handleImageError
    }
  }
}
</script>
