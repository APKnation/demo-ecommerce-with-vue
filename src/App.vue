<template>
  <div id="app" class="min-h-screen flex flex-col">
    <!-- Header -->
    <nav class="bg-gradient-to-r from-indigo-600 via-purple-600 to-indigo-800 fixed w-full z-20 top-0 start-0 border-b border-indigo-700 shadow-2xl">
      <div class="max-w-screen-xl flex flex-wrap items-center justify-between mx-auto p-4">
        <!-- Logo Section -->
        <router-link to="/" class="flex items-center space-x-3 rtl:space-x-reverse">
          <img 
            src="/images/IMG-20240518-WA0002.jpg" 
            alt="KAFUKA Store Logo" 
            class="w-8 h-8 rounded-lg object-cover shadow-md hover:shadow-lg transition-shadow duration-300"
          >
          <span class="self-center text-xl text-white font-semibold whitespace-nowrap">KAFUKA Store</span>
        </router-link>
        
        
        <!-- Mobile Menu Toggle -->
        <button @click="toggleMobileMenu" data-collapse-toggle="navbar-default" type="button" class="inline-flex items-center p-2 w-10 h-10 justify-center text-sm text-white rounded-lg md:hidden hover:bg-indigo-700 hover:text-white focus:outline-none focus:ring-2 focus:ring-indigo-300" aria-controls="navbar-default" aria-expanded="false">
          <span class="sr-only">Open main menu</span>
          <div class="w-6 h-6 flex flex-col justify-center space-y-1">
            <div class="w-6 h-0.5 bg-white rounded-full"></div>
            <div class="w-6 h-0.5 bg-white rounded-full"></div>
            <div class="w-6 h-0.5 bg-white rounded-full"></div>
          </div>
        </button>
        
        <!-- Desktop Navigation -->
        <div class="hidden w-full md:block md:w-auto" id="navbar-default">
          <ul class="font-medium flex flex-col p-4 md:p-0 mt-4 border border-indigo-700 rounded-lg bg-indigo-900/50 backdrop-blur-sm md:flex-row md:space-x-8 rtl:space-x-reverse md:mt-0 md:border-0 md:bg-transparent">
            <!-- Home Link -->
            <li>
              <router-link to="/" class="block py-2 px-3 text-white bg-primary-600 rounded md:bg-transparent md:text-primary-600 md:p-0" aria-current="page">Home</router-link>
            </li>
            
            <!-- Admin Link -->
            <li>
              <router-link to="/admin" class="block py-2 px-3 text-white rounded hover:bg-indigo-700 md:hover:bg-transparent md:border-0 md:hover:text-primary-600 md:p-0">Admin</router-link>
            </li>
            
            <!-- Cart Link -->
            <li class="relative">
              <router-link to="/cart" class="block py-2 px-3 text-white rounded hover:bg-indigo-700 md:hover:bg-transparent md:border-0 md:hover:text-primary-600 md:p-0">
                Cart
                <span v-if="cartCount > 0" class="absolute -top-1 -right-1 bg-error-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center font-bold">
                  {{ cartCount }}
                </span>
              </router-link>
            </li>
            
            <!-- Orders Link -->
            <li>
              <router-link to="/orders" class="block py-2 px-3 text-white rounded hover:bg-indigo-700 md:hover:bg-transparent md:border-0 md:hover:text-primary-600 md:p-0">Orders</router-link>
            </li>
            
            <!-- Wishlist Link -->
            <li class="relative">
              <button @click="showWishlist" class="block py-2 px-3 text-white rounded hover:bg-indigo-700 md:hover:bg-transparent md:border-0 md:hover:text-primary-600 md:p-0">
                Wishlist
                <span v-if="wishlist.length > 0" class="absolute -top-1 -right-1 bg-secondary-500 text-white text-xs rounded-full h-5 w-5 flex items-center justify-center font-bold">
                  {{ wishlist.length }}
                </span>
              </button>
            </li>
          </ul>
        </div>
      </div>
      
      <!-- Mobile Menu -->
      <div v-if="mobileMenuOpen" class="md:hidden bg-indigo-900/95 backdrop-blur-sm border-t border-indigo-700">
        <ul class="font-medium flex flex-col p-4 space-y-2">
          <li>
            <router-link to="/" @click="toggleMobileMenu" class="block py-2 px-3 text-white rounded hover:bg-indigo-700">
              Home
            </router-link>
          </li>
          <li>
            <router-link to="/admin" @click="toggleMobileMenu" class="block py-2 px-3 text-white rounded hover:bg-indigo-700">
              Admin
            </router-link>
          </li>
          <li>
            <router-link to="/cart" @click="toggleMobileMenu" class="block py-2 px-3 text-white rounded hover:bg-indigo-700">
              Cart ({{ cartCount }})
            </router-link>
          </li>
          <li>
            <router-link to="/orders" @click="toggleMobileMenu" class="block py-2 px-3 text-white rounded hover:bg-indigo-700">
              Orders
            </router-link>
          </li>
          <li>
            <button @click="showWishlist" class="block py-2 px-3 text-white rounded hover:bg-indigo-700">
              Wishlist ({{ wishlist.length }})
            </button>
          </li>
        </ul>
      </div>
    </nav>

    <!-- Main Content -->
    <main class="flex-grow container mx-auto px-4 pt-24 pb-8">
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
import { ref, computed, inject, onMounted, provide } from 'vue'
import { useRouter } from 'vue-router'
import Swal from 'sweetalert2'

