<template>
  <div class="product-card" :class="cardClasses">
    <div class="product-image-container">
      <img 
        :src="product.image" 
        :alt="product.name"
        class="product-image"
        @error="handleImageError"
      >
      <div class="product-badges">
        <span v-if="product.isNew" class="badge badge-new">New</span>
        <span v-if="product.discount" class="badge badge-discount">-{{ product.discount }}%</span>
      </div>
    </div>
    
    <div class="product-info">
      <h3 class="product-title">{{ product.name }}</h3>
      <p class="product-category">{{ product.category }}</p>
      <div class="product-price">
        <span v-if="product.discount" class="original-price">Tsh {{ product.price.toLocaleString() }}</span>
        <span class="current-price">Tsh {{ discountedPrice.toLocaleString() }}</span>
      </div>
    </div>
    
    <div class="product-actions">
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
        @click="$emit('toggle-wishlist', product)" 
        class="btn btn-secondary btn-sm"
        :class="{ 'text-red-500': isInWishlist }"
      >
        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24">
          <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
        </svg>
      </button>
      
      <button 
        @click="$emit('add-to-compare', product)" 
        class="btn btn-secondary btn-sm"
        :disabled="isInCompare"
      >
        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
        </svg>
      </button>
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
    wishlist: {
      type: Array,
      default: () => []
    },
    compareList: {
      type: Array,
      default: () => []
    }
  },
  emits: ['add-to-cart', 'toggle-wishlist', 'add-to-compare'],
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
    
    const isInWishlist = computed(() => {
      return props.wishlist.some(item => item.name === props.product.name)
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
    
    return {
      discountedPrice,
      inStock,
      isInWishlist,
      isInCompare,
      cardClasses,
      handleImageError
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
