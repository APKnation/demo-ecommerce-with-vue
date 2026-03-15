<template>
  <div>
    <!-- Vue Notification Component -->
    <div v-if="showNotification" class="fixed top-4 right-4 bg-success-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300 transform">
      {{ notification }}
    </div>

    <!-- Hero Section with Premium Design -->
    <section class="relative min-h-screen bg-gradient-to-br from-blue-600/90 via-purple-600/90 to-orange-600/90 overflow-hidden rounded-3xl mx-4 mt-4">
      <!-- Animated Background Elements -->
      <div class="absolute inset-0">
        <!-- Gradient Mesh -->
        <div class="absolute inset-4 bg-gradient-to-r from-blue-600/20 via-purple-600/20 to-orange-500/20 rounded-3xl"></div>
        
        <!-- Floating Particles -->
        <div class="absolute top-20 left-20 w-2 h-2 bg-blue-400 rounded-full animate-pulse"></div>
        <div class="absolute top-40 right-32 w-3 h-3 bg-purple-400 rounded-full animate-ping"></div>
        <div class="absolute bottom-32 left-40 w-2 h-2 bg-orange-400 rounded-full animate-pulse"></div>
        <div class="absolute top-60 right-20 w-4 h-4 bg-blue-300 rounded-full animate-ping"></div>
        <div class="absolute bottom-20 right-40 w-2 h-2 bg-purple-300 rounded-full animate-pulse"></div>
        
        <!-- Geometric Shapes -->
        <div class="absolute top-0 right-0 w-96 h-96 bg-gradient-to-br from-blue-500/10 to-purple-500/10 rounded-full blur-3xl transform translate-x-1/2 -translate-y-1/2"></div>
        <div class="absolute bottom-0 left-0 w-80 h-80 bg-gradient-to-tr from-orange-500/10 to-red-500/10 rounded-full blur-3xl transform -translate-x-1/2 translate-y-1/2"></div>
      </div>
      
      <!-- Hero Content -->
      <div class="relative z-10 min-h-screen flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-16 items-center">
            
            <!-- Left Content -->
            <div class="space-y-8">
              <!-- Badge -->
              <div class="inline-flex items-center px-8 py-4 bg-gradient-to-r from-orange-500 via-orange-600 to-orange-700 text-white rounded-full text-lg font-bold shadow-xl shadow-orange-500/30 transform hover:scale-105 transition-all duration-300">
                <div class="w-3 h-3 bg-white rounded-full mr-4 animate-pulse"></div>
                <span class="tracking-wide">WELCOME TO KAFUKA STORE</span>
              </div>
              
              <!-- Main Title -->
              <div class="space-y-6">
                <h2 class="text-4xl md:text-6xl lg:text-7xl font-bold text-white/95 leading-tight italic">
                  Where Innovation
                  <br>
                  Meets
                  <br>
                  <span class="bg-gradient-to-r from-orange-400 via-orange-500 to-orange-600 bg-clip-text text-transparent drop-shadow-lg italic">Excellence</span>
                </h2>
                <p class="text-xl md:text-2xl text-gray-300 leading-relaxed max-w-xl font-light italic">
                  Discover cutting-edge electronics and premium gadgets that redefine your digital experience. Quality, innovation, and service delivered.
                </p>
              </div>
              
              <!-- Call-to-Action Buttons -->
              <div class="flex flex-col sm:flex-row gap-6 pt-4">
                <router-link to="/cart" class="relative inline-flex items-center justify-center px-12 py-5 bg-gradient-to-r from-orange-500 to-orange-600 text-white font-bold text-lg rounded-2xl hover:from-orange-600 hover:to-orange-700 transition-all duration-300 transform hover:scale-105 shadow-2xl shadow-orange-500/30 hover:shadow-orange-600/40">
                  <span class="relative z-10">Shop Now</span>
                  <div class="absolute inset-0 bg-gradient-to-r from-orange-600 to-orange-700 rounded-2xl opacity-0 hover:opacity-100 transition-opacity duration-300"></div>
                </router-link>
                
                <router-link to="/admin" class="relative inline-flex items-center justify-center px-12 py-5 bg-white/10 backdrop-blur-md text-white font-bold text-lg rounded-2xl hover:bg-white/20 transition-all duration-300 transform hover:scale-105 border-2 border-white/30 hover:border-white/50 shadow-xl">
                  <span class="relative z-10">Admin Panel</span>
                </router-link>
              </div>
            </div>
            
            <!-- Right Content - 3D Product Showcase -->
            <div class="relative scale-110 lg:scale-125">
              <!-- Glow Effect -->
              <div class="absolute inset-0 bg-gradient-to-r from-orange-500/20 to-purple-500/20 rounded-3xl blur-3xl transform scale-110"></div>
              
              <!-- Main Product Container -->
              <div class="relative z-10">
                <!-- Product Image -->
                <div class="relative group">
                  <img 
                    src="/images/w.jpg" 
                    alt="Featured Product" 
                    class="w-full h-auto max-w-2xl mx-auto rounded-3xl shadow-2xl transform transition-all duration-500 group-hover:scale-105 group-hover:rotate-1"
                  >
                  
                  <!-- Image Overlay Gradient -->
                  <div class="absolute inset-0 bg-gradient-to-t from-black/20 via-transparent to-transparent rounded-3xl"></div>
                </div>
              </div>
              
              <!-- Floating Cards - At Top of Image -->
              <div class="absolute -top-16 left-1/2 transform -translate-x-1/2 flex gap-4">
                <div class="bg-white/90 backdrop-blur-sm rounded-2xl shadow-xl p-4 transform hover:scale-110 transition-all duration-300 border border-white/20">
                  <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-gradient-to-br from-orange-500 to-orange-600 rounded-xl flex items-center justify-center">
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
                
                <div class="bg-white/90 backdrop-blur-sm rounded-2xl shadow-xl p-4 transform hover:scale-110 transition-all duration-300 border border-white/20">
                  <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-blue-600 rounded-xl flex items-center justify-center">
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
                
                <div class="bg-white/90 backdrop-blur-sm rounded-2xl shadow-xl p-4 transform hover:scale-110 transition-all duration-300 border border-white/20">
                  <div class="flex items-center space-x-3">
                    <div class="w-10 h-10 bg-gradient-to-br from-purple-500 to-purple-600 rounded-xl flex items-center justify-center">
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
              <div class="absolute -top-10 right-10 w-20 h-20 bg-gradient-to-br from-orange-400/20 to-orange-600/20 rounded-full blur-2xl animate-pulse"></div>
              <div class="absolute -bottom-10 left-10 w-16 h-16 bg-gradient-to-br from-blue-400/20 to-blue-600/20 rounded-full blur-2xl animate-pulse"></div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- Search and Filter Section -->
    <section class="mb-8 -mt-16 relative z-20">
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
            class="px-4 py-3 border-2 border-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500"
            @change="filterProducts"
          >
            <option value="">All Categories</option>
            <option value="laptops">Laptops</option>
            <option value="phones">Smartphones</option>
            <option value="accessories">Accessories</option>
          </select>
          
          <!-- Price Filter -->
          <select
            v-model="priceFilter"
            class="px-4 py-3 border-2 border-orange-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-orange-500 focus:border-orange-500"
            @change="filterProducts"
          >
            <option value="">All Prices</option>
            <option value="0-200000">Under Tsh 200,000</option>
            <option value="200000-1000000">Tsh 200,000 - 1,000,000</option>
            <option value="1000000+">Above Tsh 1,000,000</option>
          </select>
        </div>
        
        <!-- Sort Filter -->
        <div class="mt-4">
          <select
            v-model="sortFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            @change="filterProducts"
          >
            <option value="">Sort By</option>
            <option value="name-asc">Name (A-Z)</option>
            <option value="name-desc">Name (Z-A)</option>
            <option value="price-asc">Price (Low to High)</option>
            <option value="price-desc">Price (High to Low)</option>
          </select>
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
      
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="product in filteredProducts"
          :key="product.name"
          class="card bg-white rounded-xl shadow-md hover:shadow-2xl hover:bg-gradient-to-br from-orange-50 via-yellow-50 to-orange-100 transition-all duration-300 transform hover:scale-105 hover:-translate-y-2 hover:rotate-1 group border-2 border-transparent hover:border-orange-300"
        >
          <div class="relative overflow-hidden rounded-t-lg">
            <img
              :src="product.image"
              :alt="product.name"
              class="w-full h-48 object-cover rounded-t-lg mb-4 group-hover:scale-110 transition-transform duration-500"
            >
            <!-- Image Overlay Effect -->
            <div class="absolute inset-0 bg-gradient-to-t from-transparent via-transparent to-orange-200/30 opacity-0 group-hover:opacity-100 transition-opacity duration-300 rounded-t-lg"></div>
          </div>
          <div class="p-4">
            <h3 class="text-xl font-semibold mb-2 text-gray-800 group-hover:text-orange-600 transition-colors duration-300">{{ product.name }}</h3>
            <p class="text-gray-600 mb-2 group-hover:text-orange-500 transition-colors duration-300">{{ product.category }}</p>
            <div class="flex items-center justify-between mb-4">
              <p class="text-2xl font-bold text-blue-600 group-hover:text-orange-500 transition-colors duration-300">Tsh {{ product.price.toLocaleString() }}</p>
              <div class="w-8 h-8 bg-gradient-to-br from-green-400 to-green-500 rounded-full flex items-center justify-center group-hover:from-green-500 group-hover:to-green-600 transition-all duration-300">
                <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 9"></path>
                </svg>
              </div>
            </div>
            
            <div class="flex flex-wrap gap-2">
              <button
                @click="addToCart(product.name, product.price)"
                class="btn btn-primary flex-grow bg-gradient-to-r from-orange-500 to-orange-600 hover:from-orange-600 hover:to-orange-700 hover:shadow-lg hover:scale-105 transform transition-all duration-300"
              >
                <span class="flex items-center justify-center">
                  <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                  </svg>
                  Add to Cart
                </span>
              </button>
              <button
                @click="toggleWishlist(product.name, product.price, product.image)"
                :class="isInWishlist(product.name) ? 'bg-gradient-to-r from-red-500 to-pink-600 hover:from-red-600 hover:to-pink-700 text-white' : 'bg-gradient-to-r from-gray-200 to-gray-300 hover:from-gray-300 hover:to-gray-400 text-gray-700 hover:text-white'"
                class="btn text-sm px-3 transition-all duration-300 hover:scale-110 hover:shadow-lg"
              >
                <span class="flex items-center justify-center">
                  <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                  </svg>
                  {{ isInWishlist(product.name) ? '❤️' : '🤍' }}
                </span>
              </button>
              <button
                @click="addToCompare(product.name, product.price)"
                :class="isInCompare(product.name) ? 'bg-gradient-to-r from-red-500 to-pink-600 hover:from-red-600 hover:to-pink-700 text-white' : 'bg-gradient-to-r from-green-500 to-green-600 hover:from-green-600 hover:to-green-700 text-white hover:scale-110'"
                class="btn text-sm px-3 transition-all duration-300 hover:shadow-lg"
              >
                <span class="flex items-center justify-center">
                  <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v10a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002-2v2a2 2 0 002 2h2a2 2 0 002-2V7a2 2 0 00-2-2H9z"></path>
                  </svg>
                  ⚖️
                </span>
              </button>
            </div>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, computed, inject, onMounted } from 'vue'

