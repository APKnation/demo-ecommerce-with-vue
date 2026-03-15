<template>
  <div class="product-specifications">
    <h3 class="spec-title">Technical Specifications</h3>
    
    <!-- Category-specific specifications -->
    <div class="spec-sections">
      <!-- General Specifications -->
      <div class="spec-section">
        <h4 class="section-title">General</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Brand</span>
            <span class="spec-value">{{ specifications.brand || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Model</span>
            <span class="spec-value">{{ specifications.model || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Color</span>
            <span class="spec-value">{{ specifications.color || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Weight</span>
            <span class="spec-value">{{ specifications.weight || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Dimensions</span>
            <span class="spec-value">{{ specifications.dimensions || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Warranty</span>
            <span class="spec-value">{{ specifications.warranty || '1 Year' }}</span>
          </div>
        </div>
      </div>
      
      <!-- Category-specific specifications -->
      <div v-if="category === 'smartphones'" class="spec-section">
        <h4 class="section-title">Display & Performance</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Screen Size</span>
            <span class="spec-value">{{ specifications.screen_size || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Resolution</span>
            <span class="spec-value">{{ specifications.resolution || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Processor</span>
            <span class="spec-value">{{ specifications.processor || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">RAM</span>
            <span class="spec-value">{{ specifications.ram || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Storage</span>
            <span class="spec-value">{{ specifications.storage || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Camera</span>
            <span class="spec-value">{{ specifications.camera || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Battery</span>
            <span class="spec-value">{{ specifications.battery || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Operating System</span>
            <span class="spec-value">{{ specifications.os || 'N/A' }}</span>
          </div>
        </div>
      </div>
      
      <div v-else-if="category === 'laptops'" class="spec-section">
        <h4 class="section-title">Performance & Display</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Processor</span>
            <span class="spec-value">{{ specifications.processor || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">RAM</span>
            <span class="spec-value">{{ specifications.ram || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Storage</span>
            <span class="spec-value">{{ specifications.storage || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Graphics</span>
            <span class="spec-value">{{ specifications.graphics || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Screen Size</span>
            <span class="spec-value">{{ specifications.screen_size || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Resolution</span>
            <span class="spec-value">{{ specifications.resolution || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Battery Life</span>
            <span class="spec-value">{{ specifications.battery_life || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Operating System</span>
            <span class="spec-value">{{ specifications.os || 'N/A' }}</span>
          </div>
        </div>
      </div>
      
      <div v-else-if="category === 'headphones'" class="spec-section">
        <h4 class="section-title">Audio Features</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Type</span>
            <span class="spec-value">{{ specifications.type || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Connectivity</span>
            <span class="spec-value">{{ specifications.connectivity || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Battery Life</span>
            <span class="spec-value">{{ specifications.battery_life || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Noise Cancelling</span>
            <span class="spec-value">{{ specifications.noise_cancelling || 'No' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Frequency Response</span>
            <span class="spec-value">{{ specifications.frequency_response || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Driver Size</span>
            <span class="spec-value">{{ specifications.driver_size || 'N/A' }}</span>
          </div>
        </div>
      </div>
      
      <div v-else-if="category === 'wearables'" class="spec-section">
        <h4 class="section-title">Smart Features</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Display</span>
            <span class="spec-value">{{ specifications.display || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Battery Life</span>
            <span class="spec-value">{{ specifications.battery_life || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Water Resistance</span>
            <span class="spec-value">{{ specifications.water_resistance || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Compatibility</span>
            <span class="spec-value">{{ specifications.compatibility || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Health Features</span>
            <span class="spec-value">{{ specifications.health_features || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">GPS</span>
            <span class="spec-value">{{ specifications.gps || 'No' }}</span>
          </div>
        </div>
      </div>
      
      <!-- Camera Specifications -->
      <div v-else-if="category === 'cameras'" class="spec-section">
        <h4 class="section-title">Camera Features</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Sensor Type</span>
            <span class="spec-value">{{ specifications.sensor_type || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Megapixels</span>
            <span class="spec-value">{{ specifications.megapixels || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Lens</span>
            <span class="spec-value">{{ specifications.lens || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Video Resolution</span>
            <span class="spec-value">{{ specifications.video_resolution || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">ISO Range</span>
            <span class="spec-value">{{ specifications.iso_range || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Connectivity</span>
            <span class="spec-value">{{ specifications.connectivity || 'N/A' }}</span>
          </div>
        </div>
      </div>
      
      <!-- Gaming Specifications -->
      <div v-else-if="category === 'gaming'" class="spec-section">
        <h4 class="section-title">Gaming Features</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Platform</span>
            <span class="spec-value">{{ specifications.platform || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Storage</span>
            <span class="spec-value">{{ specifications.storage || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Resolution</span>
            <span class="spec-value">{{ specifications.resolution || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Connectivity</span>
            <span class="spec-value">{{ specifications.connectivity || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Controllers</span>
            <span class="spec-value">{{ specifications.controllers || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Online Features</span>
            <span class="spec-value">{{ specifications.online_features || 'N/A' }}</span>
          </div>
        </div>
      </div>
      
      <!-- Accessories Specifications -->
      <div v-else class="spec-section">
        <h4 class="section-title">Product Details</h4>
        <div class="spec-grid">
          <div class="spec-item">
            <span class="spec-label">Type</span>
            <span class="spec-value">{{ specifications.type || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Compatibility</span>
            <span class="spec-value">{{ specifications.compatibility || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Capacity</span>
            <span class="spec-value">{{ specifications.capacity || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Speed</span>
            <span class="spec-value">{{ specifications.speed || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Interface</span>
            <span class="spec-value">{{ specifications.interface || 'N/A' }}</span>
          </div>
          <div class="spec-item">
            <span class="spec-label">Power Requirements</span>
            <span class="spec-value">{{ specifications.power || 'N/A' }}</span>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Additional Information -->
    <div class="additional-info">
      <h4 class="section-title">What's in the Box</h4>
      <ul class="box-contents">
        <li v-for="item in boxContents" :key="item">{{ item }}</li>
      </ul>
    </div>
  </div>
</template>

<script>
import { computed } from 'vue'

export default {
  name: 'ProductSpecifications',
  props: {
    specifications: {
      type: Object,
      default: () => ({})
    },
    category: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const boxContents = computed(() => {
      const defaultContents = ['Product Unit', 'User Manual', 'Warranty Card']
      
      // Category-specific contents
      const categoryContents = {
        smartphones: ['Phone', 'Charging Cable', 'Power Adapter', 'SIM Ejector Tool'],
        laptops: ['Laptop', 'Power Adapter', 'User Guide'],
        headphones: ['Headphones', 'Charging Cable', 'Carrying Case'],
        wearables: ['Device', 'Charging Cable', 'User Manual'],
        cameras: ['Camera Body', 'Battery', 'Charger', 'Camera Strap'],
        gaming: ['Console', 'Controller', 'Power Cable', 'HDMI Cable']
      }
      
      return categoryContents[props.category] || defaultContents
    })
    
    return {
      boxContents
    }
  }
}
</script>

<style scoped>
.product-specifications {
  @apply space-y-8;
}

.spec-title {
  @apply text-2xl font-bold text-gray-900 mb-6;
}

.spec-sections {
  @apply space-y-8;
}

.spec-section {
  @apply space-y-4;
}

.section-title {
  @apply text-lg font-semibold text-gray-800 border-b border-gray-200 pb-2;
}

.spec-grid {
  @apply grid grid-cols-1 md:grid-cols-2 gap-4;
}

.spec-item {
  @apply flex justify-between py-3 border-b border-gray-100;
}

.spec-label {
  @apply font-medium text-gray-600;
}

.spec-value {
  @apply text-gray-900 font-medium;
}

.additional-info {
  @apply mt-8 p-6 bg-gray-50 rounded-lg;
}

.box-contents {
  @apply list-disc list-inside space-y-2 text-gray-700;
}

@media (max-width: 768px) {
  .spec-grid {
    @apply grid-cols-1;
  }
  
  .spec-item {
    @apply flex-col gap-1;
  }
}
</style>
