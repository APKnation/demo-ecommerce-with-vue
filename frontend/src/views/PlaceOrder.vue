<template>
  <div class="min-h-screen bg-gradient-to-br from-gray-50 via-white to-gray-100">
    <!-- Header -->
    <div class="bg-white shadow-sm border-b border-gray-200">
      <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-6">
        <div class="flex items-center justify-between">
          <div class="flex items-center space-x-3">
            <div class="w-10 h-10 bg-gradient-to-br from-green-500 to-green-600 rounded-xl flex items-center justify-center shadow-lg">
              <span class="text-white text-xl font-bold">📦</span>
            </div>
            <h1 class="text-3xl font-bold bg-gradient-to-r from-green-600 to-green-700 bg-clip-text text-transparent">Place Order</h1>
          </div>
          <router-link to="/cart" class="text-blue-600 hover:text-blue-800">
            ← Back to Cart
          </router-link>
        </div>
      </div>
    </div>

    <!-- Main Content -->
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">
      <div class="grid grid-cols-1 lg:grid-cols-3 gap-8">
        
        <!-- Order Summary -->
        <div class="lg:col-span-2">
          <div class="bg-white rounded-2xl shadow-lg border border-gray-200 overflow-hidden">
            <div class="p-6 bg-gradient-to-r from-green-50 to-green-100 border-b border-gray-200">
              <h2 class="text-xl font-bold text-gray-800">Order Summary</h2>
            </div>
            
            <div class="p-6">
              <!-- Cart Items -->
              <div class="space-y-4 mb-6">
                <div v-for="(item, index) in cartItems" :key="index" class="flex justify-between items-center p-4 bg-gray-50 rounded-xl">
                  <div class="flex items-center space-x-4">
                    <img 
                      :src="getProductImage(item.product || item)" 
                      :alt="item.product?.title || item.name || 'Product'" 
                      class="w-16 h-16 object-cover rounded-lg"
                    >
                    <div>
                      <h4 class="font-semibold text-gray-800">{{ item.product?.title || item.name || 'Unknown Product' }}</h4>
                      <p class="text-gray-600">Quantity: {{ item.quantity }}</p>
                      <p class="text-gray-600">Price: Tsh {{ Number(item.price || item.product?.price || 0).toLocaleString() }}</p>
                    </div>
                  </div>
                  <div class="text-right">
                    <p class="font-bold text-gray-800">Tsh {{ (item.quantity * Number(item.price || item.product?.price || 0)).toLocaleString() }}</p>
                  </div>
                </div>
              </div>

              <!-- Order Form -->
              <form @submit.prevent="handleSubmit" class="space-y-6">
                <!-- Shipping Address -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Shipping Address</label>
                  <textarea
                    v-model="orderForm.shipping_address"
                    rows="3"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                    placeholder="Enter your shipping address"
                    required
                  ></textarea>
                </div>

                <!-- Notes -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Order Notes (Optional)</label>
                  <textarea
                    v-model="orderForm.notes"
                    rows="2"
                    class="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-green-500 focus:border-transparent"
                    placeholder="Any special instructions..."
                  ></textarea>
                </div>

                <!-- Payment Method -->
                <div>
                  <label class="block text-sm font-medium text-gray-700 mb-2">Payment Method</label>
                  <div class="space-y-2">
                    <label class="flex items-center">
                      <input type="radio" v-model="orderForm.payment_method" value="cash" class="mr-2">
                      <span>Cash on Delivery</span>
                    </label>
                    <label class="flex items-center">
                      <input type="radio" v-model="orderForm.payment_method" value="mobile" class="mr-2">
                      <span>Mobile Money</span>
                    </label>
                  </div>
                </div>

                <!-- Submit Button -->
                <button
                  type="submit"
                  :disabled="isProcessing || cartItems.length === 0"
                  class="w-full py-3 bg-gradient-to-r from-green-500 to-green-600 text-white font-semibold rounded-xl hover:from-green-600 hover:to-green-700 transition-all duration-300 transform hover:scale-105 shadow-lg disabled:opacity-50 disabled:cursor-not-allowed"
                >
                  <span v-if="isProcessing">Processing...</span>
                  <span v-else>Place Order • Tsh {{ totalPrice.toLocaleString() }}</span>
                </button>
              </form>
            </div>
          </div>
        </div>

        <!-- Order Total -->
        <div class="lg:col-span-1">
          <div class="bg-white rounded-2xl shadow-lg border border-gray-200 p-6 sticky top-6">
            <h3 class="text-lg font-bold text-gray-800 mb-4">Order Total</h3>
            
            <div class="space-y-2 mb-4">
              <div class="flex justify-between text-gray-600">
                <span>Subtotal ({{ cartItems.length }} items)</span>
                <span>Tsh {{ totalPrice.toLocaleString() }}</span>
              </div>
              <div class="flex justify-between text-gray-600">
                <span>Shipping</span>
                <span>Tsh 0</span>
              </div>
              <div class="flex justify-between text-gray-600">
                <span>Tax</span>
                <span>Tsh 0</span>
              </div>
              <div class="border-t pt-2">
                <div class="flex justify-between font-bold text-lg">
                  <span>Total</span>
                  <span class="text-green-600">Tsh {{ totalPrice.toLocaleString() }}</span>
                </div>
              </div>
            </div>

            <!-- Order Info -->
            <div class="bg-blue-50 rounded-lg p-4">
              <h4 class="font-semibold text-blue-800 mb-2">Order Information</h4>
              <ul class="text-sm text-blue-700 space-y-1">
                <li>• Order confirmation will be sent to your email</li>
                <li>• Estimated delivery: 3-5 business days</li>
                <li>• You can track your order status</li>
                <li>• 24/7 customer support available</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { useUnifiedCart } from '../composables/useUnifiedCart'
