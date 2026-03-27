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
    
    <ProductDetailComponent
      v-else
      :product="product"
      :related-products="relatedProducts"
      @add-to-cart="handleAddToCart"
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
    
    const loadProduct = async () => {
      loading.value = true
      
      try {
        const productId = route.params.id
        const response = await fetch(`http://localhost:8000/api/products/${productId}/`)
        
        if (response.ok) {
          const productData = await response.json()
          product.value = productData
          loadRelatedProducts(productData)
        } else {
          console.error('Failed to load product')
          product.value = null
        }
      } catch (error) {
        console.error('Error loading product:', error)
        product.value = null
      } finally {
        loading.value = false
      }
    }
    
    const loadRelatedProducts = async (currentProduct) => {
      if (!currentProduct) return
      
      try {
        const response = await fetch(`http://localhost:8000/api/products/?category=${currentProduct.category}`)
        
        if (response.ok) {
          const allProducts = await response.json()
          // Filter out current product and get related ones
          relatedProducts.value = allProducts
            .filter(p => p.category === currentProduct.category && p.id !== currentProduct.id)
            .slice(0, 4)
        }
      } catch (error) {
        console.error('Error loading related products:', error)
        relatedProducts.value = []
      }
    }
    
    const handleAddToCart = (cartItem) => {
      emit('add-to-cart', cartItem)
    }
    
    const handleAddToCompare = (product) => {
      emit('add-to-compare', product)
    }
    
    // Helper functions for image handling
    const getImageUrl = (imagePath) => {
      if (!imagePath) return '/images/placeholder.jpg'
      
      // If it's already a full URL, return as is
      if (imagePath.startsWith('http://') || imagePath.startsWith('https://')) {
        return imagePath
      }
      
      // If it's a backend media URL, return as is
      if (imagePath.startsWith('/media/')) {
        return `http://localhost:8000${imagePath}` 
      }
      
      // If it's a full URL from backend, return as is
      if (imagePath.includes('localhost:8000')) {
        return imagePath
      }
      
      // If it's a relative path starting with /images/, use as is
      if (imagePath.startsWith('/images/')) {
        return imagePath
      }
      
      // Otherwise, assume it's a relative path and construct backend URL
      return `http://localhost:8000/media/${imagePath}` 
    }

    const handleImageError = (event) => {
      event.target.src = '/images/placeholder.jpg'
    }
    
    onMounted(() => {
      loadProduct()
    })
    
    return {
      product,
      relatedProducts,
      handleAddToCart,
      handleAddToCompare,
      getImageUrl,
      handleImageError
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
