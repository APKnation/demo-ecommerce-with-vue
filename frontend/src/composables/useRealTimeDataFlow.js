import { ref, computed, watch } from 'vue'
import { useAuth } from './useAuth'

const API_BASE_URL = 'http://localhost:8000/api'

export function useRealTimeDataFlow() {
  const { user, isAuthenticated } = useAuth()
  
  // Real-time data stores
  const globalOrders = ref([])
  const globalProducts = ref([])
  const globalUsers = ref([])
  const notifications = ref([])
  
  // WebSocket connection for real-time updates
  const wsConnection = ref(null)
  const isConnected = ref(false)
  
  // Role-specific data filters
  const customerOrders = computed(() => {
    if (!user.value || user.value.role !== 'customer') return []
    return globalOrders.value.filter(order => order.customer === user.value.id)
  })
  
  const vendorOrders = computed(() => {
    if (!user.value || user.value.role !== 'vendor') return []
    return globalOrders.value.filter(order => 
      order.items.some(item => item.product.vendor === user.value.id)
    )
  })
  
  const vendorProducts = computed(() => {
    if (!user.value || user.value.role !== 'vendor') return []
    return globalProducts.value.filter(product => product.vendor === user.value.id)
  })
  
  const adminData = computed(() => {
    if (!user.value || user.value.role !== 'admin') return null
    return {
      orders: globalOrders.value,
      products: globalProducts.value,
      users: globalUsers.value,
      stats: calculateAdminStats()
    }
  })
  
  // Initialize WebSocket connection
  const initWebSocket = () => {
    if (!isAuthenticated.value) return
    
    try {
      wsConnection.value = new WebSocket('ws://localhost:8000/ws/ecommerce/')
      
      wsConnection.value.onopen = () => {
        isConnected.value = true
        console.log('WebSocket connected for real-time updates')
        
        // Subscribe to role-specific channels
        subscribeToChannels()
      }
      
      wsConnection.value.onmessage = (event) => {
        const data = JSON.parse(event.data)
        handleRealTimeUpdate(data)
      }
      
      wsConnection.value.onclose = () => {
        isConnected.value = false
        console.log('WebSocket disconnected')
        // Attempt to reconnect after 3 seconds
        setTimeout(initWebSocket, 3000)
      }
      
      wsConnection.value.onerror = (error) => {
        console.error('WebSocket error:', error)
        isConnected.value = false
      }
    } catch (error) {
      console.error('Failed to initialize WebSocket:', error)
      // Fallback to polling
      startPolling()
    }
  }
  
  // Subscribe to role-specific channels
  const subscribeToChannels = () => {
    if (!wsConnection.value || !user.value) return
    
    const subscription = {
      type: 'subscribe',
      role: user.value.role,
      user_id: user.value.id
    }
    
    wsConnection.value.send(JSON.stringify(subscription))
  }
  
  // Handle real-time updates
  const handleRealTimeUpdate = (data) => {
    switch (data.type) {
      case 'order_created':
        handleOrderCreated(data.payload)
        break
      case 'order_updated':
        handleOrderUpdated(data.payload)
        break
      case 'product_created':
        handleProductCreated(data.payload)
        break
      case 'product_updated':
        handleProductUpdated(data.payload)
        break
      case 'user_registered':
        handleUserRegistered(data.payload)
        break
      case 'notification':
        handleNotification(data.payload)
        break
    }
  }
  
  // Order event handlers
  const handleOrderCreated = (order) => {
    globalOrders.value.unshift(order)
    
    // Send notifications to relevant parties
    if (user.value?.role === 'admin') {
      addNotification({
        type: 'order',
        message: `New order #${order.order_number} received`,
        level: 'info',
        data: order
      })
    }
    
    if (user.value?.role === 'vendor' && orderHasVendorProducts(order)) {
      addNotification({
        type: 'order',
        message: `New order #${order.order_number} contains your products`,
        level: 'success',
        data: order
      })
    }
  }
  
  const handleOrderUpdated = (order) => {
    const index = globalOrders.value.findIndex(o => o.id === order.id)
    if (index !== -1) {
      globalOrders.value[index] = order
    }
    
    // Notify customers about order status changes
    if (user.value?.role === 'customer' && order.customer === user.value.id) {
      addNotification({
        type: 'order_status',
        message: `Order #${order.order_number} status: ${order.status}`,
        level: 'info',
        data: order
      })
    }
  }
  
  // Product event handlers
  const handleProductCreated = (product) => {
    globalProducts.value.unshift(product)
    
    if (user.value?.role === 'admin') {
      addNotification({
        type: 'product',
        message: `New product "${product.title}" added by vendor`,
        level: 'info',
        data: product
      })
    }
  }
  
  const handleProductUpdated = (product) => {
    const index = globalProducts.value.findIndex(p => p.id === product.id)
    if (index !== -1) {
      globalProducts.value[index] = product
    }
  }
  
  // User event handlers
  const handleUserRegistered = (newUser) => {
    globalUsers.value.push(newUser)
    
    if (user.value?.role === 'admin') {
      addNotification({
        type: 'user',
        message: `New ${newUser.role} registered: ${newUser.username}`,
        level: 'info',
        data: newUser
      })
    }
  }
  
  // Notification handler
  const handleNotification = (notification) => {
    addNotification(notification)
  }
  
  // Add notification to store
  const addNotification = (notification) => {
    notifications.value.unshift({
      ...notification,
      id: Date.now(),
      timestamp: new Date().toISOString()
    })
    
    // Keep only last 50 notifications
    if (notifications.value.length > 50) {
      notifications.value = notifications.value.slice(0, 50)
    }
  }
  
  // Check if order contains vendor's products
  const orderHasVendorProducts = (order) => {
    if (!user.value || user.value.role !== 'vendor') return false
    
    return order.items.some(item => 
      item.product && item.product.vendor === user.value.id
    )
  }
  
  // Calculate admin statistics
  const calculateAdminStats = () => {
    return {
      totalOrders: globalOrders.value.length,
      pendingOrders: globalOrders.value.filter(o => o.status === 'pending').length,
      totalProducts: globalProducts.value.length,
      activeProducts: globalProducts.value.filter(p => p.is_active).length,
      totalUsers: globalUsers.value.length,
      activeVendors: globalUsers.value.filter(u => u.role === 'vendor' && u.is_active).length,
      totalRevenue: globalOrders.value
        .filter(o => o.status === 'completed')
        .reduce((sum, order) => sum + Number(order.total_amount || 0), 0)
    }
  }
  
  // Polling fallback for when WebSocket is not available
  let pollingInterval = null
  const startPolling = () => {
    if (pollingInterval) return
    
    pollingInterval = setInterval(async () => {
      await fetchLatestData()
    }, 10000) // Poll every 10 seconds
  }
  
  const stopPolling = () => {
    if (pollingInterval) {
      clearInterval(pollingInterval)
      pollingInterval = null
    }
  }
  
  // Fetch latest data from API
  const fetchLatestData = async () => {
    if (!isAuthenticated.value) return
    
    try {
      const token = localStorage.getItem('token')
      const headers = {
        'Authorization': `Token ${token}`,
        'Content-Type': 'application/json'
      }
      
      // Fetch data based on user role
      if (user.value?.role === 'admin') {
        const [ordersRes, productsRes, usersRes] = await Promise.all([
          fetch(`${API_BASE_URL}/orders/admin/all/`, { headers }),
          fetch(`${API_BASE_URL}/products/`, { headers }),
          fetch(`${API_BASE_URL}/accounts/admin/users/`, { headers })
        ])
        
        if (ordersRes.ok) globalOrders.value = await ordersRes.json()
        if (productsRes.ok) globalProducts.value = await productsRes.json()
        if (usersRes.ok) globalUsers.value = await usersRes.json()
      } else if (user.value?.role === 'vendor') {
        const [ordersRes, productsRes] = await Promise.all([
          fetch(`${API_BASE_URL}/orders/vendor/orders/`, { headers }),
          fetch(`${API_BASE_URL}/products/vendor/`, { headers })
        ])
        
        if (ordersRes.ok) globalOrders.value = await ordersRes.json()
        if (productsRes.ok) globalProducts.value = await productsRes.json()
      } else if (user.value?.role === 'customer') {
        const ordersRes = await fetch(`${API_BASE_URL}/orders/`, { headers })
        if (ordersRes.ok) globalOrders.value = await ordersRes.json()
      }
    } catch (error) {
      console.error('Error fetching latest data:', error)
    }
  }
  
  // Send data updates to other users
  const broadcastUpdate = (type, payload) => {
    if (!wsConnection.value || !isConnected.value) return
    
    const message = {
      type: 'broadcast',
      sender_role: user.value?.role,
      sender_id: user.value?.id,
      data_type: type,
      payload: payload
    }
    
    wsConnection.value.send(JSON.stringify(message))
  }
  
  // Initialize data flow
  const initialize = () => {
    if (isAuthenticated.value) {
      fetchLatestData()
      initWebSocket()
    }
  }
  
  // Cleanup
  const cleanup = () => {
    if (wsConnection.value) {
      wsConnection.value.close()
      wsConnection.value = null
    }
    stopPolling()
  }
  
  // Watch for authentication changes
  watch(isAuthenticated, (newValue) => {
    if (newValue) {
      initialize()
    } else {
      cleanup()
      // Clear data
      globalOrders.value = []
      globalProducts.value = []
      globalUsers.value = []
      notifications.value = []
    }
  }, { immediate: true })
  
  return {
    // Data
    globalOrders,
    globalProducts,
    globalUsers,
    notifications,
    isConnected,
    
    // Computed
    customerOrders,
    vendorOrders,
    vendorProducts,
    adminData,
    
    // Methods
    initialize,
    cleanup,
    broadcastUpdate,
    addNotification,
    fetchLatestData
  }
}
