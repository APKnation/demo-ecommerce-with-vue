<template>
  <div class="shopping-cart" :class="{ 'is-empty': isEmpty }">
    <div class="cart-header">
      <h2 class="cart-title">Shopping Cart</h2>
      <div class="cart-summary">
        <span class="item-count">{{ totalItems }} items</span>
        <span class="total-price">Tsh {{ totalPrice.toLocaleString() }}</span>
      </div>
    </div>
    
    <div v-if="isEmpty" class="cart-empty">
      <div class="empty-icon">
        <svg class="w-16 h-16 text-gray-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707 1.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
        </svg>
      </div>
      <h3 class="empty-title">Your cart is empty</h3>
      <p class="empty-message">Add some products to get started!</p>
      <button @click="$emit('continue-shopping')" class="btn btn-primary">
        Continue Shopping
      </button>
    </div>
    
    <div v-else class="cart-content">
      <div class="cart-items">
        <div 
          v-for="(item, index) in cartItems" 
          :key="index"
          class="cart-item"
        >
          <div class="item-image">
            <img :src="item.image || '/images/placeholder.jpg'" :alt="item.name">
          </div>
          
          <div class="item-details">
            <h4 class="item-name">{{ item.name }}</h4>
            <p class="item-price">Tsh {{ item.price.toLocaleString() }}</p>
            <div class="item-quantity">
              <button 
                @click="updateQuantity(index, -1)"
                class="quantity-btn"
                :disabled="item.quantity <= 1"
              >
                -
              </button>
              <span class="quantity-value">{{ item.quantity }}</span>
              <button 
                @click="updateQuantity(index, 1)"
                class="quantity-btn"
              >
                +
              </button>
            </div>
          </div>
          
          <div class="item-actions">
            <div class="item-total">
              Tsh {{ (item.price * item.quantity).toLocaleString() }}
            </div>
            <button 
              @click="removeItem(index)"
              class="remove-btn"
              title="Remove item"
            >
              <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16"></path>
              </svg>
            </button>
          </div>
        </div>
      </div>
      
      <div class="cart-footer">
        <div class="cart-totals">
          <div class="total-row">
            <span>Subtotal:</span>
            <span>Tsh {{ totalPrice.toLocaleString() }}</span>
          </div>
          <div class="total-row">
            <span>Tax (10%):</span>
            <span>Tsh {{ taxAmount.toLocaleString() }}</span>
          </div>
          <div class="total-row final-total">
            <span>Total:</span>
            <span>Tsh {{ finalTotal.toLocaleString() }}</span>
          </div>
        </div>
        
        <div class="cart-actions">
          <button 
            @click="$emit('clear-cart')"
            class="btn btn-secondary"
          >
            Clear Cart
          </button>
          <button 
            @click="$emit('checkout')"
            class="btn btn-primary"
            :disabled="isEmpty"
          >
            Proceed to Checkout
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'ShoppingCart',
  props: {
    cartItems: {
      type: Array,
      required: true
    }
  },
  emits: ['update-quantity', 'remove-item', 'clear-cart', 'checkout', 'continue-shopping'],
  setup(props, { emit }) {
    const isEmpty = computed(() => {
      return props.cartItems.length === 0
    })
    
    const totalItems = computed(() => {
      return props.cartItems.reduce((total, item) => total + item.quantity, 0)
    })
    
    const totalPrice = computed(() => {
      return props.cartItems.reduce((total, item) => total + (item.price * item.quantity), 0)
    })
    
    const taxAmount = computed(() => {
      return totalPrice.value * 0.1
    })
    
    const finalTotal = computed(() => {
      return totalPrice.value + taxAmount.value
    })
    
    const updateQuantity = (index, change) => {
      emit('update-quantity', { index, change })
    }
    
    const removeItem = (index) => {
      emit('remove-item', index)
    }
    
    return {
      isEmpty,
      totalItems,
      totalPrice,
      taxAmount,
      finalTotal,
      updateQuantity,
      removeItem
    }
  }
}
</script>

<style scoped>
.shopping-cart {
  @apply bg-white rounded-lg shadow-lg p-6 max-w-4xl mx-auto;
}

.is-empty {
  @apply text-center;
}

.cart-header {
  @apply flex justify-between items-center mb-6 pb-4 border-b border-gray-200;
}

.cart-title {
  @apply text-2xl font-bold text-gray-800;
}

.cart-summary {
  @apply text-right;
}

.item-count {
  @apply text-sm text-gray-600 block;
}

.total-price {
  @apply text-lg font-bold text-blue-600;
}

.cart-empty {
  @apply py-12;
}

.empty-icon {
  @apply flex justify-center mb-4;
}

.empty-title {
  @apply text-xl font-semibold text-gray-700 mb-2;
}

.empty-message {
  @apply text-gray-600 mb-6;
}

.cart-items {
  @apply space-y-4 mb-6;
}

.cart-item {
  @apply flex items-center gap-4 p-4 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors;
}

.item-image {
  @apply w-20 h-20 rounded-lg overflow-hidden flex-shrink-0;
}

.item-image img {
  @apply w-full h-full object-cover;
}

.item-details {
  @apply flex-1;
}

.item-name {
  @apply font-semibold text-gray-800 mb-1;
}

.item-price {
  @apply text-gray-600 mb-2;
}

.item-quantity {
  @apply flex items-center gap-2;
}

.quantity-btn {
  @apply w-8 h-8 rounded-full border border-gray-300 flex items-center justify-center hover:bg-gray-100 disabled:opacity-50 disabled:cursor-not-allowed;
}

.quantity-value {
  @apply font-semibold min-w-8 text-center;
}

.item-actions {
  @apply text-right;
}

.item-total {
  @apply font-bold text-lg mb-2;
}

.remove-btn {
  @apply text-red-500 hover:text-red-700 p-2 rounded-full hover:bg-red-50 transition-colors;
}

.cart-footer {
  @apply border-t border-gray-200 pt-6;
}

.cart-totals {
  @apply space-y-2 mb-6;
}

.total-row {
  @apply flex justify-between text-gray-700;
}

.final-total {
  @apply font-bold text-lg text-blue-600 pt-2 border-t border-gray-200;
}

.cart-actions {
  @apply flex gap-4 justify-end;
}
</style>
