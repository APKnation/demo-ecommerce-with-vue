<template>
  <div class="fixed inset-0 bg-black/50 flex items-center justify-center z-50 p-4">
    <div 
      class="bg-white rounded-2xl shadow-2xl max-w-2xl w-full max-h-[90vh] overflow-hidden"
      @click.stop
    >
      <!-- Modal Header -->
      <div class="bg-gradient-to-r from-primary-600 to-secondary-600 text-white p-6">
        <div class="flex items-center justify-between">
          <div>
            <h2 class="text-2xl font-bold mb-2">Share Your Wishlist</h2>
            <p class="text-white/80">Share your favorite products with friends and family</p>
          </div>
          <button 
            @click="$emit('close')"
            class="w-10 h-10 bg-white/20 backdrop-blur-sm rounded-full flex items-center justify-center hover:bg-white/30 transition-colors"
          >
            <svg class="w-6 h-6 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
      </div>

      <!-- Modal Content -->
      <div class="p-6 overflow-auto max-h-[calc(90vh-120px)]">
        <!-- Wishlist Summary -->
        <div class="bg-gradient-to-r from-neutral-50 to-neutral-100 p-6 rounded-xl mb-6">
          <div class="flex items-center justify-between">
            <div>
              <h3 class="text-lg font-semibold text-neutral-900 mb-1">Your Wishlist</h3>
              <p class="text-neutral-600">{{ wishlist.length }} items • Total: Tsh {{ totalValue.toLocaleString() }}</p>
            </div>
            <div class="w-16 h-16 bg-gradient-to-br from-red-500 to-pink-600 rounded-xl flex items-center justify-center">
              <svg class="w-8 h-8 text-white" fill="currentColor" viewBox="0 0 24 24">
                <path d="M12 21.35l-1.45-1.32C5.4 15.36 2 12.28 2 8.5 2 5.42 4.42 3 7.5 3c1.74 0 3.41.81 4.5 2.09C13.09 3.81 14.76 3 16.5 3 19.58 3 22 5.42 22 8.5c0 3.78-3.4 6.86-8.55 11.54L12 21.35z"/>
              </svg>
            </div>
          </div>
        </div>

        <!-- Share Options -->
        <div class="space-y-4">
          <!-- Copy Link -->
          <div class="border border-neutral-200 rounded-lg p-4">
            <h4 class="font-semibold text-neutral-900 mb-3">Share Link</h4>
            <div class="flex gap-2">
              <input 
                :value="shareableLink"
                readonly
                class="flex-grow px-4 py-2 border border-neutral-300 rounded-lg bg-neutral-50"
              >
              <button 
                @click="copyLink"
                class="btn btn-primary"
              >
                <svg class="w-5 h-5 mr-2" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 5H6a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2v-1M8 5a2 2 0 002 2h2a2 2 0 002-2M8 5a2 2 0 012-2h2a2 2 0 012 2m0 0h2a2 2 0 012 2v3m2 4H10m0 0l3-3m-3 3l3 3"></path>
                </svg>
                {{ copied ? 'Copied!' : 'Copy Link' }}
              </button>
            </div>
          </div>

          <!-- Social Media -->
          <div class="border border-neutral-200 rounded-lg p-4">
            <h4 class="font-semibold text-neutral-900 mb-3">Share on Social Media</h4>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-3">
              <button 
                @click="shareOnSocial('facebook')"
                class="flex flex-col items-center p-3 border border-neutral-200 rounded-lg hover:bg-neutral-50 transition-colors"
              >
                <div class="w-8 h-8 bg-blue-600 rounded-full flex items-center justify-center mb-2">
                  <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M24 12.073c0-6.627-5.373-12-12-12s-12 5.373-12 12c0 5.99 4.388 10.954 10.125 11.854v-8.385H7.078v-3.47h3.047V9.43c0-3.007 1.792-4.669 4.533-4.669 1.312 0 2.686.235 2.686.235v2.953H15.83c-1.491 0-1.956.925-1.956 1.874v2.25h3.328l-.532 3.47h-2.796v8.385C19.612 23.027 24 18.062 24 12.073z"/>
                  </svg>
                </div>
                <span class="text-sm text-neutral-700">Facebook</span>
              </button>

              <button 
                @click="shareOnSocial('twitter')"
                class="flex flex-col items-center p-3 border border-neutral-200 rounded-lg hover:bg-neutral-50 transition-colors"
              >
                <div class="w-8 h-8 bg-sky-500 rounded-full flex items-center justify-center mb-2">
                  <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z"/>
                  </svg>
                </div>
                <span class="text-sm text-neutral-700">Twitter</span>
              </button>

              <button 
                @click="shareOnSocial('whatsapp')"
                class="flex flex-col items-center p-3 border border-neutral-200 rounded-lg hover:bg-neutral-50 transition-colors"
              >
                <div class="w-8 h-8 bg-green-500 rounded-full flex items-center justify-center mb-2">
                  <svg class="w-5 h-5 text-white" fill="currentColor" viewBox="0 0 24 24">
                    <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.149-.67.149-.197.297-.767.966-.94 1.163-.173.197-.347.223-.644.074-.297-.149-1.255-.462-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.297-.347.446-.521.151-.172.2-.296.3-.495.099-.198.05-.371-.05-.521-.05-.149-.445-1.075-.645-1.472-.2-.397-.398-.345-.598-.345-.198 0-.447-.025-.696-.025-.25 0-.645.099-.995.495-.349.397-1.348 1.319-1.348 3.219 0 1.9 1.395 3.732 1.593 3.947.198.215 2.792 4.265 6.777 5.983.945.408 1.693.646 2.27.839.945.297 1.845.128 2.543-.074.698-.203 2.143-.887 2.442-1.742.298-.855.298-1.593.223-1.742-.075-.149-.273-.247-.57-.397z"/>
                  </svg>
                </div>
                <span class="text-sm text-neutral-700">WhatsApp</span>
              </button>

              <button 
                @click="shareOnSocial('email')"
                class="flex flex-col items-center p-3 border border-neutral-200 rounded-lg hover:bg-neutral-50 transition-colors"
              >
                <div class="w-8 h-8 bg-red-500 rounded-full flex items-center justify-center mb-2">
                  <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 8l7.89 5.26a2 2 0 002.22 0L21 8M5 19h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"></path>
                  </svg>
                </div>
                <span class="text-sm text-neutral-700">Email</span>
              </button>
            </div>
          </div>

          <!-- QR Code -->
          <div class="border border-neutral-200 rounded-lg p-4">
            <h4 class="font-semibold text-neutral-900 mb-3">QR Code</h4>
            <div class="flex items-center gap-4">
              <div class="w-32 h-32 bg-neutral-100 rounded-lg flex items-center justify-center">
                <svg class="w-16 h-16 text-neutral-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                  <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 4v1m6 11h2m-6 0h-2v4m0-11v3m0 0h.01M12 12h4.01M16 20h4M4 12h4m12 0h.01M5 8h2a1 1 0 001-1V5a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1zm12 0h2a1 1 0 001-1V5a1 1 0 00-1-1h-2a1 1 0 00-1 1v2a1 1 0 001 1zM5 20h2a1 1 0 001-1v-2a1 1 0 00-1-1H5a1 1 0 00-1 1v2a1 1 0 001 1z"></path>
                </svg>
              </div>
              <div>
                <p class="text-sm text-neutral-600 mb-2">Scan this QR code to view the wishlist</p>
                <button 
                  @click="downloadQR"
                  class="btn btn-outline btn-sm"
                >
                  Download QR Code
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { ref, computed } from 'vue'

