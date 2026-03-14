<template>
  <div>
    <!-- Vue Notification Component -->
    <div v-if="showNotification" class="fixed top-4 right-4 bg-success-500 text-white px-6 py-3 rounded-lg shadow-lg z-50 transition-all duration-300 transform">
      {{ notification }}
    </div>

    <!-- Hero Section with Advanced Design -->
    <section class="relative min-h-screen bg-gradient-to-br from-orange-50 via-white to-orange-100 overflow-hidden">
      <!-- Background Pattern -->
      <div class="absolute inset-0 opacity-10">
        <div class="absolute top-0 left-0 w-full h-full bg-gradient-to-r from-orange-200 to-orange-300"></div>
        <div class="absolute top-10 left-10 w-32 h-32 bg-orange-300 rounded-full blur-3xl"></div>
        <div class="absolute bottom-10 right-10 w-48 h-48 bg-orange-400 rounded-full blur-3xl"></div>
        <div class="absolute top-1/2 left-1/4 w-24 h-24 bg-orange-200 rounded-full blur-2xl"></div>
      </div>
      
      <!-- Advanced Grid Pattern -->
      <div class="absolute inset-0 opacity-5">
        <div class="h-full w-full" style="background-image: linear-gradient(rgba(251, 146, 60, 0.3) 1px, transparent 1px), linear-gradient(90deg, rgba(251, 146, 60, 0.3) 1px, transparent 1px); background-size: 50px 50px;"></div>
      </div>
      
      <!-- Hero Content -->
      <div class="relative z-10 min-h-screen flex items-center">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 w-full">
          <div class="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            
            <!-- Left Content -->
            <div class="text-left space-y-8">
              <!-- Badge -->
              <div class="inline-flex items-center px-4 py-2 bg-orange-100 text-orange-600 rounded-full text-sm font-semibold">
                <svg class="w-4 h-4 mr-2" fill="currentColor" viewBox="0 0 20 20">
                  <path d="M9.049 2.927c.3-.921 1.603-.921 1.902 0l1.07 3.292a1 1 0 00.95.69h3.462c.969 0 1.371 1.24.588 1.81l-2.8 2.034a1 1 0 00-.364 1.118l1.07 3.292c.3.921-.755 1.688-1.54 1.118l-2.8-2.034a1 1 0 00-1.175 0l-2.8 2.034c-.784.57-1.838-.197-1.539-1.118l1.07-3.292a1 1 0 00-.364-1.118L2.98 8.72c-.783-.57-.38-1.81.588-1.81h3.461a1 1 0 00.951-.69l1.07-3.292z"></path>
                </svg>
                Premium Electronics Store
              </div>
              
              <!-- Main Title -->
              <h1 class="text-5xl md:text-6xl lg:text-7xl font-bold text-gray-900 leading-tight">
                Discover the
                <br>
                <span class="text-orange-500">Future of</span>
                <br>
                <span class="text-orange-600">Technology</span>
              </h1>
              
              <!-- Description -->
              <p class="text-xl text-gray-600 leading-relaxed max-w-lg">
                Experience cutting-edge electronics and gadgets that transform your digital life. From smartphones to smart homes, we bring innovation to your fingertips.
              </p>
              
              <!-- Stats -->
              <div class="flex flex-wrap gap-8">
                <div>
                  <div class="text-3xl font-bold text-orange-600">500+</div>
                  <div class="text-gray-600">Products</div>
                </div>
                <div>
                  <div class="text-3xl font-bold text-orange-600">24/7</div>
                  <div class="text-gray-600">Support</div>
                </div>
                <div>
                  <div class="text-3xl font-bold text-orange-600">100%</div>
                  <div class="text-gray-600">Quality</div>
                </div>
              </div>
              
              <!-- Call-to-Action Buttons -->
              <div class="flex flex-col sm:flex-row gap-4">
                <router-link 
                  to="/cart" 
                  class="inline-flex items-center px-8 py-4 bg-orange-500 text-white font-bold rounded-xl hover:bg-orange-600 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl"
                >
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                  </svg>
                  Shop Now
                </router-link>
                <router-link 
                  to="/admin" 
                  class="inline-flex items-center px-8 py-4 bg-white text-orange-600 font-bold rounded-xl hover:bg-orange-50 transition-all duration-300 transform hover:scale-105 shadow-lg hover:shadow-xl border-2 border-orange-200"
                >
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573 1.066c-1.543-.94-3.31.826-2.37 2.37a1.724 1.724 0 00-1.065 2.572C18.375 12.838 20.05 11.507 20.05 9.5s-1.675-3.338-2.675-4.317c-.426-1.756-2.924-1.756-3.35 0a1.724 1.724 0 00-2.573 1.066c-1.543-.94-3.31.826-2.37 2.37a1.724 1.724 0 00-1.065 2.572C12.838 18.375 11.507 20.05 9.5 20.05S6.162 18.375 5.183 17.017a1.724 1.724 0 00-2.572-1.065c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 3.352.018 1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 002.573-1.066c1.543.94 3.31-.826 2.37-2.37a1.724 1.724 0 00-1.065-2.572C6.162 18.375 4.833 20.05 2.825 20.05S.675 18.375.675 16.983c-.426-1.756-2.924-1.756-3.35 0A1.724 1.724 0 001.825 16.917c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 3.352.018z"></path>
                  </svg>
                  Admin Panel
                </router-link>
              </div>
            </div>
            
            <!-- Right Content - Product Showcase -->
            <div class="relative">
              <!-- Main Product Image -->
              <div class="relative z-10">
                <img 
                  src="/images/w.jpg" 
                  alt="Featured Product" 
                  class="w-full h-auto rounded-2xl shadow-2xl transform hover:scale-105 transition-transform duration-500"
                >
                
                <!-- Floating Cards -->
                <div class="absolute -top-4 -right-4 bg-white rounded-xl shadow-xl p-4 transform hover:scale-110 transition-transform duration-300">
                  <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                      <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
                      </svg>
                    </div>
                    <div>
                      <div class="font-bold text-gray-900">Fast</div>
                      <div class="text-sm text-gray-600">Delivery</div>
                    </div>
                  </div>
                </div>
                
                <div class="absolute -bottom-4 -left-4 bg-white rounded-xl shadow-xl p-4 transform hover:scale-110 transition-transform duration-300">
                  <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                      <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
                      </svg>
                    </div>
                    <div>
                      <div class="font-bold text-gray-900">Premium</div>
                      <div class="text-sm text-gray-600">Quality</div>
                    </div>
                  </div>
                </div>
                
                <div class="absolute top-1/2 -right-8 bg-white rounded-xl shadow-xl p-4 transform hover:scale-110 transition-transform duration-300">
                  <div class="flex items-center space-x-3">
                    <div class="w-12 h-12 bg-orange-100 rounded-full flex items-center justify-center">
                      <svg class="w-6 h-6 text-orange-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4.318 6.318a4.5 4.5 0 000 6.364L12 20.364l7.682-7.682a4.5 4.5 0 00-6.364-6.364L12 7.636l-1.318-1.318a4.5 4.5 0 00-6.364 0z"></path>
                      </svg>
                    </div>
                    <div>
                      <div class="font-bold text-gray-900">Trusted</div>
                      <div class="text-sm text-gray-600">Service</div>
                    </div>
                  </div>
                </div>
              </div>
              
              <!-- Background Elements -->
              <div class="absolute -top-20 -right-20 w-40 h-40 bg-orange-200 rounded-full opacity-20 blur-2xl"></div>
              <div class="absolute -bottom-20 -left-20 w-32 h-32 bg-orange-300 rounded-full opacity-20 blur-2xl"></div>
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
