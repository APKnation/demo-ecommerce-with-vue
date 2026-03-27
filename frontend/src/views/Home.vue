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
            Add items to your cart and enjoy a fast, secure checkout with reliable delivery.
          </p>
        </div>
        
        <!-- Call-to-Action Buttons -->
        <div class="flex flex-col sm:flex-row gap-6 pt-4">
          <router-link to="/cart" class="relative inline-flex items-center justify-center px-12 py-5 bg-gradient-to-r from-orange-500 to-orange-600 text-white font-bold text-lg rounded-2xl hover:from-orange-600 hover:to-orange-700 transition-all duration-300 transform hover:scale-105 shadow-2xl shadow-orange-500/30 hover:shadow-orange-600/40">
            <span class="relative z-10">Browse Products</span>
            <div class="absolute inset-0 bg-gradient-to-r from-orange-600 to-orange-700 rounded-2xl opacity-0 hover:opacity-100 transition-opacity duration-300"></div>
          </router-link>
          
          <router-link v-if="isAuthenticated" to="/user-dashboard" class="relative inline-flex items-center justify-center px-12 py-5 bg-gradient-to-r from-purple-500 to-purple-600 text-white font-bold text-lg rounded-2xl hover:from-purple-600 hover:to-purple-700 transition-all duration-300 transform hover:scale-105 shadow-2xl shadow-purple-500/30 hover:shadow-purple-600/40">
            <span class="relative z-10">My Dashboard</span>
            <div class="absolute inset-0 bg-gradient-to-r from-purple-600 to-purple-700 rounded-2xl opacity-0 hover:opacity-100 transition-opacity duration-300"></div>
          </router-link>
          
          <router-link v-if="!isAuthenticated" to="/login" class="relative inline-flex items-center justify-center px-12 py-5 bg-white/10 backdrop-blur-md text-white font-bold text-lg rounded-2xl hover:bg-white/20 transition-all duration-300 transform hover:scale-105 border-2 border-white/30 hover:border-white/50 shadow-xl">
            <span class="relative z-10">Sign In</span>
          </router-link>
          
          <router-link v-if="isAuthenticated && user?.is_staff" to="/admin" class="relative inline-flex items-center justify-center px-12 py-5 bg-white/10 backdrop-blur-md text-white font-bold text-lg rounded-2xl hover:bg-white/20 transition-all duration-300 transform hover:scale-105 border-2 border-white/30 hover:border-white/50 shadow-xl">
            <span class="relative z-10">Admin Panel</span>
          </router-link>
        </div>
      </div>
      
      <!-- Right Content - Product Showcase -->
      <div class="relative">
        
        <!-- Simplified Glow Effect -->
        <div class="absolute inset-0 bg-gradient-to-r from-orange-500/10 to-purple-500/10 rounded-3xl blur-2xl"></div>
        
        <!-- Dynamic Product Image -->
        <div class="relative z-10 group">
          <img 
            src="/images/Computer.jpeg" 
            alt="Electronics Products" 
            class="w-full h-auto max-w-2xl mx-auto rounded-3xl shadow-2xl transition-all duration-300 group-hover:scale-105"
            loading="lazy"
          >
          
          <!-- Simple Overlay -->
          <div class="absolute inset-0 bg-gradient-to-t from-black/10 via-transparent to-transparent rounded-3xl opacity-0 group-hover:opacity-20 transition-opacity duration-300"></div>
        </div>
        
        <!-- Simplified Floating Features -->
        <div class="absolute -top-16 left-1/2 transform -translate-x-1/2 flex gap-4">
          
          <!-- Fast Delivery -->
          <div class="bg-white/95 backdrop-blur-sm rounded-2xl shadow-lg p-4 transition-all duration-300 hover:scale-105">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-orange-500 rounded-lg flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                </svg>
              </div>
              <div>
                <div class="font-bold text-gray-900 text-sm">Fast</div>
                <div class="text-gray-600 text-xs">Delivery</div>
              </div>
            </div>
          </div>
          
          <!-- Premium Quality -->
          <div class="bg-white/95 backdrop-blur-sm rounded-2xl shadow-lg p-4 transition-all duration-300 hover:scale-105">
            <div class="flex items-center space-x-3">
              <div class="w-8 h-8 bg-purple-500 rounded-lg flex items-center justify-center">
                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2M7 13h10l4-8H5.4M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
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
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364z"></path>
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
      
      <div v-else class="grid grid-cols-1 xs:grid-cols-2 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-3 xl:grid-cols-4 gap-3 xs:gap-3 sm:gap-4 md:gap-4 lg:gap-6">
        <div
          v-for="product in filteredProducts"
          :key="product.id || product.name"
          class="card bg-white rounded-xl shadow-md hover:shadow-2xl hover:bg-gradient-to-br from-orange-50 via-yellow-50 to-orange-100 transition-all duration-300 transform hover:scale-105 hover:-translate-y-2 hover:rotate-1 group border-2 border-transparent hover:border-orange-300"
        >
          <div class="relative overflow-hidden rounded-t-lg">
            <img
              :src="getImageUrl(product.image)"
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
            @click="addToCart(product)"
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
            :class="[
              'relative group transform hover:scale-105 transition-all duration-300 px-3 py-2 rounded-lg border-2 focus:outline-none focus:ring-4 overflow-hidden',
              isProductLiked(product) 
                ? 'bg-gradient-to-br from-red-600 via-pink-600 to-red-700 hover:from-red-700 hover:via-pink-700 hover:to-red-800 text-white shadow-lg hover:shadow-xl border-pink-500 focus:ring-pink-400' 
                : 'bg-gradient-to-br from-red-500 via-pink-500 to-pink-600 hover:from-red-600 hover:via-pink-600 hover:to-pink-700 text-white shadow-lg hover:shadow-xl border-pink-400 hover:border-pink-500 focus:ring-pink-300'
            ]"
          >
            <!-- Heart Animation Background -->
            <div :class="[
              'absolute inset-0 transition-opacity duration-300 rounded-lg',
              isProductLiked(product) 
                ? 'bg-gradient-to-br from-pink-700 to-red-700 opacity-100' 
                : 'bg-gradient-to-br from-pink-600 to-red-600 opacity-0 group-hover:opacity-100'
            ]"></div>
            
            <span class="relative z-10 flex items-center justify-center">
              <!-- Animated Heart Icon -->
              <svg 
                class="w-4 h-4 transform transition-all duration-300" 
                :class="[
                  'group-hover:scale-110',
                  isProductLiked(product) ? 'scale-125' : ''
                ]" 
                :fill="isProductLiked(product) ? 'currentColor' : 'none'" 
                viewBox="0 0 24 24"
              >
                <!-- Enhanced Heart Path -->
                <path 
                  :class="[
                    'transition-colors duration-300',
                    isProductLiked(product) ? 'fill-pink-200' : 'group-hover:fill-pink-200'
                  ]" 
                  stroke-linecap="round" 
                  stroke-linejoin="round" 
                  stroke-width="1.5" 
                  d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"
                />
              </svg>
            </span>
          </button>
          
          <!-- Admin CRUD Buttons - Only show for admin users -->
          <div v-if="isAuthenticated && user?.is_staff" class="flex flex-wrap gap-1 mt-2">
            <button
              @click="viewProduct(product)"
              class="btn btn-sm bg-blue-500 text-white hover:bg-blue-600 px-2 py-1 rounded text-xs"
              title="View Product"
            >
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
              </svg>
            </button>
            
            <button
              @click="editProduct(product)"
              class="btn btn-sm bg-yellow-500 text-white hover:bg-yellow-600 px-2 py-1 rounded text-xs"
              title="Edit Product"
            >
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z"></path>
              </svg>
            </button>
            
            <button
              @click="deleteProduct(product)"
              class="btn btn-sm bg-red-500 text-white hover:bg-red-600 px-2 py-1 rounded text-xs"
              title="Delete Product"
            >
              <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
              </svg>
            </button>
          </div>
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
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'
import { useAuth } from '../composables/useAuth'
import { useAuthenticatedCart } from '../composables/useAuthenticatedCart'