export default {
  name: 'App',
  setup() {
    const router = useRouter()
    const cart = ref([])
    const wishlist = ref([])
    const compareList = ref([])
    const mobileMenuOpen = ref(false)
    const wishlistModalOpen = ref(false)
    const compareModalOpen = ref(false)
    const profileMenuOpen = ref(false)

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

    // SweetAlert notification system
    const showNotificationMessage = (message, type = 'success', isPopup = false) => {
      if (isPopup) {
        // Popup with colors for welcome message
        Swal.fire({
          icon: type === 'success' ? 'success' : type === 'error' ? 'error' : 'info',
          title: type === 'success' ? 'Welcome!' : type === 'error' ? 'Error!' : 'Hello!',
          text: message,
          position: 'center',
          showConfirmButton: true,
          confirmButtonText: 'Get Started',
          confirmButtonColor: '#f97316',
          cancelButtonColor: '#6b7280',
          background: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
          color: '#ffffff',
          customClass: {
            popup: 'swal2-welcome-popup'
          }
        })
      } else {
        // Toast for regular notifications
        Swal.fire({
          icon: type === 'success' ? 'success' : type === 'error' ? 'error' : 'info',
          title: type === 'success' ? 'Success!' : type === 'error' ? 'Error!' : 'Notification',
          text: message,
          position: 'top-end',
          timer: 3000,
          toast: true,
          showConfirmButton: false,
          showCancelButton: false,
          customClass: {
            popup: 'swal2-popup'
          }
        })
      }
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

    const removeFromCart = (index) => {
      const itemName = cart.value[index].name
      cart.value.splice(index, 1)
      saveData()
      showNotificationMessage(`${itemName} removed from cart`)
    }

    const updateQuantity = (index, change) => {
      cart.value[index].quantity += change
      
      if (cart.value[index].quantity <= 0) {
        removeFromCart(index)
      } else {
        saveData()
      }
    }

    const clearCart = () => {
      cart.value = []
      saveData()
      showNotificationMessage('Cart cleared successfully')
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

    const removeFromCompare = (index) => {
      const itemName = compareList.value[index].name
      compareList.value.splice(index, 1)
      saveData()
      showNotificationMessage(`${itemName} removed from comparison`)
    }

    const closeCompareModal = () => {
      compareModalOpen.value = false
    }

    // Mobile menu
    const toggleMobileMenu = () => {
      mobileMenuOpen.value = !mobileMenuOpen.value
    }

    // Profile menu
    const toggleProfileMenu = () => {
      profileMenuOpen.value = !profileMenuOpen.value
    }

    onMounted(() => {
      loadData()
    })

    // Provide data to child components
    provide('cart', cart)
    provide('wishlist', wishlist)
    provide('compareList', compareList)
    provide('addToCart', addToCart)
    provide('toggleWishlist', toggleWishlist)
    provide('addToCompare', addToCompare)

    return {
      cart,
      cartCount,
      wishlist,
      compareList,
      mobileMenuOpen,
      wishlistModalOpen,
      compareModalOpen,
      profileMenuOpen,
      saveData,
      addToCart,
      removeFromCart,
      updateQuantity,
      clearCart,
      toggleWishlist,
      showWishlist,
      addToCompare,
      removeFromCompare,
      closeCompareModal,
      toggleMobileMenu,
      toggleProfileMenu
    }
  }
}
</script>

<style scoped>
/* Navigation styles are now handled by Tailwind classes */

/* SweetAlert Custom Styles */
:global(.swal2-popup) {
  border-radius: 16px !important;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2) !important;
}

:global(.swal2-welcome-popup) {
  border-radius: 20px !important;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3) !important;
  backdrop-filter: blur(8px) !important;
}

:global(.swal2-welcome-popup .swal2-title) {
  color: #1f2937 !important;
  font-size: 2rem !important;
  font-weight: 700 !important;
  margin-bottom: 1rem !important;
}

:global(.swal2-welcome-popup .swal2-confirm) {
  background: linear-gradient(135deg, #f97316 0%, #ea580c 100%) !important;
  color: white !important;
  font-weight: 600 !important;
  padding: 12px 24px !important;
  border-radius: 12px !important;
  border: none !important;
  box-shadow: 0 4px 15px rgba(249, 115, 22, 0.3) !important;
  transition: all 0.3s ease !important;
}

:global(.swal2-welcome-popup .swal2-confirm:hover) {
  background: linear-gradient(135deg, #ea580c 0%, #f97316 100%) !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(249, 115, 22, 0.4) !important;
}

:global(.swal2-welcome-popup .swal2-cancel) {
  background: #6b7280 !important;
  color: white !important;
  font-weight: 500 !important;
  padding: 12px 24px !important;
  border-radius: 12px !important;
  border: none !important;
  box-shadow: 0 4px 15px rgba(107, 114, 128, 0.3) !important;
  transition: all 0.3s ease !important;
}

:global(.swal2-welcome-popup .swal2-cancel:hover) {
  background: #4b5563 !important;
  transform: translateY(-2px) !important;
  box-shadow: 0 6px 20px rgba(75, 85, 99, 0.4) !important;
}

:global(.swal2-welcome-popup .swal2-html-container) {
  color: #374151 !important;
  font-size: 1.1rem !important;
  line-height: 1.6 !important;
  text-align: center !important;
  margin-top: 1rem !important;
}

/* Ensure SweetAlert doesn't affect navbar z-index */
.swal2-container {
  z-index: 9999 !important;
}

/* Ensure navbar stays on top */
nav {
  z-index: 50 !important;
}
</style>
