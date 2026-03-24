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
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        }
      })

      if (!response.ok) {
        throw new Error('Failed to load cart')
      }

      const data = await response.json()
      cartItems.value = data.items || []
      return data
    } catch (err) {
      error.value = err.message
      throw err
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

    isLoading.value = true
    error.value = null

    try {
      const response = await fetch(`${API_BASE_URL}/orders/cart/add/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          product_id: productId,
          quantity: quantity
        })
      })

      if (!response.ok) {
        const data = await response.json()
        throw new Error(data.error || 'Failed to add item to cart')
      }

      // Reload cart to get updated items
      await loadCart()
      return { success: true }
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      isLoading.value = false
    }
  }

  // Update cart item quantity
  const updateCartItem = async (itemId, quantity) => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Not authenticated')
    }

    isLoading.value = true
    error.value = null

    try {
      const response = await fetch(`${API_BASE_URL}/orders/cart/items/${itemId}/`, {
        method: 'PUT',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          quantity: quantity
        })
      })

      if (!response.ok) {
        const data = await response.json()
        throw new Error(data.error || 'Failed to update cart item')
      }

      // Reload cart to get updated items
      await loadCart()
      return { success: true }
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      isLoading.value = false
    }
  }

  // Remove item from cart
  const removeFromCart = async (itemId) => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Not authenticated')
    }

    isLoading.value = true
    error.value = null

    try {
      const response = await fetch(`${API_BASE_URL}/orders/cart/items/${itemId}/`, {
        method: 'DELETE',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        }
      })

      if (!response.ok) {
        const data = await response.json()
        throw new Error(data.error || 'Failed to remove item from cart')
      }

      // Reload cart to get updated items
      await loadCart()
      return { success: true }
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      isLoading.value = false
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
    updateCartItem,
    removeFromCart
  }
}
