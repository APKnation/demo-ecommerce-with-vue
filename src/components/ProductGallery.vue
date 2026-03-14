<template>
  <div class="product-gallery" :class="{ 'is-loading': isLoading }">
    <div class="gallery-header">
      <h3 class="gallery-title">{{ title }}</h3>
      <div class="gallery-controls">
        <button 
          @click="previousImage" 
          class="control-btn"
          :disabled="!hasPrevious"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"></path>
          </svg>
        </button>
        
        <span class="image-counter">{{ currentImageIndex + 1 }} / {{ images.length }}</span>
        
        <button 
          @click="nextImage" 
          class="control-btn"
          :disabled="!hasNext"
        >
          <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"></path>
          </svg>
        </button>
      </div>
    </div>
    
    <div class="gallery-main">
      <transition name="fade" mode="out-in">
        <img
          :key="currentImageIndex"
          :src="currentImage"
          :alt="`Product image ${currentImageIndex + 1}`"
          class="gallery-image"
          @load="handleImageLoad"
          @error="handleImageError"
        >
      </transition>
    </div>
    
    <div class="gallery-thumbnails">
      <button
        v-for="(image, index) in images"
        :key="index"
        @click="selectImage(index)"
        class="thumbnail-btn"
        :class="{ 'is-active': index === currentImageIndex }"
      >
        <img
          :src="image"
          :alt="`Thumbnail ${index + 1}`"
          class="thumbnail-image"
        >
      </button>
    </div>
    
    <div v-if="showZoom" class="zoom-overlay" @click="closeZoom">
      <img
        :src="currentImage"
        :alt="`Zoomed product image ${currentImageIndex + 1}`"
        class="zoom-image"
      >
      <button class="zoom-close-btn">
        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
        </svg>
      </button>
    </div>
  </div>
</template>

<script>
import { ref, computed, watch } from 'vue'

export default {
  name: 'ProductGallery',
  props: {
    images: {
      type: Array,
      required: true,
      default: () => []
    },
    title: {
      type: String,
      default: 'Product Gallery'
    },
    initialIndex: {
      type: Number,
      default: 0
    },
    isLoading: {
      type: Boolean,
      default: false
    }
  },
  emits: ['image-change', 'image-load', 'image-error'],
  setup(props, { emit }) {
    const currentImageIndex = ref(props.initialIndex)
    const showZoom = ref(false)
    
    const currentImage = computed(() => {
      return props.images[currentImageIndex.value] || ''
    })
    
    const hasPrevious = computed(() => {
      return currentImageIndex.value > 0
    })
    
    const hasNext = computed(() => {
      return currentImageIndex.value < props.images.length - 1
    })
    
    const selectImage = (index) => {
      if (index >= 0 && index < props.images.length) {
        currentImageIndex.value = index
        emit('image-change', {
          index,
          image: props.images[index]
        })
      }
    }
    
    const nextImage = () => {
      if (hasNext.value) {
        selectImage(currentImageIndex.value + 1)
      }
    }
    
    const previousImage = () => {
      if (hasPrevious.value) {
        selectImage(currentImageIndex.value - 1)
      }
    }
    
    const openZoom = () => {
      showZoom.value = true
    }
    
    const closeZoom = () => {
      showZoom.value = false
    }
    
    const handleImageLoad = (event) => {
      emit('image-load', {
        index: currentImageIndex.value,
        image: props.images[currentImageIndex.value],
        event
      })
    }
    
    const handleImageError = (event) => {
      emit('image-error', {
        index: currentImageIndex.value,
        image: props.images[currentImageIndex.value],
        event
      })
    }
    
    // Keyboard navigation
    const handleKeydown = (event) => {
      switch (event.key) {
        case 'ArrowLeft':
          previousImage()
          break
        case 'ArrowRight':
          nextImage()
          break
        case 'Escape':
          if (showZoom.value) {
            closeZoom()
          }
          break
        case 'Enter':
        case ' ':
          if (!showZoom.value) {
            openZoom()
          }
          break
      }
    }
    
    // Watch for prop changes
    watch(() => props.initialIndex, (newIndex) => {
      if (newIndex >= 0 && newIndex < props.images.length) {
        currentImageIndex.value = newIndex
      }
    })
    
    // Add keyboard event listeners
    const addKeyboardListeners = () => {
      document.addEventListener('keydown', handleKeydown)
    }
    
    const removeKeyboardListeners = () => {
      document.removeEventListener('keydown', handleKeydown)
    }
    
    return {
      currentImageIndex,
      currentImage,
      hasPrevious,
      hasNext,
      showZoom,
      selectImage,
      nextImage,
      previousImage,
      openZoom,
      closeZoom,
      handleImageLoad,
      handleImageError,
      addKeyboardListeners,
      removeKeyboardListeners
    }
  },
  mounted() {
    this.addKeyboardListeners()
  },
  beforeUnmount() {
    this.removeKeyboardListeners()
  }
}
</script>

<style scoped>
.product-gallery {
  @apply bg-white rounded-lg shadow-lg overflow-hidden;
}

.gallery-header {
  @apply flex justify-between items-center p-4 border-b border-gray-200;
}

.gallery-title {
  @apply text-lg font-semibold text-gray-800;
}

.gallery-controls {
  @apply flex items-center gap-4;
}

.control-btn {
  @apply p-2 rounded-full bg-gray-100 hover:bg-gray-200 disabled:opacity-50 disabled:cursor-not-allowed transition-colors;
}

.image-counter {
  @apply text-sm text-gray-600 font-medium;
}

.gallery-main {
  @apply relative h-96 bg-gray-100 flex items-center justify-center;
}

.gallery-image {
  @apply max-w-full max-h-full object-contain cursor-pointer;
}

.gallery-thumbnails {
  @apply flex gap-2 p-4 overflow-x-auto;
}

.thumbnail-btn {
  @apply flex-shrink-0 border-2 border-transparent rounded-lg overflow-hidden transition-all;
}

.thumbnail-btn.is-active {
  @apply border-blue-500;
}

.thumbnail-btn:hover {
  @apply border-gray-300;
}

.thumbnail-image {
  @apply w-16 h-16 object-cover;
}

.zoom-overlay {
  @apply fixed inset-0 bg-black bg-opacity-90 flex items-center justify-center z-50 cursor-pointer;
}

.zoom-image {
  @apply max-w-[22.5rem] max-h-[16rem] object-contain;
}

.zoom-close-btn {
  @apply absolute top-4 right-4 p-2 bg-white rounded-full hover:bg-gray-100 transition-colors;
}

.fade-enter-active, .fade-leave-active {
  @apply transition-opacity duration-300;
}

.fade-enter-from, .fade-leave-to {
  @apply opacity-0;
}

.is-loading .gallery-image {
  @apply opacity-50;
}

.is-loading .gallery-main::after {
  content: '';
  @apply absolute inset-0 bg-white bg-opacity-50 flex items-center justify-center;
}

.is-loading .gallery-main::before {
  content: 'Loading...';
  @apply absolute text-gray-600 font-medium;
}
</style>
