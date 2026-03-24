<template>
  <div class="shipping-calculator">
    <!-- Shipping Calculator Header -->
    <div class="shipping-header">
      <h3 class="shipping-title">Calculate Shipping</h3>
      <p class="shipping-description">Get accurate shipping costs for your order</p>
    </div>
    
    <!-- Shipping Form -->
    <div class="shipping-form">
      <!-- Region Selection -->
      <div class="form-group">
        <label class="form-label">Delivery Region *</label>
        <select 
          v-model="selectedRegion" 
          @change="calculateShipping"
          class="form-select"
          :class="{ 'has-error': errors.region }"
        >
          <option value="">Select your region</option>
          <optgroup 
            v-for="zone in shippingZones" 
            :key="zone.key" 
            :label="zone.name"
          >
            <option 
              v-for="region in getRegionsByZone(zone.key)"
              :key="region.code"
              :value="region.code"
            >
              {{ region.name }}
            </option>
          </optgroup>
        </select>
        <span v-if="errors.region" class="form-error">{{ errors.region }}</span>
      </div>
      
      <!-- Shipping Method -->
      <div class="form-group">
        <label class="form-label">Shipping Method</label>
        <div class="shipping-methods">
          <div 
            v-for="method in shippingMethods" 
            :key="method.key"
            class="method-option"
            :class="{ 'is-selected': selectedMethod === method.key }"
            @click="selectShippingMethod(method.key)"
          >
            <div class="method-info">
              <div class="method-name">{{ method.name }}</div>
              <div class="method-description">{{ method.description }}</div>
            </div>
            <div class="method-price">
              {{ getMethodPrice(method.key) }}
            </div>
          </div>
        </div>
      </div>
      
      <!-- Address Form -->
      <div v-if="selectedRegion" class="address-form">
        <h4 class="address-title">Delivery Address</h4>
        
        <div class="form-row">
          <div class="form-group">
            <label class="form-label">City/Area *</label>
            <input 
              v-model="address.city"
              type="text"
              class="form-input"
              placeholder="e.g. Kinondoni, Mwenge"
              :class="{ 'has-error': errors.city }"
            >
            <span v-if="errors.city" class="form-error">{{ errors.city }}</span>
          </div>
          
          <div class="form-group">
            <label class="form-label">Postal Code</label>
            <input 
              v-model="address.postalCode"
              type="text"
              class="form-input"
              placeholder="e.g. 11000"
            >
          </div>
        </div>
        
        <div class="form-group">
          <label class="form-label">Street Address *</label>
          <textarea 
            v-model="address.street"
            class="form-textarea"
            rows="3"
            placeholder="Enter your complete street address"
            :class="{ 'has-error': errors.street }"
          ></textarea>
          <span v-if="errors.street" class="form-error">{{ errors.street }}</span>
        </div>
        
        <div class="form-group">
          <label class="form-label">Phone Number *</label>
          <input 
            v-model="address.phone"
            type="tel"
            class="form-input"
            placeholder="e.g. +255 712 345 678"
            :class="{ 'has-error': errors.phone }"
          >
          <span v-if="errors.phone" class="form-error">{{ errors.phone }}</span>
        </div>
      </div>
    </div>
    
    <!-- Shipping Results -->
    <div v-if="shippingResult" class="shipping-results">
      <div class="result-header">
        <h4>Shipping Summary</h4>
        <span class="delivery-time">{{ shippingResult.estimatedDelivery }}</span>
      </div>
      
      <div class="result-details">
        <div class="result-row">
          <span>Shipping Zone:</span>
          <span>{{ shippingResult.zone.name }}</span>
        </div>
        
        <div class="result-row">
          <span>Method:</span>
          <span>{{ shippingResult.method.name }}</span>
        </div>
        
        <div v-if="shippingResult.baseCost > 0" class="result-row">
          <span>Base Cost:</span>
          <span>Tsh {{ shippingResult.baseCost.toLocaleString() }}</span>
        </div>
        
        <div v-if="shippingResult.additionalCosts > 0" class="result-row">
          <span>Additional Fees:</span>
          <span>Tsh {{ shippingResult.additionalCosts.toLocaleString() }}</span>
        </div>
        
        <div class="result-row total">
          <span>Total Shipping:</span>
          <span class="total-cost">
            {{ shippingResult.freeShipping ? 'FREE' : `Tsh ${shippingResult.totalCost.toLocaleString()}` }}
          </span>
        </div>
      </div>
      
      <!-- Free Shipping Progress -->
      <div v-if="!shippingResult.freeShipping && shippingResult.zone.freeShippingThreshold > 0" class="free-shipping-progress">
        <div class="progress-header">
          <span>Add Tsh {{ freeShippingRemaining.toLocaleString() }} more for FREE shipping!</span>
        </div>
        <div class="progress-bar">
          <div 
            class="progress-fill" 
            :style="{ width: `${freeShippingProgress}%` }"
          ></div>
        </div>
      </div>
      
      <!-- Tracking Info -->
      <div v-if="shippingResult.tracking" class="tracking-info">
        <div class="tracking-icon">📦</div>
        <span>Order tracking included</span>
      </div>
    </div>
    
    <!-- Action Buttons -->
    <div class="shipping-actions">
      <button 
        @click="resetCalculator"
        class="btn btn-secondary"
      >
        Reset
      </button>
      <button 
        @click="applyShipping"
        class="btn btn-primary"
        :disabled="!canApplyShipping"
      >
        Apply Shipping
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch, onMounted } from 'vue'
import { 
  shippingCalculator, 
  getShippingZones, 
  getShippingMethods,
  validateShippingAddress 
} from '../utils/shipping.js'

