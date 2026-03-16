<template>
  <div class="wishlist-management">
    <!-- Wishlist Header -->
    <div class="bg-white shadow-sm border-b border-neutral-200">
      <div class="container py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-3">
            <div class="w-10 h-10 bg-gradient-to-br from-red-500 to-pink-600 rounded-xl flex items-center justify-center shadow-lg">
              <svg class="w-6 h-6 text-white" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </div>
            <h1 class="text-3xl font-bold text-gradient">My Wishlist</h1>
          </div>
          <div class="flex items-center gap-2">
            <span class="text-neutral-500">{{ wishlist.length }} item{{ wishlist.length !== 1 ? 's' : '' }}</span>
            <span class="text-neutral-400">•</span>
            <span class="font-semibold text-primary-600">Tsh {{ totalValue.toLocaleString() }}</span>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="container py-8">
      <!-- Empty State -->
      <div v-if="wishlist.length === 0" class="text-center py-16">
        <div class="card card-elevated p-8 max-w-md mx-auto">
          <div class="w-24 h-24 mx-auto bg-gradient-to-br from-red-100 to-pink-200 rounded-full flex items-center justify-center mb-6">
            <svg class="w-12 h-12 text-red-500" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
          </div>
          <h2 class="text-2xl font-bold text-neutral-800 mb-4">Your wishlist is empty</h2>
          <p class="text-neutral-600 mb-6">Start adding products you love to your wishlist!</p>
          <router-link to="/" class="btn btn-primary">
            <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            Continue Shopping
          </router-link>
        </div>
      </div>

      <!-- Wishlist Items -->
      <div v-else class="space-y-6">
        <!-- Actions Bar -->
        <div class="flex items-center justify-between bg-white p-4 rounded-lg shadow-sm border border-neutral-200">
          <div class="flex items-center gap-4">
            <button 
              @click="selectAll"
              class="btn btn-ghost btn-sm"
            >
              {{ allSelected ? 'Deselect All' : 'Select All' }}
            </button>
            <span class="text-sm text-neutral-500">
              {{ selectedItems.length }} selected
            </span>
          </div>
          <div class="flex gap-3">
            <button 
              @click="addSelectedToCart"
              class="btn btn-primary btn-sm"
              :disabled="selectedItems.length === 0"
            >
              Add Selected to Cart ({{ selectedItems.length }})
            </button>
            <button 
              @click="clearWishlist"
              class="btn btn-ghost btn-sm text-error-600 hover:text-error-700"
            >
              Clear Wishlist
            </button>
          </div>
        </div>

        <!-- Product Grid -->
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <div 
            v-for="product in wishlist" 
            :key="product.id"
            class="card card-interactive overflow-hidden group"
          >
            <!-- Product Image -->
            <div class="relative overflow-hidden">
              <img 
                :src="product.image" 
                :alt="product.name"
                class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
              >
              
              <!-- Checkbox -->
              <div class="absolute top-2 left-2">
                <input 
                  v-model="selectedItems"
                  :value="product.id"
                  type="checkbox"
                  class="w-5 h-5 text-primary-600 border-neutral-300 rounded focus:ring-primary-500"
                >
              </div>

              <!-- Quick Actions -->
              <div class="absolute top-2 right-2 flex flex-col gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
                <button 
                  @click="removeFromWishlist(product)"
                  class="w-8 h-8 bg-white/90 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white transition-colors shadow-lg text-error-500"
                  title="Remove from wishlist"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                </button>
              </div>

              <!-- Badges -->
              <div class="absolute bottom-2 left-2 flex gap-2">
                <span v-if="product.isNew" class="badge badge-accent">New</span>
                <span v-if="product.discount" class="badge badge-error">-{{ product.discount }}%</span>
                <span v-if="!product.inStock" class="badge badge-neutral">Out of Stock</span>
              </div>
            </div>

            <!-- Product Info -->
            <div class="p-4">
              <h3 class="product-title text-lg font-semibold text-neutral-900 mb-2">{{ product.name }}</h3>
              <p class="product-category text-sm text-neutral-500 mb-3">{{ product.category }}</p>
              
              <!-- Price -->
              <div class="product-price mb-4">
                <span v-if="product.discount" class="original-price text-sm text-neutral-500 line-through mr-2">Tsh {{ product.price.toLocaleString() }}</span>
                <span class="current-price text-2xl font-bold text-primary-600">Tsh {{ discountedPrice(product).toLocaleString() }}</span>
              </div>

              <!-- Rating -->
              <div class="flex items-center text-sm text-neutral-500 mb-4">
                <span class="text-warning-500">★</span>
                <span class="ml-1">{{ product.rating || 4.5 }}</span>
                <span class="ml-1">({{ product.reviews || 23 }})</span>
              </div>

              <!-- Actions -->
              <div class="flex gap-2">
                <button 
                  @click="addToCart(product)"
                  class="btn btn-primary btn-sm flex-1"
                  :disabled="!product.inStock"
                >
                  {{ product.inStock ? 'Add to Cart' : 'Out of Stock' }}
                </button>
                <router-link 
                  :to="`/product/${product.id}`"
                  class="btn btn-ghost btn-sm"
                >
                  <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                  </svg>
                </router-link>
              </div>
            </div>
          </div>
        </div>

        <!-- Wishlist Summary -->
        <div class="bg-white p-6 rounded-lg shadow-sm border border-neutral-200">
          <div class="grid grid-cols-1 md:grid-cols-4 gap-4 text-center">
            <div>
              <p class="text-sm text-neutral-500 mb-1">Total Items</p>
              <p class="text-2xl font-bold text-neutral-900">{{ wishlist.length }}</p>
            </div>
            <div>
              <p class="text-sm text-neutral-500 mb-1">Total Value</p>
              <p class="text-2xl font-bold text-primary-600">Tsh {{ totalValue.toLocaleString() }}</p>
            </div>
            <div>
              <p class="text-sm text-neutral-500 mb-1">In Stock</p>
              <p class="text-2xl font-bold text-success-600">{{ inStockCount }}</p>
            </div>
            <div>
              <p class="text-sm text-neutral-500 mb-1">On Sale</p>
              <p class="text-2xl font-bold text-error-600">{{ onSaleCount }}</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useWishlist } from '@/composables/useWishlist'
