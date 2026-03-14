<template>
  <form @submit.prevent="handleSubmit" class="vue-form" :class="formClasses">
    <div v-if="title" class="form-header">
      <h3 class="form-title">{{ title }}</h3>
      <p v-if="description" class="form-description">{{ description }}</p>
    </div>
    
    <div class="form-fields">
      <div 
        v-for="field in fields" 
        :key="field.name"
        class="form-field"
        :class="getFieldClasses(field)"
      >
        <label 
          :for="field.name" 
          class="form-label"
          :class="{ 'is-required': field.required }"
        >
          {{ field.label }}
          <span v-if="field.required" class="required-indicator">*</span>
        </label>
        
        <!-- Text Input -->
        <input
          v-if="field.type === 'text' || field.type === 'email' || field.type === 'password'"
          :type="field.type"
          :id="field.name"
          v-model="formData[field.name]"
          :placeholder="field.placeholder"
          :disabled="field.disabled"
          :readonly="field.readonly"
          class="form-input"
          :class="getInputClasses(field)"
          @blur="validateField(field.name)"
          @input="handleInput(field.name, $event.target.value)"
        >
        
        <!-- Textarea -->
        <textarea
          v-else-if="field.type === 'textarea'"
          :id="field.name"
          v-model="formData[field.name]"
          :placeholder="field.placeholder"
          :disabled="field.disabled"
          :readonly="field.readonly"
          :rows="field.rows || 4"
          class="form-input form-textarea"
          :class="getInputClasses(field)"
          @blur="validateField(field.name)"
          @input="handleInput(field.name, $event.target.value)"
        ></textarea>
        
        <!-- Select -->
        <select
          v-else-if="field.type === 'select'"
          :id="field.name"
          v-model="formData[field.name]"
          :disabled="field.disabled"
          class="form-input form-select"
          :class="getInputClasses(field)"
          @blur="validateField(field.name)"
          @change="handleInput(field.name, $event.target.value)"
        >
          <option value="" disabled>{{ field.placeholder || 'Select an option' }}</option>
          <option
            v-for="option in field.options"
            :key="option.value"
            :value="option.value"
          >
            {{ option.label }}
          </option>
        </select>
        
        <!-- Checkbox -->
        <div v-else-if="field.type === 'checkbox'" class="form-checkbox-wrapper">
          <input
            :id="field.name"
            v-model="formData[field.name]"
            :disabled="field.disabled"
            type="checkbox"
            class="form-checkbox"
            @change="handleInput(field.name, $event.target.checked)"
          >
          <label :for="field.name" class="form-checkbox-label">
            {{ field.checkboxLabel || field.label }}
          </label>
        </div>
        
        <!-- Radio -->
        <div v-else-if="field.type === 'radio'" class="form-radio-group">
          <div
            v-for="option in field.options"
            :key="option.value"
            class="form-radio-wrapper"
          >
            <input
              :id="`${field.name}_${option.value}`"
              v-model="formData[field.name]"
              :value="option.value"
              :disabled="field.disabled"
              type="radio"
              class="form-radio"
              :name="field.name"
              @change="handleInput(field.name, option.value)"
            >
            <label :for="`${field.name}_${option.value}`" class="form-radio-label">
              {{ option.label }}
            </label>
          </div>
        </div>
        
        <!-- File Input -->
        <div v-else-if="field.type === 'file'" class="form-file-wrapper">
          <input
            :id="field.name"
            type="file"
            :disabled="field.disabled"
            :accept="field.accept"
            :multiple="field.multiple"
            class="form-file"
            @change="handleFileInput(field.name, $event.target.files)"
          >
          <div class="form-file-label">
            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M7 16a4 4 0 01-.88-7.903A5 5 0 1115.9 8.904L16 8a4 4 0 011.88 7.904A5 5 0 018.1 8.904L16 8a4 4 0 11-1.88 7.904A5 5 0 018.1 8.904L16 8a4 4 0 01-1.88 7.904A5 5 0 018.1 8.904L16 8z"></path>
            </svg>
            <span>{{ field.placeholder || 'Choose file' }}</span>
          </div>
        </div>
        
        <!-- Field Error -->
        <div v-if="errors[field.name]" class="form-error">
          {{ errors[field.name] }}
        </div>
        
        <!-- Field Help -->
        <div v-if="field.help" class="form-help">
          {{ field.help }}
        </div>
      </div>
    </div>
    
    <div class="form-actions">
      <button
        v-for="action in actions"
        :key="action.key"
        :type="action.type || 'button'"
        @click="handleAction(action)"
        class="form-btn"
        :class="getActionClasses(action)"
        :disabled="action.disabled || isSubmitting"
      >
        <span v-if="action.loading" class="btn-loading">
          <svg class="w-4 h-4 animate-spin" fill="none" viewBox="0 0 24 24">
            <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
            <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V8C4 4 4 0 8 0s4 4 4 4v4a8 8 0 01-8 8z"></path>
          </svg>
        </span>
        <span v-else>{{ action.label }}</span>
      </button>
    </div>
  </form>