export default {
  name: 'ShippingCalculator',
  props: {
    cartTotal: {
      type: Number,
      default: 0
    },
    products: {
      type: Array,
      default: () => []
    },
    initialAddress: {
      type: Object,
      default: () => ({})
    }
  },
  emits: ['shipping-calculated', 'shipping-applied'],
  setup(props, { emit }) {
    const selectedRegion = ref('')
    const selectedMethod = ref('standard')
    const shippingResult = ref(null)
    const errors = ref({})
    
    const address = ref({
      city: '',
      street: '',
      postalCode: '',
      phone: ''
    })
    
    const shippingZones = ref([])
    const shippingMethods = ref([])
    const allRegions = ref([])
    
    // Load shipping data
    const loadShippingData = () => {
      shippingZones.value = getShippingZones()
      shippingMethods.value = getShippingMethods()
      allRegions.value = shippingCalculator.getAllRegions()
    }
    
    // Get regions by zone
    const getRegionsByZone = (zoneKey) => {
      return allRegions.value.filter(region => region.zoneCode === zoneKey)
    }
    
    // Calculate shipping
    const calculateShipping = () => {
      if (!selectedRegion.value) return
      
      try {
        const result = shippingCalculator.calculateShipping({
          region: selectedRegion.value,
          cartTotal: props.cartTotal,
          products: props.products,
          method: selectedMethod.value
        })
        
        shippingResult.value = result
        emit('shipping-calculated', result)
        
      } catch (error) {
        console.error('Shipping calculation error:', error)
      }
    }
    
    // Select shipping method
    const selectShippingMethod = (method) => {
      selectedMethod.value = method
      calculateShipping()
    }
    
    // Get method price display
    const getMethodPrice = (method) => {
      if (!selectedRegion.value) return 'Select region first'
      
      const result = shippingCalculator.calculateShipping({
        region: selectedRegion.value,
        cartTotal: props.cartTotal,
        products: props.products,
        method: method
      })
      
      return result.freeShipping ? 'FREE' : `Tsh ${result.totalCost.toLocaleString()}`
    }
    
    // Validate address
    const validateAddress = () => {
      const addressData = {
        region: selectedRegion.value,
        city: address.value.city,
        address: address.value.street,
        postalCode: address.value.postalCode
      }
      
      const validation = validateShippingAddress(addressData)
      errors.value = {}
      
      validation.errors.forEach(error => {
        const field = error.toLowerCase().includes('region') ? 'region' :
                     error.toLowerCase().includes('city') ? 'city' :
                     error.toLowerCase().includes('street') ? 'street' :
                     error.toLowerCase().includes('postal') ? 'postalCode' :
                     error.toLowerCase().includes('phone') ? 'phone' : 'general'
        errors.value[field] = error
      })
      
      return validation.isValid
    }
    
    // Apply shipping
    const applyShipping = () => {
      if (!validateAddress()) return
      
      const shippingData = {
        ...shippingResult.value,
        address: {
          ...address.value,
          region: selectedRegion.value
        },
        method: selectedMethod.value
      }
      
      emit('shipping-applied', shippingData)
    }
    
    // Reset calculator
    const resetCalculator = () => {
      selectedRegion.value = ''
      selectedMethod.value = 'standard'
      shippingResult.value = null
      errors.value = {}
      address.value = {
        city: '',
        street: '',
        postalCode: '',
        phone: ''
      }
    }
    
    // Computed properties
    const canApplyShipping = computed(() => {
      return selectedRegion.value && address.value.city && address.value.street && address.value.phone
    })
    
    const freeShippingRemaining = computed(() => {
      if (!shippingResult.value || shippingResult.value.freeShipping) return 0
      return shippingResult.value.zone.freeShippingThreshold - props.cartTotal
    })
    
    const freeShippingProgress = computed(() => {
      if (!shippingResult.value) return 0
      const threshold = shippingResult.value.zone.freeShippingThreshold
      return Math.min((props.cartTotal / threshold) * 100, 100)
    })
    
    // Watch for changes
    watch(() => props.cartTotal, calculateShipping)
    watch(() => props.products, calculateShipping, { deep: true })
    
    // Initialize
    onMounted(() => {
      loadShippingData()
      if (props.initialAddress) {
        address.value = { ...address.value, ...props.initialAddress }
      }
    })
    
    return {
      selectedRegion,
      selectedMethod,
      shippingResult,
      errors,
      address,
      shippingZones,
      shippingMethods,
      allRegions,
      getRegionsByZone,
      calculateShipping,
      selectShippingMethod,
      getMethodPrice,
      validateAddress,
      applyShipping,
      resetCalculator,
      canApplyShipping,
      freeShippingRemaining,
      freeShippingProgress
    }
  }
}
</script>

