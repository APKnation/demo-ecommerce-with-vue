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

// Define routes
const routes = [
  { path: '/', component: Home },
  { path: '/cart', component: Cart },
  { path: '/admin', component: Admin },
  { path: '/orders', component: Orders },
  { path: '/order/:id', component: Order, props: true }
]

// Create router
const router = createRouter({
  history: createWebHistory(),
  routes
})

// Create and mount app
const app = createApp(App)
app.use(router)
app.mount('#app')
