import { createApp } from 'vue'
import { createRouter, createWebHistory } from 'vue-router'
import App from './App.vue'
import './style.css'

// Import components
import Home from './views/Home.vue'
import Cart from './views/Cart.vue'
import Admin from './views/Admin.vue'
import Orders from './views/Orders.vue'
import Order from './views/Order.vue'

// Import Vue.js components
import ProductCard from './components/ProductCard.vue'
import ShoppingCart from './components/ShoppingCart.vue'
import SearchFilter from './components/SearchFilter.vue'

// Define routes with Vue.js features
const routes = [
  { 
    path: '/', 
    component: Home,
    name: 'home',
    meta: {
      title: 'Home - KAFUKA Electronics Store',
      description: 'Welcome to KAFUKA Electronics Store - Your trusted electronics partner'
    }
  },
  { 
    path: '/cart', 
    component: Cart,
    name: 'cart',
    meta: {
      title: 'Shopping Cart - KAFUKA Electronics Store',
      description: 'View and manage your shopping cart'
    }
  },
  { 
    path: '/admin', 
    component: Admin,
    name: 'admin',
    meta: {
      title: 'Admin Panel - KAFUKA Electronics Store',
      description: 'Manage products and orders'
    }
  },
  { 
    path: '/orders', 
    component: Orders,
    name: 'orders',
    meta: {
      title: 'My Orders - KAFUKA Electronics Store',
      description: 'View your order history'
    }
  },
  { 
    path: '/order/:id', 
    component: Order, 
    name: 'order-detail',
    props: true,
    meta: {
      title: 'Order Details - KAFUKA Electronics Store',
      description: 'View detailed order information'
    }
  }
]

// Create router with Vue.js navigation guards
const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    if (savedPosition) {
      return savedPosition
    } else {
      return { top: 0 }
    }
  }
})

// Vue.js navigation guards
router.beforeEach((to, from, next) => {
  // Update page title
  if (to.meta.title) {
    document.title = to.meta.title
  }
  
  // Update meta description
  if (to.meta.description) {
    const metaDescription = document.querySelector('meta[name="description"]')
    if (metaDescription) {
      metaDescription.setAttribute('content', to.meta.description)
    } else {
      const meta = document.createElement('meta')
      meta.name = 'description'
      meta.content = to.meta.description
      document.head.appendChild(meta)
    }
  }
  
  next()
})

router.afterEach((to, from) => {
  // Analytics or logging could go here
  console.log(`Navigated from ${from.path} to ${to.path}`)
})

// Create and mount Vue.js app with enhanced features
const app = createApp(App)

// Register global components
app.component('ProductCard', ProductCard)
app.component('ShoppingCart', ShoppingCart)
app.component('SearchFilter', SearchFilter)

// Use router
app.use(router)

// Global properties
app.config.globalProperties.$appName = 'KAFUKA Electronics Store'
app.config.globalProperties.$version = '1.0.0'

// Global error handler
app.config.errorHandler = (err, vm, info) => {
  console.error('Vue.js Error:', err, info)
  // You could send this to an error tracking service
}

// Global warning handler
app.config.warnHandler = (msg, vm, trace) => {
  console.warn('Vue.js Warning:', msg, trace)
}

// Custom directive for lazy loading
app.directive('lazy', {
  mounted(el, binding) {
    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          el.src = binding.value
          observer.unobserve(el)
        }
      })
    })
    
    observer.observe(el)
  }
})

// Custom directive for auto-focus
app.directive('focus', {
  mounted(el) {
    el.focus()
  }
})

// Custom directive for click-outside
app.directive('click-outside', {
  mounted(el, binding) {
    el.clickOutsideEvent = function(event) {
      if (!(el === event.target || el.contains(event.target))) {
        binding.value(event)
      }
    }
    document.addEventListener('click', el.clickOutsideEvent)
  },
  unmounted(el) {
    document.removeEventListener('click', el.clickOutsideEvent)
  }
})

// Mount the app
app.mount('#app')

// Export for testing
export { app, router }
