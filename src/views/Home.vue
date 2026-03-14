<template>
  <div>
    <!-- Vue Notification Component -->
    <div v-if="showNotification" class="fixed top-4 right-4 bg-green-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300 transform">
      {{ notification }}
    </div>

    <!-- Search and Filter Section -->
    <section class="mb-8">
      <div class="bg-white rounded-lg shadow-md p-6">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
          <!-- Search Bar -->
          <div class="md:col-span-2">
            <div class="flex">
              <input
                v-model="searchTerm"
                type="text"
                placeholder="Search products..."
                class="flex-grow px-4 py-2 border border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                @input="filterProducts"
              >
              <button
                @click="filterProducts"
                class="btn btn-primary rounded-l-none"
              >
                Search
              </button>
            </div>
          </div>
          
          <!-- Category Filter -->
          <select
            v-model="categoryFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
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
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
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

    <!-- Shopping Cart Information Section -->
    <section class="mb-12">
      <div class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-xl shadow-lg p-8">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8 items-center">
          <!-- Cart Information -->
          <div>
            <h2 class="text-3xl font-bold text-gray-800 mb-4">Shopping Cart Made Easy</h2>
            <p class="text-gray-600 mb-6 text-lg leading-relaxed">
              Our shopping cart system provides a seamless online shopping experience. Browse through our wide selection of electronics, add items to your cart with a single click, and manage your purchases effortlessly.
            </p>
            
            <!-- Features List -->
            <div class="space-y-3 mb-6">
              <div class="flex items-start space-x-3">
                <div class="flex-shrink-0 w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <div>
                  <h3 class="font-semibold text-gray-800">Easy Product Management</h3>
                  <p class="text-gray-600 text-sm">Add, remove, and update quantities with simple controls</p>
                </div>
              </div>
              
              <div class="flex items-start space-x-3">
                <div class="flex-shrink-0 w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <div>
                  <h3 class="font-semibold text-gray-800">Real-time Price Calculation</h3>
                  <p class="text-gray-600 text-sm">See your total update instantly as you shop</p>
                </div>
              </div>
              
              <div class="flex items-start space-x-3">
                <div class="flex-shrink-0 w-6 h-6 bg-green-500 rounded-full flex items-center justify-center">
                  <svg class="w-4 h-4 text-white" fill="currentColor" viewBox="0 0 20 20">
                    <path fill-rule="evenodd" d="M16.707 5.293a1 1 0 010 1.414l-8 8a1 1 0 01-1.414 0l-4-4a1 1 0 011.414-1.414L8 12.586l7.293-7.293a1 1 0 011.414 0z" clip-rule="evenodd"></path>
                  </svg>
                </div>
                <div>
                  <h3 class="font-semibold text-gray-800">Secure Checkout Process</h3>
                  <p class="text-gray-600 text-sm">Safe and secure payment processing</p>
                </div>
              </div>
            </div>
            
            <!-- Call to Action -->
            <div class="flex flex-col sm:flex-row gap-4">
              <router-link to="/cart" class="btn btn-primary flex items-center justify-center">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                View Cart
              </router-link>
              <router-link to="/orders" class="btn btn-secondary flex items-center justify-center">
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                </svg>
                Order History
              </router-link>
            </div>
          </div>
          
          <!-- Cart Visual -->
          <div class="flex justify-center">
            <div class="bg-white rounded-lg shadow-xl p-6 max-w-sm w-full">
              <div class="text-center mb-4">
                <svg class="w-20 h-20 mx-auto text-blue-500 mb-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                <h3 class="text-xl font-bold text-gray-800 mb-2">Your Shopping Cart</h3>
                <p class="text-gray-600">Manage your items efficiently</p>
              </div>
              
              <!-- Cart Stats -->
              <div class="grid grid-cols-2 gap-4 mb-4">
                <div class="bg-blue-50 rounded-lg p-3 text-center">
                  <div class="text-2xl font-bold text-blue-600">{{ cart.length }}</div>
                  <div class="text-xs text-gray-600">Items in Cart</div>
                </div>
                <div class="bg-green-50 rounded-lg p-3 text-center">
                  <div class="text-2xl font-bold text-green-600">Tsh {{ cartTotal.toLocaleString() }}</div>
                  <div class="text-xs text-gray-600">Cart Total</div>
                </div>
              </div>
              
              <!-- Quick Actions -->
              <div class="space-y-2">
                <button 
                  @click="$router.push('/cart')" 
                  class="w-full btn btn-primary text-sm py-2"
                  :disabled="cart.length === 0"
                >
                  {{ cart.length === 0 ? 'Cart is Empty' : 'Proceed to Cart' }}
                </button>
                <button 
                  @click="$router.push('/')" 
                  class="w-full btn btn-secondary text-sm py-2"
                >
                  Continue Shopping
                </button>
              </div>
            </div>
          </div>
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
          class="card hover:shadow-lg transition-shadow duration-300"
        >
          <img
            :src="product.image"
            :alt="product.name"
            class="w-full h-48 object-cover rounded-t-lg mb-4"
          >
          <h3 class="text-xl font-semibold mb-2">{{ product.name }}</h3>
          <p class="text-gray-600 mb-2">{{ product.category }}</p>
          <p class="text-2xl font-bold text-blue-600 mb-4">Tsh {{ product.price.toLocaleString() }}</p>
          
          <div class="flex flex-wrap gap-2">
            <button
              @click="addToCart(product.name, product.price)"
              class="btn btn-primary flex-grow"
            >
              Add to Cart
            </button>
            <button
              @click="toggleWishlist(product.name, product.price, product.image)"
              :class="isInWishlist(product.name) ? 'bg-red-500 hover:bg-red-600' : 'bg-gray-200 hover:bg-gray-300'"
              class="btn text-sm px-3"
            >
              {{ isInWishlist(product.name) ? '❤️' : '🤍' }}
            </button>
            <button
              @click="addToCompare(product.name, product.price)"
              :class="isInCompare(product.name) ? 'bg-red-500 hover:bg-red-600 text-white' : 'bg-green-500 hover:bg-green-600 text-white'"
              class="btn text-sm px-3"
            >
              ⚖️
            </button>
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
        showNotificationMessage('Products loaded successfully!')
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
