<template>
  <div class="card card-interactive p-6">
    <div class="flex gap-6">
      <!-- Checkbox -->
      <div class="flex items-start pt-2">
        <input 
          :checked="selected"
          @change="$emit('toggle-select', product.id)"
          type="checkbox"
          class="w-5 h-5 text-primary-600 border-neutral-300 rounded focus:ring-primary-500"
        >
      </div>

      <!-- Product Image -->
      <div class="flex-shrink-0">
        <img 
          :src="product.image" 
          :alt="product.name"
          class="w-32 h-32 object-cover rounded-lg"
        >
      </div>

      <!-- Product Details -->
      <div class="flex-grow">
        <div class="flex items-start justify-between">
          <div class="flex-grow">
            <h3 class="text-xl font-semibold text-neutral-900 mb-2">{{ product.name }}</h3>
            <p class="text-neutral-600 mb-3">{{ product.category }}</p>
            
            <!-- Rating and Reviews -->
            <div class="flex items-center text-sm text-neutral-500 mb-3">
              <span class="text-warning-500">★</span>
              <span class="ml-1">{{ product.rating || 4.5 }}</span>
              <span class="ml-1">({{ product.reviews || 23 }} reviews)</span>
            </div>

            <!-- Features -->
            <div v-if="product.features" class="mb-3">
              <div class="flex flex-wrap gap-2">
                <span 
                  v-for="feature in product.features.slice(0, 3)" 
                  :key="feature"
                  class="text-xs bg-neutral-100 text-neutral-700 px-2 py-1 rounded-full"
                >
                  {{ feature }}
                </span>
                <span v-if="product.features.length > 3" class="text-xs text-neutral-500">
                  +{{ product.features.length - 3 }} more
                </span>
              </div>
            </div>
          </div>

          <!-- Price and Actions -->
          <div class="text-right">
            <!-- Price -->
            <div class="mb-4">
              <div v-if="product.discount" class="text-lg text-neutral-500 line-through">
                Tsh {{ product.price.toLocaleString() }}
              </div>
              <div class="text-2xl font-bold text-primary-600">
                Tsh {{ discountedPrice.toLocaleString() }}
              </div>
              <div v-if="product.discount" class="text-sm text-success-600">
                Save {{ product.discount }}%
              </div>
            </div>

            <!-- Stock Status -->
            <div class="mb-4">
              <span 
                :class="product.inStock ? 'text-success-600' : 'text-error-600'"
                class="text-sm font-medium"
              >
                {{ product.inStock ? '✓ In Stock' : '✗ Out of Stock' }}
              </span>
            </div>

            <!-- Action Buttons -->
            <div class="flex gap-2">
              <button 
                @click="$emit('add-to-cart', product)"
                class="btn btn-primary btn-sm"
                :disabled="!product.inStock"
              >
                {{ product.inStock ? 'Add to Cart' : 'Out of Stock' }}
              </button>
              
              <button 
                @click="$emit('remove', product)"
                class="btn btn-ghost btn-sm text-error-600 hover:text-error-700"
              >
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
                </svg>
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
    </div>
  </div>
</template>

<script>
export default {
  name: 'WishlistProductListItem',
  props: {
    product: {
      type: Object,
      required: true
    },
    selected: {
      type: Boolean,
      default: false
    }
  },
  emits: ['toggle-select', 'remove', 'add-to-cart'],
  computed: {
    discountedPrice() {
      if (this.product.discount) {
        return this.product.price * (1 - this.product.discount / 100)
      }
      return this.product.price
    }
  }
}
</script>