import { useCart } from '@/composables/useCart'

export default {
  name: 'WishlistManagement',
  setup() {
    const { wishlist, removeFromWishlist, clearWishlist, toggleWishlist } = useWishlist()
    const { addToCart } = useCart()
    const selectedItems = ref([])

    const allSelected = computed(() => {
      return wishlist.value.length > 0 && selectedItems.value.length === wishlist.value.length
    })

    const totalValue = computed(() => {
      return wishlist.value.reduce((total, product) => {
        return total + discountedPrice(product)
      }, 0)
    })

    const inStockCount = computed(() => {
      return wishlist.value.filter(product => product.inStock !== false).length
    })

    const onSaleCount = computed(() => {
      return wishlist.value.filter(product => product.discount).length
    })

    const discountedPrice = (product) => {
      if (product.discount) {
        return product.price * (1 - product.discount / 100)
      }
      return product.price
    }

    const selectAll = () => {
      if (allSelected.value) {
        selectedItems.value = []
      } else {
        selectedItems.value = wishlist.value.map(product => product.id)
      }
    }

    const addSelectedToCart = () => {
      const selectedProducts = wishlist.value.filter(product => 
        selectedItems.value.includes(product.id)
      )
      
      selectedProducts.forEach(product => {
        if (product.inStock !== false) {
          addToCart(product)
        }
      })
      
      // Remove selected items from wishlist after adding to cart
      selectedProducts.forEach(product => {
        removeFromWishlist(product)
      })
      
      selectedItems.value = []
    }

    return {
      wishlist,
      selectedItems,
      allSelected,
      totalValue,
      inStockCount,
      onSaleCount,
      removeFromWishlist,
      clearWishlist,
      addToCart,
      discountedPrice,
      selectAll,
      addSelectedToCart
    }
  }
}
</script>
