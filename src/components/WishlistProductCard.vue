<template>
  <div class="card card-interactive overflow-hidden group">
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
          :checked="selected"
          @change="$emit('toggle-select', product.id)"
          type="checkbox"
          class="w-5 h-5 text-primary-600 border-neutral-300 rounded focus:ring-primary-500"
        >
      </div>

      <!-- Quick Actions -->
      <div class="absolute top-2 right-2 flex flex-col gap-2 opacity-0 group-hover:opacity-100 transition-opacity duration-200">
        <button 
          @click="$emit('remove', product)"
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
      <h3 class="product-title text-lg font-semibold text-neutral-900 mb-2 line-clamp-2">{{ product.name }}</h3>
      <p class="product-category text-sm text-neutral-500 mb-3">{{ product.category }}</p>
      
      <!-- Price -->
      <div class="product-price mb-4">
        <span v-if="product.discount" class="text-lg text-neutral-500 line-through mr-2">Tsh {{ product.price.toLocaleString() }}</span>
        <span class="text-2xl font-bold text-primary-600">Tsh {{ discountedPrice.toLocaleString() }}</span>
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
          @click="$emit('add-to-cart', product)"
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
</template>

<script>
export default {
  name: 'WishlistProductCard',
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

<style scoped>
.line-clamp-2 {
  display: -webkit-box;
  -webkit-line-clamp: 2;
  -webkit-box-orient: vertical;
  overflow: hidden;
}
</style>
