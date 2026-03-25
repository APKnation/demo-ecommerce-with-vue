<template>
  <div>
    <!-- Admin Header -->
    <div class="bg-gradient-to-r from-primary-600 to-secondary-600 text-white rounded-lg shadow-xl p-8 mb-8">
    <div class="flex items-center justify-between">
      <div>
        <h1 class="text-4xl font-bold mb-2">Admin Dashboard</h1>
        <p class="text-primary-100">Manage your e-commerce store</p>
      </div>
      <div class="text-right">
        <div class="text-3xl font-bold">{{ products.length }}</div>
        <div class="text-sm text-primary-100">Total Products</div>
      </div>
    </div>
    </div>

    <!-- Navigation Tabs -->
    <div class="mt-8 flex space-x-1 bg-white rounded-lg p-1 shadow-md">
      <button 
        v-for="tab in tabs" 
        :key="tab.id"
        @click="tab.route ? $router.push(tab.route) : activeTab = tab.id"
        :class="[
          'px-6 py-3 rounded-md font-medium transition-all text-sm',
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

    <!-- Dashboard Stats Section -->
    <div v-if="activeTab === 'dashboard'" class="mt-8">
      <!-- Main Stats Row -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
        <div v-for="stat in dashboardStats.slice(0, 4)" :key="stat.label" 
             class="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">{{ stat.label }}</p>
              <p class="text-2xl font-bold text-gray-900 mt-1">{{ stat.value }}</p>
            </div>
            <div :class="`w-12 h-12 ${stat.bgColor} rounded-xl flex items-center justify-center`">
              <svg class="w-6 h-6" :class="stat.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="stat.icon"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Secondary Stats Row -->
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        <div v-for="stat in dashboardStats.slice(4)" :key="stat.label" 
             class="bg-white rounded-xl shadow-lg p-6 hover:shadow-xl transition-shadow duration-300">
          <div class="flex items-center justify-between">
            <div>
              <p class="text-sm font-medium text-gray-600">{{ stat.label }}</p>
              <p class="text-2xl font-bold text-gray-900 mt-1">{{ stat.value }}</p>
            </div>
            <div :class="`w-12 h-12 ${stat.bgColor} rounded-xl flex items-center justify-center`">
              <svg class="w-6 h-6" :class="stat.iconColor" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" :d="stat.icon"></path>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- View Product Modal -->
    <div v-if="viewingProduct" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-96 overflow-y-auto">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold text-gray-900">Product Details</h2>
          <button @click="closeViewModal" class="text-gray-500 hover:text-gray-700 font-medium">
            Close
          </button>
        </div>
        
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <img v-if="viewingProduct.image" :src="viewingProduct.image" :alt="viewingProduct.name" 
                 class="w-full h-64 object-cover rounded-lg">
            <div v-else class="w-full h-64 bg-gray-200 rounded-lg flex items-center justify-center">
              <span class="text-gray-400">No Image</span>
            </div>
          </div>
          
          <div class="space-y-4">
            <div>
              <h3 class="text-lg font-semibold text-gray-900 mb-2">{{ viewingProduct.name }}</h3>
              <span class="px-3 py-1 text-sm rounded-full bg-blue-100 text-blue-800">
                {{ viewingProduct.category }}
              </span>
            </div>
            
            <div class="text-2xl font-bold text-blue-600">
              Tsh {{ viewingProduct.price.toLocaleString() }}
            </div>
            
            <div class="text-sm text-gray-600">
              <p><strong>Status:</strong> <span class="px-2 py-1 rounded-full bg-green-100 text-green-800">Active</span></p>
              <p><strong>Added:</strong> {{ formatDate(viewingProduct.addedDate) }}</p>
            </div>
          </div>
        </div>
        
        <div class="flex justify-end space-x-3 mt-6 pt-4 border-t">
          <button @click="closeViewModal" class="btn btn-secondary">
            Close
          </button>
          <button @click="editProduct(viewingProduct)" class="btn btn-primary">
            Edit Product
          </button>
        </div>
      </div>
    </div>

    <!-- Edit Product Modal -->
    <div v-if="isEditing && editingProduct" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-96 overflow-y-auto">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold text-gray-900 mb-4">Edit Product</h2>
          <div class="flex items-center space-x-2">
            <div class="flex items-center">
              <div class="w-3 h-3 bg-green-500 rounded-full animate-pulse"></div>
              <span class="text-sm text-green-600 font-medium">Editing Mode</span>
            </div>
            <button @click="closeEditModal" class="text-gray-500 hover:text-gray-700 font-medium">
            Cancel
          </button>
        </div>
        
        <form @submit.prevent="updateProduct" class="space-y-6">
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
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
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
          </div>
          
          <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Category</label>
              <select
                v-model="editingProduct.category"
                required
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
                <option value="">Select Category</option>
                <option value="laptops">Laptops</option>
                <option value="phones">Smartphones</option>
                <option value="accessories">Accessories</option>
              </select>
            </div>
            
            <div>
              <label class="block text-sm font-semibold text-gray-700 mb-2">Image URL</label>
              <input
                v-model="editingProduct.image"
                type="text"
                required
                placeholder="/images/product.jpg"
                class="w-full px-4 py-3 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all text-gray-900"
              >
            </div>
          </div>
          
          <div class="flex space-x-3">
            <button type="button" @click="closeEditModal" class="btn btn-secondary">
              Cancel
            </button>
            <button type="submit" class="btn btn-primary">
              Update Product
            </button>
          </div>
        </form>
      </div>
    </div>
    </div>
    
    <!-- Orders Management Section -->
    <div v-if="activeTab === 'orders'" class="mt-8">
      <div class="bg-white rounded-xl shadow-lg p-6">
        <div class="flex justify-between items-center mb-6">
          <h2 class="text-2xl font-bold">Order Management</h2>
          <div class="flex gap-4">
            <select v-model="orderStatusFilter" class="border rounded-lg px-3 py-2 focus:ring-2 focus:ring-blue-500">
              <option value="all">All Orders</option>
              <option value="Pending">Pending</option>
              <option value="Confirmed">Confirmed</option>
              <option value="Completed">Completed</option>
              <option value="Cancelled">Cancelled</option>
            </select>
          </div>
        </div>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Order #</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Customer</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Items</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Amount</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Status</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Date</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="order in filteredOrdersList" :key="order.id">
                <td class="px-6 py-4 text-sm font-medium text-gray-900">{{ order.order_number || order.id }}</td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ order.customer?.username || 'Unknown' }}</td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ order.items?.length || 0 }} items</td>
                <td class="px-6 py-4 text-sm text-gray-900 font-semibold">Tsh {{ Number(order.total_amount || order.total).toLocaleString() }}</td>
                <td class="px-6 py-4">
                  <span :class="getStatusClass(order.status)">{{ order.status }}</span>
                </td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ formatDate(order.created_at || order.date) }}</td>
                <td class="px-6 py-4 text-sm">
                  <div class="flex flex-wrap gap-2">
                    <button @click="viewOrderDetails(order)" class="bg-gray-500 hover:bg-gray-600 text-white px-3 py-1 rounded text-xs">View</button>
                    <button v-if="order.status === 'Pending'" @click="confirmOrder(order.id)" class="bg-green-500 hover:bg-green-600 text-white px-3 py-1 rounded text-xs">Confirm</button>
                    <button v-if="order.status === 'Confirmed'" @click="completeOrder(order.id)" class="bg-blue-500 hover:bg-blue-600 text-white px-3 py-1 rounded text-xs">Complete</button>
                    <button v-if="['Pending', 'Confirmed'].includes(order.status)" @click="cancelOrder(order.id)" class="bg-red-500 hover:bg-red-600 text-white px-3 py-1 rounded text-xs">Cancel</button>
                    <button v-if="order.status !== 'Cancelled'" @click="deleteOrder(order.id)" class="bg-gray-700 hover:bg-gray-800 text-white px-3 py-1 rounded text-xs">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    
    <!-- Users Management Section -->
    <div v-if="activeTab === 'users'" class="mt-8">
      <div class="bg-white rounded-xl shadow-lg p-6">
        <h2 class="text-2xl font-bold mb-4">User Management</h2>
        <div class="overflow-x-auto">
          <table class="min-w-full divide-y divide-gray-200">
            <thead class="bg-gray-50">
              <tr>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">User</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Role</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Phone</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Joined</th>
                <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Actions</th>
              </tr>
            </thead>
            <tbody class="bg-white divide-y divide-gray-200">
              <tr v-for="user in allUsers" :key="user.id">
                <td class="px-6 py-4">
                  <div class="flex items-center">
                    <div class="w-8 h-8 bg-gray-300 rounded-full flex items-center justify-center text-sm font-medium">{{ user.username?.charAt(0).toUpperCase() }}</div>
                    <div class="ml-3">
                      <p class="text-sm font-medium text-gray-900">{{ user.username }}</p>
                      <p class="text-sm text-gray-500">{{ user.first_name }} {{ user.last_name }}</p>
                    </div>
                  </div>
                </td>
                <td class="px-6 py-4"><span :class="getRoleClass(user.role)">{{ user.role }}</span></td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ user.phone }}</td>
                <td class="px-6 py-4 text-sm text-gray-500">{{ formatDate(user.created_at) }}</td>
                <td class="px-6 py-4 text-sm">
                  <button v-if="user.id !== currentUser?.id" @click="deleteUser(user.id)" class="bg-red-500 text-white px-3 py-1 rounded text-xs">Delete</button>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
    
    <!-- Products Tab (existing content wrapped) -->
    <div v-if="activeTab === 'products'" class="mt-8">
      <!-- Product Management Header -->
      <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6 mb-8">
        <div class="flex flex-col md:flex-row md:items-center md:justify-between gap-4">
          <div>
            <h2 class="text-2xl font-bold text-gray-800">Product Management</h2>
            <p class="text-gray-600 mt-1">Manage your store inventory</p>
          </div>
          <div class="flex flex-col sm:flex-row gap-3">
            <div class="relative">
              <input
                v-model="productSearchQuery"
                type="text"
                placeholder="Search products..."
                class="pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500 w-full sm:w-64"
              >
              <span class="absolute left-3 top-2.5 text-gray-400">🔍</span>
            </div>
            <select
              v-model="productCategoryFilter"
              class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="">All Categories</option>
              <option value="Electronics">Electronics</option>
              <option value="Phones">Phones</option>
              <option value="Laptops">Laptops</option>
              <option value="Accessories">Accessories</option>
              <option value="Other">Other</option>
            </select>
            <select
              v-model="productStatusFilter"
              class="px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
            >
              <option value="">All Status</option>
              <option value="active">Active</option>
              <option value="inactive">Inactive</option>
            </select>
          </div>
        </div>
      </div>

      <div class="grid grid-cols-1 xl:grid-cols-3 gap-8">
        <!-- Add Product Section -->
        <div class="xl:col-span-2">
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden">
            <div class="bg-gradient-to-r from-blue-500 to-blue-600 text-white px-6 py-4">
              <h2 class="text-xl font-semibold flex items-center">
                <span class="mr-2">➕</span>
                Add New Product
              </h2>
            </div>
            <form @submit.prevent="addProduct" class="p-6">
              <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Product Name</label>
                  <input
                    v-model="newProduct.name"
                    type="text"
                    required
                    class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="Enter product name"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Price (Tsh)</label>
                  <input
                    v-model.number="newProduct.price"
                    type="number"
                    required
                    min="0"
                    step="0.01"
                    class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="Enter price"
                  />
                </div>
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Category</label>
                  <select
                    v-model="newProduct.category"
                    required
                    class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
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
                <label class="block text-sm font-medium text-gray-700 mb-2">Product Image</label>
                <div class="space-y-2">
                  <input
                    v-model="newProduct.image"
                    type="url"
                    class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                    placeholder="Enter image URL (optional)"
                  />
                  <div class="text-sm text-gray-500 text-center">OR</div>
                  <input
                    type="file"
                    accept="image/*"
                    @change="handleProductImageChange"
                    class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                  />
                  <p class="text-xs text-gray-500">Upload image from your device</p>
                </div>
              </div>
            </div>
            <div class="mt-6">
              <label class="block text-sm font-medium text-gray-700 mb-2">Description</label>
              <textarea
                v-model="newProduct.description"
                rows="3"
                class="w-full px-3 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-blue-500"
                placeholder="Enter product description"
              ></textarea>
            </div>
            <div class="mt-6 flex justify-end space-x-3">
              <button
                type="button"
                @click="resetProductForm"
                class="px-4 py-2 border border-gray-300 rounded-lg hover:bg-gray-50"
              >
                Reset
              </button>
              <button
                type="submit"
                :disabled="isAddingProduct"
                class="px-6 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600 disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="isAddingProduct">Adding...</span>
                <span v-else>Add Product</span>
              </button>
            </div>
          </form>
        </div>
        
        <!-- Product List -->
        <div class="bg-white rounded-xl shadow-lg border border-gray-200 overflow-hidden mt-8">
          <div class="bg-gradient-to-r from-green-500 to-green-600 text-white px-6 py-4">
            <h2 class="text-xl font-semibold flex items-center justify-between">
              <span>
                <span class="mr-2">📦</span>
                Product Inventory ({{ filteredProducts.length }} items)
              </span>
              <span class="text-sm bg-white/20 px-3 py-1 rounded-full">
                {{ filteredProducts.length }} of {{ products.length }} products
              </span>
            </h2>
          </div>
          
          <div class="overflow-x-auto">
            <table class="w-full">
              <thead class="bg-gray-50 border-b">
                <tr>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Product</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Category</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Price</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Stock</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Status</th>
                  <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Actions</th>
                </tr>
              </thead>
              <tbody class="bg-white divide-y divide-gray-200">
                <tr v-for="product in filteredProducts" :key="product.id" class="hover:bg-gray-50">
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center space-x-4">
                      <div class="relative">
                        <img 
                          v-if="product.image && product.image !== '' && product.image !== '/images/placeholder.jpg'" 
                          :src="product.image" 
                          :alt="product.name || 'Product'" 
                          class="w-16 h-16 object-cover rounded-xl shadow-md hover:shadow-lg transition-shadow duration-300"
                          @error="$event.target.src='/images/placeholder.jpg'"
                        >
                        <div v-else class="w-16 h-16 bg-gradient-to-br from-gray-100 to-gray-200 rounded-xl flex items-center justify-center shadow-md">
                          <span class="text-2xl">📦</span>
                        </div>
                        <!-- Stock indicator badge -->
                        <div :class="[
                          'absolute -top-1 -right-1 w-5 h-5 rounded-full flex items-center justify-center text-xs font-bold',
                          product.stock > 10 ? 'bg-green-500' : 
                          product.stock > 0 ? 'bg-yellow-500' : 
                          'bg-red-500'
                        ]">
                          <span class="text-white">{{ product.stock || 0 }}</span>
                        </div>
                      </div>
                      <div class="flex-1">
                        <h4 class="text-sm font-bold text-gray-900 mb-1 line-clamp-1">{{ product.name || product.title || 'Unnamed Product' }}</h4>
                        <p class="text-xs text-gray-600 line-clamp-2 mb-2">{{ product.description || 'No description available' }}</p>
                        <div class="flex items-center space-x-2">
                          <span class="px-2 py-1 text-xs font-medium rounded-full bg-gradient-to-r from-blue-100 to-blue-200 text-blue-800 border border-blue-300">
                            {{ product.category }}
                          </span>
                          <span :class="[
                            'px-2 py-1 text-xs font-medium rounded-full',
                            product.is_active ? 'bg-green-100 text-green-800 border border-green-300' : 'bg-red-100 text-red-800 border border-red-300'
                          ]">
                            {{ product.is_active ? 'Active' : 'Inactive' }}
                          </span>
                        </div>
                      </div>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="text-lg font-bold text-transparent bg-gradient-to-r from-green-600 to-emerald-600 bg-clip-text">
                      Tsh {{ Number(product.price).toLocaleString() }}
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex items-center space-x-2">
                      <span :class="[
                        'px-3 py-1 text-sm font-bold rounded-full border',
                        product.stock > 10 ? 'bg-green-100 text-green-800 border-green-300' : 
                        product.stock > 0 ? 'bg-yellow-100 text-yellow-800 border-yellow-300' : 
                        'bg-red-100 text-red-800 border-red-300'
                      ]">
                        {{ product.stock || 0 }} units
                      </span>
                      <span v-if="product.stock <= 10 && product.stock > 0" class="text-xs text-yellow-600 font-medium">
                        ⚠️ Low Stock
                      </span>
                      <span v-if="product.stock === 0" class="text-xs text-red-600 font-medium">
                        🚫 Out of Stock
                      </span>
                    </div>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <span :class="[
                      'px-3 py-1 text-sm font-semibold rounded-full border',
                      product.is_active ? 'bg-gradient-to-r from-green-100 to-emerald-100 text-green-800 border-green-300' : 'bg-gradient-to-r from-red-100 to-rose-100 text-red-800 border-red-300'
                    ]">
                      {{ product.is_active ? '✅ Active' : '❌ Inactive' }}
                    </span>
                  </td>
                  <td class="px-6 py-4 whitespace-nowrap">
                    <div class="flex flex-col space-y-2">
                      <div class="flex space-x-2">
                        <button @click="viewProduct(product)" class="px-3 py-1 bg-gradient-to-r from-blue-500 to-blue-600 text-white text-xs font-medium rounded-lg hover:from-blue-600 hover:to-blue-700 transition-all duration-200 shadow-sm hover:shadow-md">
                          👁️ View
                        </button>
                        <button @click="editProduct(product)" class="px-3 py-1 bg-gradient-to-r from-green-500 to-green-600 text-white text-xs font-medium rounded-lg hover:from-green-600 hover:to-green-700 transition-all duration-200 shadow-sm hover:shadow-md">
                          ✏️ Edit
                        </button>
                      </div>
                      <button @click="deleteProduct(product.id)" class="px-3 py-1 bg-gradient-to-r from-red-500 to-red-600 text-white text-xs font-medium rounded-lg hover:from-red-600 hover:to-red-700 transition-all duration-200 shadow-sm hover:shadow-md">
                        🗑️ Delete
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
            
            <div v-if="filteredProducts.length === 0" class="text-center py-8 text-gray-500">
              <span class="text-4xl mb-4 block">📦</span>
              <p>No products found</p>
              <p class="text-sm">Try adjusting your search or filters</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Statistics Section -->
      <div class="space-y-6">
        <!-- Stats Cards -->
        <div class="grid grid-cols-1 gap-4">
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Total Products</p>
                <p class="text-3xl font-bold text-blue-600 mt-1">{{ products.length }}</p>
              </div>
              <div class="bg-blue-100 p-3 rounded-lg">
                <span class="text-blue-600 font-bold text-xl">📦</span>
              </div>
            </div>
          </div>
          
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Total Orders</p>
                <p class="text-3xl font-bold text-green-600 mt-1">{{ orders.length }}</p>
              </div>
              <div class="bg-green-100 p-3 rounded-lg">
                <span class="text-green-600 font-bold text-xl">📋</span>
              </div>
            </div>
          </div>
          
          <div class="bg-white rounded-xl shadow-lg border border-gray-200 p-6">
            <div class="flex items-center justify-between">
              <div>
                <p class="text-sm font-medium text-gray-600">Total Revenue</p>
                <p class="text-3xl font-bold text-yellow-600 mt-1">Tsh {{ Math.floor(totalSpend).toLocaleString() }}</p>
              </div>
              <div class="bg-yellow-100 p-3 rounded-lg">
                <span class="text-yellow-600 font-bold text-xl">💰</span>
              </div>
            </div>
          </div>
        </div>
      </div>
      </div>
    </div>
    </div>
    
    <!-- Order Details Modal -->
    <div v-if="selectedOrder" class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50">
      <div class="bg-white rounded-xl p-6 max-w-2xl w-full mx-4 max-h-[90vh] overflow-y-auto">
        <div class="flex justify-between items-center mb-4">
          <h3 class="text-xl font-bold">Order Details #{{ selectedOrder.order_number || selectedOrder.id }}</h3>
          <button @click="selectedOrder = null" class="text-gray-500 hover:text-gray-700">
            <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        <div class="space-y-4">
          <div class="grid grid-cols-2 gap-4">
            <div>
              <p class="text-sm text-gray-600">Customer</p>
              <p class="font-medium">{{ selectedOrder.customer?.username || 'Unknown' }}</p>
            </div>
            <div>
              <p class="text-sm text-gray-600">Status</p>
              <span :class="getStatusClass(selectedOrder.status)">{{ selectedOrder.status }}</span>
            </div>
          </div>
          <div>
            <p class="text-sm text-gray-600 mb-2">Items</p>
            <div class="bg-gray-50 rounded-lg p-4 space-y-2">
              <div v-for="item in selectedOrder.items" :key="item.id" class="flex justify-between items-center py-2 border-b last:border-0">
                <div class="flex items-center space-x-3">
                  <img v-if="item.product?.image || item.image" :src="item.product?.image || item.image" class="w-12 h-12 object-cover rounded" />
                  <div>
                    <p class="font-medium">{{ item.product?.title || item.name }}</p>
                    <p class="text-sm text-gray-500">Qty: {{ item.quantity }}</p>
                  </div>
                </div>
                <span class="font-semibold">Tsh {{ Number(item.price).toLocaleString() }}</span>
              </div>
            </div>
          </div>
          <div class="flex justify-between items-center pt-4 border-t">
            <div>
              <p class="text-sm text-gray-600">Order Date</p>
              <p class="font-medium">{{ formatDate(selectedOrder.created_at || selectedOrder.date) }}</p>
            </div>
            <div class="text-right">
              <p class="text-sm text-gray-600">Total Amount</p>
              <p class="text-2xl font-bold text-blue-600">
                Tsh {{ Number(selectedOrder.total_amount || selectedOrder.total).toLocaleString() }}
              </p>
            </div>
          </div>
          <div class="flex justify-end space-x-3 pt-4">
            <button @click="selectedOrder = null" class="px-4 py-2 border rounded-lg hover:bg-gray-50">Close</button>
            <button v-if="selectedOrder.status === 'Pending'" @click="confirmOrder(selectedOrder.id); selectedOrder = null" class="px-4 py-2 bg-green-500 text-white rounded-lg hover:bg-green-600">Confirm</button>
            <button v-if="selectedOrder.status === 'Confirmed'" @click="completeOrder(selectedOrder.id); selectedOrder = null" class="px-4 py-2 bg-blue-500 text-white rounded-lg hover:bg-blue-600">Complete</button>
            <button v-if="['Pending', 'Confirmed'].includes(selectedOrder.status)" @click="cancelOrder(selectedOrder.id); selectedOrder = null" class="px-4 py-2 bg-red-500 text-white rounded-lg hover:bg-red-600">Cancel</button>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