import { useOrderManagement } from '../composables/useOrderManagement'
import Swal from 'sweetalert2'

export default {
  name: 'PlaceOrder',
  setup() {
    const router = useRouter()
    const unifiedCart = useUnifiedCart()
    const orderManagement = useOrderManagement()
    
    const isProcessing = ref(false)
    
    const orderForm = ref({
      shipping_address: '',
      notes: '',
      payment_method: 'cash'
    })

    // Computed properties
    const cartItems = computed(() => unifiedCart?.cartItems?.value || [])
    const totalPrice = computed(() => unifiedCart?.totalPrice?.value || 0)

    // Methods
    const getProductImage = (item) => {
      if (item.product?.image) return item.product.image
      if (item.image) return item.image
      return '/images/placeholder.jpg'
    }

    const handleSubmit = async () => {
      if (cartItems.value.length === 0) {
        Swal.fire('Error', 'Your cart is empty', 'error')
        return
      }

      isProcessing.value = true

      try {
        // Create order from cart
        const result = await orderManagement.createOrderFromCart(
          cartItems.value,
          orderForm.value.shipping_address,
          orderForm.value.notes
        )

        // Show success message
        await Swal.fire({
          icon: 'success',
          title: 'Order Placed Successfully!',
          html: `
            <p>Order #${result.order.order_number || result.order.id}</p>
            <p>Total: Tsh ${totalPrice.value.toLocaleString()}</p>
            <p class="text-sm text-gray-600">You can track your order in Order History</p>
          `,
          confirmButtonText: 'View Order Details',
          showCancelButton: true,
          cancelButtonText: 'Continue Shopping'
        })

        // Save order data for success page
        const orderData = {
          items: cartItems.value,
          total: totalPrice.value,
          paymentMethod: orderForm.value.payment_method,
          orderNumber: result.order.order_number || result.order.id
        }
        localStorage.setItem('recentOrder', JSON.stringify(orderData))

        // Clear cart
        await unifiedCart.clearCart()

        // Navigate to success page
        router.push({
          path: '/order-success',
          query: {
            order: result.order.order_number || result.order.id,
            total: totalPrice.value,
            payment: orderForm.value.payment_method
          }
        })

      } catch (error) {
        console.error('Order placement error:', error)
        Swal.fire('Error', error.message || 'Failed to place order', 'error')
      } finally {
        isProcessing.value = false
      }
    }

    onMounted(() => {
      // Load cart
      unifiedCart.loadCart()
    })

    return {
      cartItems,
      totalPrice,
      orderForm,
      isProcessing,
      getProductImage,
      handleSubmit
    }
  }
}
</script>
