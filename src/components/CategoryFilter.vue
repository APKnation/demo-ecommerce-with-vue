<template>
  <div class="category-filter">
    <!-- Category Header -->
    <div class="category-header">
      <h3 class="category-title">Browse Categories</h3>
      <button 
        @click="toggleAllCategories"
        class="toggle-btn"
      >
        {{ allExpanded ? 'Collapse All' : 'Expand All' }}
      </button>
    </div>
    
    <!-- Category List -->
    <div class="category-list">
      <div 
        v-for="category in categories" 
        :key="category.id"
        class="category-item"
        :class="{ 
          'is-active': selectedCategory === category.id,
          'is-expanded': expandedCategories.includes(category.id)
        }"
      >
        <!-- Category Main -->
        <div 
          class="category-main"
          @click="selectCategory(category.id)"
        >
          <div class="category-info">
            <span class="category-icon">{{ category.icon }}</span>
            <div class="category-details">
              <h4 class="category-name">{{ category.name }}</h4>
              <p class="category-description">{{ category.description }}</p>
            </div>
          </div>
          
          <div class="category-actions">
            <span v-if="getProductCount(category.id)" class="product-count">
              {{ getProductCount(category.id) }} products
            </span>
            <button 
              @click.stop="toggleCategory(category.id)"
              class="expand-btn"
            >
              <svg 
                class="w-4 h-4 transition-transform"
                :class="{ 'rotate-180': expandedCategories.includes(category.id) }"
                fill="none" 
                stroke="currentColor" 
                viewBox="0 0 24 24"
              >
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"></path>
              </svg>
            </button>
          </div>
        </div>
        
        <!-- Subcategories -->
        <transition name="slide-down">
          <div 
            v-if="expandedCategories.includes(category.id)"
            class="subcategory-list"
          >
            <div 
              v-for="subcategory in category.subcategories"
              :key="subcategory.id"
              class="subcategory-item"
              :class="{ 'is-active': selectedSubcategory === subcategory.id }"
              @click="selectSubcategory(category.id, subcategory.id)"
            >
              <span class="subcategory-name">{{ subcategory.name }}</span>
              <span v-if="getSubcategoryProductCount(category.id, subcategory.id)" class="subcategory-count">
                {{ getSubcategoryProductCount(category.id, subcategory.id) }}
              </span>
            </div>
          </div>
        </transition>
      </div>
    </div>
    
    <!-- Filter Actions -->
    <div class="filter-actions">
      <button 
        @click="clearFilters"
        class="clear-btn"
        :disabled="!selectedCategory"
      >
        Clear Filters
      </button>
      <button 
        @click="applyFilters"
        class="apply-btn"
        :disabled="!selectedCategory"
      >
        Apply Filters
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { getAllCategories, getSubcategoriesByCategory } from '../data/categories.js'

