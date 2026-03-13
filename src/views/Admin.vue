<template>
  <div>
    <h1 class="text-3xl font-bold mb-8">Admin Panel</h1>
    
    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
      <!-- Add Product Section -->
      <div class="card">
        <h2 class="text-xl font-semibold mb-4">Add New Product</h2>
        <form @submit.prevent="addProduct" class="space-y-4">
          <div>
            <label class="block text-sm font-medium mb-2">Product Name</label>
            <input
              v-model="newProduct.name"
              type="text"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
          </div>
          
          <div>
            <label class="block text-sm font-medium mb-2">Price (Tsh)</label>
            <input
              v-model.number="newProduct.price"
              type="number"
              required
              min="0"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
          </div>
          
          <div>
            <label class="block text-sm font-medium mb-2">Category</label>
            <select
              v-model="newProduct.category"
              required
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
              <option value="">Select Category</option>
              <option value="laptops">Laptops</option>
              <option value="phones">Smartphones</option>
              <option value="accessories">Accessories</option>
            </select>
          </div>
          
          <div>
            <label class="block text-sm font-medium mb-2">Image URL</label>
            <input
              v-model="newProduct.image"
              type="text"
              required
              placeholder="/images/product.jpg"
              class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
            >
          </div>
          
          <button type="submit" class="btn btn-primary w-full">
            Add Product
          </button>
        </form>
      </div>
      
      <!-- Statistics Section -->
      <div class="card">
        <h2 class="text-xl font-semibold mb-4">Store Statistics</h2>
        <div class="space-y-4">
          <div class="flex justify-between items-center p-4 bg-blue-50 rounded-lg">
            <span class="font-medium">Total Products</span>
            <span class="text-2xl font-bold text-blue-600">{{ products.length }}</span>
          </div>
          
          <div class="flex justify-between items-center p-4 bg-green-50 rounded-lg">
            <span class="font-medium">Total Orders</span>
            <span class="text-2xl font-bold text-green-600">{{ orders.length }}</span>
          </div>
          
          <div class="flex justify-between items-center p-4 bg-yellow-50 rounded-lg">
            <span class="font-medium">Total Revenue</span>
            <span class="text-2xl font-bold text-yellow-600">Tsh {{ totalRevenue.toLocaleString() }}</span>
          </div>
          
          <div class="flex justify-between items-center p-4 bg-purple-50 rounded-lg">
            <span class="font-medium">Pending Orders</span>
            <span class="text-2xl font-bold text-purple-600">{{ pendingOrders }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'

export default {
  name: 'Admin',
  setup() {
    const products = ref([])
    const orders = ref([])
    const newProduct = ref({
      name: '',
      price: 0,
      category: '',
      image: ''
    })

    // Load data from localStorage
    const loadData = () => {
      const savedProducts = localStorage.getItem('adminProducts')
      if (savedProducts) {
        products.value = JSON.parse(savedProducts)
      } else {
        // Load default products
        products.value = [
          { name: 'Mac Book', price: 1000000, category: 'laptops', image: '/images/w.jpg' },
          { name: 'HP-Brand', price: 150000, category: 'laptops', image: '/images/j.jpg' },
          { name: 'Dell', price: 200000, category: 'laptops', image: '/images/k.jpg' },
          { name: 'Apple', price: 1000000, category: 'phones', image: '/images/d.jpg' },
          { name: 'HP-Elite', price: 1500000, category: 'laptops', image: '/images/a.jpg' },
          { name: 'Sony', price: 200000, category: 'accessories', image: '/images/f.jpg' },
          { name: 'Infinix', price: 400000, category: 'phones', image: '/images/g.jpg' },
          { name: 'iPhone', price: 1500000, category: 'phones', image: '/images/p.jpg' },
          { name: 'Samsung', price: 3000000, category: 'phones', image: '/images/l.jpg' }
        ]
        saveProducts()
      }
      
      orders.value = JSON.parse(localStorage.getItem('orders')) || []
    }

    const saveProducts = () => {
      localStorage.setItem('adminProducts', JSON.stringify(products.value))
    }

    const addProduct = () => {
      products.value.push({ ...newProduct.value })
      saveProducts()
      
      // Reset form
      newProduct.value = {
        name: '',
        price: 0,
        category: '',
        image: ''
      }
      
      alert('Product added successfully!')
    }

    const totalRevenue = computed(() => {
      return orders.value.reduce((total, order) => total + order.total, 0)
    })

    const pendingOrders = computed(() => {
      return orders.value.filter(order => order.status === 'Pending').length
    })

    onMounted(() => {
      loadData()
    })

    return {
      products,
      orders,
      newProduct,
      totalRevenue,
      pendingOrders,
      addProduct
    }
  }
}
</script>
