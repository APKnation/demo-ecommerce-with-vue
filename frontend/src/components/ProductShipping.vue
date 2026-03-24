<template>
  <div class="product-shipping">
    <h3 class="shipping-title">Shipping & Returns</h3>
    
    <div class="shipping-sections">
      <!-- Shipping Information -->
      <div class="shipping-section">
        <h4 class="section-title">Shipping Options</h4>
        <div class="shipping-options">
          <div class="shipping-option">
            <div class="option-header">
              <div class="option-icon">🚚</div>
              <div class="option-info">
                <h5>Standard Delivery</h5>
                <p>2-5 business days</p>
              </div>
              <div class="option-price">
                {{ getShippingPrice('standard') }}
              </div>
            </div>
            <p class="option-description">
              Regular delivery service to your address. Available nationwide.
            </p>
          </div>
          
          <div class="shipping-option">
            <div class="option-header">
              <div class="option-icon">⚡</div>
              <div class="option-info">
                <h5>Express Delivery</h5>
                <p>1-2 business days</p>
              </div>
              <div class="option-price">
                {{ getShippingPrice('express') }}
              </div>
            </div>
            <p class="option-description">
              Fast delivery service for urgent orders. Available in major cities.
            </p>
          </div>
          
          <div class="shipping-option">
            <div class="option-header">
              <div class="option-icon">🏪</div>
              <div class="option-info">
                <h5>Store Pickup</h5>
                <p>Same day</p>
              </div>
              <div class="option-price">
                FREE
              </div>
            </div>
            <p class="option-description">
              Pick up your order from our store. No shipping charges.
            </p>
          </div>
        </div>
      </div>
      
      <!-- Free Shipping Info -->
      <div v-if="hasFreeShipping" class="free-shipping-info">
        <div class="free-shipping-banner">
          <div class="free-shipping-icon">🎉</div>
          <div class="free-shipping-text">
            <h5>FREE Shipping Available!</h5>
            <p>Orders over Tsh {{ freeShippingThreshold.toLocaleString() }} qualify for free shipping</p>
          </div>
        </div>
      </div>
      
      <!-- Delivery Areas -->
      <div class="shipping-section">
        <h4 class="section-title">Delivery Areas</h4>
        <div class="delivery-areas">
          <div class="area-group">
            <h5>Dar es Salaam</h5>
            <p>1-2 business days • Tsh 5,000</p>
            <ul class="area-list">
              <li>Kinondoni, Ilala, Temeke, Ubungo</li>
            </ul>
          </div>
          
          <div class="area-group">
            <h5>Major Cities</h5>
            <p>2-3 business days • Tsh 8,000</p>
            <ul class="area-list">
              <li>Arusha, Mwanza, Dodoma, Mbeya, Tanga, Morogoro</li>
            </ul>
          </div>
          
          <div class="area-group">
            <h5>Other Regions</h5>
            <p>3-5 business days • Tsh 12,000</p>
            <ul class="area-list">
              <li>All other regions in Tanzania</li>
            </ul>
          </div>
        </div>
      </div>
      
      <!-- Return Policy -->
      <div class="shipping-section">
        <h4 class="section-title">Return Policy</h4>
        <div class="return-policy">
          <div class="policy-item">
            <div class="policy-icon">↩️</div>
            <div class="policy-content">
              <h5>30-Day Return Policy</h5>
              <p>Return within 30 days of purchase for a full refund or exchange.</p>
            </div>
          </div>
          
          <div class="policy-item">
            <div class="policy-icon">📦</div>
            <div class="policy-content">
              <h5>Product Condition</h5>
              <p>Product must be unused and in original packaging with all accessories.</p>
            </div>
          </div>
          
          <div class="policy-item">
            <div class="policy-icon">🚫</div>
            <div class="policy-content">
              <h5>Non-Returnable Items</h5>
              <p>Software, downloadable products, and personalized items cannot be returned.</p>
            </div>
          </div>
          
          <div class="policy-item">
            <div class="policy-icon">💰</div>
            <div class="policy-content">
              <h5>Refund Process</h5>
              <p>Refunds processed within 5-7 business days after product inspection.</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- Warranty Information -->
      <div class="shipping-section">
        <h4 class="section-title">Warranty</h4>
        <div class="warranty-info">
          <div class="warranty-item">
            <div class="warranty-icon">🛡️</div>
            <div class="warranty-content">
              <h5>Manufacturer Warranty</h5>
              <p>{{ product.warranty || '1 year' }} manufacturer warranty covering defects.</p>
            </div>
          </div>
          
          <div class="warranty-item">
            <div class="warranty-icon">🔧</div>
            <div class="warranty-content">
              <h5>Service Centers</h5>
              <p>Authorized service centers available nationwide for repairs and maintenance.</p>
            </div>
          </div>
          
          <div class="warranty-item">
            <div class="warranty-icon">📞</div>
            <div class="warranty-content">
              <h5>Support</h5>
              <p>24/7 customer support for warranty claims and technical assistance.</p>
            </div>
          </div>
        </div>
      </div>
      
      <!-- International Shipping -->
      <div class="shipping-section">
        <h4 class="section-title">International Shipping</h4>
        <div class="international-shipping">
          <div class="international-item">
            <div class="international-icon">🌍</div>
            <div class="international-content">
              <h5>East Africa</h5>
              <p>Kenya, Uganda, Rwanda, Burundi • 5-7 days • Tsh 25,000</p>
            </div>
          </div>
          
          <div class="international-item">
            <div class="international-icon">✈️</div>
            <div class="international-content">
              <h5>International</h5>
              <p>Other countries • 7-14 days • Tsh 50,000</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'
