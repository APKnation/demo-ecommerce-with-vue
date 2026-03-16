import { ref, computed } from 'vue'
import { useStorage } from './useStorage'

export function useWishlist() {
  const wishlist = useStorage('wishlist', [])

  const addToWishlist = (product) => {
    if (!isInWishlist(product.value || product)) {
      wishlist.value.push(product.value || product)
      showNotification('Product added to wishlist', 'success')
    } else {
      showNotification('Product already in wishlist', 'warning')
    }
  }

  const removeFromWishlist = (product) => {
    const index = wishlist.value.findIndex(p => p.id === product.id)
    if (index > -1) {
      wishlist.value.splice(index, 1)
      showNotification('Product removed from wishlist', 'info')
    }
  }

  const toggleWishlist = (product) => {
    if (isInWishlist(product.value || product)) {
      removeFromWishlist(product.value || product)
    } else {
      addToWishlist(product.value || product)
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
    console.log(`${type}: ${message}`)
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
