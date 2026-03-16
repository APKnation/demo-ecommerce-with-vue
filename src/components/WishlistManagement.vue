<template>
  <div class="wishlist-management">
    <!-- Enhanced Header with Background -->
    <div class="relative bg-gradient-to-br from-red-500 via-pink-500 to-rose-600 text-white">
      <div class="absolute inset-0 bg-black/10"></div>
      <div class="relative container py-12">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4">
            <div class="w-16 h-16 bg-white/20 backdrop-blur-sm rounded-2xl flex items-center justify-center shadow-xl">
              <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </div>
            <div>
              <h1 class="text-4xl font-bold mb-2">My Wishlist</h1>
              <p class="text-white/80">Save your favorite products for later</p>
            </div>
          </div>
          <div class="text-right">
            <div class="text-3xl font-bold mb-1">{{ wishlist.length }}</div>
            <div class="text-white/80 text-sm">item{{ wishlist.length !== 1 ? 's' : '' }}</div>
            <div class="text-2xl font-semibold mt-2">Tsh {{ totalValue.toLocaleString() }}</div>
          </div>
        </div>
      </div>
    </div>

    <!-- Advanced Filter and Sort Bar -->
    <div class="bg-white shadow-sm border-b border-neutral-200 sticky top-0 z-30">
      <div class="container py-4">
        <div class="flex flex-col lg:flex-row gap-4 items-center justify-between">
          <!-- Search -->
          <div class="relative w-full lg:w-80">
            <input 
              v-model="searchQuery"
              type="text"
              placeholder="Search wishlist..."
              class="w-full pl-10 pr-4 py-2 border border-neutral-300 rounded-lg focus:ring-2 focus:ring-primary-500 focus:border-primary-500"
            >
            <svg class="absolute left-3 top-2.5 w-5 h-5 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
            </svg>
          </div>

          <!-- Filters -->
          <div class="flex gap-3 items-center">
            <!-- Category Filter -->
            <select v-model="categoryFilter" class="px-4 py-2 border border-neutral-300 rounded-lg focus:ring-2 focus:ring-primary-500">
              <option value="">All Categories</option>
              <option value="smartphones">Smartphones</option>
              <option value="laptops">Laptops</option>
              <option value="tablets">Tablets</option>
              <option value="accessories">Accessories</option>
            </select>

            <!-- Price Range -->
            <select v-model="priceRange" class="px-4 py-2 border border-neutral-300 rounded-lg focus:ring-2 focus:ring-primary-500">
              <option value="">All Prices</option>
              <option value="0-100000">Under Tsh 100K</option>
              <option value="100000-500000">Tsh 100K - 500K</option>
              <option value="500000-1000000">Tsh 500K - 1M</option>
              <option value="1000000+">Over Tsh 1M</option>
            </select>

            <!-- Sort -->
            <select v-model="sortBy" class="px-4 py-2 border border-neutral-300 rounded-lg focus:ring-2 focus:ring-primary-500">
              <option value="name">Name</option>
              <option value="price-low">Price: Low to High</option>
              <option value="price-high">Price: High to Low</option>
              <option value="date">Date Added</option>
            </select>
          </div>

          <!-- View Toggle -->
          <div class="flex gap-2">
            <button 
              @click="viewMode = 'grid'"
              :class="viewMode === 'grid' ? 'bg-primary-600 text-white' : 'bg-neutral-100 text-neutral-600'"
              class="p-2 rounded-lg transition-colors"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2V6zM14 6a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2V6zM4 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2H6a2 2 0 01-2-2v-2zM14 16a2 2 0 012-2h2a2 2 0 012 2v2a2 2 0 01-2 2h-2a2 2 0 01-2-2v-2z"></path>
              </svg>
            </button>
            <button 
              @click="viewMode = 'list'"
              :class="viewMode === 'list' ? 'bg-primary-600 text-white' : 'bg-neutral-100 text-neutral-600'"
              class="p-2 rounded-lg transition-colors"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="container py-8">
      <!-- Empty State -->
      <div v-if="filteredWishlist.length === 0" class="text-center py-16">
        <div class="card card-elevated p-12 max-w-lg mx-auto">
          <div class="w-32 h-32 mx-auto bg-gradient-to-br from-red-100 to-pink-200 rounded-full flex items-center justify-center mb-8">
            <svg class="w-16 h-16 text-red-500" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
          </div>
          <h2 class="text-3xl font-bold text-neutral-800 mb-4">Your wishlist is empty</h2>
          <p class="text-neutral-600 mb-8 text-lg">Start adding products you love to your wishlist!</p>
          <div class="flex gap-4 justify-center">
            <router-link to="/" class="btn btn-primary">
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
              Continue Shopping
            </router-link>
            <button 
              @click="showRecommendations = true"
              class="btn btn-secondary"
            >
              <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
              </svg>
              Get Recommendations
            </button>
          </div>
        </div>
      </div>

      <!-- Wishlist Items -->
      <div v-else class="space-y-6">
        <!-- Enhanced Actions Bar -->
        <div class="bg-white p-6 rounded-xl shadow-sm border border-neutral-200">
          <div class="flex flex-col lg:flex-row gap-4 items-center justify-between">
            <div class="flex items-center gap-4">
              <button 
                @click="selectAll"
                class="btn btn-ghost"
              >
                {{ allSelected ? 'Deselect All' : 'Select All' }}
              </button>
              <span class="text-sm text-neutral-500">
                {{ selectedItems.length }} of {{ filteredWishlist.length }} selected
              </span>
            </div>
            
            <div class="flex flex-wrap gap-3">
              <button 
                @click="addSelectedToCart"
                class="btn btn-primary"
                :disabled="selectedItems.length === 0"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                Add Selected to Cart ({{ selectedItems.length }})
              </button>
              
              <button 
                @click="shareWishlist"
                class="btn btn-secondary"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.684 13.342C8.886 12.938 9 12.482 9 12c0-.482-.114-.938-.316-1.342m0 2.684a3 3 0 110-2.684m9.032 4.026a9.001 9.001 0 01-7.432 0m9.032-4.026A9.001 9.001 0 0112 3c-4.474 0-8.268 2.943-9.543 7a9.001 9.001 0 019.543 7z"></path>
                </svg>
                Share Wishlist
              </button>
              
              <button 
                @click="exportWishlist"
                class="btn btn-outline"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 10v6m0 0l-3-3m3 3l3-3m2 8H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"></path>
                </svg>
                Export
              </button>
              
              <button 
                @click="clearWishlist"
                class="btn btn-ghost text-error-600 hover:text-error-700"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                </svg>
                Clear Wishlist
              </button>
            </div>
          </div>
        </div>

        <!-- Products Display -->
        <div v-if="viewMode === 'grid'" class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6">
          <WishlistProductCard 
            v-for="product in filteredWishlist" 
            :key="product.id"
            :product="product"
            :selected="selectedItems.includes(product.id)"
            @toggle-select="toggleProductSelection"
            @remove="removeFromWishlist"
            @add-to-cart="addToCart"
          />
        </div>

        <div v-else class="space-y-4">
          <WishlistProductListItem 
            v-for="product in filteredWishlist" 
            :key="product.id"
            :product="product"
            :selected="selectedItems.includes(product.id)"
            @toggle-select="toggleProductSelection"
            @remove="removeFromWishlist"
            @add-to-cart="addToCart"
          />
        </div>

        <!-- Advanced Statistics -->
        <div class="bg-gradient-to-r from-neutral-50 to-neutral-100 p-8 rounded-xl">
          <h3 class="text-xl font-bold text-neutral-900 mb-6">Wishlist Statistics</h3>
          <div class="grid grid-cols-2 md:grid-cols-4 gap-6">
            <div class="text-center">
              <div class="text-3xl font-bold text-primary-600 mb-2">{{ wishlist.length }}</div>
              <div class="text-sm text-neutral-600">Total Items</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-success-600 mb-2">Tsh {{ totalValue.toLocaleString() }}</div>
              <div class="text-sm text-neutral-600">Total Value</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-warning-600 mb-2">{{ onSaleCount }}</div>
              <div class="text-sm text-neutral-600">On Sale</div>
            </div>
            <div class="text-center">
              <div class="text-3xl font-bold text-error-600 mb-2">{{ outOfStockCount }}</div>
              <div class="text-sm text-neutral-600">Out of Stock</div>
            </div>
          </div>
          
          <!-- Category Breakdown -->
          <div class="mt-8">
            <h4 class="font-semibold text-neutral-900 mb-4">Category Breakdown</h4>
            <div class="space-y-3">
              <div 
                v-for="(count, category) in categoryBreakdown" 
                :key="category"
                class="flex items-center justify-between"
              >
                <span class="text-neutral-700 capitalize">{{ category }}</span>
                <div class="flex items-center gap-2">
                  <div class="w-32 bg-neutral-200 rounded-full h-2">
                    <div 
                      class="bg-gradient-to-r from-primary-500 to-primary-600 h-2 rounded-full"
                      :style="{ width: `${(count / wishlist.length) * 100}%` }"
                    ></div>
                  </div>
                  <span class="text-sm font-medium text-neutral-900">{{ count }}</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Share Modal -->
    <ShareWishlistModal 
      v-if="showShareModal"
      :wishlist="wishlist"
      @close="showShareModal = false"
    />

    <!-- Recommendations Modal -->
    <RecommendationsModal 
      v-if="showRecommendations"
      :wishlist="wishlist"
      @close="showRecommendations = false"
    />
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue'
import { useWishlist } from '@/composables/useWishlist'
import { useCart } from '@/composables/useCart'
import WishlistProductCard from './WishlistProductCard.vue'
import WishlistProductListItem from './WishlistProductListItem.vue'
import ShareWishlistModal from './ShareWishlistModal.vue'
import RecommendationsModal from './RecommendationsModal.vue'

