<template>
  <div class="product-detail">
    <!-- Product Header -->
    <div class="product-header">
      <nav class="breadcrumb">
        <router-link to="/" class="breadcrumb-link">Home</router-link>
        <span class="breadcrumb-separator">/</span>
        <router-link 
          :to="`/category/${product.category}`" 
          class="breadcrumb-link"
        >
          {{ categoryName }}
        </router-link>
        <span class="breadcrumb-separator">/</span>
        <span class="breadcrumb-current">{{ product.name }}</span>
      </nav>
    </div>
    
    <!-- Product Main Content -->
    <div class="product-main">
      <div class="product-grid">
        <!-- Product Images Section -->
        <div class="product-images">
          <ProductGallery 
            :images="productImages"
            :title="product.name"
            @image-change="handleImageChange"
          />
        </div>
        
        <!-- Product Information Section -->
        <div class="product-info">
          <!-- Product Title & Basic Info -->
          <div class="product-title-section">
            <h1 class="product-name">{{ product.name }}</h1>
            <div class="product-meta">
              <span class="product-category">{{ categoryName }}</span>
              <span class="product-rating">
                ⭐ {{ product.rating || 4.5 }} ({{ product.reviews || 23 }} reviews)
              </span>
            </div>
          </div>
          
          <!-- Product Price -->
          <div class="product-price-section">
            <div class="price-container">
              <span v-if="product.discount" class="original-price">
                Tsh {{ product.price.toLocaleString() }}
              </span>
              <span class="current-price">
                Tsh {{ discountedPrice.toLocaleString() }}
              </span>
              <span v-if="product.discount" class="discount-badge">
                -{{ product.discount }}%
              </span>
            </div>
            <div class="price-info">
              <span class="tax-info">Inclusive of VAT</span>
              <span class="stock-info" :class="{ 'in-stock': product.stock > 0, 'out-of-stock': product.stock === 0 }">
                {{ product.stock > 0 ? `${product.stock} in stock` : 'Out of stock' }}
              </span>
            </div>
          </div>
          
          <!-- Product Actions -->
          <div class="product-actions">
            <div class="quantity-selector">
              <button 
                @click="decreaseQuantity"
                class="quantity-btn"
                :disabled="quantity <= 1"
              >
                -
              </button>
              <input 
                v-model.number="quantity"
                type="number"
                min="1"
                :max="product.stock"
                class="quantity-input"
              >
              <button 
                @click="increaseQuantity"
                class="quantity-btn"
                :disabled="quantity >= product.stock"
              >
                +
              </button>
            </div>
            
            <div class="action-buttons">
              <button 
                @click="addToCart"
                class="btn btn-primary add-to-cart"
                :disabled="product.stock === 0"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 3h2l.4 2M7 13h10l4-8H5.4M7 13L5.4 5M7 13l-2.293 2.293c-.63.63-.184 1.707.707H17m0 0a2 2 0 100 4 2 2 0 000-4zm-8 2a2 2 0 11-4 0 2 2 0 014 0z"></path>
                </svg>
                Add to Cart
              </button>
              
              <button 
                @click="toggleWishlist"
                class="btn btn-secondary wishlist-btn"
                :class="{ 'is-active': isInWishlist }"
              >
                <svg class="w-5 h-5" fill="currentColor" viewBox="0 0 24 24">
                  <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
                </svg>
              </button>
              
              <button 
                @click="addToCompare"
                class="btn btn-secondary compare-btn"
                :disabled="isInCompare"
              >
                <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"></path>
                </svg>
              </button>
            </div>
          </div>
          
          <!-- Product Features -->
          <div class="product-features">
            <div class="feature-item">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <span>Official Warranty</span>
            </div>
            <div class="feature-item">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"></path>
              </svg>
              <span>Fast Delivery</span>
            </div>
            <div class="feature-item">
              <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z"></path>
              </svg>
              <span>24/7 Support</span>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Product Tabs Section -->
    <div class="product-tabs">
      <div class="tabs-header">
        <button 
          v-for="tab in tabs" 
          :key="tab.key"
          @click="activeTab = tab.key"
          class="tab-button"
          :class="{ 'is-active': activeTab === tab.key }"
        >
          {{ tab.label }}
        </button>
      </div>
      
      <div class="tabs-content">
        <!-- Specifications Tab -->
        <div v-if="activeTab === 'specifications'" class="tab-panel">
          <ProductSpecifications 
            :specifications="product.specifications"
            :category="product.category"
          />
        </div>
        
        <!-- Description Tab -->
        <div v-if="activeTab === 'description'" class="tab-panel">
          <div class="product-description">
            <h3>Product Description</h3>
            <div v-html="product.description || getDefaultDescription()"></div>
          </div>
        </div>
        
        <!-- Reviews Tab -->
        <div v-if="activeTab === 'reviews'" class="tab-panel">
          <ProductReviews 
            :productId="product.id"
            :reviews="product.reviewsData || []"
          />
        </div>
        
        <!-- Shipping Tab -->
        <div v-if="activeTab === 'shipping'" class="tab-panel">
          <ProductShipping :product="product" />
        </div>
      </div>
    </div>
    
    <!-- Related Products -->
    <div class="related-products">
      <h2 class="section-title">Related Products</h2>
      <div class="products-grid">
        <ProductCard 
          v-for="relatedProduct in relatedProducts"
          :key="relatedProduct.id"
          :product="relatedProduct"
          @add-to-cart="$emit('add-to-cart', $event)"
        />
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { getCategoryById } from '../data/categories.js'
import ProductGallery from './ProductGallery.vue'
import ProductCard from './ProductCard.vue'
import ProductSpecifications from './ProductSpecifications.vue'
import ProductReviews from './ProductReviews.vue'
import ProductShipping from './ProductShipping.vue'
import Swal from 'sweetalert2'

