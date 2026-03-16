import { ref, computed } from 'vue'
import { useStorage } from './useStorage.js'

export function useProductComparison() {
  const compareList = useStorage('product-compare-list', [])

  const addToCompare = (product) => {
    if (!isInCompareList(product.value || product)) {
      if (compareList.value.length >= 4) {
        // Remove oldest product if list is full
        compareList.value.shift()
      }
      compareList.value.push(product.value || product)
      showNotification('Product added to comparison', 'success')
    } else {
      showNotification('Product already in comparison list', 'warning')
    }
  }

  const removeFromCompare = (product) => {
    const index = compareList.value.findIndex(p => p.id === product.id)
    if (index > -1) {
      compareList.value.splice(index, 1)
      showNotification('Product removed from comparison', 'info')
    }
  }

  const clearCompareList = () => {
    compareList.value = []
    showNotification('Comparison list cleared', 'info')
  }

  const isInCompareList = (product) => {
    return compareList.value.some(p => p.id === product.id)
  }

  const compareCount = computed(() => compareList.value.length)

  const canCompare = computed(() => compareList.value.length >= 2)

  const showNotification = (message, type = 'info') => {
    // This would integrate with your notification system
    console.log(`${type}: ${message}`)
  }

  return {
    compareList,
    addToCompare,
    removeFromCompare,
    clearCompareList,
    isInCompareList,
    compareCount,
    canCompare
  }
}
