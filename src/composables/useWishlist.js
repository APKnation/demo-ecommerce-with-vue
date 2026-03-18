import { ref, computed } from 'vue'
import { useStorage } from './useStorage.js'

export function useWishlist() {
  const wishlist = useStorage('wishlist', [])

  const addToWishlist = (product) => {
    const productToAdd = product.value || product
    if (!isInWishlist(productToAdd)) {
      wishlist.value.push(productToAdd)
      showNotification('Product added to wishlist', 'success')
    } else {
      showNotification('Product already in wishlist', 'warning')
    }
  }

  const removeFromWishlist = (product) => {
    const productToRemove = product.value || product
    const index = wishlist.value.findIndex(p => p.id === productToRemove.id)
    if (index > -1) {
      wishlist.value.splice(index, 1)
      showNotification('Product removed from wishlist', 'info')
    }
  }

  const toggleWishlist = (product) => {
    const productToToggle = product.value || product
    if (isInWishlist(productToToggle)) {
      removeFromWishlist(productToToggle)
    } else {
      addToWishlist(productToToggle)
    }
  }

  const clearWishlist = () => {
    wishlist.value = []
    showNotification('Wishlist cleared', 'info')
  }

  const isInWishlist = (product) => {
    return wishlist.value.some(p => p.id === product.id)
  }

  const wishlistCount = computed(() => wishlist.value.length)

  const wishlistTotal = computed(() => {
    return wishlist.value.reduce((total, product) => {
      const price = product.discount 
        ? product.price * (1 - product.discount / 100)
        : product.price
      return total + price
    }, 0)
  })

  const showNotification = (message, type = 'info') => {
    // This would integrate with your notification system
    // For now, just log to console to avoid errors
    if (typeof console !== 'undefined') {
      console.log(`${type}: ${message}`)
    }
  }

  return {
    wishlist,
    addToWishlist,
    removeFromWishlist,
    toggleWishlist,
    clearWishlist,
    isInWishlist,
    wishlistCount,
    wishlistTotal
  }
}
