<template>
  <div class="product-card card card-interactive overflow-hidden group w-full xs:w-full sm:w-full md:w-auto lg:w-auto" :class="cardClasses">
    <div class="relative overflow-hidden">
      <img 
        :src="product.image" 
        :alt="product.name"
        class="product-image w-full h-32 xs:h-32 sm:h-40 md:h-48 lg:h-56 object-cover group-hover:scale-105 transition-transform duration-300"
        @error="handleImageError"
      >
      <div class="absolute top-2 left-2 flex gap-2">
        <span v-if="product.isNew" class="badge badge-accent">New</span>
        <span v-if="product.discount" class="badge badge-error">-{{ product.discount }}%</span>
      </div>
      
      <!-- Quick Actions -->
      <div class="absolute top-2 right-2 flex flex-col gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
        <button 
          @click="$emit('add-to-compare', product)" 
          class="w-8 h-8 bg-white/90 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white transition-colors shadow-lg"
          :class="{ 'text-orange-500': isInCompareList }"
          :title="isInCompareList ? 'Remove from comparison' : 'Add to comparison'"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
          </svg>
        </button>
        
        <button 
          @click="$emit('quick-view', product)" 
          class="w-8 h-8 bg-white/90 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white transition-colors shadow-lg text-primary-600"
          title="Quick view"
        >
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"></path>
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M2.458 12C3.732 7.943 7.523 5 12 5c4.478 0 8.268 2.943 9.542 7-1.274 4.057-5.064 7-9.542 7-4.477 0-8.268-2.943-9.542-7z"></path>
          </svg>
        </button>
      </div>
    </div>
    
    <div class="p-4">
      <h3 class="product-title text-lg font-semibold text-neutral-900 mb-2">{{ product.title }}</h3>
      <p class="product-category text-sm text-neutral-500 mb-3">{{ product.category }}</p>
      <p class="product-description text-sm text-neutral-600 mb-4 line-clamp-2">{{ product.description }}</p>
      <div class="product-price mb-4">
        <span v-if="product.discount" class="original-price text-sm text-neutral-500 line-through mr-2">Tsh {{ product.price.toLocaleString() }}</span>
        <span class="current-price text-2xl font-bold text-primary-600">Tsh {{ discountedPrice.toLocaleString() }}</span>
      </div>
      
      <!-- Advanced Electronics Features -->
      <div class="advanced-features mb-4">
        <div class="flex items-center gap-2 text-xs text-neutral-500 mb-2">
          <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2m0 0l-2-2m2 0l2 2m0 0l-2-2"></path>
          </svg>
          <span>Premium Electronics</span>
        </div>
        <div class="flex flex-wrap gap-1">
          <span class="badge badge-accent text-xs">1 Year Warranty</span>
          <span class="badge badge-success text-xs">Professional Grade</span>
          <span class="badge badge-info text-xs">Advanced Tech</span>
        </div>
      </div>
      
      <div class="flex items-center justify-between">
        <div class="flex items-center text-sm text-neutral-500">
          <span class="text-warning-500">★</span>
          <span class="ml-1">{{ product.rating || 4.5 }}</span>
          <span class="ml-1">({{ product.reviews || 23 }})</span>
        </div>
        <div class="flex gap-2">
          <button 
            @click="$emit('add-to-cart', product)" 
            class="btn btn-primary btn-sm"
            :disabled="!inStock"
          >
            <svg class="w-4 h-4 mr-1" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
            </svg>
            {{ inStock ? 'Add to Cart' : 'Out of Stock' }}
          </button>
          
          <button 
            @click="likeProduct" 
            class="btn btn-ghost btn-sm text-red-500 hover:text-red-600"
          >
            <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
              <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
            </svg>
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'ProductCard',
  props: {
    product: {
      type: Object,
      required: true
    },
    compareList: {
      type: Array,
      default: () => []
    }
  },
  emits: ['add-to-cart', 'add-to-compare', 'quick-view', 'select-all-products'],
  setup(props) {
    const discountedPrice = computed(() => {
      if (props.product.discount) {
        return props.product.price * (1 - props.product.discount / 100)
      }
      return props.product.price
    })
    
    const inStock = computed(() => {
      return props.product.stock !== undefined ? props.product.stock > 0 : true
    })
    
    const isInCompare = computed(() => {
      return props.compareList.some(item => item.name === props.product.name)
    })
    
    const cardClasses = computed(() => {
      return {
        'out-of-stock': !inStock.value,
        'has-discount': props.product.discount
      }
    })
    
    const handleImageError = (event) => {
      event.target.src = '/images/placeholder.jpg'
    }
    
    const likeProduct = () => {
      // Simple like function without wishlist
    }
    
    return {
      discountedPrice,
      inStock,
      isInCompareList: isInCompare,
      cardClasses,
      handleImageError,
      likeProduct
    }
  }
}
</script>

<style scoped>
.product-card {
  @apply bg-white rounded-lg shadow-md hover:shadow-xl transition-all duration-300 overflow-hidden;
}

.product-image-container {
  @apply relative h-48 overflow-hidden;
}

.product-image {
  @apply w-full h-full object-cover transition-transform duration-300;
}

.product-card:hover .product-image {
  @apply scale-110;
}

.product-badges {
  @apply absolute top-2 left-2 flex flex-col gap-1;
}

.badge {
  @apply px-2 py-1 text-xs font-semibold rounded-full;
}

.badge-new {
  @apply bg-green-500 text-white;
}

.badge-discount {
  @apply bg-red-500 text-white;
}

.product-info {
  @apply p-4;
}

.product-title {
  @apply text-lg font-semibold text-gray-800 mb-1;
}

.product-category {
  @apply text-sm text-gray-600 mb-2;
}

.product-price {
  @apply flex items-center gap-2;
}

.original-price {
  @apply text-sm text-gray-500 line-through;
}

.current-price {
  @apply text-lg font-bold text-blue-600;
}

.product-actions {
  @apply p-4 flex gap-2 border-t border-gray-100;
}

.btn-sm {
  @apply px-3 py-2 text-sm;
}

.out-of-stock {
  @apply opacity-75;
}

.has-discount .current-price {
  @apply text-red-600;
}
</style>
