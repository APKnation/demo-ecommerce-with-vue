import { ref, computed } from 'vue'

export function useGuestCart() {
  const cartItems = ref([])
  const isLoading = ref(false)
  const error = ref(null)

  // Load cart from localStorage
  const loadCart = () => {
    try {
      const savedCart = localStorage.getItem('guestCart')
      if (savedCart) {
        cartItems.value = JSON.parse(savedCart)
      }
    } catch (err) {
      console.error('Error loading guest cart:', err)
      cartItems.value = []
    }
  }

  // Save cart to localStorage
  const saveCart = () => {
    try {
      localStorage.setItem('guestCart', JSON.stringify(cartItems.value))
    } catch (err) {
      console.error('Error saving guest cart:', err)
    }
  }

  // Calculate total price
  const totalPrice = computed(() => {
    return cartItems.value.reduce((total, item) => {
      return total + (item.quantity * Number(item.price || item.product?.price || 0))
    }, 0)
  })

  // Calculate total items count
  const totalItems = computed(() => {
    return cartItems.value.reduce((total, item) => {
      return total + item.quantity
    }, 0)
  })

  // Add item to cart
  const addToCart = (product, quantity = 1) => {
    isLoading.value = true
    error.value = null

    try {
      const existingItemIndex = cartItems.value.findIndex(item => 
        item.id === product.id || item.product?.id === product.id
      )

      if (existingItemIndex > -1) {
        // Update existing item quantity
        cartItems.value[existingItemIndex].quantity += quantity
      } else {
        // Add new item
        const cartItem = {
          id: product.id,
          product: product,
          name: product.title || product.name,
          price: product.price,
          quantity: quantity,
          image: product.image,
          subtotal: quantity * Number(product.price || 0)
        }
        cartItems.value.push(cartItem)
      }

      saveCart()
      return { success: true }
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      isLoading.value = false
    }
  }

  // Update cart item quantity
  const updateQuantity = (itemId, quantity) => {
    isLoading.value = true
    error.value = null

    try {
      const itemIndex = cartItems.value.findIndex(item => 
        item.id === itemId || item.product?.id === itemId
      )

      if (itemIndex > -1) {
        if (quantity <= 0) {
          cartItems.value.splice(itemIndex, 1)
        } else {
          cartItems.value[itemIndex].quantity = quantity
          cartItems.value[itemIndex].subtotal = quantity * Number(cartItems.value[itemIndex].price || 0)
        }
        saveCart()
      }
      return { success: true }
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      isLoading.value = false
    }
  }

  // Remove item from cart
  const removeFromCart = (itemId) => {
    isLoading.value = true
    error.value = null

    try {
      const itemIndex = cartItems.value.findIndex(item => 
        item.id === itemId || item.product?.id === itemId
      )

      if (itemIndex > -1) {
        cartItems.value.splice(itemIndex, 1)
        saveCart()
      }
      return { success: true }
    } catch (err) {
      error.value = err.message
      throw err
    } finally {
      isLoading.value = false
    }
  }

  // Clear entire cart
  const clearCart = () => {
    cartItems.value = []
    localStorage.removeItem('guestCart')
  }

  // Initialize cart on load
  loadCart()

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
