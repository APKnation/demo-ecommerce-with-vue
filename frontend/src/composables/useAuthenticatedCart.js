import { ref, computed } from 'vue'

const API_BASE_URL = 'http://localhost:8000/api'

export function useAuthenticatedCart() {
  const cartItems = ref([])
  const isLoading = ref(false)
  const error = ref(null)

  // Calculate total price
  const totalPrice = computed(() => {
    return cartItems.value.reduce((total, item) => {
      return total + (item.quantity * item.product.price)
    }, 0)
  })

  // Calculate total items count
  const totalItems = computed(() => {
    return cartItems.value.reduce((total, item) => {
      return total + item.quantity
    }, 0)
  })

  // Load cart from backend
  const loadCart = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Not authenticated')
    }

    isLoading.value = true
    error.value = null

    try {
      const response = await fetch(`${API_BASE_URL}/orders/cart/`, {
        headers: {
          'Authorization': `Token ${token}`
        }
      })

      if (response.ok) {
        const cartData = await response.json()
        cartItems.value = cartData.items || []
        console.log('Cart data received:', cartData)
      } else {
        console.warn('Failed to load cart from backend, using empty cart')
        cartItems.value = []
      }
    } catch (error) {
      console.error('Error loading cart:', error)
      cartItems.value = []
    } finally {
      isLoading.value = false
    }
  }

  // Add item to cart
  const addToCart = async (productId, quantity = 1) => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Not authenticated')
    }

    try {
      const response = await fetch(`${API_BASE_URL}/orders/cart/add/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          product_id: productId,
          quantity: quantity
        })
      })

      if (response.ok) {
        await loadCart() // Reload cart to get updated items
        return { success: true }
      } else {
        const errorData = await response.json()
        throw new Error(errorData.error || 'Failed to add to cart')
      }
    } catch (error) {
      console.error('Error adding to cart:', error)
      throw error
    }
  }

  // Update cart item quantity
  const updateQuantity = async (itemId, quantity) => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Not authenticated')
    }

    try {
      const response = await fetch(`${API_BASE_URL}/orders/cart/items/${itemId}/`, {
        method: 'PUT',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          quantity: quantity
        })
      })

      if (response.ok) {
        await loadCart() // Reload cart to get updated items
        return { success: true }
      } else {
        const errorData = await response.json()
        throw new Error(errorData.error || 'Failed to update cart')
      }
    } catch (error) {
      console.error('Error updating cart:', error)
      throw error
    }
  }

  // Remove item from cart
  const removeFromCart = async (itemId) => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Not authenticated')
    }

    try {
      const response = await fetch(`${API_BASE_URL}/orders/cart/items/${itemId}/`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Token ${token}`
        }
      })

      if (response.ok) {
        await loadCart() // Reload cart to get updated items
        return { success: true }
      } else {
        const errorData = await response.json()
        throw new Error(errorData.error || 'Failed to remove from cart')
      }
    } catch (error) {
      console.error('Error removing from cart:', error)
      throw error
    }
  }

  // Clear cart
  const clearCart = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Not authenticated')
    }

    try {
      // Remove all items one by one
      const itemsToRemove = [...cartItems.value]
      for (const item of itemsToRemove) {
        await removeFromCart(item.id)
      }
      return { success: true }
    } catch (error) {
      console.error('Error clearing cart:', error)
      throw error
    }
  }

  return {
    cartItems,
    isLoading,
    error,
    totalPrice,
    totalItems,
    loadCart,
    addToCart,
    updateQuantity,
    removeFromCart,
    clearCart
  }
}
