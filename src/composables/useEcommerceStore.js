import { reactive, computed } from 'vue'
import { useCart, useWishlist, useCompare } from './useEcommerce.js'

export const useEcommerceStore = () => {
  // Use composables for state management
  const { cart, addToCart, removeFromCart, updateQuantity, clearCart, totalItems, totalPrice, isEmpty: cartIsEmpty } = useCart()
  const { wishlist, toggleWishlist, isInWishlist, wishlistCount, isEmpty: wishlistIsEmpty } = useWishlist()
  const { compareList, addToCompare, removeFromCompare, isInCompare, compareCount, canCompare, isFull } = useCompare()
  
  // Reactive state
  const state = reactive({
    isLoading: false,
    searchQuery: '',
    selectedCategory: '',
    priceRange: { min: '', max: '' },
    sortBy: 'name',
    products: [],
    filteredProducts: []
  })
  
  // Computed properties
  const cartBadgeCount = computed(() => totalItems.value)
  const wishlistBadgeCount = computed(() => wishlistCount.value)
  const compareBadgeCount = computed(() => compareCount.value)
  
  const hasItemsInCart = computed(() => !cartIsEmpty.value)
  const hasItemsInWishlist = computed(() => !wishlistIsEmpty.value)
  const canCompareProducts = computed(() => canCompare.value)
  const compareListFull = computed(() => isFull.value)
  
  // Product filtering
  const filterProducts = () => {
    let filtered = [...state.products]
    
    // Apply search filter
    if (state.searchQuery) {
      const query = state.searchQuery.toLowerCase()
      filtered = filtered.filter(product => 
        product.name.toLowerCase().includes(query) ||
        product.category.toLowerCase().includes(query)
      )
    }
    
    // Apply category filter
    if (state.selectedCategory) {
      filtered = filtered.filter(product => product.category === state.selectedCategory)
    }
    
    // Apply price range filter
    if (state.priceRange.min) {
      filtered = filtered.filter(product => product.price >= state.priceRange.min)
    }
    if (state.priceRange.max) {
      filtered = filtered.filter(product => product.price <= state.priceRange.max)
    }
    
    // Apply sorting
    switch (state.sortBy) {
      case 'name':
        filtered.sort((a, b) => a.name.localeCompare(b.name))
        break
      case 'price-low':
        filtered.sort((a, b) => a.price - b.price)
        break
      case 'price-high':
        filtered.sort((a, b) => b.price - a.price)
        break
      case 'newest':
        filtered.sort((a, b) => (b.isNew ? 1 : 0) - (a.isNew ? 1 : 0))
        break
    }
    
    state.filteredProducts = filtered
  }
  
  // Actions
  const setLoading = (loading) => {
    state.isLoading = loading
  }
  
  const setProducts = (products) => {
    state.products = products
    filterProducts()
  }
  
  const setSearchQuery = (query) => {
    state.searchQuery = query
    filterProducts()
  }
  
  const setSelectedCategory = (category) => {
    state.selectedCategory = category
    filterProducts()
  }
  
  const setPriceRange = (range) => {
    state.priceRange = range
    filterProducts()
  }
  
  const setSortBy = (sort) => {
    state.sortBy = sort
    filterProducts()
  }
  
  const clearFilters = () => {
    state.searchQuery = ''
    state.selectedCategory = ''
    state.priceRange = { min: '', max: '' }
    state.sortBy = 'name'
    filterProducts()
  }
  
  // Product actions
  const addProductToCart = (product) => {
    addToCart(product)
  }
  
  const removeProductFromCart = (index) => {
    removeFromCart(index)
  }
  
  const updateProductQuantity = (index, change) => {
    updateQuantity(index, change)
  }
  
  const clearShoppingCart = () => {
    clearCart()
  }
  
  const toggleProductWishlist = (product) => {
    toggleWishlist(product)
  }
  
  const addProductToCompare = (product) => {
    addToCompare(product)
  }
  
  const removeProductFromCompare = (index) => {
    removeFromCompare(index)
  }
  
  // Utility methods
  const getProductInCart = (productName) => {
    return cart.value.find(item => item.name === productName)
  }
  
  const getProductQuantity = (productName) => {
    const item = getProductInCart(productName)
    return item ? item.quantity : 0
  }
  
  const getCategories = () => {
    return [...new Set(state.products.map(product => product.category))]
  }
  
  const getPriceRange = () => {
    if (state.products.length === 0) return { min: 0, max: 0 }
    
    const prices = state.products.map(product => product.price)
    return {
      min: Math.min(...prices),
      max: Math.max(...prices)
    }
  }
  
  // Initialize with sample products
  const initializeProducts = () => {
    const sampleProducts = [
      {
        name: 'iPhone 15 Pro',
        price: 2500000,
        category: 'phones',
        image: '/images/iphone.jpg',
        isNew: true,
        discount: 10,
        stock: 15
      },
      {
        name: 'Samsung Galaxy S24',
        price: 2200000,
        category: 'phones',
        image: '/images/samsung.jpg',
        isNew: true,
        stock: 20
      },
      {
        name: 'MacBook Pro',
        price: 4500000,
        category: 'laptops',
        image: '/images/macbook.jpg',
        isNew: false,
        discount: 5,
        stock: 8
      },
      {
        name: 'Dell XPS 13',
        price: 1800000,
        category: 'laptops',
        image: '/images/dell.jpg',
        isNew: false,
        stock: 12
      },
      {
        name: 'AirPods Pro',
        price: 450000,
        category: 'accessories',
        image: '/images/airpods.jpg',
        isNew: true,
        stock: 25
      },
      {
        name: 'Sony WH-1000XM5',
        price: 650000,
        category: 'accessories',
        image: '/images/sony.jpg',
        isNew: false,
        discount: 15,
        stock: 10
      }
    ]
    
    setProducts(sampleProducts)
  }
  
  return {
    // State
    state,
    
    // Cart
    cart,
    addToCart: addProductToCart,
    removeFromCart: removeProductFromCart,
    updateQuantity: updateProductQuantity,
    clearCart: clearShoppingCart,
    totalItems,
    totalPrice,
    cartIsEmpty,
    cartBadgeCount,
    hasItemsInCart,
    
    // Wishlist
    wishlist,
    toggleWishlist: toggleProductWishlist,
    isInWishlist,
    wishlistCount,
    wishlistIsEmpty,
    wishlistBadgeCount,
    hasItemsInWishlist,
    
    // Compare
    compareList,
    addToCompare: addProductToCompare,
    removeFromCompare: removeProductFromCompare,
    isInCompare,
    compareCount,
    canCompare: canCompareProducts,
    isFull: compareListFull,
    compareBadgeCount,
    
    // Products
    products: computed(() => state.products),
    filteredProducts: computed(() => state.filteredProducts),
    isLoading: computed(() => state.isLoading),
    searchQuery: computed(() => state.searchQuery),
    selectedCategory: computed(() => state.selectedCategory),
    priceRange: computed(() => state.priceRange),
    sortBy: computed(() => state.sortBy),
    
    // Actions
    setLoading,
    setProducts,
    setSearchQuery,
    setSelectedCategory,
    setPriceRange,
    setSortBy,
    clearFilters,
    filterProducts,
    
    // Utilities
    getProductInCart,
    getProductQuantity,
    getCategories,
    getPriceRange,
    initializeProducts
  }
}