import { shippingCalculator } from '../utils/shipping.js'

export default {
  name: 'ProductShipping',
  props: {
    product: {
      type: Object,
      required: true
    }
  },
  setup(props) {
    const freeShippingThreshold = 50000 // Tsh 50,000 for free shipping
    
    const hasFreeShipping = computed(() => {
      return props.product.price >= freeShippingThreshold
    })
    
    const getShippingPrice = (method) => {
      // Calculate shipping for Dar es Salaam as default
      const shipping = shippingCalculator.calculateShipping({
        region: 'dar_es_salaam',
        cartTotal: props.product.price,
        products: [props.product],
        method: method
      })
      
      return shipping.freeShipping ? 'FREE' : `Tsh ${shipping.totalCost.toLocaleString()}`
    }
    
    return {
      hasFreeShipping,
      freeShippingThreshold,
      getShippingPrice
    }
  }
}
</script>

<style scoped>
.product-shipping {
  @apply space-y-8;
}

.shipping-title {
  @apply text-2xl font-bold text-gray-900 mb-6;
}

.shipping-sections {
  @apply space-y-8;
}

.shipping-section {
  @apply space-y-4;
}

.section-title {
  @apply text-lg font-semibold text-gray-800 border-b border-gray-200 pb-2;
}

.shipping-options {
  @apply space-y-4;
}

.shipping-option {
  @apply bg-gray-50 rounded-lg p-4;
}

.option-header {
  @apply flex items-center gap-4 mb-2;
}

.option-icon {
  @apply text-2xl;
}

.option-info {
  @apply flex-1;
}

.option-info h5 {
  @apply font-semibold text-gray-900;
}

.option-info p {
  @apply text-sm text-gray-600;
}

.option-price {
  @apply font-semibold text-blue-600;
}

.option-description {
  @apply text-sm text-gray-700;
}

.free-shipping-info {
  @apply mt-6;
}

.free-shipping-banner {
  @apply bg-green-50 border border-green-200 rounded-lg p-4 flex items-center gap-4;
}

.free-shipping-icon {
  @apply text-2xl;
}

.free-shipping-text h5 {
  @apply font-semibold text-green-800;
}

.free-shipping-text p {
  @apply text-sm text-green-700;
}

.delivery-areas {
  @apply grid grid-cols-1 md:grid-cols-3 gap-4;
}

.area-group {
  @apply bg-gray-50 rounded-lg p-4;
}

.area-group h5 {
  @apply font-semibold text-gray-900 mb-1;
}

.area-group p {
  @apply text-sm text-blue-600 mb-2;
}

.area-list {
  @apply list-disc list-inside text-sm text-gray-700 space-y-1;
}

.return-policy {
  @apply space-y-4;
}

.policy-item {
  @apply flex items-start gap-4 bg-gray-50 rounded-lg p-4;
}

.policy-icon {
  @apply text-2xl;
}

.policy-content h5 {
  @apply font-semibold text-gray-900 mb-1;
}

.policy-content p {
  @apply text-sm text-gray-700;
}

.warranty-info {
  @apply space-y-4;
}

.warranty-item {
  @apply flex items-start gap-4 bg-gray-50 rounded-lg p-4;
}

.warranty-icon {
  @apply text-2xl;
}

.warranty-content h5 {
  @apply font-semibold text-gray-900 mb-1;
}

.warranty-content p {
  @apply text-sm text-gray-700;
}

.international-shipping {
  @apply space-y-4;
}

.international-item {
  @apply flex items-start gap-4 bg-gray-50 rounded-lg p-4;
}

.international-icon {
  @apply text-2xl;
}

.international-content h5 {
  @apply font-semibold text-gray-900 mb-1;
}

.international-content p {
  @apply text-sm text-gray-700;
}

@media (max-width: 768px) {
  .delivery-areas {
    @apply grid-cols-1;
  }
  
  .option-header {
    @apply flex-col items-start gap-2;
  }
  
  .policy-item, .warranty-item, .international-item {
    @apply flex-col items-start gap-2;
  }
}
</style>
