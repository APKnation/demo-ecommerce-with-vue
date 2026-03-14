<template>
  <div class="search-filter">
    <div class="search-container">
      <div class="search-input-wrapper">
        <svg class="search-icon" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 21l-6-6m2-5a7 7 0 11-14 0 7 7 0 0114 0z"></path>
        </svg>
        <input
          v-model="searchQuery"
          @input="handleSearch"
          type="text"
          placeholder="Search products..."
          class="search-input"
        >
      </div>
    </div>
    
    <div class="filter-container">
      <div class="filter-dropdown" ref="filterDropdown">
        <button 
          @click="toggleDropdown"
          class="filter-btn"
          :class="{ 'is-active': isDropdownOpen }"
        >
          <svg class="w-4 h-4 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 4a1 1 0 011-1h16a1 1 0 011 1v2.586a1 1 0 01-.293.707l-6.414 6.414a1 1 0 00-.293.707V17l-4 4v-6.586a1 1 0 00-.293-.707L3.293 7.293A1 1 0 013 6.586V4z"></path>
          </svg>
          Filters
          <span v-if="activeFiltersCount > 0" class="filter-count">
            {{ activeFiltersCount }}
          </span>
          <svg class="w-4 h-4 ml-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
          </svg>
        </button>
        
        <transition name="dropdown">
          <div v-if="isDropdownOpen" class="dropdown-menu">
            <div class="filter-section">
              <h4 class="filter-title">Categories</h4>
              <div class="filter-options">
                <label 
                  v-for="category in categories" 
                  :key="category"
                  class="filter-option"
                >
                  <input
                    v-model="selectedCategories"
                    :value="category"
                    type="checkbox"
                    @change="applyFilters"
                  >
                  <span class="filter-label">{{ category }}</span>
                </label>
              </div>
            </div>
            
            <div class="filter-section">
              <h4 class="filter-title">Price Range</h4>
              <div class="price-range">
                <div class="price-input">
                  <label>Min:</label>
                  <input
                    v-model="priceRange.min"
                    type="number"
                    @input="applyFilters"
                    class="price-field"
                  >
                </div>
                <div class="price-input">
                  <label>Max:</label>
                  <input
                    v-model="priceRange.max"
                    type="number"
                    @input="applyFilters"
                    class="price-field"
                  >
                </div>
              </div>
            </div>
            
            <div class="filter-section">
              <h4 class="filter-title">Sort By</h4>
              <select 
                v-model="sortBy"
                @change="applyFilters"
                class="sort-select"
              >
                <option value="name">Name</option>
                <option value="price-low">Price: Low to High</option>
                <option value="price-high">Price: High to Low</option>
                <option value="newest">Newest First</option>
              </select>
            </div>
            
            <div class="filter-actions">
              <button 
                @click="clearFilters"
                class="btn btn-secondary btn-sm"
              >
                Clear All
              </button>
              <button 
                @click="applyFilters"
                class="btn btn-primary btn-sm"
              >
                Apply Filters
              </button>
            </div>
          </div>
        </transition>
      </div>
    </div>
    
    <div v-if="searchQuery || activeFiltersCount > 0" class="active-filters">
      <span class="filter-summary">
        {{ filteredProductsCount }} products found
      </span>
      <button 
        @click="clearAll"
        class="clear-all-btn"
      >
        Clear all
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue'

