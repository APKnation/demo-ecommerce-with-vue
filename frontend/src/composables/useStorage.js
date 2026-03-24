import { ref, watch } from 'vue'

export function useStorage(key, defaultValue) {
  // Get value from localStorage or use default
  const storedValue = localStorage.getItem(key)
  const value = ref(storedValue ? JSON.parse(storedValue) : defaultValue)

  // Watch for changes and update localStorage
  watch(value, (newValue) => {
    if (newValue === null || newValue === undefined) {
      localStorage.removeItem(key)
    } else {
      localStorage.setItem(key, JSON.stringify(newValue))
    }
  }, { deep: true })

  return value
}
