<template>
  <div v-if="showModal" class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
    <div 
      class="bg-white rounded-2xl shadow-2xl max-w-4xl w-full max-h-[90vh] overflow-hidden"
      @click.stop
    >
      <!-- Modal Header -->
      <div class="sticky top-0 bg-white border-b border-neutral-200 p-6 z-10">
        <div class="flex items-center justify-between">
          <h2 class="text-2xl font-bold text-neutral-900">Quick View</h2>
          <button 
            @click="closeModal"
            class="btn btn-ghost btn-sm"
          >
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Modal Content -->
      <div class="p-6 overflow-auto max-h-[calc(90vh-120px)]">
        <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
          <!-- Product Images -->
          <div class="space-y-4">
            <div class="relative overflow-hidden rounded-lg">
              <img 
                :src="selectedImage || product.image" 
                :alt="product.name"
                class="w-full h-80 object-cover"
              >
              <div class="absolute top-2 left-2 flex gap-2">
                <span v-if="product.isNew" class="badge badge-accent">New</span>
                <span v-if="product.discount" class="badge badge-error">-{{ product.discount }}%</span>
              </div>
            </div>
            
            <!-- Thumbnail Gallery -->
            <div class="flex gap-2 overflow-x-auto">
              <img 
                v-for="(image, index) in product.images || [product.image]" 
                :key="index"
                :src="image"
                :alt="`${product.name} ${index + 1}`"
                class="w-20 h-20 object-cover rounded-lg cursor-pointer border-2 transition-colors"
                :class="selectedImage === image ? 'border-primary-500' : 'border-neutral-200'"
                @click="selectedImage = image"
              >
            </div>
          </div>

          <!-- Product Details -->
          <div class="space-y-6">
            <!-- Basic Info -->
            <div>
              <h3 class="text-2xl font-bold text-neutral-900 mb-2">{{ product.name }}</h3>
              <p class="text-neutral-600 mb-4">{{ product.description }}</p>
              
              <!-- Rating -->
              <div class="flex items-center gap-4 mb-4">
                <div class="flex items-center">
                  <span class="text-warning-500">★</span>
                  <span class="ml-1 font-semibold">{{ product.rating || 4.5 }}</span>
                  <span class="ml-1 text-neutral-500">({{ product.reviews || 23 }} reviews)</span>
                </div>
                <span class="text-neutral-400">|</span>
                <span class="text-neutral-600">{{ product.category }}</span>
              </div>

              <!-- Price -->
              <div class="flex items-center gap-4 mb-6">
                <div class="flex items-baseline">
                  <span v-if="product.discount" class="text-lg text-neutral-500 line-through mr-2">
                    Tsh {{ product.price.toLocaleString() }}
                  </span>
                  <span class="text-3xl font-bold text-primary-600">
                    Tsh {{ discountedPrice.toLocaleString() }}
                  </span>
                </div>
                <span v-if="product.discount" class="badge badge-success">Save {{ product.discount }}%</span>
              </div>

              <!-- Availability -->
              <div class="mb-6">
                <span 
                  :class="product.inStock ? 'text-success-600' : 'text-error-600'"
                  class="font-medium"
                >
                  {{ product.inStock ? '✓ In Stock' : '✗ Out of Stock' }}
                </span>
                <span v-if="product.inStock" class="text-neutral-500 ml-2">
                  (Usually ships within 24 hours)
                </span>
              </div>
            </div>

            <!-- Key Specifications -->
            <div v-if="product.specifications" class="space-y-3">
              <h4 class="font-semibold text-neutral-900 mb-3">Key Specifications</h4>
              <div class="grid grid-cols-2 gap-3">
                <div 
                  v-for="(value, key, index) in getTopSpecifications(product.specifications)" 
                  :key="index"
                  class="flex justify-between py-2 border-b border-neutral-100"
                >
                  <span class="text-sm text-neutral-600 capitalize">{{ formatSpecName(key) }}</span>
                  <span class="text-sm font-medium text-neutral-900">{{ value }}</span>
                </div>
              </div>
            </div>

            <!-- Actions -->
            <div class="space-y-4">
              <div class="flex gap-3">
                <button 
                  @click="addToCart(product)"
                  class="btn btn-primary flex-1"
                  :disabled="!product.inStock"
                >
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4 8H5.4M7 13l2.293 2.293c.63.63.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                  </svg>
                  {{ product.inStock ? 'Add to Cart' : 'Out of Stock' }}
                </button>
                
                <button 
                  @click="toggleWishlist(product)"
                  class="btn btn-ghost"
                  :class="{ 'text-red-500': isInWishlist(product) }"
                >
                  <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                  </svg>
                </button>
              </div>

              <div class="flex gap-3">
                <button 
                  @click="addToCompare(product)"
                  class="btn btn-outline flex-1"
                >
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
                  </svg>
                  Compare
                </button>
                
                <router-link 
                  :to="`/product/${product.id}`"
                  class="btn btn-secondary flex-1"
                  @click="closeModal"
                >
                  <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
                  </svg>
                  View Details
                </router-link>
              </div>
            </div>

            <!-- Features -->
            <div v-if="product.features" class="space-y-2">
              <h4 class="font-semibold text-neutral-900 mb-3">Features</h4>
              <div class="space-y-2">
                <div 
                  v-for="feature in product.features" 
                  :key="feature"
                  class="flex items-center text-sm text-neutral-600"
                >
                  <svg class="w-4 h-4 text-success-500 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path>
                  </svg>
                  {{ feature }}
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
import { useCart } from '@/composables/useCart'
import { useWishlist } from '@/composables/useWishlist'
import { useProductComparison } from '@/composables/useProductComparison'

export default {
  name: 'QuickViewModal',
  props: {
    product: {
      type: Object,
      required: true
    },
    showModal: {
      type: Boolean,
      default: false
    }
  },
  emits: ['close'],
  setup(props, { emit }) {
    const selectedImage = ref('')
    const { addToCart } = useCart()
    const { toggleWishlist, isInWishlist } = useWishlist()
    const { addToCompare } = useProductComparison()

    const discountedPrice = computed(() => {
      if (props.product.discount) {
        return props.product.price * (1 - props.product.discount / 100)
      }
      return props.product.price
    })

    const getTopSpecifications = (specifications) => {
      const specs = Object.entries(specifications)
      return specs.slice(0, 4).reduce((acc, [key, value]) => {
        acc[key] = value
        return acc
      }, {})
    }

    const formatSpecName = (spec) => {
      return spec.replace(/_/g, ' ')
    }

    const closeModal = () => {
      emit('close')
    }

    return {
      selectedImage,
      discountedPrice,
      getTopSpecifications,
      formatSpecName,
      closeModal,
      addToCart,
      toggleWishlist,
      isInWishlist,
      addToCompare
    }
  },
  watch: {
    'product.image': {
      immediate: true,
      handler(newImage) {
        this.selectedImage = newImage
      }
    }
  }
}
</script>