export default {
  name: 'WishlistManagement',
  components: {
    WishlistProductCard,
    WishlistProductListItem,
    ShareWishlistModal,
    RecommendationsModal
  },
  setup() {
    const { wishlist, removeFromWishlist, clearWishlist, toggleWishlist } = useWishlist()
    const { addToCart } = useCart()
    
    // State
    const selectedItems = ref([])
    const searchQuery = ref('')
    const categoryFilter = ref('')
    const priceRange = ref('')
    const sortBy = ref('name')
    const viewMode = ref('grid')
    const showShareModal = ref(false)
    const showRecommendations = ref(false)

    // Computed
    const allSelected = computed(() => {
      return filteredWishlist.value.length > 0 && 
             selectedItems.value.length === filteredWishlist.value.length
    })

    const filteredWishlist = computed(() => {
      let filtered = wishlist.value

      // Search filter
      if (searchQuery.value) {
        filtered = filtered.filter(product => 
          product.name.toLowerCase().includes(searchQuery.value.toLowerCase())
        )
      }

      // Category filter
      if (categoryFilter.value) {
        filtered = filtered.filter(product => 
          product.category === categoryFilter.value
        )
      }

      // Price range filter
      if (priceRange.value) {
        const [min, max] = priceRange.value.split('-').map(p => p.replace('+', ''))
        filtered = filtered.filter(product => {
          const price = discountedPrice(product)
          if (max) {
            return price >= parseInt(min) && price <= parseInt(max)
          } else {
            return price >= parseInt(min)
          }
        })
      }

      // Sort
      filtered.sort((a, b) => {
        switch (sortBy.value) {
          case 'name':
            return a.name.localeCompare(b.name)
          case 'price-low':
            return discountedPrice(a) - discountedPrice(b)
          case 'price-high':
            return discountedPrice(b) - discountedPrice(a)
          case 'date':
            return (b.addedDate || 0) - (a.addedDate || 0)
          default:
            return 0
        }
      })

      return filtered
    })

    const totalValue = computed(() => {
      return filteredWishlist.value.reduce((total, product) => {
        return total + discountedPrice(product)
      }, 0)
    })

    const onSaleCount = computed(() => {
      return filteredWishlist.value.filter(product => product.discount).length
    })

    const outOfStockCount = computed(() => {
      return filteredWishlist.value.filter(product => !product.inStock).length
    })

    const categoryBreakdown = computed(() => {
      const categories = {}
      filteredWishlist.value.forEach(product => {
        categories[product.category] = (categories[product.category] || 0) + 1
      })
      return categories
    })

    // Methods
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
        selectedItems.value = filteredWishlist.value.map(product => product.id)
      }
    }

    const toggleProductSelection = (productId) => {
      const index = selectedItems.value.indexOf(productId)
      if (index > -1) {
        selectedItems.value.splice(index, 1)
      } else {
        selectedItems.value.push(productId)
      }
    }

    const addSelectedToCart = () => {
      const selectedProducts = filteredWishlist.value.filter(product => 
        selectedItems.value.includes(product.id)
      )
      
      selectedProducts.forEach(product => {
        if (product.inStock !== false) {
          addToCart(product)
        }
      })
      
      selectedItems.value = []
    }

    const shareWishlist = () => {
      showShareModal.value = true
    }

    const exportWishlist = () => {
      const data = {
        wishlist: filteredWishlist.value,
        exportDate: new Date().toISOString(),
        totalValue: totalValue.value
      }
      
      const blob = new Blob([JSON.stringify(data, null, 2)], { type: 'application/json' })
      const url = URL.createObjectURL(blob)
      const a = document.createElement('a')
      a.href = url
      a.download = `wishlist-${new Date().toISOString().split('T')[0]}.json`
      a.click()
      URL.revokeObjectURL(url)
    }

    return {
      wishlist,
      selectedItems,
      searchQuery,
      categoryFilter,
      priceRange,
      sortBy,
      viewMode,
      showShareModal,
      showRecommendations,
      allSelected,
      filteredWishlist,
      totalValue,
      onSaleCount,
      outOfStockCount,
      categoryBreakdown,
      removeFromWishlist,
      clearWishlist,
      addToCart,
      selectAll,
      toggleProductSelection,
      addSelectedToCart,
      shareWishlist,
      exportWishlist
    }
  }
}
</script>

<style scoped>
.wishlist-management {
  min-height: 100vh;
  background: linear-gradient(to bottom, #fafafa, #f3f4f6);
}
</style>
