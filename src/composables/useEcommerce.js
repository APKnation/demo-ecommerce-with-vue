import { ref, computed, watch } from 'vue'
import Swal from 'sweetalert2'

export function useCart() {
  const cart = ref([])
  
  // Load cart from localStorage
  const loadCart = () => {
    const savedCart = localStorage.getItem('cart')
    if (savedCart) {
      cart.value = JSON.parse(savedCart)
    }
  }
  
  // Save cart to localStorage
  const saveCart = () => {
    localStorage.setItem('cart', JSON.stringify(cart.value))
  }
  
  // Add item to cart
  const addToCart = (product) => {
    const existingItem = cart.value.find(item => item.name === product.name)
    
    if (existingItem) {
      existingItem.quantity += 1
      Swal.fire({
        icon: 'info',
        title: 'Quantity Updated',
        text: `${product.name} quantity increased to ${existingItem.quantity}`,
        timer: 2000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    } else {
      cart.value.push({
        ...product,
        quantity: 1
      })
      Swal.fire({
        icon: 'success',
        title: 'Added to Cart',
        text: `${product.name} added to cart successfully`,
        timer: 2000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    }
    
    saveCart()
  }
  
  // Remove item from cart
  const removeFromCart = (index) => {
    const item = cart.value[index]
    cart.value.splice(index, 1)
    saveCart()
    
    Swal.fire({
      icon: 'info',
      title: 'Removed',
      text: `${item.name} removed from cart`,
      timer: 2000,
      toast: true,
      position: 'top-end',
      showConfirmButton: false
    })
  }
  
  // Update item quantity
  const updateQuantity = (index, change) => {
    const item = cart.value[index]
    item.quantity += change
    
    if (item.quantity <= 0) {
      removeFromCart(index)
    } else {
      saveCart()
    }
  }
  
  // Clear cart
  const clearCart = () => {
    Swal.fire({
      title: 'Clear Cart?',
      text: 'Are you sure you want to clear your cart?',
      icon: 'question',
      showCancelButton: true,
      confirmButtonColor: '#ef4444',
      cancelButtonColor: '#6b7280',
      confirmButtonText: 'Clear Cart'
    }).then((result) => {
      if (result.isConfirmed) {
        cart.value = []
        saveCart()
        Swal.fire({
          icon: 'success',
          title: 'Cart Cleared',
          text: 'Your cart has been cleared successfully',
          timer: 2000,
          toast: true,
          position: 'top-end',
          showConfirmButton: false
        })
      }
    })
  }
  
  // Computed properties
  const totalItems = computed(() => {
    return cart.value.reduce((total, item) => total + item.quantity, 0)
  })
  
  const totalPrice = computed(() => {
    return cart.value.reduce((total, item) => total + (item.price * item.quantity), 0)
  })
  
  const isEmpty = computed(() => {
    return cart.value.length === 0
  })
  
  // Watch for changes and save
  watch(cart, saveCart, { deep: true })
  
  // Initialize
  loadCart()
  
  return {
    cart,
    addToCart,
    removeFromCart,
    updateQuantity,
    clearCart,
    totalItems,
    totalPrice,
    isEmpty,
    saveCart,
    loadCart
  }
}

export function useWishlist() {
  const wishlist = ref([])
  
  // Load wishlist from localStorage
  const loadWishlist = () => {
    const savedWishlist = localStorage.getItem('wishlist')
    if (savedWishlist) {
      wishlist.value = JSON.parse(savedWishlist)
    }
  }
  
  // Save wishlist to localStorage
  const saveWishlist = () => {
    localStorage.setItem('wishlist', JSON.stringify(wishlist.value))
  }
  
  // Toggle wishlist item
  const toggleWishlist = (product) => {
    const index = wishlist.value.findIndex(item => item.name === product.name)
    
    if (index > -1) {
      wishlist.value.splice(index, 1)
      Swal.fire({
        icon: 'info',
        title: 'Removed from Wishlist',
        text: `${product.name} removed from wishlist`,
        timer: 2000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    } else {
      wishlist.value.push(product)
      Swal.fire({
        icon: 'success',
        title: 'Added to Wishlist',
        text: `${product.name} added to wishlist`,
        timer: 2000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    }
    
    saveWishlist()
  }
  
  // Check if product is in wishlist
  const isInWishlist = (productName) => {
    return wishlist.value.some(item => item.name === productName)
  }
  
  // Computed properties
  const wishlistCount = computed(() => {
    return wishlist.value.length
  })
  
  const isEmpty = computed(() => {
    return wishlist.value.length === 0
  })
  
  // Watch for changes and save
  watch(wishlist, saveWishlist, { deep: true })
  
  // Initialize
  loadWishlist()
  
  return {
    wishlist,
    toggleWishlist,
    isInWishlist,
    wishlistCount,
    isEmpty,
    saveWishlist,
    loadWishlist
  }
}

export function useCompare() {
  const compareList = ref([])
  
  // Load compare list from localStorage
  const loadCompareList = () => {
    const savedCompareList = localStorage.getItem('compareList')
    if (savedCompareList) {
      compareList.value = JSON.parse(savedCompareList)
    }
  }
  
  // Save compare list to localStorage
  const saveCompareList = () => {
    localStorage.setItem('compareList', JSON.stringify(compareList.value))
  }
  
  // Add to compare list
  const addToCompare = (product) => {
    if (compareList.value.length >= 3) {
      Swal.fire({
        icon: 'warning',
        title: 'Compare Limit',
        text: 'You can compare up to 3 products at a time',
        timer: 3000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
      return
    }
    
    const existingIndex = compareList.value.findIndex(item => item.name === product.name)
    
    if (existingIndex > -1) {
      compareList.value.splice(existingIndex, 1)
      Swal.fire({
        icon: 'info',
        title: 'Removed from Compare',
        text: `${product.name} removed from comparison`,
        timer: 2000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    } else {
      compareList.value.push(product)
      Swal.fire({
        icon: 'success',
        title: 'Added to Compare',
        text: `${product.name} added to comparison`,
        timer: 2000,
        toast: true,
        position: 'top-end',
        showConfirmButton: false
      })
    }
    
    saveCompareList()
  }
  
  // Remove from compare list
  const removeFromCompare = (index) => {
    const item = compareList.value[index]
    compareList.value.splice(index, 1)
    saveCompareList()
    
    Swal.fire({
      icon: 'info',
      title: 'Removed',
      text: `${item.name} removed from comparison`,
      timer: 2000,
      toast: true,
      position: 'top-end',
      showConfirmButton: false
    })
  }
  
  // Check if product is in compare list
  const isInCompare = (productName) => {
    return compareList.value.some(item => item.name === productName)
  }
  
  // Clear compare list
  const clearCompareList = () => {
    compareList.value = []
    saveCompareList()
  }
  
  // Computed properties
  const compareCount = computed(() => {
    return compareList.value.length
  })
  
  const canCompare = computed(() => {
    return compareList.value.length >= 2
  })
  
  const isFull = computed(() => {
    return compareList.value.length >= 3
  })
  
  // Watch for changes and save
  watch(compareList, saveCompareList, { deep: true })
  
  // Initialize
  loadCompareList()
  
  return {
    compareList,
    addToCompare,
    removeFromCompare,
    isInCompare,
    clearCompareList,
    compareCount,
    canCompare,
    isFull,
    saveCompareList,
    loadCompareList
  }
}

export function useNotifications() {
  const showNotification = (message, type = 'success', options = {}) => {
    const defaultOptions = {
      icon: type,
      title: type === 'success' ? 'Success!' : type === 'error' ? 'Error!' : 'Info',
      text: message,
      timer: 3000,
      toast: true,
      position: 'top-end',
      showConfirmButton: false,
      showCancelButton: false
    }
    
    return Swal.fire({ ...defaultOptions, ...options })
  }
  
  const showSuccess = (message, options = {}) => {
    return showNotification(message, 'success', options)
  }
  
  const showError = (message, options = {}) => {
    return showNotification(message, 'error', options)
  }
  
  const showInfo = (message, options = {}) => {
    return showNotification(message, 'info', options)
  }
  
  const showWarning = (message, options = {}) => {
    return showNotification(message, 'warning', options)
  }
  
  const showConfirm = (message, options = {}) => {
    return Swal.fire({
      title: 'Confirm',
      text: message,
      icon: 'question',
      showCancelButton: true,
      confirmButtonColor: '#3b82f6',
      cancelButtonColor: '#6b7280',
      confirmButtonText: 'Confirm',
      cancelButtonText: 'Cancel',
      ...options
    })
  }
  
  return {
    showNotification,
    showSuccess,
    showError,
    showInfo,
    showWarning,
    showConfirm
  }
}
