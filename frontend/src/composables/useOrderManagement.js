import { ref, computed } from 'vue'

const API_BASE_URL = 'http://localhost:8000/api'

export function useOrderManagement() {
  const orders = ref([])
  const isLoading = ref(false)
  const error = ref(null)
  const currentOrder = ref(null)

  // Order status options
  const orderStatuses = {
    PENDING: 'Pending',
    PAID: 'Paid',
    SHIPPED: 'Shipped',
    DELIVERED: 'Delivered',
    CANCELLED: 'Cancelled'
  }

  // Status colors for UI
  const statusColors = {
    'Pending': 'bg-yellow-100 text-yellow-800',
    'Paid': 'bg-blue-100 text-blue-800',
    'Shipped': 'bg-purple-100 text-purple-800',
    'Delivered': 'bg-green-100 text-green-800',
    'Cancelled': 'bg-red-100 text-red-800'
  }

  // Calculate total spent
  const totalSpent = computed(() => {
    console.log('=== ORDERS TOTAL SPENT DEBUG ===')
    console.log('orders.value:', orders.value)
    console.log('Number of orders:', orders.value.length)
    
    const total = orders.value.reduce((total, order) => {
      const orderTotal = Number(order.total_amount || order.total || 0)
      console.log(`Order ${order.id || 'unknown'}: ${order.total_amount || order.total || 0} -> ${orderTotal}`)
      return total + orderTotal
    }, 0)
    
    console.log('Raw total:', total)
    const roundedTotal = Math.round(total)
    console.log('Rounded total:', roundedTotal)
    console.log('=== END DEBUG ===')
    return roundedTotal
  })

  // Calculate pending orders count
  const pendingOrders = computed(() => {
    return orders.value.filter(order => order.status === 'Pending').length
  })

  // Sort orders by date (newest first)
  const sortedOrders = computed(() => {
    return [...orders.value].sort((a, b) => {
      const dateA = new Date(a.created_at || a.date)
      const dateB = new Date(b.created_at || b.date)
      return dateB - dateA
    })
  })

  // Place a new order
  const placeOrder = async (orderData) => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Authentication required to place order')
    }

    isLoading.value = true
    error.value = null

    try {
      const response = await fetch(`${API_BASE_URL}/orders/`, {
        method: 'POST',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(orderData)
      })

      if (!response.ok) {
        const data = await response.json()
        // If backend fails, fallback to localStorage
        console.warn('Backend API failed, using localStorage fallback:', data.error || 'API Error')
        return createOrderInLocalStorage(orderData)
      }

      const newOrder = await response.json()
      orders.value.unshift(newOrder)
      currentOrder.value = newOrder
      
      return { success: true, order: newOrder }
    } catch (err) {
      console.warn('Backend API error, using localStorage fallback:', err)
      // Fallback to localStorage when network fails
      return createOrderInLocalStorage(orderData)
    } finally {
      isLoading.value = false
    }
  }

  // Create order in localStorage (fallback when backend fails)
  const createOrderInLocalStorage = (orderData) => {
    const newOrder = {
      id: Date.now(), // Use timestamp as ID
      order_number: `ORD-${Date.now()}`,
      items: orderData.items,
      shipping_address: orderData.shipping_address,
      notes: orderData.notes,
      total_amount: orderData.total_amount,
      status: 'pending',
      payment_method: orderData.payment_method || 'cash',
      created_at: new Date().toISOString(),
      updated_at: new Date().toISOString(),
      user: localStorage.getItem('user') ? JSON.parse(localStorage.getItem('user')).id : null
    }

    // Save to localStorage
    saveOrderToLocalStorage(newOrder)
    
    return { success: true, order: newOrder }
  }

  // Load order history
  const loadOrderHistory = async () => {
    const token = localStorage.getItem('token')
    if (!token) {
      // For guest users, load from localStorage
      const savedOrders = localStorage.getItem('orders')
      if (savedOrders) {
        orders.value = JSON.parse(savedOrders)
      }
      return
    }

    isLoading.value = true
    error.value = null

    try {
      const response = await fetch(`${API_BASE_URL}/orders/`, {
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        }
      })

      if (!response.ok) {
        // If backend fails, load from localStorage
        console.warn('Backend API failed, loading orders from localStorage')
        const savedOrders = localStorage.getItem('orders')
        if (savedOrders) {
          orders.value = JSON.parse(savedOrders)
        }
        return orders.value
      }

      const data = await response.json()
      orders.value = Array.isArray(data) ? data : (data.results || [])
      
      // Also merge with localStorage orders for complete history
      const savedOrders = localStorage.getItem('orders')
      if (savedOrders) {
        const localOrders = JSON.parse(savedOrders)
        // Merge backend and local orders, avoiding duplicates
        const allOrders = [...orders.value, ...localOrders]
        const uniqueOrders = allOrders.filter((order, index, self) =>
          index === self.findIndex((o) => o.id === order.id || o.order_number === order.order_number)
        )
        orders.value = uniqueOrders.sort((a, b) => new Date(b.created_at) - new Date(a.created_at))
      }
      
      return orders.value
    } catch (err) {
      console.warn('Backend API error, loading orders from localStorage:', err)
      // Fallback to localStorage when network fails
      const savedOrders = localStorage.getItem('orders')
      if (savedOrders) {
        orders.value = JSON.parse(savedOrders)
      }
      return orders.value
    } finally {
      isLoading.value = false
    }
  }

  // Get order details by ID
  const getOrderDetails = async (orderId) => {
    const token = localStorage.getItem('token')
    
    try {
      let order
      if (token) {
        // Authenticated user - fetch from API
        const response = await fetch(`${API_BASE_URL}/orders/${orderId}/`, {
          headers: {
            'Authorization': `Token ${token}`,
            'Content-Type': 'application/json',
          }
        })

        if (!response.ok) {
          throw new Error('Failed to load order details')
        }
        order = await response.json()
      } else {
        // Guest user - find in localStorage
        const savedOrders = JSON.parse(localStorage.getItem('orders') || '[]')
        order = savedOrders.find(o => o.id === orderId)
      }

      currentOrder.value = order
      return order
    } catch (err) {
      error.value = err.message
      throw err
    }
  }

  // Update order status (admin function)
  const updateOrderStatus = async (orderId, status) => {
    const token = localStorage.getItem('token')
    if (!token) {
      throw new Error('Authentication required')
    }

    try {
      const response = await fetch(`${API_BASE_URL}/orders/${orderId}/update-status/`, {
        method: 'PATCH',
        headers: {
          'Authorization': `Token ${token}`,
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ status })
      })

      if (!response.ok) {
        const data = await response.json()
        throw new Error(data.error || 'Failed to update order status')
      }

      const updatedOrder = await response.json()
      
      // Update order in local state
      const index = orders.value.findIndex(order => order.id === orderId)
      if (index > -1) {
        orders.value[index] = updatedOrder
      }

      if (currentOrder.value?.id === orderId) {
        currentOrder.value = updatedOrder
      }

      return { success: true, order: updatedOrder }
    } catch (err) {
      error.value = err.message
      throw err
    }
  }

  // Cancel order
  const cancelOrder = async (orderId) => {
    return updateOrderStatus(orderId, 'CANCELLED')
  }

  // Mark order as paid
  const markOrderAsPaid = async (orderId) => {
    return updateOrderStatus(orderId, 'PAID')
  }

  // Mark order as shipped
  const markOrderAsShipped = async (orderId) => {
    return updateOrderStatus(orderId, 'SHIPPED')
  }

  // Mark order as delivered
  const markOrderAsDelivered = async (orderId) => {
    return updateOrderStatus(orderId, 'DELIVERED')
  }

  // Format date for display
  const formatDate = (dateString) => {
    if (!dateString) return 'Unknown date'
    
    const date = new Date(dateString)
    return date.toLocaleDateString('en-US', {
      year: 'numeric',
      month: 'short',
      day: 'numeric',
      hour: '2-digit',
      minute: '2-digit'
    })
  }

  // Get status color class
  const getStatusClass = (status) => {
    return statusColors[status] || 'bg-gray-100 text-gray-800'
  }

  // Create order from cart
  const createOrderFromCart = async (cartItems, shippingAddress = null, notes = '') => {
    if (!cartItems || cartItems.length === 0) {
      throw new Error('Cart is empty')
    }

    const orderData = {
      items: cartItems.map(item => ({
        product: item.product?.id || item.id,
        quantity: item.quantity,
        price: item.price || item.product?.price
      })),
      shipping_address: shippingAddress,
      notes: notes,
      total_amount: cartItems.reduce((total, item) => {
        return total + (item.quantity * Number(item.price || item.product?.price || 0))
      }, 0)
    }

    return await placeOrder(orderData)
  }

  // Save order to localStorage (for guests)
  const saveOrderToLocalStorage = (order) => {
    const existingOrders = JSON.parse(localStorage.getItem('orders') || '[]')
    existingOrders.unshift(order)
    localStorage.setItem('orders', JSON.stringify(existingOrders))
    orders.value = existingOrders
  }

  return {
    // State
    orders,
    currentOrder,
    isLoading,
    error,
    
    // Computed
    totalSpent,
    pendingOrders,
    sortedOrders,
    
    // Constants
    orderStatuses,
    statusColors,
    
    // Methods
    placeOrder,
    loadOrderHistory,
    getOrderDetails,
    updateOrderStatus,
    cancelOrder,
    markOrderAsPaid,
    markOrderAsShipped,
    markOrderAsDelivered,
    formatDate,
    getStatusClass,
    createOrderFromCart,
    saveOrderToLocalStorage
  }
}
