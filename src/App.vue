<template>
  <div id="app" class="min-h-screen flex flex-col">
    <!-- Header -->
    <header class="bg-white shadow-lg sticky top-0 z-40 border-b border-gray-200 backdrop-blur-lg bg-opacity-95">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center h-16">
          <!-- Logo Section -->
          <div class="flex items-center space-x-3">
            <div class="relative group">
              <div class="w-10 h-10 bg-gradient-to-br from-blue-600 via-purple-600 to-blue-700 rounded-xl flex items-center justify-center transform transition-all duration-300 group-hover:scale-105 group-hover:shadow-lg">
                <span class="text-white font-bold text-lg tracking-tight">K</span>
                <div class="absolute inset-0 rounded-xl bg-gradient-to-br from-blue-600 via-purple-600 to-blue-700 opacity-0 group-hover:opacity-20 transition-opacity duration-300"></div>
              </div>
              <h1 class="text-2xl font-bold bg-gradient-to-r from-blue-600 to-purple-600 bg-clip-text text-transparent tracking-tight">KAFUKA Store</h1>
            </div>
          </div>
          
          <!-- Desktop Navigation -->
          <nav class="hidden md:flex items-center space-x-1">
            <!-- Admin Link -->
            <router-link to="/admin" class="nav-link group">
              <div class="flex items-center px-4 py-2 rounded-xl bg-gray-50 hover:bg-gradient-to-r hover:from-blue-50 hover:to-purple-50 border border border-transparent hover:border-blue-200 transition-all duration-300">
                <div class="w-2 h-2 bg-gradient-to-r from-blue-600 to-purple-600 rounded-full mr-2 group-hover:scale-110 transition-transform duration-300"></div>
                <span class="font-medium text-gray-700 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-purple-600 group-hover:bg-clip-text transition-all duration-300">
                  Admin
                </span>
              </div>
            </router-link>
            
            <!-- Home Link -->
            <router-link to="/" class="nav-link group">
              <div class="flex items-center px-4 py-2 rounded-xl bg-gray-50 hover:bg-gradient-to-r hover:from-blue-50 hover:to-purple-50 border border border-transparent hover:border-blue-200 transition-all duration-300">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-gray-100 to-gray-200 mr-2 flex items-center justify-center group-hover:from-blue-100 group-hover:to-blue-200 transition-all duration-300">
                  <div class="w-3 h-3 bg-gray-600 rounded-sm group-hover:bg-blue-600 transition-colors duration-300"></div>
                </div>
                <span class="font-medium text-gray-700 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-purple-600 group-hover:bg-clip-text transition-all duration-300">
                  Home
                </span>
              </div>
            </router-link>
            
            <!-- Cart Link -->
            <router-link to="/cart" class="nav-link group relative">
              <div class="flex items-center px-4 py-2 rounded-xl bg-gray-50 hover:bg-gradient-to-r hover:from-blue-50 hover:to-purple-50 border border border-transparent hover:border-blue-200 transition-all duration-300">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-green-100 to-emerald-100 mr-2 flex items-center justify-center group-hover:from-blue-100 group-hover:to-blue-200 transition-all duration-300">
                  <div class="w-4 h-4 bg-green-600 rounded group-hover:bg-blue-600 transition-colors duration-300"></div>
                </div>
                <span class="font-medium text-gray-700 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-purple-600 group-hover:bg-clip-text transition-all duration-300">
                  Cart
                </span>
                <span v-if="cartCount > 0" class="absolute -top-1 -right-1 bg-gradient-to-r from-red-500 to-red-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center font-bold shadow-lg animate-pulse">
                  {{ cartCount }}
                </span>
              </div>
            </router-link>
            
            <!-- Orders Link -->
            <router-link to="/orders" class="nav-link group">
              <div class="flex items-center px-4 py-2 rounded-xl bg-gray-50 hover:bg-gradient-to-r hover:from-blue-50 hover:to-purple-50 border border border-transparent hover:border-blue-200 transition-all duration-300">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-orange-100 to-amber-100 mr-2 flex items-center justify-center group-hover:from-blue-100 group-hover:to-blue-200 transition-all duration-300">
                  <div class="w-4 h-1 bg-orange-600 rounded-full group-hover:bg-blue-600 transition-all duration-300"></div>
                </div>
                <span class="font-medium text-gray-700 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-purple-600 group-hover:bg-clip-text transition-all duration-300">
                  Orders
                </span>
              </div>
            </router-link>
            
            <!-- Wishlist Button -->
            <button @click="showWishlist" class="nav-link group relative">
              <div class="flex items-center px-4 py-2 rounded-xl bg-gray-50 hover:bg-gradient-to-r hover:from-blue-50 hover:to-purple-50 border border border-transparent hover:border-blue-200 transition-all duration-300">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-pink-100 to-rose-100 mr-2 flex items-center justify-center group-hover:from-blue-100 group-hover:to-blue-200 transition-all duration-300">
                  <div class="w-4 h-4 bg-pink-600 rounded-lg group-hover:bg-blue-600 transition-colors duration-300"></div>
                </div>
                <span class="font-medium text-gray-700 group-hover:text-transparent group-hover:bg-gradient-to-r group-hover:from-blue-600 group-hover:to-purple-600 group-hover:bg-clip-text transition-all duration-300">
                  Wishlist
                </span>
                <span v-if="wishlist.length > 0" class="absolute -top-1 -right-1 bg-gradient-to-r from-pink-500 to-rose-600 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center font-bold shadow-lg animate-pulse">
                  {{ wishlist.length }}
                </span>
              </div>
            </button>
          </nav>
          
          <!-- Mobile Menu Toggle -->
          <button @click="toggleMobileMenu" class="md:hidden p-2 rounded-xl hover:bg-gray-100 transition-all duration-300">
            <div class="w-6 h-6 flex flex-col justify-center space-y-1">
              <div class="w-6 h-0.5 bg-gray-600 rounded-full transition-all duration-300"></div>
              <div class="w-6 h-0.5 bg-gray-600 rounded-full transition-all duration-300"></div>
              <div class="w-6 h-0.5 bg-gray-600 rounded-full transition-all duration-300"></div>
            </div>
          </button>
        </div>
        
        <!-- Mobile Navigation -->
        <nav v-if="mobileMenuOpen" class="md:hidden py-4 border-t bg-gray-50">
          <div class="flex flex-col space-y-2">
            <!-- Mobile Admin -->
            <router-link to="/admin" @click="toggleMobileMenu" class="mobile-nav-link">
              <div class="flex items-center">
                <div class="w-2 h-2 bg-gradient-to-r from-blue-600 to-purple-600 rounded-full mr-3"></div>
                <span class="font-medium">Admin Panel</span>
              </div>
            </router-link>
            
            <!-- Mobile Home -->
            <router-link to="/" @click="toggleMobileMenu" class="mobile-nav-link">
              <div class="flex items-center">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-gray-100 to-gray-200 mr-3 flex items-center justify-center">
                  <div class="w-3 h-3 bg-gray-600 rounded-sm"></div>
                </div>
                <span class="font-medium">Shop Home</span>
              </div>
            </router-link>
            
            <!-- Mobile Cart -->
            <router-link to="/cart" @click="toggleMobileMenu" class="mobile-nav-link relative">
              <div class="flex items-center">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-green-100 to-emerald-100 mr-3 flex items-center justify-center">
                  <div class="w-4 h-4 bg-green-600 rounded"></div>
                </div>
                <span class="font-medium">Shopping Cart ({{ cartCount }})</span>
              </div>
            </router-link>
            
            <!-- Mobile Orders -->
            <router-link to="/orders" @click="toggleMobileMenu" class="mobile-nav-link">
              <div class="flex items-center">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-orange-100 to-amber-100 mr-3 flex items-center justify-center">
                  <div class="w-4 h-1 bg-orange-600 rounded-full"></div>
                </div>
                <span class="font-medium">Order History</span>
              </div>
            </router-link>
            
            <!-- Mobile Wishlist -->
            <button @click="showWishlist" class="mobile-nav-link text-left">
              <div class="flex items-center">
                <div class="w-6 h-6 rounded-lg bg-gradient-to-br from-pink-100 to-rose-100 mr-3 flex items-center justify-center">
                  <div class="w-4 h-4 bg-pink-600 rounded-lg"></div>
                </div>
                <span class="font-medium">My Wishlist ({{ wishlist.length }})</span>
              </div>
            </button>
          </div>
        </nav>
      </div>
    </header>

    <!-- Main Content -->
    <main class="flex-grow container mx-auto px-4 py-8">
      <router-view />
    </main>

    <!-- Footer -->
    <footer class="bg-gray-800 text-white py-6 mt-8">
      <div class="container mx-auto px-4 text-center">
        <p>&copy; 2024 KAFUKA E-commerce Store</p>
      </div>
    </footer>

    <!-- Notification -->
    <div v-if="notification" class="notification slide-in">
      {{ notification }}
    </div>

    <!-- Wishlist Modal -->
    <div v-if="wishlistModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg p-6 max-w-2xl w-full mx-4 max-h-96 overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-bold">Your Wishlist</h2>
          <button @click="closeWishlistModal" class="text-gray-500 hover:text-gray-700">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        
        <div v-if="wishlist.length === 0" class="text-gray-500 text-center py-8">
          Your wishlist is empty.
        </div>
        
        <div v-else class="space-y-4">
          <div v-for="item in wishlist" :key="item.name" class="flex items-center justify-between p-4 border rounded-lg">
            <div class="flex items-center space-x-4">
              <img :src="item.image" :alt="item.name" class="w-16 h-16 object-cover rounded">
              <div>
                <h4 class="font-semibold">{{ item.name }}</h4>
                <p class="text-gray-600">Tsh {{ item.price.toLocaleString() }}</p>
              </div>
            </div>
            <div class="flex space-x-2">
              <button @click="addToCart(item.name, item.price)" class="btn btn-primary text-sm">
                Add to Cart
              </button>
              <button @click="toggleWishlist(item.name, item.price, item.image)" class="btn btn-danger text-sm">
                Remove
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Compare Modal -->
    <div v-if="compareModalOpen" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-lg p-6 max-w-2xl w-full mx-4">
        <div class="flex justify-between items-center mb-4">
          <h2 class="text-2xl font-bold">Compare Products</h2>
          <button @click="closeCompareModal" class="text-gray-500 hover:text-gray-700">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        
        <div class="overflow-x-auto">
          <table class="w-full border-collapse">
            <thead>
              <tr class="border-b">
                <th class="text-left p-2">Product</th>
                <th class="text-left p-2">Price</th>
                <th class="text-left p-2">Action</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="item in compareList" :key="item.name" class="border-b">
                <td class="p-2">{{ item.name }}</td>
                <td class="p-2">Tsh {{ item.price.toLocaleString() }}</td>
                <td class="p-2">
                  <button @click="addToCart(item.name, item.price)" class="btn btn-primary text-sm">
                    Add to Cart
                  </button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, provide } from 'vue'