</template>

<script>
import { ref, reactive, computed, watch } from 'vue'

export default {
  name: 'VueForm',
  props: {
    fields: {
      type: Array,
      required: true,
      validator: (fields) => {
        return fields.every(field => field.name && field.type && field.label)
      }
    },
    initialData: {
      type: Object,
      default: () => ({})
    },
    title: {
      type: String,
      default: ''
    },
    description: {
      type: String,
      default: ''
    },
    actions: {
      type: Array,
      default: () => [
        { key: 'submit', label: 'Submit', type: 'submit', primary: true }
      ]
    },
    validation: {
      type: Object,
      default: () => ({})
    },
    formClasses: {
      type: String,
      default: ''
    }
  },
  emits: ['submit', 'input', 'change', 'action'],
  setup(props, { emit }) {
    const formData = reactive({ ...props.initialData })
    const errors = reactive({})
    const isSubmitting = ref(false)
    
    const validateField = (fieldName) => {
      const field = props.fields.find(f => f.name === fieldName)
      if (!field || !props.validation[fieldName]) {
        delete errors[fieldName]
        return
      }
      
      const value = formData[fieldName]
      const rules = props.validation[fieldName]
      const fieldErrors = []
      
      // Required validation
      if (rules.required && (!value || value.toString().trim() === '')) {
        fieldErrors.push(`${field.label} is required`)
      }
      
      // Email validation
      if (rules.email && value) {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/
        if (!emailRegex.test(value)) {
          fieldErrors.push(`${field.label} must be a valid email`)
        }
      }
      
      // Min length validation
      if (rules.minLength && value && value.length < rules.minLength) {
        fieldErrors.push(`${field.label} must be at least ${rules.minLength} characters`)
      }
      
      // Max length validation
      if (rules.maxLength && value && value.length > rules.maxLength) {
        fieldErrors.push(`${field.label} must not exceed ${rules.maxLength} characters`)
      }
      
      // Pattern validation
      if (rules.pattern && value) {
        if (!rules.pattern.test(value)) {
          fieldErrors.push(rules.message || `${field.label} is invalid`)
        }
      }
      
      // Custom validation
      if (rules.custom && typeof rules.custom === 'function') {
        const customError = rules.custom(value)
        if (customError) {
          fieldErrors.push(customError)
        }
      }
      
      if (fieldErrors.length > 0) {
        errors[fieldName] = fieldErrors[0]
      } else {
        delete errors[fieldName]
      }
    }
    
    const validateAll = () => {
      let isValid = true
      
      props.fields.forEach(field => {
        validateField(field.name)
        if (errors[field.name]) {
          isValid = false
        }
      })
      
      return isValid
    }
    
    const handleInput = (fieldName, value) => {
      formData[fieldName] = value
      validateField(fieldName)
      emit('input', { fieldName, value, formData: { ...formData } })
    }
    
    const handleFileInput = (fieldName, files) => {
      formData[fieldName] = files
      emit('input', { fieldName, value: files, formData: { ...formData } })
    }
    
    const handleSubmit = () => {
      if (validateAll()) {
        isSubmitting.value = true
        emit('submit', { data: { ...formData }, isValid: true })
        
        // Reset submitting state after a delay
        setTimeout(() => {
          isSubmitting.value = false
        }, 1000)
      } else {
        emit('submit', { data: { ...formData }, isValid: false })
      }
    }
    
    const handleAction = (action) => {
      if (action.key === 'submit') {
        handleSubmit()
      } else {
        emit('action', { action, data: { ...formData } })
      }
    }
    
    const getFieldClasses = (field) => {
      return {
        'has-error': errors[field.name],
        'is-disabled': field.disabled,
        'is-readonly': field.readonly
      }
    }
    
    const getInputClasses = (field) => {
      return {
        'has-error': errors[field.name],
        'is-disabled': field.disabled,
        'is-readonly': field.readonly
      }
    }
    
    const getActionClasses = (action) => {
      return {
        'btn-primary': action.primary,
        'btn-secondary': !action.primary,
        'btn-danger': action.danger,
        'is-loading': action.loading
      }
    }
    
    // Watch for initial data changes
    watch(() => props.initialData, (newData) => {
      Object.keys(formData).forEach(key => {
        if (key in newData) {
          formData[key] = newData[key]
        }
      })
    }, { deep: true })
    
    return {
      formData,
      errors,
      isSubmitting,
      validateField,
      validateAll,
      handleInput,
      handleFileInput,
      handleSubmit,
      handleAction,
      getFieldClasses,
      getInputClasses,
      getActionClasses
    }
  }
}
</script>