export default {
  name: 'ShareWishlistModal',
  props: {
    wishlist: {
      type: Array,
      default: () => []
    }
  },
  emits: ['close'],
  setup(props) {
    const copied = ref(false)

    const totalValue = computed(() => {
      return props.wishlist.reduce((total, product) => {
        const price = product.discount 
          ? product.price * (1 - product.discount / 100)
          : product.price
        return total + price
      }, 0)
    })

    const shareableLink = computed(() => {
      // In a real app, this would generate a unique shareable URL
      return `https://kafuka-electronics.com/wishlist/${generateWishlistId()}`
    })

    const generateWishlistId = () => {
      return Math.random().toString(36).substr(2, 9)
    }

    const copyLink = async () => {
      try {
        await navigator.clipboard.writeText(shareableLink.value)
        copied.value = true
        setTimeout(() => {
          copied.value = false
        }, 2000)
      } catch (err) {
        console.error('Failed to copy link:', err)
      }
    }

    const shareOnSocial = (platform) => {
      const url = shareableLink.value
      const text = `Check out my wishlist with ${props.wishlist.length} items! Total value: Tsh ${totalValue.value.toLocaleString()}`
      
      let shareUrl = ''
      
      switch (platform) {
        case 'facebook':
          shareUrl = `https://www.facebook.com/sharer/sharer.php?u=${encodeURIComponent(url)}`
          break
        case 'twitter':
          shareUrl = `https://twitter.com/intent/tweet?text=${encodeURIComponent(text)}&url=${encodeURIComponent(url)}`
          break
        case 'whatsapp':
          shareUrl = `https://wa.me/?text=${encodeURIComponent(text + ' ' + url)}`
          break
        case 'email':
          shareUrl = `mailto:?subject=My Wishlist&body=${encodeURIComponent(text + '\n\n' + url)}`
          break
      }
      
      window.open(shareUrl, '_blank', 'width=600,height=400')
    }

    const downloadQR = () => {
      // In a real app, this would generate and download a QR code image
      console.log('Download QR code functionality')
    }

    return {
      copied,
      totalValue,
      shareableLink,
      copyLink,
      shareOnSocial,
      downloadQR
    }
  }
}
</script>