export default {
  name: 'CategoryFilter',
  props: {
    products: {
      type: Array,
      default: () => []
    },
    initialCategory: {
      type: String,
      default: ''
    },
    initialSubcategory: {
      type: String,
      default: ''
    }
  },
  emits: ['category-change', 'subcategory-change', 'filter-apply'],
  setup(props, { emit }) {
    const categories = ref([])
    const selectedCategory = ref(props.initialCategory)
    const selectedSubcategory = ref(props.initialSubcategory)
    const expandedCategories = ref([])
    const allExpanded = ref(false)
    
    // Load categories with subcategories
    const loadCategories = () => {
      const allCats = getAllCategories()
      categories.value = allCats.map(cat => ({
        ...cat,
        subcategories: getSubcategoriesByCategory(cat.id)
      }))
    }
    
    // Toggle category expansion
    const toggleCategory = (categoryId) => {
      const index = expandedCategories.value.indexOf(categoryId)
      if (index > -1) {
        expandedCategories.value.splice(index, 1)
      } else {
        expandedCategories.value.push(categoryId)
      }
    }
    
    // Toggle all categories
    const toggleAllCategories = () => {
      if (allExpanded.value) {
        expandedCategories.value = []
      } else {
        expandedCategories.value = categories.value.map(cat => cat.id)
      }
      allExpanded.value = !allExpanded.value
    }
    
    // Select category
    const selectCategory = (categoryId) => {
      selectedCategory.value = categoryId
      selectedSubcategory.value = ''
      emit('category-change', categoryId)
    }
    
    // Select subcategory
    const selectSubcategory = (categoryId, subcategoryId) => {
      selectedCategory.value = categoryId
      selectedSubcategory.value = subcategoryId
      emit('subcategory-change', { categoryId, subcategoryId })
    }
    
    // Get product count for category
    const getProductCount = (categoryId) => {
      return props.products.filter(product => product.category === categoryId).length
    }
    
    // Get product count for subcategory
    const getSubcategoryProductCount = (categoryId, subcategoryId) => {
      return props.products.filter(product => 
        product.category === categoryId && product.subcategory === subcategoryId
      ).length
    }
    
    // Clear filters
    const clearFilters = () => {
      selectedCategory.value = ''
      selectedSubcategory.value = ''
      emit('filter-apply', { category: '', subcategory: '' })
    }
    
    // Apply filters
    const applyFilters = () => {
      emit('filter-apply', { 
        category: selectedCategory.value, 
        subcategory: selectedSubcategory.value 
      })
    }
    
    onMounted(() => {
      loadCategories()
      // Auto-expand selected category
      if (selectedCategory.value) {
        expandedCategories.value.push(selectedCategory.value)
      }
    })
    
    return {
      categories,
      selectedCategory,
      selectedSubcategory,
      expandedCategories,
      allExpanded,
      toggleCategory,
      toggleAllCategories,
      selectCategory,
      selectSubcategory,
      getProductCount,
      getSubcategoryProductCount,
      clearFilters,
      applyFilters
    }
  }
}
</script>

<style scoped>
.category-filter {
  @apply bg-white rounded-lg shadow-md p-6;
}

.category-header {
  @apply flex justify-between items-center mb-6 pb-4 border-b border-gray-200;
}

.category-title {
  @apply text-lg font-semibold text-gray-800;
}

.toggle-btn {
  @apply text-sm text-blue-600 hover:text-blue-700 font-medium;
}

.category-list {
  @apply space-y-2;
}

.category-item {
  @apply border border-gray-200 rounded-lg overflow-hidden transition-all duration-200;
}

.category-item.is-active {
  @apply border-blue-500 bg-blue-50;
}

.category-main {
  @apply flex items-center justify-between p-4 cursor-pointer hover:bg-gray-50 transition-colors;
}

.category-info {
  @apply flex items-center gap-3;
}

.category-icon {
  @apply text-2xl;
}

.category-details {
  @apply flex-1;
}

.category-name {
  @apply font-semibold text-gray-800 mb-1;
}

.category-description {
  @apply text-sm text-gray-600;
}

.category-actions {
  @apply flex items-center gap-3;
}

.product-count {
  @apply text-sm text-gray-500;
}

.expand-btn {
  @apply p-1 rounded hover:bg-gray-200 transition-colors;
}

.subcategory-list {
  @apply bg-gray-50 border-t border-gray-200;
}

.subcategory-item {
  @apply flex items-center justify-between px-4 py-3 cursor-pointer hover:bg-gray-100 transition-colors;
}

.subcategory-item.is-active {
  @apply bg-blue-100 text-blue-700;
}

.subcategory-name {
  @apply text-sm font-medium;
}

.subcategory-count {
  @apply text-xs text-gray-500 bg-gray-200 px-2 py-1 rounded-full;
}

.filter-actions {
  @apply flex gap-3 mt-6 pt-6 border-t border-gray-200;
}

.clear-btn {
  @apply px-4 py-2 text-gray-600 hover:text-gray-800 font-medium transition-colors disabled:opacity-50 disabled:cursor-not-allowed;
}

.apply-btn {
  @apply px-4 py-2 bg-blue-600 text-white rounded-lg hover:bg-blue-700 transition-colors disabled:opacity-50 disabled:cursor-not-allowed;
}

/* Transitions */
.slide-down-enter-active, .slide-down-leave-active {
  @apply transition-all duration-300;
}

.slide-down-enter-from {
  @apply opacity-0 transform -translate-y-2;
}

.slide-down-leave-to {
  @apply opacity-0 transform -translate-y-2;
}
</style>