import { useRouter } from 'vue-router'

export default {
  name: 'App',
  setup() {
    const router = useRouter()
    const cart = ref([])
    const wishlist = ref([])
    const compareList = ref([])
    const notification = ref('')
    const mobileMenuOpen = ref(false)
    const wishlistModalOpen = ref(false)
    const compareModalOpen = ref(false)

    const cartCount = computed(() => {
      return cart.value.reduce((total, item) => total + item.quantity, 0)
    })

    // Load data from localStorage
    const loadData = () => {
      cart.value = JSON.parse(localStorage.getItem('cart')) || []
      wishlist.value = JSON.parse(localStorage.getItem('wishlist')) || []
      compareList.value = JSON.parse(localStorage.getItem('compareList')) || []
    }

    // Save data to localStorage
    const saveData = () => {
      localStorage.setItem('cart', JSON.stringify(cart.value))
      localStorage.setItem('wishlist', JSON.stringify(wishlist.value))
      localStorage.setItem('compareList', JSON.stringify(compareList.value))
    }

    // Show notification
    const showNotificationMessage = (message) => {
      notification.value = message
      setTimeout(() => {
        notification.value = ''
      }, 3000)
    }

    // Cart functions
    const addToCart = (name, price) => {
      const existingItemIndex = cart.value.findIndex(item => item.name === name)
      if (existingItemIndex !== -1) {
        cart.value[existingItemIndex].quantity += 1
      } else {
        cart.value.push({ name, price, quantity: 1 })
      }
      saveData()
      showNotificationMessage(`${name} added to cart!`)
    }

    // Wishlist functions
    const toggleWishlist = (name, price, image) => {
      const existingIndex = wishlist.value.findIndex(item => item.name === name)
      
      if (existingIndex !== -1) {
        wishlist.value.splice(existingIndex, 1)
        showNotificationMessage(`${name} removed from wishlist`)
      } else {
        wishlist.value.push({ name, price, image })
        showNotificationMessage(`${name} added to wishlist`)
      }
      
      saveData()
    }

    const showWishlist = () => {
      wishlistModalOpen.value = true
    }

    const closeWishlistModal = () => {
      wishlistModalOpen.value = false
    }

    // Compare functions
    const addToCompare = (name, price) => {
      if (compareList.value.length >= 3) {
        showNotificationMessage('You can compare up to 3 products at a time')
        return
      }
      
      const existingIndex = compareList.value.findIndex(item => item.name === name)
      if (existingIndex === -1) {
        compareList.value.push({ name, price })
        showNotificationMessage(`${name} added to comparison`)
      } else {
        compareList.value.splice(existingIndex, 1)
        showNotificationMessage(`${name} removed from comparison`)
      }
      
      saveData()
      
      if (compareList.value.length >= 2) {
        compareModalOpen.value = true
      }
    }

    const closeCompareModal = () => {
      compareModalOpen.value = false
    }

    // Mobile menu
    const toggleMobileMenu = () => {
      mobileMenuOpen.value = !mobileMenuOpen.value
    }

    onMounted(() => {
      loadData()
    })

    // Provide data to child components
    provide('cart', cart)
    provide('wishlist', wishlist)
    provide('compareList', compareList)
    provide('notification', notification)
    provide('addToCart', addToCart)
    provide('toggleWishlist', toggleWishlist)
    provide('addToCompare', addToCompare)

    return {
      cart,
      wishlist,
      compareList,
      notification,
      mobileMenuOpen,
      wishlistModalOpen,
      compareModalOpen,
      cartCount,
      addToCart,
      toggleWishlist,
      showWishlist,
      closeWishlistModal,
      addToCompare,
      closeCompareModal,
      toggleMobileMenu
    }
  }
}
</script>