<style scoped>
.shipping-calculator {
  @apply bg-white rounded-lg shadow-md p-6;
}

.shipping-header {
  @apply mb-6;
}

.shipping-title {
  @apply text-lg font-semibold text-gray-800 mb-2;
}

.shipping-description {
  @apply text-sm text-gray-600;
}

.shipping-form {
  @apply space-y-4;
}

.form-group {
  @apply space-y-2;
}

.form-label {
  @apply block text-sm font-medium text-gray-700;
}

.form-select, .form-input, .form-textarea {
  @apply w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent;
}

.form-select.has-error, .form-input.has-error, .form-textarea.has-error {
  @apply border-red-500;
}

.form-error {
  @apply text-red-500 text-xs;
}

.form-row {
  @apply grid grid-cols-1 md:grid-cols-2 gap-4;
}

.shipping-methods {
  @apply space-y-2;
}

.method-option {
  @apply flex items-center justify-between p-3 border border-gray-200 rounded-lg cursor-pointer hover:bg-gray-50 transition-colors;
}

.method-option.is-selected {
  @apply border-blue-500 bg-blue-50;
}

.method-info {
  @apply flex-1;
}

.method-name {
  @apply font-medium text-gray-800;
}

.method-description {
  @apply text-sm text-gray-600;
}

.method-price {
  @apply font-semibold text-blue-600;
}

.address-form {
  @apply mt-6 p-4 bg-gray-50 rounded-lg space-y-4;
}

.address-title {
  @apply font-semibold text-gray-800 mb-3;
}

.shipping-results {
  @apply mt-6 p-4 bg-blue-50 rounded-lg;
}

.result-header {
  @apply flex justify-between items-center mb-4;
}

.result-header h4 {
  @apply font-semibold text-gray-800;
}

.delivery-time {
  @apply text-sm text-blue-600;
}

.result-details {
  @apply space-y-2;
}

.result-row {
  @apply flex justify-between text-sm;
}

.result-row.total {
  @apply pt-2 border-t border-blue-200 font-semibold;
}

.total-cost {
  @apply text-blue-600;
}

.free-shipping-progress {
  @apply mt-4 space-y-2;
}

.progress-header {
  @apply text-sm text-gray-600;
}

.progress-bar {
  @apply w-full bg-blue-200 rounded-full h-2;
}

.progress-fill {
  @apply bg-blue-600 h-2 rounded-full transition-all duration-300;
}

.tracking-info {
  @apply flex items-center gap-2 mt-4 text-sm text-green-600;
}

.shipping-actions {
  @apply flex gap-3 mt-6;
}

.btn {
  @apply px-4 py-2 rounded-lg font-medium transition-colors;
}

.btn-primary {
  @apply bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed;
}

.btn-secondary {
  @apply bg-gray-200 text-gray-800 hover:bg-gray-300;
}
</style>