export default {
  name: 'Home',
  setup() {
    const router = useRouter()
    const { isAuthenticated, user } = useAuth()
    const { addToCart: addToAuthenticatedCart } = useAuthenticatedCart()
    const searchTerm = ref('')
    const categoryFilter = ref('')
    const priceFilter = ref('')
    const sortFilter = ref('')
    const products = ref([])
    const isLoading = ref(true)
    const notification = ref('')
    const showNotification = ref(false)
    const likedProducts = ref([]) // Track liked products
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
      const index = likedProducts.value.findIndex(p => p.id === product.id)
      if (index === -1) {
        // Add to liked products
        likedProducts.value.push(product)
        showNotificationMessage(`${product.name || product.title} added to liked products!`, 'success')
      } else {
        // Remove from liked products
        likedProducts.value.splice(index, 1)
        showNotificationMessage(`${product.name || product.title} removed from liked products!`, 'info')
      }
    }
    
    // Check if product is liked
    const isProductLiked = (product) => {
      return likedProducts.value.some(p => p.id === product.id)
    }
    
    // Load products from backend API
    const loadProducts = async () => {
      isLoading.value = true
      try {
        const response = await fetch('http://localhost:8000/api/products/')
        if (response.ok) {
          const data = await response.json()
          console.log('Loaded products for Home:', data)
          products.value = data
        } else {
          // If API fails, show empty state
          products.value = []
          showNotificationMessage('Unable to load products. Please try again.', 'error')
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
    const addToCart = async (product) => {
      // Debug logging to see what we're getting
      console.log('addToCart called with product:', product)
      
      // Extract product name and price from the product object
      const productName = product.title || product.name || 'Unknown Product'
      const productPrice = Number(product.price)
      // Always use guest cart first (localStorage)
      if (guestAddToCart) {
        guestAddToCart(product)
        showNotificationMessage(`${productName} added to cart!`, 'success')
        
        // If user is authenticated and has token, also try to add to backend cart
        if (isAuthenticated.value && localStorage.getItem('token')) {
          try {
            if (product && product.id) {
              await addToAuthenticatedCart(product.id, 1)
            }
          } catch (error) {
            // Silently ignore backend cart errors, guest cart already worked
            console.log('Backend cart not available, using guest cart')
          }
        }
      }
    }

    // Cart total computed property
    const cartTotal = computed(() => {
      if (!cart.value || !Array.isArray(cart.value)) {
        return 0
      }
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

    // Helper function to get proper image URL from backend
    const getImageUrl = (imagePath) => {
      if (!imagePath) {
        return '/images/placeholder.jpg' // Fallback for truly missing images
      }
      
      // If it's already a full URL, return as is
      if (imagePath.startsWith('http://') || imagePath.startsWith('https://')) {
        return imagePath
      }
      
      // If it's a backend media URL, return as is
      if (imagePath.startsWith('/media/')) {
        return `http://localhost:8000${imagePath}` 
      }
      
      // If it's a full URL from backend, return as is
      if (imagePath.includes('localhost:8000')) {
        return imagePath
      }
      
      // If it's a relative path starting with /images/, use as is
      if (imagePath.startsWith('/images/')) {
        return imagePath
      }
      
      // Otherwise, assume it's a relative path to products folder
      return `http://localhost:8000/media/products/${imagePath}`
    }

    // Handle image loading errors
    const handleImageError = (event) => {
      event.target.src = '/images/placeholder.jpg'
    }

    // Admin CRUD Functions
    const viewProduct = (product) => {
      // Navigate to product detail page
      const productId = product.id
      if (productId) {
        router.push(`/product/${productId}`)
      } else {
        showNotificationMessage('Product ID not found', 'error')
      }
    }

    const editProduct = (product) => {
      // Navigate to admin edit page or open edit modal
      const productId = product.id
      if (productId) {
        router.push(`/admin/edit-product/${productId}`)
      } else {
        showNotificationMessage('Product ID not found', 'error')
      }
    }

    const deleteProduct = async (product) => {
      const productId = product.id
      if (!productId) {
        showNotificationMessage('Product ID not found', 'error')
        return
      }

      // Confirm deletion
      const result = await Swal.fire({
        title: 'Are you sure?',
        text: `Do you want to delete "${product.title || product.name}"?`,
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#d33',
        cancelButtonColor: '#3085d6',
        confirmButtonText: 'Yes, delete it!'
      })

      if (result.isConfirmed) {
        try {
          const token = localStorage.getItem('token')
          const response = await fetch(`http://localhost:8000/api/products/${productId}/manage/`, {
            method: 'DELETE',
            headers: {
              'Authorization': `Token ${token}`,
              'Content-Type': 'application/json'
            }
          })

          if (response.ok) {
            // Remove product from local list
            products.value = products.value.filter(p => p.id !== productId)
            showNotificationMessage('Product deleted successfully!')
          } else {
            const error = await response.json()
            showNotificationMessage('Failed to delete product: ' + JSON.stringify(error), 'error')
          }
        } catch (error) {
          showNotificationMessage('Failed to delete product', 'error')
        }
      }
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
      likedProducts,
      addToCart,
      filteredProducts,
      likeProduct,
      isProductLiked,
      getImageUrl,
      handleImageError,
      viewProduct,
      editProduct,
      deleteProduct,
      isAuthenticated,
      user
    }
  }
}
</script>