export default {
  name: 'SearchFilter',
  props: {
    products: {
      type: Array,
      required: true
    }
  },
  emits: ['filter-change'],
  setup(props, { emit }) {
    const searchQuery = ref('')
    const selectedCategories = ref([])
    const priceRange = ref({ min: '', max: '' })
    const sortBy = ref('name')
    const isDropdownOpen = ref(false)
    const filterDropdown = ref(null)
    
    const categories = computed(() => {
      const uniqueCategories = [...new Set(props.products.map(p => p.category))]
      return uniqueCategories.filter(Boolean)
    })
    
    const activeFiltersCount = computed(() => {
      let count = selectedCategories.value.length
      if (priceRange.value.min) count++
      if (priceRange.value.max) count++
      return count
    })
    
    const filteredProductsCount = computed(() => {
      return filteredProducts.value.length
    })
    
    const filteredProducts = computed(() => {
      let result = [...props.products]
      
      // Apply search
      if (searchQuery.value) {
        const query = searchQuery.value.toLowerCase()
        result = result.filter(product => 
          product.name.toLowerCase().includes(query) ||
          product.category.toLowerCase().includes(query)
        )
      }
      
      // Apply category filter
      if (selectedCategories.value.length > 0) {
        result = result.filter(product => 
          selectedCategories.value.includes(product.category)
        )
      }
      
      // Apply price range
      if (priceRange.value.min) {
        result = result.filter(product => product.price >= priceRange.value.min)
      }
      if (priceRange.value.max) {
        result = result.filter(product => product.price <= priceRange.value.max)
      }
      
      // Apply sorting
      switch (sortBy.value) {
        case 'name':
          result.sort((a, b) => a.name.localeCompare(b.name))
          break
        case 'price-low':
          result.sort((a, b) => a.price - b.price)
          break
        case 'price-high':
          result.sort((a, b) => b.price - a.price)
          break
        case 'newest':
          result.sort((a, b) => (b.isNew ? 1 : 0) - (a.isNew ? 1 : 0))
          break
      }
      
      return result
    })
    
    const toggleDropdown = () => {
      isDropdownOpen.value = !isDropdownOpen.value
    }
    
    const closeDropdown = (event) => {
      if (filterDropdown.value && !filterDropdown.value.contains(event.target)) {
        isDropdownOpen.value = false
      }
    }
    
    const handleSearch = () => {
      applyFilters()
    }
    
    const applyFilters = () => {
      emit('filter-change', {
        products: filteredProducts.value,
        searchQuery: searchQuery.value,
        filters: {
          categories: selectedCategories.value,
          priceRange: priceRange.value,
          sortBy: sortBy.value
        }
      })
    }
    
    const clearFilters = () => {
      selectedCategories.value = []
      priceRange.value = { min: '', max: '' }
      sortBy.value = 'name'
      applyFilters()
    }
    
    const clearAll = () => {
      searchQuery.value = ''
      clearFilters()
    }
    
    onMounted(() => {
      document.addEventListener('click', closeDropdown)
    })
    
    onUnmounted(() => {
      document.removeEventListener('click', closeDropdown)
    })
    
    return {
      searchQuery,
      selectedCategories,
      priceRange,
      sortBy,
      isDropdownOpen,
      filterDropdown,
      categories,
      activeFiltersCount,
      filteredProductsCount,
      toggleDropdown,
      handleSearch,
      applyFilters,
      clearFilters,
      clearAll
    }
  }
}
</script>

<style scoped>
.search-filter {
  @apply bg-white rounded-lg shadow-md p-4 mb-6;
}

.search-container {
  @apply mb-4;
}

.search-input-wrapper {
  @apply relative;
}

.search-icon {
  @apply absolute left-3 top-1/2 transform -translate-y-1/2 w-5 h-5 text-gray-400;
}

.search-input {
  @apply w-full pl-10 pr-4 py-3 border border-gray-300 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-all;
}

.filter-container {
  @apply relative;
}

.filter-btn {
  @apply flex items-center px-4 py-2 bg-gray-100 hover:bg-gray-200 rounded-lg transition-colors;
}

.filter-btn.is-active {
  @apply bg-blue-100 text-blue-700;
}

.filter-count {
  @apply bg-blue-600 text-white text-xs rounded-full px-2 py-1 ml-2;
}

.dropdown-menu {
  @apply absolute top-full left-0 mt-2 w-80 bg-white rounded-lg shadow-xl border border-gray-200 p-4 z-50;
}

.filter-section {
  @apply mb-4;
}

.filter-title {
  @apply font-semibold text-gray-800 mb-2;
}

.filter-options {
  @apply space-y-2;
}

.filter-option {
  @apply flex items-center cursor-pointer;
}

.filter-option input[type="checkbox"] {
  @apply mr-2;
}

.filter-label {
  @apply text-gray-700;
}

.price-range {
  @apply flex gap-4;
}

.price-input {
  @apply flex-1;
}

.price-input label {
  @apply block text-sm text-gray-600 mb-1;
}

.price-field {
  @apply w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent;
}

.sort-select {
  @apply w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent;
}

.filter-actions {
  @apply flex gap-2 justify-end pt-4 border-t border-gray-200;
}

.btn-sm {
  @apply px-3 py-2 text-sm;
}

.active-filters {
  @apply flex justify-between items-center mt-4 p-3 bg-blue-50 rounded-lg;
}

.filter-summary {
  @apply text-blue-700 font-medium;
}

.clear-all-btn {
  @apply text-blue-600 hover:text-blue-800 font-medium;
}

.dropdown-enter-active, .dropdown-leave-active {
  @apply transition-all duration-200;
}

.dropdown-enter-from {
  @apply opacity-0 transform -translate-y-2;
}

.dropdown-leave-to {
  @apply opacity-0 transform -translate-y-2;
}
</style>
