/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: {
          50: '#eff6ff',
          500: '#769f55',
          600: 'rgb(125, 136, 161)',
          700: 'rgb(104, 216, 29)',
        },
        secondary: {
          50: '#fefce8',
          500: '#eab308',
          600: '#ca8a04',
        },
        'neutral-primary': '#1f2937',
        'neutral-secondary': '#374151',
        'neutral-secondary-soft': '#f3f4f6',
        'neutral-tertiary': '#e5e7eb',
        'brand': '#3b82f6',
        'fg-brand': '#3b82f6',
        'heading': '#111827',
        'body': '#6b7280',
        'default': '#d1d5db'
      }
    },
  },
  plugins: [],
}
