<template>
  <div>
    <!-- Search and Filter Section -->
    <section class="mb-8">
      <div class="bg-white rounded-lg shadow-md p-6">
        <div class="grid grid-cols-1 md:grid-cols-4 gap-4">
          <!-- Search Bar -->
          <div class="md:col-span-2">
            <div class="flex">
              <input
                v-model="searchTerm"
                type="text"
                placeholder="Search products..."
                class="flex-grow px-4 py-2 border border-gray-300 rounded-l-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                @input="filterProducts"
              >
              <button
                @click="filterProducts"
                class="btn btn-primary rounded-l-none"
              >
                Search
              </button>
            </div>
          </div>
          
          <!-- Category Filter -->
          <select
            v-model="categoryFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            @change="filterProducts"
          >
            <option value="">All Categories</option>
            <option value="laptops">Laptops</option>
            <option value="phones">Smartphones</option>
            <option value="accessories">Accessories</option>
          </select>
          
          <!-- Price Filter -->
          <select
            v-model="priceFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            @change="filterProducts"
          >
            <option value="">All Prices</option>
            <option value="0-200000">Under Tsh 200,000</option>
            <option value="200000-1000000">Tsh 200,000 - 1,000,000</option>
            <option value="1000000+">Above Tsh 1,000,000</option>
          </select>
        </div>
        
        <!-- Sort Filter -->
        <div class="mt-4">
          <select
            v-model="sortFilter"
            class="px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            @change="filterProducts"
          >
            <option value="">Sort By</option>
            <option value="name-asc">Name (A-Z)</option>
            <option value="name-desc">Name (Z-A)</option>
            <option value="price-asc">Price (Low to High)</option>
            <option value="price-desc">Price (High to Low)</option>
          </select>
        </div>
      </div>
    </section>

    <!-- Product Listing -->
    <section>
      <div v-if="filteredProducts.length === 0" class="text-center py-12">
        <p class="text-gray-500 text-lg">No products found matching your criteria.</p>
      </div>
      
      <div v-else class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <div
          v-for="product in filteredProducts"
          :key="product.name"
          class="card hover:shadow-lg transition-shadow duration-300"
        >
          <img
            :src="product.image"
            :alt="product.name"
            class="w-full h-48 object-cover rounded-t-lg mb-4"
          >
          <h3 class="text-xl font-semibold mb-2">{{ product.name }}</h3>
          <p class="text-gray-600 mb-2">{{ product.category }}</p>
          <p class="text-2xl font-bold text-blue-600 mb-4">Tsh {{ product.price.toLocaleString() }}</p>
          
          <div class="flex flex-wrap gap-2">
            <button
              @click="addToCart(product.name, product.price)"
              class="btn btn-primary flex-grow"
            >
              Add to Cart
            </button>
            <button
              @click="toggleWishlist(product.name, product.price, product.image)"
              :class="isInWishlist(product.name) ? 'bg-red-500 hover:bg-red-600' : 'bg-gray-200 hover:bg-gray-300'"
              class="btn text-sm px-3"
            >
              {{ isInWishlist(product.name) ? '❤️' : '🤍' }}
            </button>
            <button
              @click="addToCompare(product.name, product.price)"
              :class="isInCompare(product.name) ? 'bg-red-500 hover:bg-red-600 text-white' : 'bg-green-500 hover:bg-green-600 text-white'"
              class="btn text-sm px-3"
            >
              ⚖️
            </button>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script>
import { ref, computed, inject, onMounted } from 'vue'

export default {
  name: 'Home',
  setup() {
    const searchTerm = ref('')
    const categoryFilter = ref('')
    const priceFilter = ref('')
    const sortFilter = ref('')
    const products = ref([])
    
    // Load products from localStorage or use defaults
    const loadProducts = () => {
      const savedProducts = localStorage.getItem('adminProducts')
      if (savedProducts) {
        products.value = JSON.parse(savedProducts)
      } else {
        // Default products
        products.value = [
          { name: 'Mac Book', price: 1000000, category: 'laptops', image: '/images/w.jpg' },
          { name: 'HP-Brand', price: 150000, category: 'laptops', image: '/images/j.jpg' },
          { name: 'Dell', price: 200000, category: 'laptops', image: '/images/k.jpg' },
          { name: 'Apple', price: 1000000, category: 'phones', image: '/images/d.jpg' },
          { name: 'HP-Elite', price: 1500000, category: 'laptops', image: '/images/a.jpg' },
          { name: 'Sony', price: 200000, category: 'accessories', image: '/images/f.jpg' },
          { name: 'Infinix', price: 400000, category: 'phones', image: '/images/g.jpg' },
          { name: 'iPhone', price: 1500000, category: 'phones', image: '/images/p.jpg' },
          { name: 'Samsung', price: 3000000, category: 'phones', image: '/images/l.jpg' }
        ]
      }
    }

    // Load products on mount
    onMounted(() => {
      loadProducts()
    })

    // Inject parent data and methods
    const wishlist = inject('wishlist', ref([]))
    const compareList = inject('compareList', ref([]))
    const addToCart = inject('addToCart')
    const toggleWishlist = inject('toggleWishlist')
    const addToCompare = inject('addToCompare')

    // Filter and sort products
    const filteredProducts = computed(() => {
      let filtered = products.value.filter(product => {
        // Search filter
        const matchesSearch = product.name.toLowerCase().includes(searchTerm.value.toLowerCase())
        
        // Category filter
        const matchesCategory = !categoryFilter.value || product.category === categoryFilter.value
        
        // Price filter
        let matchesPrice = true
        if (priceFilter.value === '0-200000') {
          matchesPrice = product.price <= 200000
        } else if (priceFilter.value === '200000-1000000') {
          matchesPrice = product.price > 200000 && product.price <= 1000000
        } else if (priceFilter.value === '1000000+') {
          matchesPrice = product.price > 1000000
        }
        
        return matchesSearch && matchesCategory && matchesPrice
      })

      // Sort products
      if (sortFilter.value) {
        filtered.sort((a, b) => {
          switch(sortFilter.value) {
            case 'name-asc':
              return a.name.localeCompare(b.name)
            case 'name-desc':
              return b.name.localeCompare(a.name)
            case 'price-asc':
              return a.price - b.price
            case 'price-desc':
              return b.price - a.price
            default:
              return 0
          }
        })
      }

      return filtered
    })

    // Check if product is in wishlist
    const isInWishlist = (productName) => {
      return wishlist.value.some(item => item.name === productName)
    }

    // Check if product is in compare list
    const isInCompare = (productName) => {
      return compareList.value.some(item => item.name === productName)
    }

    // Filter products function
    const filterProducts = () => {
      // This function is reactive due to computed property
    }

    return {
      searchTerm,
      categoryFilter,
      priceFilter,
      sortFilter,
      filteredProducts,
      isInWishlist,
      isInCompare,
      filterProducts,
      addToCart,
      toggleWishlist,
      addToCompare
    }
  }
}
</script>
