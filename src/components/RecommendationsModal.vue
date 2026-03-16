<template>
  <div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
    <div 
      class="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden"
      @click.stop
    >
      <!-- Modal Header -->
      <div class="bg-gradient-to-r from-primary-600 to-secondary-600 text-white p-6">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold mb-2">Recommended for You</h2>
            <p class="text-white/80">Based on your wishlist preferences</p>
          </div>
          <button 
            @click="$emit('close')"
            class="w-10 h-10 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white/30 transition-colors"
          >
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Modal Content -->
      <div class="p-6 overflow-auto max-h-[calc(90vh-120px)]">
        <!-- Recommendation Categories -->
        <div class="space-y-8">
          <!-- Similar Products -->
          <div>
            <h3 class="text-xl font-bold text-neutral-900 mb-4 flex items-center">
              <svg class="w-6 h-6 mr-2 text-primary-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"></path>
              </svg>
              Similar Products
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
              <div 
                v-for="product in similarProducts" 
                :key="product.id"
                class="card card-interactive overflow-hidden group"
              >
                <div class="relative overflow-hidden">
                  <img 
                    :src="product.image" 
                    :alt="product.name"
                    class="w-full h-48 object-cover group-hover:scale-105 transition-transform duration-300"
                  >
                  <div class="absolute top-2 left-2">
                    <span class="badge badge-accent">Recommended</span>
                  </div>
                </div>
                <div class="p-4">
                  <h4 class="font-semibold text-neutral-900 mb-2">{{ product.name }}</h4>
                  <p class="text-sm text-neutral-600 mb-3">{{ product.category }}</p>
                  <div class="flex items-center justify-between mb-3">
                    <span class="text-xl font-bold text-primary-600">Tsh {{ product.price.toLocaleString() }}</span>
                    <div class="flex items-center text-sm text-neutral-500">
                      <span class="text-warning-500">★</span>
                      <span class="ml-1">{{ product.rating || 4.5 }}</span>
                    </div>
                  </div>
                  <div class="flex gap-2">
                    <button class="btn btn-primary btn-sm flex-1">
                      Add to Cart
                    </button>
                    <button class="btn btn-ghost btn-sm">
                      <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
                        <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                      </svg>
                    </button>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Trending in Your Categories -->
          <div>
            <h3 class="text-xl font-bold text-neutral-900 mb-4 flex items-center">
              <svg class="w-6 h-6 mr-2 text-warning-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7h8m0 0v8m0-8l-8 8-4-4-6 6"></path>
              </svg>
              Trending in Your Categories
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <div 
                v-for="product in trendingProducts" 
                :key="product.id"
                class="card card-interactive p-4"
              >
                <div class="flex gap-4">
                  <img 
                    :src="product.image" 
                    :alt="product.name"
                    class="w-20 h-20 object-cover rounded-lg"
                  >
                  <div class="flex-grow">
                    <h4 class="font-semibold text-neutral-900 text-sm mb-1 line-clamp-2">{{ product.name }}</h4>
                    <p class="text-primary-600 font-bold">Tsh {{ product.price.toLocaleString() }}</p>
                    <div class="flex items-center text-xs text-neutral-500 mt-1">
                      <span class="text-warning-500">★</span>
                      <span class="ml-1">{{ product.rating || 4.5 }}</span>
                      <span class="ml-1">({{ product.reviews || 23 }})</span>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- Frequently Bought Together -->
          <div>
            <h3 class="text-xl font-bold text-neutral-900 mb-4 flex items-center">
              <svg class="w-6 h-6 mr-2 text-success-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 20h5v-2a3 3 0 00-5.356-1.857M17 20H7m10 0v-2c0-.656-.126-1.283-.356-1.857M7 20H2v-2a3 3 0 015.356-1.857M7 20v-2c0-.656.126-1.283.356-1.857m0 0a5.002 5.002 0 019.288 0M15 7a3 3 0 11-6 0 3 3 0 016 0zm6 3a2 2 0 11-4 0 2 2 0 014 0zM7 10a2 2 0 11-4 0 2 2 0 014 0z"></path>
              </svg>
              Frequently Bought Together
            </h3>
            <div class="bg-gradient-to-r from-neutral-50 to-neutral-100 p-6 rounded-xl">
              <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                <div 
                  v-for="(bundle, index) in bundles" 
                  :key="index"
                  class="space-y-4"
                >
                  <div class="text-center">
                    <div class="text-sm font-medium text-neutral-600 mb-3">Bundle {{ index + 1 }}</div>
                    <div class="space-y-3">
                      <div 
                        v-for="product in bundle.products" 
                        :key="product.id"
                        class="flex items-center gap-3 bg-white p-3 rounded-lg"
                      >
                        <img 
                          :src="product.image" 
                          :alt="product.name"
                          class="w-12 h-12 object-cover rounded"
                        >
                        <div class="flex-grow">
                          <h5 class="font-medium text-sm text-neutral-900">{{ product.name }}</h5>
                          <p class="text-primary-600 font-bold text-sm">Tsh {{ product.price.toLocaleString() }}</p>
                        </div>
                      </div>
                    </div>
                    <div class="border-t pt-3 mt-3">
                      <div class="text-center">
                        <div class="text-sm text-neutral-500 line-through">Tsh {{ bundle.originalTotal.toLocaleString() }}</div>
                        <div class="text-xl font-bold text-success-600">Tsh {{ bundle.bundlePrice.toLocaleString() }}</div>
                        <div class="text-sm text-success-600">Save {{ bundle.discount }}%</div>
                        <button class="btn btn-primary btn-sm w-full mt-2">
                          Add Bundle to Cart
                        </button>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>

          <!-- New Arrivals -->
          <div>
            <h3 class="text-xl font-bold text-neutral-900 mb-4 flex items-center">
              <svg class="w-6 h-6 mr-2 text-error-600" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              New Arrivals
            </h3>
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
              <div 
                v-for="product in newArrivals" 
                :key="product.id"
                class="card card-interactive overflow-hidden"
              >
                <div class="relative">
                  <img 
                    :src="product.image" 
                    :alt="product.name"
                    class="w-full h-32 object-cover"
                  >
                  <span class="absolute top-2 right-2 badge badge-error">New</span>
                </div>
                <div class="p-4">
                  <h4 class="font-semibold text-neutral-900 text-sm mb-1">{{ product.name }}</h4>
                  <p class="text-primary-600 font-bold">Tsh {{ product.price.toLocaleString() }}</p>
                  <button class="btn btn-primary btn-sm w-full mt-2">
                    Add to Cart
                  </button>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'RecommendationsModal',
  props: {
    wishlist: {
      type: Array,
      default: () => []
    }
  },
  emits: ['close'],
  setup(props) {
    // Mock data - in a real app, this would come from an API
    const similarProducts = ref([
      {
        id: 1,
        name: 'iPhone 15 Pro Max',
        category: 'Smartphones',
        price: 2500000,
        image: '/images/iphone15.jpg',
        rating: 4.8,
        reviews: 156
      },
      {
        id: 2,
        name: 'Samsung Galaxy S24 Ultra',
        category: 'Smartphones',
        price: 2300000,
        image: '/images/s24.jpg',
        rating: 4.7,
        reviews: 203
      },
      {
        id: 3,
        name: 'MacBook Pro 16"',
        category: 'Laptops',
        price: 4500000,
        image: '/images/macbook.jpg',
        rating: 4.9,
        reviews: 89
      }
    ])

    const trendingProducts = ref([
      {
        id: 4,
        name: 'AirPods Pro 2',
        category: 'Accessories',
        price: 350000,
        image: '/images/airpods.jpg',
        rating: 4.6,
        reviews: 234
      },
      {
        id: 5,
        name: 'iPad Air',
        category: 'Tablets',
        price: 1200000,
        image: '/images/ipad.jpg',
        rating: 4.7,
        reviews: 167
      },
      {
        id: 6,
        name: 'Apple Watch Series 9',
        category: 'Accessories',
        price: 650000,
        image: '/images/watch.jpg',
        rating: 4.5,
        reviews: 298
      },
      {
        id: 7,
        name: 'Samsung Galaxy Tab S9',
        category: 'Tablets',
        price: 980000,
        image: '/images/tab.jpg',
        rating: 4.4,
        reviews: 145
      }
    ])

    const bundles = ref([
      {
        products: [
          {
            id: 8,
            name: 'iPhone 15',
            price: 1800000,
            image: '/images/iphone15.jpg'
          },
          {
            id: 9,
            name: 'AirPods Pro',
            price: 350000,
            image: '/images/airpods.jpg'
          },
          {
            id: 10,
            name: 'iPhone Case',
            price: 50000,
            image: '/images/case.jpg'
          }
        ],
        originalTotal: 2200000,
        bundlePrice: 1980000,
        discount: 10
      },
      {
        products: [
          {
            id: 11,
            name: 'MacBook Air',
            price: 2800000,
            image: '/images/macbook.jpg'
          },
          {
            id: 12,
            name: 'Magic Mouse',
            price: 250000,
            image: '/images/mouse.jpg'
          },
          {
            id: 13,
            name: 'Keyboard',
            price: 300000,
            image: '/images/keyboard.jpg'
          }
        ],
        originalTotal: 3350000,
        bundlePrice: 3015000,
        discount: 10
      },
      {
        products: [
          {
            id: 14,
            name: 'Samsung Galaxy S24',
            price: 1600000,
            image: '/images/s24.jpg'
          },
          {
            id: 15,
            name: 'Galaxy Buds Pro',
            price: 280000,
            image: '/images/buds.jpg'
          },
          {
            id: 16,
            name: 'Wireless Charger',
            price: 80000,
            image: '/images/charger.jpg'
          }
        ],
        originalTotal: 1960000,
        bundlePrice: 1764000,
        discount: 10
      }
    ])

    const newArrivals = ref([
      {
        id: 17,
        name: 'Google Pixel 8 Pro',
        price: 1900000,
        image: '/images/pixel.jpg'
      },
      {
        id: 18,
        name: 'OnePlus 12',
        price: 1400000,
        image: '/images/oneplus.jpg'
      },
      {
        id: 19,
        name: 'Xiaomi 14 Pro',
        price: 1100000,
        image: '/images/xiaomi.jpg'
      },
      {
        id: 20,
        name: 'Oppo Find X6',
        price: 1200000,
        image: '/images/oppo.jpg'
      }
    ])

    return {
      similarProducts,
      trendingProducts,
      bundles,
      newArrivals
    }
  }
}
</script>

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
