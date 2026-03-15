<template>
  <div class="product-detail-page">
    <div v-if="loading" class="loading-container">
      <div class="loading-spinner">Loading...</div>
    </div>
    
    <div v-else-if="!product" class="not-found">
      <h2>Product Not Found</h2>
      <p>The product you're looking for doesn't exist.</p>
      <router-link to="/" class="back-link">Back to Home</router-link>
    </div>
    
    <ProductDetail 
      v-else
      :product="product"
      :related-products="relatedProducts"
      @add-to-cart="handleAddToCart"
      @toggle-wishlist="handleToggleWishlist"
      @add-to-compare="handleAddToCompare"
    />
  </div>
</template>

<script>
import { ref, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import ProductDetail from '../components/ProductDetail.vue'
import { getCategoryById } from '../data/categories.js'

export default {
  name: 'ProductDetailView',
  components: {
    ProductDetail
  },
  setup(props, { emit }) {
    const route = useRoute()
    const loading = ref(true)
    const product = ref(null)
    const relatedProducts = ref([])
    
    // Sample products data (in real app, this would come from API)
    const sampleProducts = [
      {
        id: '1',
        name: 'iPhone 15 Pro',
        price: 2500000,
        category: 'smartphones',
        subcategory: 'iphone',
        image: '/images/iPhone.jpg',
        images: ['/images/iPhone.jpg', '/images/iPhone-16-Pro-max-300x300.jpg'],
        rating: 4.8,
        reviews: 156,
        stock: 15,
        discount: 10,
        description: 'Latest iPhone with advanced features',
        specifications: {
          brand: 'Apple',
          model: 'iPhone 15 Pro',
          color: 'Titanium Blue',
          weight: '187g',
          dimensions: '146.6 x 70.6 x 8.25 mm',
          warranty: '1 Year',
          screen_size: '6.1 inches',
          resolution: '2556 x 1179 pixels',
          processor: 'A17 Pro',
          ram: '8GB',
          storage: '256GB',
          camera: '48MP Main + 12MP Ultra Wide + 12MP Telephoto',
          battery: '3274 mAh',
          os: 'iOS 17'
        }
      },
      {
        id: '2',
        name: 'MacBook Pro',
        price: 4500000,
        category: 'laptops',
        subcategory: 'business',
        image: '/images/Computer.jpeg',
        images: ['/images/Computer.jpeg'],
        rating: 4.6,
        reviews: 89,
        stock: 8,
        specifications: {
          brand: 'Apple',
          model: 'MacBook Pro 14"',
          color: 'Space Gray',
          weight: '1.6kg',
          dimensions: '312.6 x 220.7 x 15.5 mm',
          warranty: '1 Year',
          processor: 'M3 Pro',
          ram: '18GB',
          storage: '512GB SSD',
          graphics: 'Integrated',
          screen_size: '14.2 inches',
          resolution: '3024 x 1964 pixels',
          battery_life: '18 hours',
          os: 'macOS Sonoma'
        }
      },
      {
        id: '3',
        name: 'AirPods Pro',
        price: 450000,
        category: 'headphones',
        subcategory: 'wireless',
        image: '/images/airpods.jpg',
        images: ['/images/airpods.jpg'],
        rating: 4.7,
        reviews: 234,
        stock: 25,
        specifications: {
          brand: 'Apple',
          model: 'AirPods Pro (2nd Gen)',
          color: 'White',
          weight: '5.3g (each earbud)',
          warranty: '1 Year',
          type: 'In-ear wireless',
          connectivity: 'Bluetooth 5.3',
          battery_life: '6 hours (30 hours with case)',
          noise_cancelling: 'Active Noise Cancellation',
          frequency_response: '20Hz - 20kHz'
        }
      },
      {
        id: '4',
        name: 'Apple Watch Series 9',
        price: 650000,
        category: 'wearables',
        subcategory: 'smartwatch',
        image: '/images/watch1.jpeg',
        images: ['/images/watch1.jpeg'],
        rating: 4.5,
        reviews: 67,
        stock: 12,
        specifications: {
          brand: 'Apple',
          model: 'Apple Watch Series 9',
          color: 'Midnight',
          weight: '38.7g',
          warranty: '1 Year',
          display: 'Always-On Retina LTPO OLED',
          battery_life: '18 hours',
          water_resistance: '50m water resistant',
          compatibility: 'iPhone',
          health_features: 'Heart rate, ECG, Blood oxygen, Sleep tracking',
          gps: 'Built-in GPS'
        }
      }
    ]
    
    const loadProduct = () => {
      loading.value = true
      
      // Simulate API call
      setTimeout(() => {
        const productId = route.params.id
        const foundProduct = sampleProducts.find(p => p.id === productId)
        
        if (foundProduct) {
          product.value = foundProduct
          loadRelatedProducts(foundProduct)
        }
        
        loading.value = false
      }, 500)
    }
    
    const loadRelatedProducts = (currentProduct) => {
      const category = getCategoryById(currentProduct.category)
      if (category) {
        relatedProducts.value = sampleProducts.filter(p => 
          p.category === currentProduct.category && 
          p.id !== currentProduct.id
        ).slice(0, 4)
      }
    }
    
    const handleAddToCart = (cartItem) => {
      emit('add-to-cart', cartItem)
    }
    
    const handleToggleWishlist = (product) => {
      emit('toggle-wishlist', product)
    }
    
    const handleAddToCompare = (product) => {
      emit('add-to-compare', product)
    }
    
    onMounted(() => {
      loadProduct()
    })
    
    return {
      loading,
      product,
      relatedProducts,
      handleAddToCart,
      handleToggleWishlist,
      handleAddToCompare
    }
  }
}
</script>

<style scoped>
.product-detail-page {
  @apply min-h-screen bg-gray-50;
}

.loading-container {
  @apply flex items-center justify-center min-h-screen;
}

.loading-spinner {
  @apply text-blue-600 text-xl;
}

.not-found {
  @apply text-center py-16;
}

.not-found h2 {
  @apply text-2xl font-bold text-gray-900 mb-4;
}

.not-found p {
  @apply text-gray-600 mb-6;
}

.back-link {
  @apply inline-block px-6 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors;
}
</style>