<style scoped>
.nav-link {
  @apply relative overflow-hidden;
}

.mobile-nav-link {
  @apply flex items-center px-4 py-3 text-gray-700 hover:text-blue-600 hover:bg-blue-50 rounded-lg transition-all duration-300 font-medium;
}

/* Custom animations */
@keyframes slideIn {
  from {
    transform: translateY(-100%);
    opacity: 0;
  }
  to {
    transform: translateY(0);
    opacity: 1;
  }
}

.notification {
  animation: slideIn 0.3s ease-out;
}

/* Enhanced hover effects */
.group:hover .group-hover\:scale-105 {
  transform: scale(1.05);
}

.group:hover .group-hover\:scale-110 {
  transform: scale(1.1);
}

/* Gradient text effects */
.group:hover .group-hover\:text-transparent {
  color: transparent;
}

.group:hover .group-hover\:bg-gradient-to-r {
  background: linear-gradient(to right, theme('colors.blue.600'), theme('colors.purple.600'));
  -webkit-background-clip: text;
  background-clip: text;
}

.group:hover .group-hover\:from-blue-600 {
  color: theme('colors.blue.600');
}

.group:hover .group-hover\:to-purple-600 {
  color: theme('colors.purple.600');
}

/* Mobile menu improvements */
.md\:hidden {
  @apply md:hidden;
}

/* Backdrop blur effect */
.backdrop-blur-lg {
  backdrop-filter: blur(16px);
}

/* Enhanced badge animations */
.animate-pulse {
  animation: pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite;
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.5;
  }
}
</style>
