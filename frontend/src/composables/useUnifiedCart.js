import { ref, computed, watch } from 'vue'
import { useAuth } from './useAuth'
import { useGuestCart } from './useGuestCart'
import { useAuthenticatedCart } from './useAuthenticatedCart'

export function useUnifiedCart() {
  const { isAuthenticated } = useAuth()
  const guestCart = useGuestCart()
  const authenticatedCart = useAuthenticatedCart()
  
  const isLoading = ref(false)
  const error = ref(null)
  const isSyncing = ref(false)

  // Current cart items (switches based on auth state)
  const cartItems = computed(() => {
    try {
      if (!isAuthenticated.value) {
        return guestCart?.cartItems?.value || []
      }
      return authenticatedCart?.cartItems?.value || []
    } catch (error) {
      console.warn('Error in cartItems computed:', error)
      return []
    }
  })

  // Current total price
  const totalPrice = computed(() => {
    try {
      if (!cartItems.value || !Array.isArray(cartItems.value)) {
        return 0
      }
      if (!isAuthenticated.value) {
        return guestCart?.totalPrice?.value || 0
      }
      return authenticatedCart?.totalPrice?.value || 0
    } catch (error) {
      console.warn('Error in totalPrice computed:', error)
      return 0
    }
  })

  // Calculate total items count
  const totalItems = computed(() => {
    try {
      if (!cartItems.value || !Array.isArray(cartItems.value)) {
        return 0
      }
      return cartItems.value.reduce((total, item) => {
        const quantity = item?.quantity || 1
        return total + (typeof quantity === 'number' ? quantity : Number(quantity) || 1)
      }, 0)
    } catch (error) {
      console.warn('Error in totalItems computed:', error)
      return 0
    }
  })

  // Sync guest cart to authenticated cart when user logs in
  const syncGuestToAuthenticated = async () => {
    if (!isAuthenticated.value || guestCart.cartItems.value.length === 0) {
      return
    }

    isSyncing.value = true
    error.value = null

    try {
      // Add each guest cart item to authenticated cart
      for (const item of guestCart.cartItems.value) {
        try {
          await authenticatedCart.addToCart(item.id, item.quantity)
        } catch (err) {
          console.warn(`Failed to sync item ${item.id}:`, err)
        }
      }

      // Clear guest cart after successful sync
      guestCart.clearCart()
      
      // Reload authenticated cart to get final state
      await authenticatedCart.loadCart()
      
      return { success: true, syncedItems: guestCart.cartItems.value.length }
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      isSyncing.value = false
    }
  }

  // Add item to cart (unified)
  const addToCart = async (product, quantity = 1) => {
    if (isAuthenticated.value) {
      try {
        return await authenticatedCart.addToCart(product.id, quantity)
      } catch (err) {
        // Fallback to guest cart if authenticated cart fails
        console.warn('Authenticated cart failed, using guest cart:', err)
        return guestCart.addToCart(product, quantity)
      }
    } else {
      return guestCart.addToCart(product, quantity)
    }
  }

  // Update quantity (unified)
  const updateQuantity = async (itemId, quantity) => {
    if (isAuthenticated.value) {
      try {
        // Find the cart item ID for authenticated cart
        const cartItem = authenticatedCart.cartItems.value.find(item => 
          item.product.id === itemId
        )
        if (cartItem) {
          return await authenticatedCart.updateCartItem(cartItem.id, quantity)
        }
      } catch (err) {
        // Fallback to guest cart
        console.warn('Authenticated cart update failed, using guest cart:', err)
        return guestCart.updateQuantity(itemId, quantity)
      }
    } else {
      return guestCart.updateQuantity(itemId, quantity)
    }
  }

  // Remove from cart (unified)
  const removeFromCart = async (itemId) => {
    if (isAuthenticated.value) {
      try {
        // Find the cart item ID for authenticated cart
        const cartItem = authenticatedCart.cartItems.value.find(item => 
          item.product.id === itemId
        )
        if (cartItem) {
          return await authenticatedCart.removeFromCart(cartItem.id)
        }
      } catch (err) {
        // Fallback to guest cart
        console.warn('Authenticated cart remove failed, using guest cart:', err)
        return guestCart.removeFromCart(itemId)
      }
    } else {
      return guestCart.removeFromCart(itemId)
    }
  }

  // Clear cart (unified)
  const clearCart = async () => {
    if (isAuthenticated.value) {
      try {
        // Clear authenticated cart items one by one
        const items = [...authenticatedCart.cartItems.value]
        for (const item of items) {
          await authenticatedCart.removeFromCart(item.id)
        }
      } catch (err) {
        console.warn('Authenticated cart clear failed:', err)
      }
    }
    
    // Always clear guest cart
    guestCart.clearCart()
  }

  // Load cart (unified)
  const loadCart = async () => {
    if (isAuthenticated.value) {
      try {
        await authenticatedCart.loadCart()
        
        // Sync any remaining guest cart items
        await syncGuestToAuthenticated()
      } catch (err) {
        console.warn('Failed to load authenticated cart:', err)
        error.value = err.message
      }
    } else {
      guestCart.loadCart()
    }
  }

  // Watch for authentication changes and sync carts
  watch(isAuthenticated, async (newValue, oldValue) => {
    try {
      if (newValue && !oldValue) {
        // User just logged in
        console.log('User logged in, syncing carts...')
        await loadCart()
      } else if (!newValue && oldValue) {
        // User just logged out
        console.log('User logged out, clearing authenticated cart data...')
        if (guestCart && guestCart.loadCart) {
          guestCart.loadCart()
        }
      }
    } catch (error) {
      console.warn('Error in authentication watch:', error)
    }
  }, { immediate: true })

  return {
    cartItems,
    isLoading,
    error,
    isSyncing,
    totalPrice,
    totalItems,
    addToCart,
    updateQuantity,
    removeFromCart,
    clearCart,
    loadCart,
    syncGuestToAuthenticated,
    // Expose individual carts for advanced usage
    guestCart,
    authenticatedCart
  }
}