<style scoped>
.vue-form {
  @apply bg-white rounded-lg shadow-md p-6;
}

.form-header {
  @apply mb-6;
}

.form-title {
  @apply text-xl font-semibold text-gray-800 mb-2;
}

.form-description {
  @apply text-gray-600 text-sm;
}

.form-fields {
  @apply space-y-4;
}

.form-field {
  @apply space-y-1;
}

.form-label {
  @apply block text-sm font-medium text-gray-700;
}

.required-indicator {
  @apply text-red-500 ml-1;
}

.form-input {
  @apply w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-blue-500 focus:border-transparent transition-colors;
}

.form-textarea {
  @apply resize-y min-h-24;
}

.form-select {
  @apply cursor-pointer;
}

.form-checkbox-wrapper {
  @apply flex items-center gap-2;
}

.form-checkbox {
  @apply w-4 h-4 text-blue-600 border-gray-300 rounded focus:ring-blue-500;
}

.form-checkbox-label {
  @apply text-sm text-gray-700 cursor-pointer;
}

.form-radio-group {
  @apply space-y-2;
}

.form-radio-wrapper {
  @apply flex items-center gap-2;
}

.form-radio {
  @apply w-4 h-4 text-blue-600 border-gray-300 focus:ring-blue-500;
}

.form-radio-label {
  @apply text-sm text-gray-700 cursor-pointer;
}

.form-file-wrapper {
  @apply relative;
}

.form-file {
  @apply hidden;
}

.form-file-label {
  @apply flex items-center gap-2 px-4 py-2 border border-gray-300 rounded-md cursor-pointer hover:bg-gray-50 transition-colors;
}

.form-error {
  @apply text-red-500 text-xs mt-1;
}

.form-help {
  @apply text-gray-500 text-xs mt-1;
}

.form-actions {
  @apply flex gap-3 justify-end mt-6;
}

.form-btn {
  @apply px-4 py-2 rounded-md font-medium transition-colors focus:outline-none focus:ring-2 focus:ring-offset-2;
}

.btn-primary {
  @apply bg-blue-600 text-white hover:bg-blue-700 focus:ring-blue-500;
}

.btn-secondary {
  @apply bg-gray-200 text-gray-800 hover:bg-gray-300 focus:ring-gray-500;
}

.btn-danger {
  @apply bg-red-600 text-white hover:bg-red-700 focus:ring-red-500;
}

.is-loading {
  @apply opacity-75 cursor-not-allowed;
}

.has-error .form-input {
  @apply border-red-500 focus:ring-red-500;
}

.is-disabled {
  @apply opacity-50 cursor-not-allowed;
}

.is-readonly {
  @apply bg-gray-50 cursor-not-allowed;
}

.btn-loading {
  @apply flex items-center gap-2;
}

@keyframes spin {
  from { transform: rotate(0deg); }
  to { transform: rotate(360deg); }
}

.animate-spin {
  animation: spin 1s linear infinite;
}
</style>