export default {
  name: 'ProductDetail',
  components: {
    ProductGallery,
    ProductCard,
    ProductSpecifications,
    ProductReviews,
    ProductShipping
  },
  props: {
    product: {
      type: Object,
      required: true
    },
    relatedProducts: {
      type: Array,
      default: () => []
    }
  },
  emits: ['add-to-cart', 'toggle-wishlist', 'add-to-compare'],
  setup(props, { emit }) {
    const router = useRouter()
    const quantity = ref(1)
    const activeTab = ref('specifications')
    const isInWishlist = ref(false)
    const isInCompare = ref(false)
    
    const tabs = [
      { key: 'specifications', label: 'Specifications' },
      { key: 'description', label: 'Description' },
      { key: 'reviews', label: 'Reviews' },
      { key: 'shipping', label: 'Shipping & Returns' }
    ]
    
    // Computed properties
    const categoryName = computed(() => {
      const category = getCategoryById(props.product.category)
      return category ? category.name : 'Electronics'
    })
    
    const productImages = computed(() => {
      return props.product.images || [props.product.image || '/images/placeholder.jpg']
    })
    
    const discountedPrice = computed(() => {
      if (props.product.discount) {
        return props.product.price * (1 - props.product.discount / 100)
      }
      return props.product.price
    })
    
    // Methods
    const increaseQuantity = () => {
      if (quantity.value < props.product.stock) {
        quantity.value++
      }
    }
    
    const decreaseQuantity = () => {
      if (quantity.value > 1) {
        quantity.value--
      }
    }
    
    const addToCart = () => {
      if (props.product.stock === 0) return
      
      const cartItem = {
        ...props.product,
        quantity: quantity.value,
        addedAt: new Date().toISOString()
      }
      
      emit('add-to-cart', cartItem)
      
      Swal.fire({
        icon: 'success',
        title: 'Added to Cart!',
        text: `${quantity.value} × ${props.product.name} added to your cart`,
        timer: 2000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    }
    
    const toggleWishlist = () => {
      isInWishlist.value = !isInWishlist.value
      emit('toggle-wishlist', props.product)
      
      const message = isInWishlist.value ? 'Added to wishlist!' : 'Removed from wishlist'
      
      Swal.fire({
        icon: 'info',
        title: message,
        timer: 1500,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    }
    
    const addToCompare = () => {
      emit('add-to-compare', props.product)
      isInCompare.value = true
    }
    
    const handleImageChange = (data) => {
      // Handle image change if needed
      console.log('Image changed:', data)
    }
    
    const getDefaultDescription = () => `
      <p>Experience the latest in technology with the ${props.product.name}. 
      This premium product combines cutting-edge features with elegant design, 
      delivering exceptional performance for all your needs.</p>
      
      <h4>Key Features:</h4>
      <ul>
        <li>Premium build quality and materials</li>
        <li>Latest technology integration</li>
        <li>User-friendly interface</li>
        <li>Energy efficient operation</li>
        <li>Comprehensive warranty coverage</li>
      </ul>
      
      <p>Perfect for both personal and professional use, this product delivers 
      reliability and performance that you can trust.</p>
    `
    
    return {
      quantity,
      activeTab,
      isInWishlist,
      isInCompare,
      tabs,
      categoryName,
      productImages,
      discountedPrice,
      increaseQuantity,
      decreaseQuantity,
      addToCart,
      toggleWishlist,
      addToCompare,
      handleImageChange,
      getDefaultDescription
    }
  }
}
</script>

<style scoped>
.product-detail {
  @apply max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8;
}

.product-header {
  @apply mb-8;
}

.breadcrumb {
  @apply flex items-center text-sm;
}

.breadcrumb-link {
  @apply text-blue-600 hover:text-blue-700 transition-colors;
}

.breadcrumb-separator {
  @apply mx-2 text-gray-400;
}

.breadcrumb-current {
  @apply text-gray-600;
}

.product-main {
  @apply mb-12;
}

.product-grid {
  @apply grid grid-cols-1 lg:grid-cols-2 gap-12;
}

.product-images {
  @apply space-y-4;
}

.product-info {
  @apply space-y-6;
}

.product-title-section {
  @apply space-y-3;
}

.product-name {
  @apply text-3xl font-bold text-gray-900;
}

.product-meta {
  @apply flex flex-wrap items-center gap-4;
}

.product-category {
  @apply px-3 py-1 bg-blue-100 text-blue-800 rounded-full text-sm font-medium;
}

.product-rating {
  @apply text-sm text-gray-600;
}

.product-price-section {
  @apply space-y-3;
}

.price-container {
  @apply flex items-center gap-3;
}

.original-price {
  @apply text-lg text-gray-500 line-through;
}

.current-price {
  @apply text-3xl font-bold text-blue-600;
}

.discount-badge {
  @apply px-2 py-1 bg-red-500 text-white rounded-full text-sm font-medium;
}

.price-info {
  @apply flex flex-wrap gap-4 text-sm;
}

.tax-info {
  @apply text-gray-600;
}

.stock-info {
  @apply font-medium;
}

.stock-info.in-stock {
  @apply text-green-600;
}

.stock-info.out-of-stock {
  @apply text-red-600;
}

.product-actions {
  @apply space-y-4;
}

.quantity-selector {
  @apply flex items-center border border-gray-300 rounded-lg w-fit;
}

.quantity-btn {
  @apply w-10 h-10 flex items-center justify-center hover:bg-gray-100 transition-colors disabled:opacity-50 disabled:cursor-not-allowed;
}

.quantity-input {
  @apply w-16 text-center border-0 focus:ring-0 focus:outline-none;
}

.action-buttons {
  @apply flex flex-wrap gap-3;
}

.btn {
  @apply px-6 py-3 rounded-lg font-medium transition-all duration-200 flex items-center justify-center;
}

.btn-primary {
  @apply bg-blue-600 text-white hover:bg-blue-700 disabled:opacity-50 disabled:cursor-not-allowed;
}

.btn-secondary {
  @apply bg-gray-200 text-gray-800 hover:bg-gray-300;
}

.wishlist-btn.is-active {
  @apply bg-red-500 text-white hover:bg-red-600;
}

.product-features {
  @apply space-y-3;
}

.feature-item {
  @apply flex items-center gap-3 text-gray-700;
}

.product-tabs {
  @apply mb-12;
}

.tabs-header {
  @apply flex border-b border-gray-200 mb-6;
}

.tab-button {
  @apply px-6 py-3 font-medium text-gray-600 hover:text-gray-800 border-b-2 border-transparent transition-colors;
}

.tab-button.is-active {
  @apply text-blue-600 border-blue-600;
}

.tab-panel {
  @apply py-6;
}

.related-products {
  @apply space-y-6;
}

.section-title {
  @apply text-2xl font-bold text-gray-900;
}

.products-grid {
  @apply grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6;
}

@media (max-width: 768px) {
  .product-grid {
    @apply grid-cols-1 gap-8;
  }
  
  .action-buttons {
    @apply flex-col;
  }
  
  .btn {
    @apply w-full;
  }
}
</style>
