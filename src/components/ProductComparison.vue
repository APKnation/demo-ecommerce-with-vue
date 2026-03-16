<template>
  <div class="product-comparison">
    <!-- Comparison Bar -->
    <div v-if="compareList.length > 0" class="fixed bottom-0 left-0 right-0 bg-white border-t border-neutral-200 shadow-lg z-40">
      <div class="container py-4">
        <div class="flex items-center justify-between">
          <div class="flex items-center gap-4">
            <span class="text-sm font-medium text-neutral-700">
              {{ compareList.length }} product{{ compareList.length !== 1 ? 's' : '' }} to compare
            </span>
            <div class="flex gap-2">
              <div 
                v-for="product in compareList" 
                :key="product.id"
                class="relative"
              >
                <img 
                  :src="product.image" 
                  :alt="product.name"
                  class="w-12 h-12 object-cover rounded-lg border border-neutral-300"
                >
                <button 
                  @click="removeFromCompare(product)"
                  class="absolute -top-2 -right-2 w-5 h-5 bg-error-500 text-white rounded-full flex items-center justify-center hover:bg-error-600 transition-colors"
                >
                  <svg class="w-3 h-3" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
                  </svg>
                </button>
              </div>
            </div>
          </div>
          <div class="flex gap-3">
            <button 
              @click="clearCompareList"
              class="btn btn-ghost btn-sm"
            >
              Clear All
            </button>
            <button 
              @click="showComparisonModal = true"
              class="btn btn-primary btn-sm"
              :disabled="compareList.length < 2"
            >
              Compare Products
            </button>
          </div>
        </div>
      </div>
    </div>

    <!-- Comparison Modal -->
    <div 
      v-if="showComparisonModal" 
      class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4"
      @click="closeComparisonModal"
    >
      <div 
        class="bg-white rounded-2xl shadow-2xl max-w-7xl w-full max-h-[90vh] overflow-hidden"
        @click.stop
      >
        <!-- Modal Header -->
        <div class="sticky top-0 bg-white border-b border-neutral-200 p-6 z-10">
          <div class="flex items-center justify-between">
            <h2 class="text-2xl font-bold text-neutral-900">Product Comparison</h2>
            <button 
              @click="closeComparisonModal"
              class="btn btn-ghost btn-sm"
            >
              <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
              </svg>
            </button>
          </div>
        </div>

        <!-- Comparison Content -->
        <div class="p-6 overflow-auto max-h-[calc(90vh-120px)]">
          <div class="overflow-x-auto">
            <table class="w-full">
              <!-- Product Headers -->
              <thead>
                <tr>
                  <th class="text-left p-4 font-semibold text-neutral-900 border-b border-neutral-200">
                    Features
                  </th>
                  <th 
                    v-for="product in compareList" 
                    :key="product.id"
                    class="p-4 border-b border-neutral-200"
                  >
                    <div class="text-center">
                      <img 
                        :src="product.image" 
                        :alt="product.name"
                        class="w-24 h-24 object-cover rounded-lg mx-auto mb-3"
                      >
                      <h3 class="font-semibold text-neutral-900 text-sm mb-1">{{ product.name }}</h3>
                      <p class="text-primary-600 font-bold text-lg">Tsh {{ formatPrice(product.price) }}</p>
                      <div class="flex items-center justify-center gap-1 mt-2">
                        <span class="text-warning-500">★</span>
                        <span class="text-sm text-neutral-600">{{ product.rating || 4.5 }}</span>
                      </div>
                    </div>
                  </th>
                </tr>
              </thead>

              <!-- Product Details -->
              <tbody>
                <!-- Basic Info -->
                <tr>
                  <td class="p-4 font-medium text-neutral-700 border-b border-neutral-100">Category</td>
                  <td 
                    v-for="product in compareList" 
                    :key="`cat-${product.id}`"
                    class="p-4 text-center border-b border-neutral-100"
                  >
                    {{ product.category }}
                  </td>
                </tr>

                <!-- Specifications -->
                <template v-for="spec in getAllSpecifications()" :key="spec">
                  <tr>
                    <td class="p-4 font-medium text-neutral-700 border-b border-neutral-100 capitalize">
                      {{ formatSpecName(spec) }}
                    </td>
                    <td 
                      v-for="product in compareList" 
                      :key="`${spec}-${product.id}`"
                      class="p-4 text-center border-b border-neutral-100"
                    >
                      {{ getSpecificationValue(product, spec) || '-' }}
                    </td>
                  </tr>
                </template>

                <!-- Features -->
                <tr>
                  <td class="p-4 font-medium text-neutral-700 border-b border-neutral-100">Features</td>
                  <td 
                    v-for="product in compareList" 
                    :key="`features-${product.id}`"
                    class="p-4 border-b border-neutral-100"
                  >
                    <div class="space-y-1">
                      <div 
                        v-for="feature in (product.features || [])" 
                        :key="feature"
                        class="text-sm text-neutral-600 text-center"
                      >
                        ✓ {{ feature }}
                      </div>
                    </div>
                  </td>
                </tr>

                <!-- Availability -->
                <tr>
                  <td class="p-4 font-medium text-neutral-700 border-b border-neutral-100">Availability</td>
                  <td 
                    v-for="product in compareList" 
                    :key="`stock-${product.id}`"
                    class="p-4 text-center border-b border-neutral-100"
                  >
                    <span 
                      :class="product.inStock ? 'text-success-600' : 'text-error-600'"
                      class="font-medium"
                    >
                      {{ product.inStock ? 'In Stock' : 'Out of Stock' }}
                    </span>
                  </td>
                </tr>

                <!-- Actions -->
                <tr>
                  <td class="p-4 font-medium text-neutral-700">Actions</td>
                  <td 
                    v-for="product in compareList" 
                    :key="`actions-${product.id}`"
                    class="p-4"
                  >
                    <div class="flex flex-col gap-2">
                      <button 
                        @click="addToCart(product)"
                        class="btn btn-primary btn-sm w-full"
                        :disabled="!product.inStock"
                      >
                        {{ product.inStock ? 'Add to Cart' : 'Out of Stock' }}
                      </button>
                      <button 
                        @click="removeFromCompare(product)"
                        class="btn btn-ghost btn-sm w-full"
                      >
                        Remove
                      </button>
                    </div>
                  </td>
                </tr>
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'
import { useCart } from '@/composables/useCart'

export default {
  name: 'ProductComparison',
  props: {
    compareList: {
      type: Array,
      default: () => []
    }
  },
  emits: ['remove-from-compare', 'clear-compare'],
  setup(props, { emit }) {
    const showComparisonModal = ref(false)
    const { addToCart } = useCart()

    const removeFromCompare = (product) => {
      emit('remove-from-compare', product)
    }

    const clearCompareList = () => {
      emit('clear-compare')
    }

    const closeComparisonModal = () => {
      showComparisonModal.value = false
    }

    const getAllSpecifications = () => {
      const specs = new Set()
      props.compareList.forEach(product => {
        if (product.specifications) {
          Object.keys(product.specifications).forEach(spec => specs.add(spec))
        }
      })
      return Array.from(specs)
    }

    const formatSpecName = (spec) => {
      return spec.replace(/_/g, ' ')
    }

    const getSpecificationValue = (product, spec) => {
      return product.specifications?.[spec] || null
    }

    const formatPrice = (price) => {
      return price.toLocaleString()
    }

    return {
      showComparisonModal,
      removeFromCompare,
      clearCompareList,
      closeComparisonModal,
      getAllSpecifications,
      formatSpecName,
      getSpecificationValue,
      formatPrice,
      addToCart
    }
  }
}
</script>