import { ref, computed, inject, onMounted } from 'vue'
import Swal from 'sweetalert2'

export default {
  name: 'Admin',
  setup() {
    const products = ref([])
    const orders = ref([])
    const allOrders = ref([])
    const allUsers = ref([])
    const stats = ref({})
    const currentUser = ref(null)
    const activeTab = ref('dashboard')
    const orderStatusFilter = ref('all')
    const selectedOrder = ref(null)
    const API_BASE_URL = 'http://localhost:8000/api'
    
    const getToken = () => localStorage.getItem('token')
    
    const tabs = computed(() => [
      { id: 'dashboard', name: 'Dashboard' },
      { id: 'orders', name: 'Orders', badge: stats.value.pending_orders, route: '/admin/orders' },
      { id: 'users', name: 'Users' },
      { id: 'products', name: 'Products' }
    ])
    
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
      description: '',
      image: '',
      stock: 0,
      condition: 'new'
    })

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
        filtered = filtered.filter(product => 
          productStatusFilter.value === 'active' ? product.is_active : !product.is_active
        )
      }

      return filtered
    })

    const isAddingProduct = ref(false)
    const editingProduct = ref(null)
    const isEditing = ref(false)
    const viewingProduct = ref(null)
    const productToDelete = ref(null)

    // Handle product image file change
    const handleProductImageChange = (event) => {
      newProduct.value.imageFile = event.target.files[0]
    }
    
    // New table functionality
    const searchQuery = ref('')
    const filterDropdownOpen = ref(false)
    const selectedProducts = ref([])
    const currentFilter = ref('all')

    // SweetAlert notification system
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

    // Vue confirm dialog
    const confirmDelete = (index) => {
      productToDelete.value = index
      showConfirmDialog.value = true
    }

    const cancelDelete = () => {
      productToDelete.value = null
      showConfirmDialog.value = false
    }

    const executeDelete = () => {
      if (productToDelete.value !== null) {
        const productName = products.value[productToDelete.value].name
        products.value.splice(productToDelete.value, 1)
        saveProducts()
        showNotificationMessage(`${productName} removed successfully!`)
        cancelDelete()
      }
    }

    // Product Management Functions
    const addProduct = async () => {
      isAddingProduct.value = true
      try {
        // Map category name to ID
        const categoryMap = {
          'Electronics': 4,
          'Phones': 5, 
          'Laptops': 4,
          'Accessories': 6,
          'Other': 4
        }
        
        // Use FormData for potential image upload
        const formData = new FormData()
        formData.append('title', newProduct.value.name)
        formData.append('price', newProduct.value.price)
        formData.append('category', categoryMap[newProduct.value.category] || 4)
        formData.append('description', newProduct.value.description)
        formData.append('is_active', true)
        formData.append('stock', 1) // Default stock
        
        // Add image if provided
        if (newProduct.value.imageFile) {
          formData.append('image', newProduct.value.imageFile)
        } else if (newProduct.value.image) {
          formData.append('image_url', newProduct.value.image)
        }
        
        const response = await fetch(`${API_BASE_URL}/products/create/`, {
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
          await loadData() // Refresh products list
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

    // Load data from backend API
    const loadData = async () => {
      try {
        // Load products from backend
        const productsResponse = await fetch(`${API_BASE_URL}/products/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (productsResponse.ok) {
          products.value = await productsResponse.json()
        } else {
          // Fallback to localStorage if API fails
          const savedProducts = localStorage.getItem('adminProducts')
          if (savedProducts) {
            products.value = JSON.parse(savedProducts)
          } else {
            // Load default products with real images from home page
            products.value = [
              { 
                id: 1,
                name: 'Mac Book', 
                title: 'Mac Book',
                price: 1000000, 
                category: 'laptops', 
                image: '/images/w.jpg',
                description: 'High-performance MacBook with latest M2 chip, 16GB RAM, 512GB SSD. Perfect for professionals and creators.',
                stock: 5,
                is_active: true
              },
              { 
                id: 2,
                name: 'HP-Brand', 
                title: 'HP-Brand Laptop',
                price: 150000, 
                category: 'laptops', 
                image: '/images/j.jpg',
                description: 'Reliable HP laptop with Intel Core i5, 8GB RAM, 256GB SSD. Great for business and everyday use.',
                stock: 10,
                is_active: true
              },
              { 
                id: 3,
                name: 'Dell', 
                title: 'Dell Laptop',
                price: 200000, 
                category: 'laptops', 
                image: '/images/k.jpg',
                description: 'Dell laptop with Intel Core i7, 16GB RAM, 1TB SSD. Excellent performance for demanding tasks.',
                stock: 3,
                is_active: true
              },
              { 
                id: 4,
                name: 'Apple', 
                title: 'Apple iPhone',
                price: 1000000, 
                category: 'phones', 
                image: '/images/d.jpg',
                description: 'Latest Apple iPhone with A17 Pro chip, 48MP camera, Dynamic Island. Premium smartphone experience.',
                stock: 8,
                is_active: true
              },
              { 
                id: 5,
                name: 'HP-Elite', 
                title: 'HP EliteBook',
                price: 1500000, 
                category: 'laptops', 
                image: '/images/a.jpg',
                description: 'Premium HP EliteBook with advanced security features, Intel Core i7, 32GB RAM, 2TB SSD.',
                stock: 2,
                is_active: true
              },
              { 
                id: 6,
                name: 'Sony', 
                title: 'Sony Headphones',
                price: 200000, 
                category: 'accessories', 
                image: '/images/f.jpg',
                description: 'Premium Sony wireless headphones with noise cancellation, 30-hour battery life.',
                stock: 15,
                is_active: true
              },
              { 
                id: 7,
                name: 'Infinix', 
                title: 'Infinix Smartphone',
                price: 400000, 
                category: 'phones', 
                image: '/images/g.jpg',
                description: 'Affordable Infinix smartphone with great features, large display, long battery life.',
                stock: 20,
                is_active: true
              },
              { 
                id: 8,
                name: 'iPhone', 
                title: 'iPhone Pro',
                price: 1500000, 
                category: 'phones', 
                image: '/images/p.jpg',
                description: 'Professional iPhone with advanced camera system, A17 Pro chip, titanium design.',
                stock: 6,
                is_active: true
              },
              { 
                id: 9,
                name: 'Samsung', 
                title: 'Samsung Galaxy',
                price: 3000000, 
                category: 'phones', 
                image: '/images/l.jpg',
                description: 'Flagship Samsung Galaxy with top-tier specifications, premium build quality, excellent camera.',
                stock: 4,
                is_active: true
              }
            ]
            saveProducts()
          }
        }
      } catch (error) {
        console.error('Failed to load products:', error)
        // Fallback to localStorage
        const savedProducts = localStorage.getItem('adminProducts')
        if (savedProducts) {
          products.value = JSON.parse(savedProducts)
        }
      }
      
      orders.value = JSON.parse(localStorage.getItem('orders')) || []
    }

    const saveProducts = () => {
      localStorage.setItem('adminProducts', JSON.stringify(products.value))
    }

    const totalRevenue = computed(() => {
      const total = allOrders.value.reduce((total, order) => {
        const orderTotal = Number(order.total_amount || order.total || 0)
        return total + orderTotal
      }, 0)
      return Math.round(total) // Ensure we return an integer
    })

    const totalSpend = computed(() => {
      console.log('=== DEBUGGING TOTAL SPEND ===')
      console.log('allOrders.value:', allOrders.value)
      console.log('Number of orders:', allOrders.value.length)
      
      // Check all possible status values
      const statusCounts = {}
      allOrders.value.forEach(order => {
        const status = order.status || 'unknown'
        statusCounts[status] = (statusCounts[status] || 0) + 1
      })
      console.log('Order status counts:', statusCounts)
      
      // Try multiple status variations
      const deliveredOrders = allOrders.value.filter(order => {
        const status = (order.status || '').toLowerCase()
        return status === 'delivered' || status === 'completed' || status === 'delivered'
      })
      console.log('Delivered orders:', deliveredOrders)
      console.log('Number of delivered orders:', deliveredOrders.length)
      
      if (deliveredOrders.length === 0) {
        console.log('No delivered orders found, checking all orders for total_amount values...')
        allOrders.value.forEach(order => {
          console.log(`Order ${order.id}: status="${order.status}", total_amount="${order.total_amount}", total="${order.total}"`)
        })
      }
      
      const total = deliveredOrders.reduce((total, order) => {
        const orderTotal = Number(order.total_amount || order.total || 0)
        console.log(`Order ${order.id || 'unknown'}: ${order.total_amount || order.total || 0} -> ${orderTotal}`)
        return total + orderTotal
      }, 0)
      
      console.log('Raw total:', total)
      const roundedTotal = Math.round(total)
      console.log('Rounded total:', roundedTotal)
      console.log('=== END DEBUGGING ===')
      return roundedTotal
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

    const updateProduct = () => {
      if (!editingProduct.value || !editingProduct.value.name) {
        showNotificationMessage('No product to update')
        return
      }
      
      const index = products.value.findIndex(p => p.name === editingProduct.value.name)
      if (index !== -1) {
        products.value[index] = JSON.parse(JSON.stringify(editingProduct.value))
        saveProducts()
        closeEditModal()
        showNotificationMessage('Product updated successfully!')
      } else {
        showNotificationMessage('Product not found')
      }
    }

    // Enhanced remove product function with Vue confirm
    const removeProduct = (index) => {
      confirmDelete(index)
    }

    // Format date function
    const formatDate = (dateString) => {
      return new Date(dateString).toLocaleDateString()
    }

    // New table functionality methods
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
        const response = await fetch(`${API_BASE_URL}/orders/`, {
          headers: { 'Authorization': `Token ${getToken()}` }
        })
        if (response.ok) {
          const ordersData = await response.json()
          console.log('Raw orders data from API:', ordersData)
          
          // Remove duplicates by order ID
          const uniqueOrders = ordersData.filter((order, index, self) => 
            index === self.findIndex((o) => o.id === order.id)
          )
          console.log('Unique orders:', uniqueOrders)
          
          allOrders.value = uniqueOrders
          console.log('Final allOrders.value:', allOrders.value)
        }
      } catch (error) { console.error('Failed to load orders:', error) }
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
      selectedOrder.value = order
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

    const getStatusClass = (status) => {
      const classes = { 'Pending': 'bg-yellow-100 text-yellow-800', 'Confirmed': 'bg-blue-100 text-blue-800', 'Completed': 'bg-green-100 text-green-800', 'Cancelled': 'bg-red-100 text-red-800' }
      return classes[status] || 'bg-gray-100 text-gray-800'
    }

    const getRoleClass = (role) => {
      const classes = { 'admin': 'bg-red-100 text-red-800', 'author': 'bg-blue-100 text-blue-800', 'customer': 'bg-green-100 text-green-800' }
      return classes[role] || 'bg-gray-100 text-gray-800'
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
      newProduct,
      editingProduct,
      isEditing,
      viewingProduct,
      productToDelete,
      productSearchQuery,
      productCategoryFilter,
      productStatusFilter,
      filteredProducts,
      searchQuery,
      filterDropdownOpen,
      selectedProducts,
      currentFilter,
      totalRevenue,
      totalSpend,
      saveProducts,
      addProduct,
      resetProductForm,
      handleProductImageChange,
      isAddingProduct,
      viewProduct,
      closeViewModal,
      editProduct,
      closeEditModal,
      updateProduct,
      removeProduct,
      confirmDelete,
      cancelDelete,
      executeDelete,
      formatDate,
      toggleFilterDropdown,
      setFilter,
      toggleSelectAll,
      // Admin Dashboard
      activeTab,
      tabs,
      dashboardStats,
      allOrders,
      allUsers,
      stats,
      currentUser,
      loadDashboardStats,
      loadAllOrders,
      loadAllUsers,
      confirmOrder,
      cancelOrder,
      completeOrder,
      deleteOrder,
      viewOrderDetails,
      selectedOrder,
      orderStatusFilter,
      filteredOrdersList,
      deleteUser,
      getStatusClass,
      getRoleClass
    }
  }
}
</script>
