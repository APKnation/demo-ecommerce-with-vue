<!-- SIMPLIFIED HERO SECTION -->
<div class="relative bg-gradient-to-br from-blue-50 via-indigo-50 to-purple-50 py-16">
  <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
    <div class="text-center">
      <h1 class="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 mb-6">
        Welcome to KAFUKA Electronics
      </h1>
      <p class="text-xl text-gray-600 mb-8 max-w-3xl mx-auto">
        Discover the latest in smartphones, laptops, and accessories
      </p>
      
      <!-- Simple Call-to-Action -->
      <div class="flex flex-col sm:flex-row gap-4 justify-center">
        <router-link 
          to="/products" 
          class="bg-blue-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-blue-700 transition-colors duration-200"
        >
          Browse Products
        </router-link>
        
        <router-link 
          v-if="isAuthenticated" 
          to="/cart" 
          class="bg-green-600 text-white px-8 py-3 rounded-lg font-semibold hover:bg-green-700 transition-colors duration-200"
        >
          View Cart
        </router-link>
      </div>
    </div>
  </div>
</div>
