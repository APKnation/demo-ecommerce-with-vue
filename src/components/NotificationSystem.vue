<template>
  <teleport to="body">
    <transition-group name="notification" tag="div" class="notification-container">
      <div
        v-for="notification in notifications"
        :key="notification.id"
        :class="getNotificationClasses(notification)"
        class="notification-item"
        @click="removeNotification(notification.id)"
      >
        <div class="notification-content">
          <div class="notification-icon">
            <component :is="getIconComponent(notification.type)" />
          </div>
          
          <div class="notification-text">
            <h4 v-if="notification.title" class="notification-title">
              {{ notification.title }}
            </h4>
            <p class="notification-message">
              {{ notification.message }}
            </p>
          </div>
          
          <button 
            @click.stop="removeNotification(notification.id)"
            class="notification-close"
          >
            <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path>
            </svg>
          </button>
        </div>
        
        <div class="notification-progress" :style="{ width: notification.progress + '%' }"></div>
      </div>
    </transition-group>
  </teleport>
</template>

<script>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// Icon components
const SuccessIcon = {
  template: `
    <svg class="w-5 h-5 text-green-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"></path>
    </svg>
  `
}

const ErrorIcon = {
  template: `
    <svg class="w-5 h-5 text-red-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
    </svg>
  `
}

const WarningIcon = {
  template: `
    <svg class="w-5 h-5 text-yellow-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-2.5L13.732 4c-.77-.833-1.732-.833-2.5 0L4.314 16.5c-.77.833.192 2.5 1.732 2.5z"></path>
    </svg>
  `
}

const InfoIcon = {
  template: `
    <svg class="w-5 h-5 text-blue-500" fill="none" stroke="currentColor" viewBox="0 0 24 24">
      <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"></path>
    </svg>
  `
}

export default {
  name: 'NotificationSystem',
  components: {
    SuccessIcon,
    ErrorIcon,
    WarningIcon,
    InfoIcon
  },
  setup() {
    const notifications = ref([])
    let notificationId = 0
    
    const getNotificationClasses = (notification) => {
      return {
        'notification-success': notification.type === 'success',
        'notification-error': notification.type === 'error',
        'notification-warning': notification.type === 'warning',
        'notification-info': notification.type === 'info',
        'notification-persistent': notification.persistent
      }
    }
    
    const getIconComponent = (type) => {
      const iconMap = {
        success: 'SuccessIcon',
        error: 'ErrorIcon',
        warning: 'WarningIcon',
        info: 'InfoIcon'
      }
      return iconMap[type] || 'InfoIcon'
    }
    
    const addNotification = (options) => {
      const notification = {
        id: ++notificationId,
        type: options.type || 'info',
        title: options.title || '',
        message: options.message || '',
        duration: options.duration || 5000,
        persistent: options.persistent || false,
        progress: 100,
        timestamp: Date.now()
      }
      
      notifications.value.push(notification)
      
      if (!notification.persistent && notification.duration > 0) {
        startProgress(notification)
        setTimeout(() => {
          removeNotification(notification.id)
        }, notification.duration)
      }
      
      return notification.id
    }
    
    const removeNotification = (id) => {
      const index = notifications.value.findIndex(n => n.id === id)
      if (index > -1) {
        notifications.value.splice(index, 1)
      }
    }
    
    const clearNotifications = () => {
      notifications.value = []
    }
    
    const startProgress = (notification) => {
      const duration = notification.duration
      const startTime = Date.now()
      
      const updateProgress = () => {
        const elapsed = Date.now() - startTime
        const progress = Math.max(0, 100 - (elapsed / duration) * 100)
        
        const index = notifications.value.findIndex(n => n.id === notification.id)
        if (index > -1) {
          notifications.value[index].progress = progress
        }
        
        if (progress > 0) {
          requestAnimationFrame(updateProgress)
        }
      }
      
      requestAnimationFrame(updateProgress)
    }
    
    // Global notification methods
    const showSuccess = (message, options = {}) => {
      return addNotification({ ...options, type: 'success', message })
    }
    
    const showError = (message, options = {}) => {
      return addNotification({ ...options, type: 'error', message })
    }
    
    const showWarning = (message, options = {}) => {
      return addNotification({ ...options, type: 'warning', message })
    }
    
    const showInfo = (message, options = {}) => {
      return addNotification({ ...options, type: 'info', message })
    }
    
    // Make notification methods globally available
    onMounted(() => {
      const app = document.querySelector('#app').__vue_app__
      if (app) {
        app.config.globalProperties.$notification = {
          success: showSuccess,
          error: showError,
          warning: showWarning,
          info: showInfo,
          clear: clearNotifications
        }
      }
    })
    
    return {
      notifications,
      getNotificationClasses,
      getIconComponent,
      addNotification,
      removeNotification,
      clearNotifications,
      showSuccess,
      showError,
      showWarning,
      showInfo
    }
  }
}
</script>

<style scoped>
.notification-container {
  @apply fixed top-4 right-4 z-50 space-y-2;
  max-width: 400px;
}

.notification-item {
  @apply bg-white rounded-lg shadow-lg border border-gray-200 overflow-hidden cursor-pointer transition-all duration-300 hover:shadow-xl;
  position: relative;
}

.notification-success {
  @apply border-l-4 border-l-green-500;
}

.notification-error {
  @apply border-l-4 border-l-red-500;
}

.notification-warning {
  @apply border-l-4 border-l-yellow-500;
}

.notification-info {
  @apply border-l-4 border-l-blue-500;
}

.notification-content {
  @apply flex items-start gap-3 p-4;
}

.notification-icon {
  @apply flex-shrink-0 mt-1;
}

.notification-text {
  @apply flex-1 min-w-0;
}

.notification-title {
  @apply font-semibold text-gray-800 mb-1;
}

.notification-message {
  @apply text-gray-600 text-sm;
}

.notification-close {
  @apply flex-shrink-0 p-1 rounded-full hover:bg-gray-100 transition-colors;
}

.notification-progress {
  @apply absolute bottom-0 left-0 h-1 bg-blue-500 transition-all duration-100;
}

.notification-success .notification-progress {
  @apply bg-green-500;
}

.notification-error .notification-progress {
  @apply bg-red-500;
}

.notification-warning .notification-progress {
  @apply bg-yellow-500;
}

.notification-persistent .notification-progress {
  @apply hidden;
}

/* Notification animations */
.notification-enter-active {
  @apply transition-all duration-300;
}

.notification-leave-active {
  @apply transition-all duration-300;
}

.notification-enter-from {
  @apply transform translate-x-full opacity-0;
}

.notification-leave-to {
  @apply transform translate-x-full opacity-0;
}

.notification-move {
  @apply transition-transform duration-300;
}
</style>