export default {
  name: 'Home',
  setup() {
    const searchTerm = ref('')
    const categoryFilter = ref('')
    const priceFilter = ref('')
    const sortFilter = ref('')
    const products = ref([])
    const isLoading = ref(true)
    const notification = ref('')
    const showNotification = ref(false)

    // Vue notification system
    const showNotificationMessage = (message) => {
      notification.value = message
      showNotification.value = true
      setTimeout(() => {
        showNotification.value = false
        notification.value = ''
      }, 3000)
    }
    
    // Load products from localStorage or use defaults
    const loadProducts = async () => {
      isLoading.value = true
      try {
        const savedProducts = localStorage.getItem('adminProducts')
        if (savedProducts) {
          products.value = JSON.parse(savedProducts)
        } else {
          // Default products
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
    const wishlist = inject('wishlist', ref([]))
    const compareList = inject('compareList', ref([]))
    const cart = inject('cart', ref([]))
    const addToCart = inject('addToCart')
    const toggleWishlist = inject('toggleWishlist')
    const addToCompare = inject('addToCompare')

    // Cart total computed property
    const cartTotal = computed(() => {
      return cart.value.reduce((total, item) => total + (item.price * item.quantity), 0)
    })

    // Filter and sort products
    const filteredProducts = computed(() => {
      let filtered = products.value.filter(product => {
        // Search filter
        const matchesSearch = product.name.toLowerCase().includes(searchTerm.value.toLowerCase())
        
        // Category filter
        const matchesCategory = !categoryFilter.value || product.category === categoryFilter.value
        
        // Price filter
        let matchesPrice = true
        if (priceFilter.value === '0-200000') {
          matchesPrice = product.price <= 200000
        } else if (priceFilter.value === '200000-1000000') {
          matchesPrice = product.price > 200000 && product.price <= 1000000
        } else if (priceFilter.value === '1000000+') {
          matchesPrice = product.price > 1000000
        }
        
        return matchesSearch && matchesCategory && matchesPrice
      })

      // Sort products
      if (sortFilter.value) {
        filtered.sort((a, b) => {
          switch(sortFilter.value) {
            case 'name-asc':
              return a.name.localeCompare(b.name)
            case 'name-desc':
              return b.name.localeCompare(a.name)
            case 'price-asc':
              return a.price - b.price
            case 'price-desc':
              return b.price - a.price
            default:
              return 0
          }
        })
      }

      return filtered
    })

    // Check if product is in wishlist
    const isInWishlist = (productName) => {
      return wishlist.value.some(item => item.name === productName)
    }

    // Check if product is in compare list
    const isInCompare = (productName) => {
      return compareList.value.some(item => item.name === productName)
    }

    // Filter products function
    const filterProducts = () => {
      // This function is reactive due to computed property
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
      filteredProducts,
      isInWishlist,
      isInCompare,
      filterProducts,
      addToCart,
      toggleWishlist,
      addToCompare
    }
  }
}
</script>
