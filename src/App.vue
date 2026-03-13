<template>
  <div id="app" class="min-h-screen flex flex-col">
    <!-- Header -->
    <header class="bg-white shadow-md sticky top-0 z-40">
      <div class="container mx-auto px-4">
        <div class="flex justify-between items-center h-16">
          <h1 class="text-2xl font-bold text-blue-600">KAFUKA E-commerce Store</h1>
          
          <!-- Desktop Navigation -->
          <nav class="hidden md:flex space-x-6">
            <router-link to="/admin" class="text-gray-700 hover:text-blue-600 transition-colors">Admin Panel</router-link>
            <router-link to="/" class="text-gray-700 hover:text-blue-600 transition-colors">Home</router-link>
            <router-link to="/cart" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center">
              Cart ({{ cartCount }})
            </router-link>
            <router-link to="/orders" class="text-gray-700 hover:text-blue-600 transition-colors">Order History</router-link>
            <button @click="showWishlist" class="text-gray-700 hover:text-blue-600 transition-colors flex items-center">
              Wishlist ({{ wishlist.length }})
            </button>
          </nav>
          
          <!-- Mobile Menu Toggle -->
          <button @click="toggleMobileMenu" class="md:hidden text-gray-700">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
          </button>
        </div>
        
        <!-- Mobile Navigation -->
        <nav v-if="mobileMenuOpen" class="md:hidden py-4 border-t">
          <div class="flex flex-col space-y-2">
            <router-link to="/admin" @click="toggleMobileMenu" class="text-gray-700 hover:text-blue-600 py-2">Admin Panel</router-link>
            <router-link to="/" @click="toggleMobileMenu" class="text-gray-700 hover:text-blue-600 py-2">Home</router-link>
            <router-link to="/cart" @click="toggleMobileMenu" class="text-gray-700 hover:text-blue-600 py-2">Cart ({{ cartCount }})</router-link>
            <router-link to="/orders" @click="toggleMobileMenu" class="text-gray-700 hover:text-blue-600 py-2">Order History</router-link>
            <button @click="showWishlist" class="text-gray-700 hover:text-blue-600 py-2 text-left">Wishlist ({{ wishlist.length }})</button>
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

    // Provide data to child components
    provide('cart', cart)
    provide('wishlist', wishlist)
    provide('compareList', compareList)
    provide('notification', notification)
    provide('addToCart', addToCart)
    provide('toggleWishlist', toggleWishlist)
    provide('addToCompare', addToCompare)

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
