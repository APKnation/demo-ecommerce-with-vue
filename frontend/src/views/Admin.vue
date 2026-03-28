<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 to-gray-100">
    <!-- Admin Header -->
    <div class="bg-gradient-to-r from-blue-600 to-purple-600 text-white shadow-2xl">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
        <div class="flex flex-col sm:flex-row sm:items-center sm:justify-between gap-4">
          <div>
            <h1 class="text-2xl sm:text-3xl lg:text-4xl font-bold mb-2">Admin Dashboard</h1>
            <p class="text-blue-100 text-sm sm:text-base">Manage your e-commerce store</p>
          </div>
          <div class="text-center sm:text-right">
            <div class="text-2xl sm:text-3xl lg:text-4xl font-bold">{{ products.length }}</div>
            <div class="text-sm sm:text-base text-blue-100">Total Products</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="bg-white shadow-lg sticky top-0 z-40 border-b border-gray-200">
      <div class="container mx-auto px-4 sm:px-6 lg:px-8">
        <div class="flex flex-col sm:flex-row sm:space-x-1 p-2 sm:p-1">
          <button 
            v-for="tab in tabs" 
            :key="tab.id"
            @click="tab.route ? $router.push(tab.route) : activeTab = tab.id"
            :class="[
              'px-3 sm:px-6 py-2 sm:py-3 rounded-lg font-medium transition-all text-xs sm:text-sm mb-1 sm:mb-0',
              (activeTab === tab.id && !tab.route) || $route.path === tab.route
                ? 'bg-blue-600 text-white shadow-md' 
                : 'text-gray-600 hover:bg-gray-100'
            ]"
          >
            {{ tab.name }}
            <span v-if="tab.badge" class="ml-2 bg-red-500 text-white text-xs px-2 py-0.5 rounded-full">
              {{ tab.badge }}
            </span>
          </button>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="container mx-auto px-4 sm:px-6 lg:px-8 py-6 sm:py-8">
      <!-- Dashboard Stats Section -->
      <div v-if="activeTab === 'dashboard'" class="space-y-6 sm:space-y-8">
        <!-- Main Stats Row -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          <div v-for="stat in dashboardStats.slice(0, 4)" :key="stat.label" 
               class="bg-white rounded-xl shadow-lg p-4 sm:p-6 hover:shadow-xl transition-shadow duration-300">
            <div class="flex items-center justify-between">
              <div class="flex-1">
                <p class="text-xs sm:text-sm font-medium text-gray-600">{{ stat.label }}</p>
                <p class="text-xl sm:text-2xl lg:text-3xl font-bold text-gray-900 mt-1">{{ stat.value }}</p>
              </div>
              <div :class="`w-10 h-10 sm:w-12 sm:h-12 ${stat.bgColor} rounded-xl flex items-center justify-center flex-shrink-0`">
                <svg class="w-5 h-5 sm:w-6 sm:h-6" :class="stat.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="stat.icon"></path>
                </svg>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Secondary Stats Row -->
        <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-4 sm:gap-6">
          <div v-for="stat in dashboardStats.slice(4)" :key="stat.label" 
               class="bg-white rounded-xl shadow-lg p-4 sm:p-6 hover:shadow-xl transition-shadow duration-300">
            <div class="flex items-center justify-between">
              <div class="flex-1">
                <p class="text-xs sm:text-sm font-medium text-gray-600">{{ stat.label }}</p>
                <p class="text-xl sm:text-2xl lg:text-3xl font-bold text-gray-900 mt-1">{{ stat.value }}</p>
              </div>
              <div :class="`w-10 h-10 sm:w-12 sm:h-12 ${stat.bgColor} rounded-xl flex items-center justify-center flex-shrink-0`">
                <svg class="w-5 h-5 sm:w-6 sm:h-6" :class="stat.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="stat.icon"></path>
                </svg>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Orders Section -->
      <div v-if="activeTab === 'orders'" class="space-y-6 sm:space-y-8">
        <div class="bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden">
          <div class="bg-gradient-to-r from-blue-600 to-indigo-600 text-white px-6 sm:px-8 py-4 sm:py-6">
            <h2 class="text-xl sm:text-2xl font-bold flex items-center justify-between">
              <span class="flex items-center">
                <span class="mr-3">📋</span>
                Order Management
              </span>
              <span class="text-sm bg-white/20 px-4 py-2 rounded-full">
                {{ allOrders.length }} total orders
              </span>
            </h2>
          </div>
          
          <div class="p-4 sm:p-6">
            <!-- Order Status Filter -->
            <div class="mb-6 flex flex-wrap gap-2">
              <button 
                v-for="status in ['all', 'Pending', 'Confirmed', 'Completed', 'Cancelled']" 
                :key="status"
                @click="orderStatusFilter = status"
                :class="[
                  'px-4 py-2 rounded-lg font-medium transition-all text-sm',
                  orderStatusFilter === status 
                    ? 'bg-blue-600 text-white shadow-md' 
                    : 'bg-gray-100 text-gray-700 hover:bg-gray-200'
                ]"
              >
                {{ status === 'all' ? 'All Orders' : status }}
                <span v-if="status !== 'all'" class="ml-2 bg-gray-200 text-gray-700 px-2 py-0.5 rounded-full text-xs">
                  {{ allOrders.filter(o => o.status === status).length }}
                </span>
              </button>
            </div>

            <!-- Orders Table -->
            <div class="overflow-x-auto">
              <table class="w-full">
                <thead class="bg-gray-50 border-b-2 border-gray-200">
                  <tr>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Order #</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Customer</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Status</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Total</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Date</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Actions</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="order in filteredOrdersList" :key="order.id" class="hover:bg-gray-50 transition-colors">
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-bold text-gray-900">#{{ order.order_number || order.id }}</div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900">{{ order.customer?.username || 'Unknown' }}</div>
                      <div class="text-xs text-gray-500">{{ order.customer?.email || '' }}</div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <span :class="getStatusClass(order.status)" class="px-3 py-1 rounded-full text-xs font-bold">
                        {{ order.status }}
                      </span>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-bold text-green-600">
                        Tsh {{ Number(order.total_amount || order.total || 0).toLocaleString() }}
                      </div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900">{{ formatDate(order.created_at) }}</div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="flex space-x-2">
                        <button @click="viewOrderDetails(order)" class="px-3 py-1 bg-blue-500 text-white text-xs font-medium rounded-lg hover:bg-blue-600 transition-colors">
                          View
                        </button>
                        <button @click="deleteOrder(order.id)" class="px-3 py-1 bg-red-500 text-white text-xs font-medium rounded-lg hover:bg-red-600 transition-colors">
                          Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
              
              <!-- Empty State -->
              <div v-if="filteredOrdersList.length === 0" class="text-center py-12">
                <h3 class="text-xl font-bold text-gray-800 mb-2">No orders found</h3>
                <p class="text-gray-600">Try adjusting your status filter</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Users Section -->
      <div v-if="activeTab === 'users'" class="space-y-6 sm:space-y-8">
        <div class="bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden">
          <div class="bg-gradient-to-r from-purple-600 to-pink-600 text-white px-6 sm:px-8 py-4 sm:py-6">
            <h2 class="text-xl sm:text-2xl font-bold flex items-center justify-between">
              <span class="flex items-center">
                <span class="mr-3">👥</span>
                User Management
              </span>
              <span class="text-sm bg-white/20 px-4 py-2 rounded-full">
                {{ allUsers.length }} total users
              </span>
            </h2>
          </div>
          
          <div class="p-4 sm:p-6">
            <!-- Users Table -->
            <div class="overflow-x-auto">
              <table class="w-full">
                <thead class="bg-gray-50 border-b-2 border-gray-200">
                  <tr>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">User</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Email</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Role</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Joined</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Actions</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="user in allUsers" :key="user.id" class="hover:bg-gray-50 transition-colors">
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center">
                        <div class="w-10 h-10 bg-gradient-to-br from-blue-500 to-purple-600 rounded-full flex items-center justify-center text-white font-bold mr-3">
                          {{ user.username?.charAt(0).toUpperCase() || 'U' }}
                        </div>
                        <div class="text-sm font-bold text-gray-900">{{ user.username }}</div>
                      </div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900">{{ user.email }}</div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <span :class="getRoleClass(user.role)" class="px-3 py-1 rounded-full text-xs font-bold">
                        {{ user.role || 'customer' }}
                      </span>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900">{{ formatDate(user.date_joined) }}</div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <button @click="deleteUser(user.id)" class="px-3 py-1 bg-red-500 text-white text-xs font-medium rounded-lg hover:bg-red-600 transition-colors">
                        Delete
                      </button>
                    </td>
                  </tr>
                </tbody>
              </table>
              
              <!-- Empty State -->
              <div v-if="allUsers.length === 0" class="text-center py-12">
                <h3 class="text-xl font-bold text-gray-800 mb-2">No users found</h3>
                <p class="text-gray-600">Users will appear here when they register</p>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Products Section -->
      <div v-if="activeTab === 'products'" class="space-y-6 sm:space-y-8">
        <div class="bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden">
          <div class="bg-gradient-to-r from-green-600 to-emerald-600 text-white px-6 sm:px-8 py-4 sm:py-6">
            <h2 class="text-xl sm:text-2xl font-bold flex items-center justify-between">
              <span class="flex items-center">
                <span class="mr-3">📦</span>
                Product Management
              </span>
              <span class="text-sm bg-white/20 px-4 py-2 rounded-full">
                {{ products.length }} total products
              </span>
            </h2>
          </div>
          
          <div class="p-4 sm:p-6">
            <!-- Product Filters -->
            <div class="mb-6 grid grid-cols-1 sm:grid-cols-3 gap-4">
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Search Products</label>
                <input
                  v-model="productSearchQuery"
                  type="text"
                  placeholder="Search by name, category..."
                  class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                >
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
                <select v-model="productCategoryFilter" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent">
                  <option value="">All Categories</option>
                  <option value="Electronics">Electronics</option>
                  <option value="Phones">Phones</option>
                  <option value="Laptops">Laptops</option>
                  <option value="Accessories">Accessories</option>
                  <option value="Other">Other</option>
                </select>
              </div>
              <div>
                <label class="block text-sm font-medium text-gray-700 mb-2">Status</label>
                <select v-model="productStatusFilter" class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent">
                  <option value="">All Status</option>
                  <option value="active">Active</option>
                  <option value="inactive">Inactive</option>
                </select>
              </div>
            </div>

            <!-- Products Table -->
            <div class="overflow-x-auto">
              <table class="w-full">
                <thead class="bg-gray-50 border-b-2 border-gray-200">
                  <tr>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Product</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Price</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Stock</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Status</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Actions</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="product in filteredProducts" :key="product.id" class="hover:bg-gray-50 transition-colors">
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center space-x-4">
                        <div class="relative">
                          <img 
                            v-if="product.image && product.image !== '' && product.image !== '/images/placeholder.jpg'" 
                            :src="getImageUrl(product.image)" 
                            :alt="product.name || 'Product'" 
                            class="w-16 h-16 object-cover rounded-xl shadow-md"
                            @error="handleImageError"
                          >
                          <div v-else class="w-16 h-16 bg-gradient-to-br from-gray-100 to-gray-200 rounded-xl flex items-center justify-center shadow-md">
                            <span class="text-xs font-bold text-gray-500">No Image</span>
                          </div>
                        </div>
                        <div class="flex-1">
                          <h4 class="text-sm font-bold text-gray-900 mb-1">{{ product.name || product.title || 'Unnamed Product' }}</h4>
                          <p class="text-xs text-gray-600 mb-2 line-clamp-2">{{ product.description || 'No description available' }}</p>
                          <div class="flex items-center space-x-2">
                            <span class="px-2 py-1 text-xs font-medium rounded-full bg-blue-100 text-blue-800">
                              {{ product.category?.name || product.category }}
                            </span>
                          </div>
                        </div>
                      </div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-lg font-bold text-green-600">
                        Tsh {{ Number(product.price).toLocaleString() }}
                      </div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <span :class="[
                        'px-3 py-1 text-sm font-bold rounded-full',
                        product.stock > 10 ? 'bg-green-100 text-green-800' : 
                        product.stock > 0 ? 'bg-yellow-100 text-yellow-800' : 
                        'bg-red-100 text-red-800'
                      ]">
                        {{ product.stock || 0 }} units
                      </span>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <span :class="[
                        'px-3 py-1 text-sm font-semibold rounded-full',
                        product.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'
                      ]">
                        {{ product.is_active ? 'Active' : 'Inactive' }}
                      </span>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="flex space-x-2">
                        <button @click="viewProduct(product)" class="px-3 py-1 bg-blue-500 text-white text-xs font-medium rounded-lg hover:bg-blue-600 transition-colors">
                          View
                        </button>
                        <button @click="editProduct(product)" class="px-3 py-1 bg-green-500 text-white text-xs font-medium rounded-lg hover:bg-green-600 transition-colors">
                          Edit
                        </button>
                        <button @click="deleteProduct(product.id)" class="px-3 py-1 bg-red-500 text-white text-xs font-medium rounded-lg hover:bg-red-600 transition-colors">
                          Delete
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
              
              <!-- Empty State -->
              <div v-if="filteredProducts.length === 0" class="text-center py-12">
                <h3 class="text-xl font-bold text-gray-800 mb-2">No products found</h3>
                <p class="text-gray-600 mb-4">Try adjusting your search or filters</p>
                <button 
                  @click="productSearchQuery = ''; productCategoryFilter = ''; productStatusFilter = ''"
                  class="px-6 py-2 bg-green-600 text-white rounded-xl hover:bg-green-700 transition-colors font-medium"
                >
                  Clear Filters
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Vendors Section -->
      <div v-if="activeTab === 'vendors'" class="space-y-6 sm:space-y-8">
        <div class="bg-white rounded-2xl shadow-xl border border-gray-100 overflow-hidden">
          <div class="bg-gradient-to-r from-purple-600 to-pink-600 text-white px-6 sm:px-8 py-4 sm:py-6">
            <h2 class="text-xl sm:text-2xl font-bold flex items-center justify-between">
              <span class="flex items-center">
                <span class="mr-3">🏪</span>
                Vendor Management
              </span>
              <span class="text-sm bg-white/20 px-4 py-2 rounded-full">
                {{ allUsers.filter(u => u.role === 'vendor').length }} total vendors
              </span>
            </h2>
          </div>
          
          <div class="p-4 sm:p-6">
            <!-- Vendor Stats -->
            <div class="grid grid-cols-1 sm:grid-cols-3 gap-4 sm:gap-6 mb-6">
              <div class="bg-purple-50 rounded-xl p-4 border border-purple-200">
                <div class="flex items-center justify-between">
                  <div>
                    <p class="text-sm font-medium text-purple-600">Active Vendors</p>
                    <p class="text-2xl font-bold text-purple-900">{{ allUsers.filter(u => u.role === 'vendor').length }}</p>
                  </div>
                  <div class="w-12 h-12 bg-purple-100 rounded-xl flex items-center justify-center">
                    <span class="text-2xl">👤</span>
                  </div>
                </div>
              </div>
              <div class="bg-pink-50 rounded-xl p-4 border border-pink-200">
                <div class="flex items-center justify-between">
                  <div>
                    <p class="text-sm font-medium text-pink-600">Total Products</p>
                    <p class="text-2xl font-bold text-pink-900">{{ products.filter(p => p.vendor_id).length }}</p>
                  </div>
                  <div class="w-12 h-12 bg-pink-100 rounded-xl flex items-center justify-center">
                    <span class="text-2xl">📦</span>
                  </div>
                </div>
              </div>
              <div class="bg-indigo-50 rounded-xl p-4 border border-indigo-200">
                <div class="flex items-center justify-between">
                  <div>
                    <p class="text-sm font-medium text-indigo-600">Pending Approval</p>
                    <p class="text-2xl font-bold text-indigo-900">{{ products.filter(p => p.vendor_id && !p.is_approved).length }}</p>
                  </div>
                  <div class="w-12 h-12 bg-indigo-100 rounded-xl flex items-center justify-center">
                    <span class="text-2xl">⏳</span>
                  </div>
                </div>
              </div>
            </div>

            <!-- Vendors Table -->
            <div class="overflow-x-auto">
              <table class="w-full">
                <thead class="bg-gray-50 border-b-2 border-gray-200">
                  <tr>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Vendor</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Email</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Products</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Status</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Joined</th>
                    <th class="px-4 sm:px-6 py-3 text-left text-xs font-bold text-gray-600 uppercase tracking-wider">Actions</th>
                  </tr>
                </thead>
                <tbody class="bg-white divide-y divide-gray-200">
                  <tr v-for="vendor in allUsers.filter(u => u.role === 'vendor')" :key="vendor.id" class="hover:bg-gray-50 transition-colors">
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="flex items-center">
                        <div class="w-10 h-10 bg-gradient-to-br from-purple-500 to-pink-600 rounded-full flex items-center justify-center text-white font-bold mr-3">
                          {{ vendor.username?.charAt(0).toUpperCase() || 'V' }}
                        </div>
                        <div>
                          <div class="text-sm font-bold text-gray-900">{{ vendor.username }}</div>
                          <div class="text-xs text-gray-500">Vendor</div>
                        </div>
                      </div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900">{{ vendor.email }}</div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm font-bold text-purple-600">
                        {{ products.filter(p => p.vendor_id === vendor.id).length }} products
                      </div>
                      <div class="text-xs text-gray-500">
                        {{ products.filter(p => p.vendor_id === vendor.id && !p.is_approved).length }} pending
                      </div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <span :class="vendor.is_active ? 'bg-green-100 text-green-800' : 'bg-red-100 text-red-800'" 
                            class="px-3 py-1 rounded-full text-xs font-bold">
                        {{ vendor.is_active ? 'Active' : 'Inactive' }}
                      </span>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="text-sm text-gray-900">{{ formatDate(vendor.date_joined) }}</div>
                    </td>
                    <td class="px-4 sm:px-6 py-4 whitespace-nowrap">
                      <div class="flex space-x-2">
                        <button @click="viewVendorProducts(vendor)" class="px-3 py-1 bg-purple-500 text-white text-xs font-medium rounded-lg hover:bg-purple-600 transition-colors">
                          View Products
                        </button>
                        <button @click="toggleVendorStatus(vendor)" :class="vendor.is_active ? 'bg-red-500 hover:bg-red-600' : 'bg-green-500 hover:bg-green-600'" 
                                class="px-3 py-1 text-white text-xs font-medium rounded-lg transition-colors">
                          {{ vendor.is_active ? 'Deactivate' : 'Activate' }}
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
              
              <!-- Empty State -->
              <div v-if="allUsers.filter(u => u.role === 'vendor').length === 0" class="text-center py-12">
                <h3 class="text-xl font-bold text-gray-800 mb-2">No vendors found</h3>
                <p class="text-gray-600">Vendors will appear here when they register</p>
              </div>
            </div>
          </div>
        </div>
      </div>

    <!-- View Product Modal -->
    <div v-if="viewingProduct" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-xl p-4 sm:p-6 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center mb-6 gap-4">
          <h2 class="text-xl sm:text-2xl font-bold text-gray-900">Product Details</h2>
          <button @click="closeViewModal" class="px-4 py-2 bg-gray-200 hover:bg-gray-300 rounded-lg transition-colors font-medium">
            Close
          </button>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <div>
            <img v-if="viewingProduct.image" :src="getImageUrl(viewingProduct.image)" :alt="viewingProduct.name" 
                 class="w-full h-48 sm:h-64 lg:h-80 object-cover rounded-lg">
            <div v-else class="w-full h-48 sm:h-64 lg:h-80 bg-gray-200 rounded-lg flex items-center justify-center">
              <span class="text-gray-400">No Image</span>
            </div>
          </div>
          
          <div class="space-y-4">
            <div>
              <h3 class="text-lg sm:text-xl font-semibold text-gray-900 mb-2">{{ viewingProduct.name }}</h3>
              <span class="px-3 py-1 text-sm rounded-full bg-blue-100 text-blue-800">
                {{ viewingProduct.category }}
              </span>
            </div>
            
            <div class="text-xl sm:text-2xl font-bold text-blue-600">
              Tsh {{ Number(viewingProduct.price).toLocaleString() }}
            </div>
            
            <div class="text-sm text-gray-600 space-y-1">
              <p><strong>Status:</strong> 
                <span :class="viewingProduct.is_active ? 'px-2 py-1 rounded-full bg-green-100 text-green-800' : 'px-2 py-1 rounded-full bg-red-100 text-red-800'">
                  {{ viewingProduct.is_active ? 'Active' : 'Inactive' }}
                </span>
              </p>
              <p><strong>Stock:</strong> {{ viewingProduct.stock || 0 }} units</p>
              <p><strong>Added:</strong> {{ formatDate(viewingProduct.addedDate) }}</p>
            </div>
          </div>
        </div>
        
        <div class="mt-6 flex flex-col sm:flex-row gap-3">
          <button @click="closeViewModal" class="px-4 py-2 border-2 border-gray-300 rounded-lg hover:bg-gray-50 transition-colors font-medium">
            Close
          </button>
          <button @click="editProduct(viewingProduct)" class="px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors font-medium">
            Edit Product
          </button>
        </div>
      </div>
    </div>

    <!-- Edit Product Modal -->
    <div v-if="isEditing && editingProduct" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-xl p-4 sm:p-6 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center mb-6 gap-4">
          <h2 class="text-xl sm:text-2xl font-bold text-gray-900">Edit Product</h2>
          <div class="flex items-center space-x-2">
            <div class="flex items-center">
              <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
              <span class="text-sm text-green-600 font-medium ml-2">Editing Mode</span>
            </div>
            <button @click="closeEditModal" class="px-4 py-2 bg-gray-200 hover:bg-gray-300 rounded-lg transition-colors font-medium">
              Cancel
            </button>
          </div>
        </div>
        
        <form @submit.prevent="saveProduct" class="space-y-6">
          <div class="grid grid-cols-1 sm:grid-cols-2 gap-4 sm:gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Product Name</label>
              <input
                v-model="editingProduct.name"
                type="text"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Price (Tsh)</label>
              <input
                v-model.number="editingProduct.price"
                type="number"
                required
                min="0"
                step="0.01"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Category</label>
              <select
                v-model="editingProduct.category"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
                <option value="">Select category</option>
                <option value="Electronics">Electronics</option>
                <option value="Phones">Phones</option>
                <option value="Laptops">Laptops</option>
                <option value="Accessories">Accessories</option>
                <option value="Other">Other</option>
              </select>
            </div>
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Stock Quantity</label>
              <input
                v-model.number="editingProduct.stock"
                type="number"
                required
                min="0"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
          </div>
          
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Description</label>
            <textarea
              v-model="editingProduct.description"
              rows="4"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              placeholder="Enter product description"
            ></textarea>
          </div>
          
          <div>
            <label class="block text-sm font-semibold text-gray-700 mb-2">Image URL</label>
            <input
              v-model="editingProduct.image"
              type="text"
              placeholder="/images/product.jpg"
              class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
            >
          </div>
          
          <div class="flex flex-col sm:flex-row space-y-3 sm:space-y-0 sm:space-x-3">
            <button type="button" @click="closeEditModal" class="px-6 py-3 border-2 border-gray-300 rounded-xl hover:bg-gray-50 transition-all duration-300 font-medium">
              Cancel
            </button>
            <button type="submit" class="px-6 py-3 bg-gradient-to-r from-green-500 to-green-600 text-white rounded-xl hover:from-green-600 hover:to-green-700 transition-all duration-300 font-bold shadow-lg hover:shadow-xl">
              Update Product
            </button>
          </div>
        </form>
      </div>
    </div>
    </div>
    
    <!-- Delete Confirmation Modal -->
    <div v-if="showConfirmDialog" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-xl p-4 sm:p-6 max-w-md w-full mx-4">
        <div class="flex items-center mb-4">
          <div class="w-12 h-12 bg-red-100 rounded-full flex items-center justify-center mr-4 flex-shrink-0">
            <svg class="w-6 h-6 text-red-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.964-.833-2.732 0L3.732 16.5c-.77.833.192 2.5 1.732 2.5z"></path>
            </svg>
          </div>
          <div class="flex-1">
            <h3 class="text-lg font-bold text-gray-900">Confirm Delete</h3>
            <p class="text-gray-600 text-sm sm:text-base">Are you sure you want to delete this product?</p>
          </div>
        </div>
        
        <div class="bg-gray-50 rounded-lg p-4 mb-6">
          <p class="text-sm text-gray-700">
            <strong>Product:</strong> {{ products[productToDelete]?.name || 'Unknown Product' }}
          </p>
          <p class="text-sm text-gray-500 mt-1">This action cannot be undone.</p>
        </div>
        
        <div class="flex flex-col sm:flex-row space-y-3 sm:space-y-0 sm:space-x-3">
          <button @click="cancelDelete" class="flex-1 px-4 py-2 border-2 border-gray-300 rounded-lg hover:bg-gray-50 transition-all duration-300 font-medium">
            Cancel
          </button>
          <button @click="executeDelete" class="flex-1 px-4 py-2 bg-gradient-to-r from-red-500 to-red-600 text-white rounded-lg hover:from-red-600 hover:to-red-700 transition-all duration-300 font-bold">
            Delete Product
          </button>
        </div>
      </div>
    </div>
    
    <!-- Order Detail Modal -->
    <div v-if="selectedOrder" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50 p-4">
      <div class="bg-white rounded-xl p-4 sm:p-6 max-w-4xl w-full max-h-[90vh] overflow-y-auto">
        <div class="flex flex-col sm:flex-row sm:justify-between sm:items-center mb-6 gap-4">
          <h2 class="text-xl sm:text-2xl font-bold text-gray-900">Order Details #{{ selectedOrder.id }}</h2>
          <button @click="selectedOrder = null" class="px-4 py-2 bg-gray-200 hover:bg-gray-300 rounded-lg transition-colors font-medium">
            Close
          </button>
        </div>
        
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-6">
          <!-- Order Information -->
          <div class="space-y-4">
            <div class="bg-gray-50 rounded-lg p-4">
              <h3 class="font-semibold text-gray-900 mb-3">Order Information</h3>
              <div class="space-y-2">
                <div class="flex justify-between">
                  <span class="text-gray-600">Order ID:</span>
                  <span class="font-medium">#{{ selectedOrder.id }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-600">Status:</span>
                  <span :class="getStatusClass(selectedOrder.status)" class="px-2 py-1 rounded-full text-xs font-medium">
                    {{ selectedOrder.status }}
                  </span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-600">Total Amount:</span>
                  <span class="font-bold text-lg">{{ formatCurrency(selectedOrder.total_price) }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-600">Order Date:</span>
                  <span class="font-medium">{{ formatDate(selectedOrder.created_at) }}</span>
                </div>
              </div>
            </div>
            
            <!-- Customer Information -->
            <div class="bg-gray-50 rounded-lg p-4">
              <h3 class="font-semibold text-gray-900 mb-3">Customer Information</h3>
              <div class="space-y-2">
                <div class="flex justify-between">
                  <span class="text-gray-600">Name:</span>
                  <span class="font-medium">{{ selectedOrder.customer_name || 'N/A' }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-600">Email:</span>
                  <span class="font-medium">{{ selectedOrder.customer_email || 'N/A' }}</span>
                </div>
                <div class="flex justify-between">
                  <span class="text-gray-600">Phone:</span>
                  <span class="font-medium">{{ selectedOrder.customer_phone || 'N/A' }}</span>
                </div>
              </div>
            </div>
          </div>
          
          <!-- Order Items -->
          <div class="bg-gray-50 rounded-lg p-4">
            <h3 class="font-semibold text-gray-900 mb-3">Order Items</h3>
            <div class="space-y-3">
              <div v-for="item in selectedOrder.items" :key="item.id" class="bg-white rounded-lg p-3 border">
                <div class="flex justify-between items-start">
                  <div class="flex-1">
                    <h4 class="font-medium text-gray-900">{{ item.product_name }}</h4>
                    <p class="text-sm text-gray-600">Quantity: {{ item.quantity }}</p>
                    <p class="text-sm text-gray-600">Price: {{ formatCurrency(item.price) }}</p>
                  </div>
                  <div class="text-right">
                    <p class="font-bold">{{ formatCurrency(item.price * item.quantity) }}</p>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
        
        <!-- Order Actions -->
        <div class="mt-6 flex flex-col sm:flex-row gap-3">
          <button @click="selectedOrder = null" class="px-4 py-2 border-2 border-gray-300 rounded-lg hover:bg-gray-50 transition-colors font-medium">
            Close
          </button>
          <select v-model="selectedOrder.status" @change="updateOrderStatus(selectedOrder.id, selectedOrder.status)" class="px-4 py-2 border-2 border-blue-300 rounded-lg focus:border-blue-500 focus:outline-none">
            <option value="Pending">Pending</option>
            <option value="Confirmed">Confirmed</option>
            <option value="Completed">Completed</option>
            <option value="Cancelled">Cancelled</option>
          </select>
        </div>
      </div>
    </div>
    
    <!-- Close Main Content Container -->
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import Swal from 'sweetalert2'

export default {
  name: 'Admin',
  setup() {
    const products = ref([])
    const orders = ref([])
    const allOrders = ref([])
    const allUsers = ref([])
    const stats = ref({
      total_revenue: 0,
      total_orders: 0,
      total_products: 0,
      total_users: 0,
      pending_orders: 0,
      completed_orders: 0,
      avg_order_value: 0,
      low_stock_products: 0
    })
    const currentUser = ref(null)
    const activeTab = ref('dashboard')
    const orderStatusFilter = ref('all')
    const selectedOrder = ref(null)
    
    const getToken = () => localStorage.getItem('token')
    const API_BASE_URL = 'http://localhost:8000/api'
    
    const tabs = computed(() => availableTabs.value)
    
    const dashboardStats = computed(() => [
      { label: 'Total Revenue', value: `Tsh ${(stats.value.total_revenue || 0).toLocaleString()}`, bgColor: 'bg-green-100', iconColor: 'text-green-600', icon: 'M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1l-1 1m-1-1l1-1m-1 1H8m8 0h-1m0 0l-1 1m1-1V6m0 2c.657 0 1.5-.895 1.5-2s-.843-2-1.5-2M8 12c-.657 0-1.5.895-1.5 2s.843 2 1.5 2m0-8c.657 0 1.5.895 1.5 2s-.843 2-1.5 2m0 0V6m0 2v2m0-4h.01M8 8v8m0-4h.01M6 20h12a2 2 0 002-2V6a2 2 0 00-2-2H6a2 2 0 00-2 2v12a2 2 0 002 2z' },
      { label: 'Total Orders', value: stats.value.total_orders || 0, bgColor: 'bg-blue-100', iconColor: 'text-blue-600', icon: 'M9 12h6m-6 4h6m2 5H7a2 2 0 01-2 2v10a2 2 0 002 2h6a2 2 0 002-2V9a2 2 0 00-2-2H9z' },
      { label: 'Total Products', value: stats.value.total_products || 0, bgColor: 'bg-orange-100', iconColor: 'text-orange-600', icon: 'M20 7l-8-4-8 4m16 0l-8 4m8-4v10l-8 4m0-10L4 7m8 4v10M4 7v10l8 4' },
      { label: 'Active Users', value: stats.value.total_users || 0, bgColor: 'bg-purple-100', iconColor: 'text-purple-600', icon: 'M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z' },
      { label: 'Pending Orders', value: stats.value.pending_orders || 0, bgColor: 'bg-yellow-100', iconColor: 'text-yellow-600', icon: 'M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z' },
      { label: 'Completed Orders', value: stats.value.completed_orders || 0, bgColor: 'bg-green-100', iconColor: 'text-green-600', icon: 'M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z' },
      { label: 'Avg Order Value', value: `Tsh ${stats.value.avg_order_value || 0}`, bgColor: 'bg-indigo-100', iconColor: 'text-indigo-600', icon: 'M9 7h6m0 10v-3m-3 3h.01M9 17h.01M9 14h.01M12 14h.01M15 11h.01M12 11h.01M9 11h.01M7 21h10a2 2 0 002-2V5a2 2 0 00-2-2H7a2 2 0 00-2 2v14a2 2 0 002 2z' },
      { label: 'Low Stock Items', value: stats.value.low_stock_products || 0, bgColor: 'bg-red-100', iconColor: 'text-red-600', icon: 'M20 12H4l1.586-1.586a2 2 0 012.828 0L12 15.414l3.586-3.586a2 2 0 012.828 0L20 12z' }
    ])

    const filteredOrdersList = computed(() => {
      if (orderStatusFilter.value === 'all') return allOrders.value
      return allOrders.value.filter(order => order.status === orderStatusFilter.value)
    })

    const newProduct = ref({
      name: '',
      price: 0,
      category: '',
      image: '',
      condition: 'new'
    })

    const imagePreview = ref('')
    const imageFile = ref(null)
    const showAddProductForm = ref(false)
    const productSearchQuery = ref('')
    const productCategoryFilter = ref('')
    const productStatusFilter = ref('')

    const filteredProducts = computed(() => {
      let filtered = products.value

      // Search filter
      if (productSearchQuery.value) {
        const query = productSearchQuery.value.toLowerCase()
        filtered = filtered.filter(product => 
          product.name.toLowerCase().includes(query) ||
          product.category.toLowerCase().includes(query) ||
          product.description.toLowerCase().includes(query)
        )
      }

      // Category filter
      if (productCategoryFilter.value) {
        filtered = filtered.filter(product => product.category === productCategoryFilter.value)
      }

      // Status filter
      if (productStatusFilter.value) {
        const isActive = productStatusFilter.value === 'active'
        filtered = filtered.filter(product => product.is_active === isActive)
      }

      return filtered
    })

    const isAddingProduct = ref(false)
    const editingProduct = ref(null)
    const isEditing = ref(false)
    const viewingProduct = ref(null)
    const productToDelete = ref(null)
    const showConfirmDialog = ref(false)

    // Handle product image file change
    const handleProductImageChange = (event) => {
      const file = event.target.files[0]
      if (file) {
        newProduct.value.imageFile = file
        const reader = new FileReader()
        reader.onload = (e) => {
          newProduct.value.image = e.target.result
        }
        reader.readAsDataURL(file)
      }
    }

    // Notification system - using SweetAlert directly instead of inject
    const showNotificationMessage = (message, type = 'success') => {
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

    // Product Management Functions
    const addProduct = async () => {
      if (!newProduct.value.name || !newProduct.value.price) {
        showNotificationMessage('Please fill in all required fields', 'error')
        return
      }

      isAddingProduct.value = true
      
      try {
        // Category mapping for backend
        const categoryMap = {
          'Electronics': 1,
          'Phones': 2, 
          'Laptops': 3,
          'Accessories': 4,
          'Other': 5
        }

        // Use FormData for potential image upload
        const formData = new FormData()
        formData.append('title', newProduct.value.name)
        formData.append('price', newProduct.value.price)
        formData.append('category', categoryMap[newProduct.value.category] || 4)
        formData.append('description', newProduct.value.description)
        formData.append('is_active', true)
        formData.append('stock', newProduct.value.stock || 1) // Use provided stock or default
        
        // Add image if provided
        if (newProduct.value.imageFile) {
          formData.append('image', newProduct.value.imageFile)
        } else if (newProduct.value.image) {
          formData.append('image_url', newProduct.value.image)
        }
        
        const response = await fetch(`${API_BASE_URL}/products/`, {
          method: 'POST',
          headers: {
            'Authorization': `Token ${getToken()}` 
            // Don't set Content-Type for FormData
          },
          body: formData
        })
        
        if (response.ok) {
          const newProductData = await response.json()
          products.value.push(newProductData)
          showNotificationMessage('Product added successfully!')
          resetProductForm()
          // Don't call loadData() here to prevent infinite loop
        } else {
          const error = await response.json()
          showNotificationMessage('Failed to add product: ' + JSON.stringify(error), 'error')
        }
      } catch (error) {
        showNotificationMessage('Failed to add product', 'error')
      } finally {
        isAddingProduct.value = false
      }
    }

    const resetProductForm = () => {
      newProduct.value = {
        name: '',
        price: 0,
        category: '',
        image: '',
        imageFile: null,
        description: ''
      }
    }

    const handleImageUpload = (event) => {
      const file = event.target.files[0]
      if (file) {
        imageFile.value = file
        const reader = new FileReader()
        reader.onload = (e) => {
          imagePreview.value = e.target.result
        }
        reader.readAsDataURL(file)
      }
    }

    const removeImage = () => {
      imagePreview.value = ''
      imageFile.value = null
      if (newProduct.value) {
        newProduct.value.image = ''
      }
    }

    // Computed properties for dashboard
    const totalRevenue = computed(() => {
      const total = allOrders.value.reduce((total, order) => {
        const orderTotal = Number(order.total_amount || order.total || 0)
        return total + orderTotal
      }, 0)
      return Math.round(total)
    })

    const totalSpend = computed(() => {
      const deliveredOrders = allOrders.value.filter(order => {
        const status = (order.status || '').toLowerCase()
        return status === 'delivered' || status === 'completed' || status === 'delivered'
      })
      
      const total = deliveredOrders.reduce((total, order) => {
        const orderTotal = Number(order.total_amount || order.total || 0)
        return total + orderTotal
      }, 0)
      
      return Math.round(total)
    })

    const pendingOrders = computed(() => {
      return allOrders.value.filter(order => order.status === 'Pending').length
    })

    // View product functions
    const viewProduct = (product) => {
      viewingProduct.value = { ...product, addedDate: new Date().toISOString() }
    }

    const closeViewModal = () => {
      viewingProduct.value = null
    }

    // Edit product functions
    const editProduct = (product) => {
      editingProduct.value = JSON.parse(JSON.stringify(product))
      isEditing.value = true
      closeViewModal()
    }

    const closeEditModal = () => {
      editingProduct.value = null
      isEditing.value = false
    }

    // Vue confirm dialog
    const confirmDelete = (index) => {
      productToDelete.value = index
      showConfirmDialog.value = true
    }

    const cancelDelete = () => {
      productToDelete.value = null
      showConfirmDialog.value = false
    }

    const executeDelete = async () => {
      if (productToDelete.value !== null) {
        try {
          const token = getToken()
          if (!token) {
            showNotificationMessage('Authentication required to delete product', 'error')
            return
          }

          const product = products.value[productToDelete.value]
          const response = await fetch(`${API_BASE_URL}/products/${product.id}/manage/`, {
            method: 'DELETE',
            headers: {
              'Authorization': `Token ${token}`
            }
          })
          
          if (response.ok) {
            const productName = product.name
            products.value.splice(productToDelete.value, 1)
            showNotificationMessage(`${productName} removed successfully!`)
            cancelDelete()
          } else {
            const error = await response.json()
            showNotificationMessage('Failed to delete product: ' + JSON.stringify(error), 'error')
          }
        } catch (error) {
          console.error('Error deleting product:', error)
          showNotificationMessage('Failed to delete product', 'error')
        }
      }
    }

    // Enhanced remove product function with Vue confirm
    const deleteProduct = (productId) => {
      const index = products.value.findIndex(p => p.id === productId)
      if (index !== -1) {
        confirmDelete(index)
      }
    }

    // Format date function
    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    // Format currency function
    const formatCurrency = (amount) => {
      return new Intl.NumberFormat('en-RW', {
        style: 'currency',
        currency: 'RWF',
        minimumFractionDigits: 0
      }).format(amount)
    }

    const saveProduct = async () => {
      try {
        const token = getToken()
        if (!token) {
          showNotificationMessage('Authentication required to update product', 'error')
          return
        }

        // Category mapping for backend
        const categoryMap = {
          'Electronics': 1,
          'Phones': 2, 
          'Laptops': 3,
          'Accessories': 4,
          'Other': 5
        }

        // Use FormData for potential image upload
        const formData = new FormData()
        formData.append('title', editingProduct.value.name || editingProduct.value.title)
        formData.append('price', editingProduct.value.price)
        
        // Handle category properly - ensure it's a single value
        let categoryValue = editingProduct.value.category
        console.log('DEBUG: Original category value:', categoryValue)
        console.log('DEBUG: Category type:', typeof categoryValue)
        console.log('DEBUG: Is array?', Array.isArray(categoryValue))
        
        if (Array.isArray(categoryValue)) {
          categoryValue = categoryValue[0] // Take first value if array
          console.log('DEBUG: Extracted category value:', categoryValue)
        }
        
        const mappedCategory = categoryMap[categoryValue] || 4
        console.log('DEBUG: Mapped category:', mappedCategory)
        
        // Try different approaches for category
        formData.append('category', mappedCategory)
        // Also try as category_id in case backend expects that
        formData.append('category_id', mappedCategory)
        
        // Debug FormData contents
        console.log('DEBUG: FormData contents:')
        for (let [key, value] of formData.entries()) {
          console.log(`  ${key}:`, value, typeof value)
        }
        
        formData.append('description', editingProduct.value.description)
        formData.append('is_active', editingProduct.value.is_active !== false)
        formData.append('stock', editingProduct.value.stock || 0)
        
        // Add image if provided
        if (editingProduct.value.imageFile) {
          formData.append('image', editingProduct.value.imageFile)
        }

        const response = await fetch(`${API_BASE_URL}/products/${editingProduct.value.id}/manage/`, {
          method: 'PUT',
          headers: { 'Authorization': `Token ${token}` },
          body: formData
        })
        
        console.log('DEBUG: Response status:', response.status)
        console.log('DEBUG: Response headers:', response.headers)
        
        if (response.ok) {
          const updatedProduct = await response.json()
          const index = products.value.findIndex(p => p.id === editingProduct.value.id)
          if (index !== -1) {
            products.value[index] = updatedProduct
          }
          closeEditModal()
          showNotificationMessage('Product updated successfully!')
        } else {
          const error = await response.json()
          console.error('Product update error details:', error)
          showNotificationMessage('Failed to update product: ' + JSON.stringify(error), 'error')
        }
      } catch (error) {
        console.error('Error updating product:', error)
        showNotificationMessage('Failed to update product', 'error')
      }
    }

    const cancelEdit = () => {
      editingProduct.value = null
      isEditing.value = false
    }

    // Helper functions for image handling
    const getImageUrl = (imagePath) => {
      if (!imagePath) return '/images/placeholder.jpg'
      
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
      
      // Otherwise, assume it's a relative path and construct backend URL
      return `http://localhost:8000/media/${imagePath}` 
    }

    const handleImageError = (event) => {
      event.target.src = '/images/placeholder.jpg'
    }

    // Load data from backend API
    const loadData = async () => {
      try {
        // Load all products from backend API (no auth required for products)
        const productsResponse = await fetch(`${API_BASE_URL}/products/`)
        
        if (productsResponse.ok) {
          const backendProducts = await productsResponse.json()
          console.log('Loaded backend products:', backendProducts)
          
          // Transform products to ensure unique names and proper image handling
          products.value = backendProducts.map((product, index) => {
            // Create unique title if missing or generic
            let title = product.title || product.name || `Product ${index + 1}`
            
            // If title is too generic, make it unique
            const genericTitles = ['Product', 'Item', 'Device', 'Gadget']
            if (genericTitles.some(generic => title.toLowerCase().includes(generic.toLowerCase()))) {
              title = `${title} - ${product.category?.name || 'General'} ${index + 1}`
            }
            
            return {
              id: product.id,
              name: title,
              title: title,
              price: Number(product.price),
              category: product.category?.name || 'Other',
              image: product.image || '/images/placeholder.jpg',
              description: product.description || `High-quality ${product.category?.name || 'product'} with excellent features.`,
              stock: product.stock || 0,
              is_active: product.is_active !== false,
              condition: product.condition || 'new',
              author: product.author,
              images: product.images || [],
              created_at: product.created_at,
              updated_at: product.updated_at,
              vendor_id: product.vendor_id,
              is_approved: product.is_approved !== false
            }
          })
          
          console.log('Transformed products for admin:', products.value)
          showNotificationMessage(`Loaded ${products.value.length} products from backend!`, 'success')
        } else {
          console.error('Failed to load products from backend')
          showNotificationMessage('Failed to load products from backend', 'error')
        }
      } catch (error) {
        console.error('Error loading products:', error)
        showNotificationMessage('Error loading products', 'error')
      }
      
      // Load other data
      await loadDashboardStats()
      await loadAllOrders()
      await loadAllUsers()
    }

    // Admin Dashboard API Functions
    const loadDashboardStats = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/dashboard-stats/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) stats.value = await response.json()
      } catch (error) { console.error('Failed to load stats:', error) }
    }

    const loadAllOrders = async () => {
      try {
        const token = getToken()
        if (!token) {
          console.log('No authentication token found, using fallback orders')
          allOrders.value = [
            { id: 1, order_number: 'ORD001', customer: { username: 'John Doe', email: 'john@example.com' }, status: 'Pending', total_amount: 1500000, items: [], created_at: new Date().toISOString() },
            { id: 2, order_number: 'ORD002', customer: { username: 'Jane Smith', email: 'jane@example.com' }, status: 'Confirmed', total_amount: 2000000, items: [], created_at: new Date().toISOString() },
            { id: 3, order_number: 'ORD003', customer: { username: 'Bob Johnson', email: 'bob@example.com' }, status: 'Completed', total_amount: 800000, items: [], created_at: new Date().toISOString() }
          ]
          return
        }

        const response = await fetch(`${API_BASE_URL}/orders/`, {
          headers: { 'Authorization': `Token ${token}` }
        })
        
        if (response.status === 401) {
          console.log('Authentication failed, using fallback orders')
          allOrders.value = [
            { id: 1, order_number: 'ORD001', customer: { username: 'John Doe', email: 'john@example.com' }, status: 'Pending', total_amount: 1500000, items: [], created_at: new Date().toISOString() },
            { id: 2, order_number: 'ORD002', customer: { username: 'Jane Smith', email: 'jane@example.com' }, status: 'Confirmed', total_amount: 2000000, items: [], created_at: new Date().toISOString() },
            { id: 3, order_number: 'ORD003', customer: { username: 'Bob Johnson', email: 'bob@example.com' }, status: 'Completed', total_amount: 800000, items: [], created_at: new Date().toISOString() }
          ]
        } else if (response.ok) {
          const ordersData = await response.json()
          console.log('Orders loaded from API:', ordersData)
          allOrders.value = ordersData
        } else {
          console.log('Failed to load orders, using fallback')
          allOrders.value = [
            { id: 1, order_number: 'ORD001', customer: { username: 'John Doe', email: 'john@example.com' }, status: 'Pending', total_amount: 1500000, items: [], created_at: new Date().toISOString() },
            { id: 2, order_number: 'ORD002', customer: { username: 'Jane Smith', email: 'jane@example.com' }, status: 'Confirmed', total_amount: 2000000, items: [], created_at: new Date().toISOString() },
            { id: 3, order_number: 'ORD003', customer: { username: 'Bob Johnson', email: 'bob@example.com' }, status: 'Completed', total_amount: 800000, items: [], created_at: new Date().toISOString() }
          ]
        }
      } catch (error) {
        console.error('Failed to load orders:', error)
        allOrders.value = [
          { id: 1, order_number: 'ORD001', customer: { username: 'John Doe', email: 'john@example.com' }, status: 'Pending', total_amount: 1500000, items: [], created_at: new Date().toISOString() },
          { id: 2, order_number: 'ORD002', customer: { username: 'Jane Smith', email: 'jane@example.com' }, status: 'Confirmed', total_amount: 2000000, items: [], created_at: new Date().toISOString() },
          { id: 3, order_number: 'ORD003', customer: { username: 'Bob Johnson', email: 'bob@example.com' }, status: 'Completed', total_amount: 800000, items: [], created_at: new Date().toISOString() }
        ]
      }
    }

    const loadAllUsers = async () => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/users/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) allUsers.value = await response.json()
      } catch (error) { console.error('Failed to load users:', error) }
    }

    const confirmOrder = async (orderId) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 'Authorization': `Token ${getToken()}`, 'Content-Type': 'application/json' },
          body: JSON.stringify({ status: 'Confirmed' })
        })
        if (response.ok) {
          showNotificationMessage('Order confirmed successfully!')
          loadAllOrders()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to confirm order', 'error') }
    }

    const cancelOrder = async (orderId) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 'Authorization': `Token ${getToken()}`, 'Content-Type': 'application/json' },
          body: JSON.stringify({ status: 'Cancelled' })
        })
        if (response.ok) {
          showNotificationMessage('Order cancelled successfully!')
          loadAllOrders()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to cancel order', 'error') }
    }

    const completeOrder = async (orderId) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 'Authorization': `Token ${getToken()}`, 'Content-Type': 'application/json' },
          body: JSON.stringify({ status: 'Completed' })
        })
        if (response.ok) {
          showNotificationMessage('Order completed successfully!')
          loadAllOrders()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to complete order', 'error') }
    }

    const deleteOrder = async (orderId) => {
      if (!confirm('Are you sure you want to delete this order?')) return
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'DELETE',
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) {
          showNotificationMessage('Order deleted successfully!')
          allOrders.value = allOrders.value.filter(o => o.id !== orderId)
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to delete order', 'error') }
    }

    const viewOrderDetails = (order) => {
      try {
        console.log('Opening order details for:', order)
        selectedOrder.value = order
      } catch (error) {
        console.error('Error opening order details:', error)
        showNotificationMessage('Failed to open order details', 'error')
      }
    }

    const updateOrderStatus = async (orderId, newStatus) => {
      try {
        console.log(`Updating order ${orderId} to status: ${newStatus}`)
        
        const token = getToken()
        if (!token) {
          showNotificationMessage('Authentication required to update order status', 'error')
          return
        }
        
        const response = await fetch(`${API_BASE_URL}/accounts/admin/orders/${orderId}/`, {
          method: 'PUT',
          headers: { 
            'Authorization': `Token ${token}`, 
            'Content-Type': 'application/json' 
          },
          body: JSON.stringify({ status: newStatus })
        })
        
        if (response.status === 401) {
          showNotificationMessage('Authentication failed. Please login again.', 'error')
        } else if (response.ok) {
          const updatedOrder = await response.json()
          console.log('Order updated successfully:', updatedOrder)
          
          // Update the order in allOrders array
          const index = allOrders.value.findIndex(o => o.id === orderId)
          if (index !== -1) {
            allOrders.value[index] = updatedOrder
          }
          
          // Update the selectedOrder if modal is open
          if (selectedOrder.value && selectedOrder.value.id === orderId) {
            selectedOrder.value = updatedOrder
          }
          
          // Show success message
          showNotificationMessage(`Order status updated to ${newStatus}!`, 'success')
          
          // Reload dashboard stats
          loadDashboardStats()
          
        } else {
          const errorData = await response.json()
          console.error('Failed to update order status:', errorData)
          showNotificationMessage('Failed to update order status', 'error')
        }
      } catch (error) {
        console.error('Error updating order status:', error)
        showNotificationMessage('Failed to update order status', 'error')
      }
    }

    const deleteUser = async (userId) => {
      if (!confirm('Are you sure you want to delete this user?')) return
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/users/${userId}/`, {
          method: 'DELETE',
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) {
          showNotificationMessage('User deleted successfully!')
          loadAllUsers()
          loadDashboardStats()
        }
      } catch (error) { showNotificationMessage('Failed to delete user', 'error') }
    }

    // Vendor management functions
    const viewVendorProducts = (vendor) => {
      // Filter products to show only this vendor's products
      const vendorProducts = products.value.filter(p => p.vendor_id === vendor.id)
      showNotificationMessage(`Viewing ${vendorProducts.length} products from ${vendor.username}`, 'info')
      // You could open a modal or navigate to a filtered view
    }

    const toggleVendorStatus = async (vendor) => {
      try {
        const response = await fetch(`${API_BASE_URL}/accounts/admin/users/${vendor.id}/`, {
          method: 'PUT',
          headers: { 
            'Authorization': `Token ${getToken()}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ is_active: !vendor.is_active })
        })
        
        if (response.ok) {
          const updatedVendor = await response.json()
          const index = allUsers.value.findIndex(u => u.id === vendor.id)
          if (index !== -1) {
            allUsers.value[index] = updatedVendor
          }
          showNotificationMessage(`Vendor ${vendor.is_active ? 'deactivated' : 'activated'} successfully!`)
        } else {
          showNotificationMessage('Failed to update vendor status', 'error')
        }
      } catch (error) {
        showNotificationMessage('Failed to update vendor status', 'error')
      }
    }

    const approveProduct = async (productId) => {
      try {
        const response = await fetch(`${API_BASE_URL}/products/${productId}/approve/`, {
          method: 'PUT',
          headers: { 
            'Authorization': `Token ${getToken()}`,
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ is_approved: true })
        })
        
        if (response.ok) {
          const updatedProduct = await response.json()
          const index = products.value.findIndex(p => p.id === productId)
          if (index !== -1) {
            products.value[index] = updatedProduct
          }
          showNotificationMessage('Product approved successfully!')
        } else {
          showNotificationMessage('Failed to approve product', 'error')
        }
      } catch (error) {
        showNotificationMessage('Failed to approve product', 'error')
      }
    }

    const getStatusClass = (status) => {
      const classes = { 'Pending': 'bg-yellow-100 text-yellow-800', 'Confirmed': 'bg-blue-100 text-blue-800', 'Completed': 'bg-green-100 text-green-800', 'Cancelled': 'bg-red-100 text-red-800' }
      return classes[status] || 'bg-gray-100 text-gray-800'
    }

    const getRoleClass = (role) => {
      const classes = { 
        'admin': 'bg-red-100 text-red-800', 
        'vendor': 'bg-purple-100 text-purple-800', 
        'customer': 'bg-green-100 text-green-800' 
      }
      return classes[role] || 'bg-gray-100 text-gray-800'
    }

    // Role-based permissions
    const userPermissions = computed(() => {
      const user = currentUser.value
      if (!user) return { canManageProducts: false, canViewOrders: false, canControlSystem: false, canAddProducts: false }
      
      switch (user.role) {
        case 'admin':
          return {
            canManageProducts: true,
            canViewOrders: true,
            canControlSystem: true,
            canAddProducts: true,
            canManageUsers: true,
            canManageVendors: true,
            canApproveProducts: true
          }
        case 'vendor':
          return {
            canManageProducts: true,
            canViewOrders: false,
            canControlSystem: false,
            canAddProducts: true,
            canManageUsers: false,
            canManageVendors: false,
            canApproveProducts: false
          }
        case 'customer':
          return {
            canManageProducts: false,
            canViewOrders: false,
            canControlSystem: false,
            canAddProducts: false,
            canManageUsers: false,
            canManageVendors: false,
            canApproveProducts: false
          }
        default:
          return {
            canManageProducts: false,
            canViewOrders: false,
            canControlSystem: false,
            canAddProducts: false,
            canManageUsers: false,
            canManageVendors: false,
            canApproveProducts: false
          }
      }
    })

    // Filter tabs based on user permissions
    const availableTabs = computed(() => {
      const allTabs = [
        { id: 'dashboard', name: 'Dashboard' },
        { id: 'orders', name: 'Orders', badge: stats.value.pending_orders },
        { id: 'users', name: 'Users' },
        { id: 'products', name: 'Products' },
        { id: 'vendors', name: 'Vendors' }
      ]
      
      return allTabs.filter(tab => {
        switch (tab.id) {
          case 'dashboard':
            return true // Everyone can see dashboard
          case 'orders':
            return userPermissions.value.canViewOrders
          case 'users':
            return userPermissions.value.canManageUsers
          case 'products':
            return userPermissions.value.canManageProducts
          case 'vendors':
            return userPermissions.value.canManageVendors
          default:
            return false
        }
      })
    })

    // New table functionality methods
    const searchQuery = ref('')
    const filterDropdownOpen = ref(false)
    const selectedProducts = ref([])
    const currentFilter = ref('all')

    const toggleFilterDropdown = () => {
      filterDropdownOpen.value = !filterDropdownOpen.value
    }

    const setFilter = (filter) => {
      currentFilter.value = filter
      filterDropdownOpen.value = false
    }

    const toggleSelectAll = (event) => {
      if (event.target.checked) {
        selectedProducts.value = filteredProducts.value.map((_, index) => index)
      } else {
        selectedProducts.value = []
      }
    }

    onMounted(async () => {
      await loadData()
      loadDashboardStats()
      loadAllOrders()
      loadAllUsers()
    })

    const userData = localStorage.getItem('user')
    if (userData) currentUser.value = JSON.parse(userData)

    return {
      products,
      orders,
      allOrders,
      allUsers,
      stats,
      currentUser,
      activeTab,
      tabs,
      dashboardStats,
      orderStatusFilter,
      selectedOrder,
      newProduct,
      imagePreview,
      imageFile,
      productSearchQuery,
      productCategoryFilter,
      productStatusFilter,
      showAddProductForm,
      filteredProducts,
      filteredOrdersList,
      totalRevenue,
      totalSpend,
      pendingOrders,
      isAddingProduct,
      // Modal variables
      viewingProduct,
      editingProduct,
      isEditing,
      productToDelete,
      showConfirmDialog,
      // Product functions
      addProduct,
      deleteProduct,
      editProduct,
      saveProduct,
      cancelEdit,
      handleImageUpload,
      removeImage,
      // Order functions
      confirmOrder,
      cancelOrder,
      completeOrder,
      deleteOrder,
      viewOrderDetails,
      updateOrderStatus,
      // User functions
      deleteUser,
      // Vendor functions
      viewVendorProducts,
      toggleVendorStatus,
      approveProduct,
      // Role-based variables
      userPermissions,
      availableTabs,
      // Utility functions
      getStatusClass,
      getRoleClass,
      getImageUrl,
      handleImageError,
      formatDate,
      formatCurrency,
      resetProductForm,
      // Product modal functions
      viewProduct,
      closeViewModal,
      closeEditModal,
      confirmDelete,
      cancelDelete,
      executeDelete,
      // Filter functions
      toggleFilterDropdown,
      setFilter,
      toggleSelectAll,
      selectedProducts,
      currentFilter,
      filterDropdownOpen,
      searchQuery,
      // Data loading functions
      loadData,
      loadDashboardStats,
      loadAllOrders,
      loadAllUsers,
      showNotificationMessage
    }
  }
}
</script>
