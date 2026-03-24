// KAFUKA Electronics Store - Design System
export const DESIGN_TOKENS = {
  // Brand Colors
  colors: {
    primary: {
      50: '#eff6ff',
      100: '#dbeafe',
      200: '#bfdbfe',
      300: '#93c5fd',
      400: '#60a5fa',
      500: '#3b82f6',
      600: '#2563eb',
      700: '#1d4ed8',
      800: '#1e40af',
      900: '#1e3a8a',
      950: '#172554',
    },
    secondary: {
      50: '#faf5ff',
      100: '#f3e8ff',
      200: '#e9d5ff',
      300: '#d8b4fe',
      400: '#c084fc',
      500: '#a855f7',
      600: '#9333ea',
      700: '#7c3aed',
      800: '#6b21a8',
      900: '#581c87',
      950: '#3b0764',
    },
    accent: {
      50: '#fff7ed',
      100: '#ffedd5',
      200: '#fed7aa',
      300: '#fdba74',
      400: '#fb923c',
      500: '#f97316',
      600: '#ea580c',
      700: '#c2410c',
      800: '#9a3412',
      900: '#7c2d12',
      950: '#431407',
    },
    success: {
      50: '#f0fdf4',
      100: '#dcfce7',
      200: '#bbf7d0',
      300: '#86efac',
      400: '#4ade80',
      500: '#22c55e',
      600: '#16a34a',
      700: '#15803d',
      800: '#166534',
      900: '#14532d',
      950: '#052e16',
    },
    warning: {
      50: '#fffbeb',
      100: '#fef3c7',
      200: '#fde68a',
      300: '#fcd34d',
      400: '#fbbf24',
      500: '#f59e0b',
      600: '#d97706',
      700: '#b45309',
      800: '#92400e',
      900: '#78350f',
      950: '#451a03',
    },
    error: {
      50: '#fef2f2',
      100: '#fee2e2',
      200: '#fecaca',
      300: '#fca5a5',
      400: '#f87171',
      500: '#ef4444',
      600: '#dc2626',
      700: '#b91c1c',
      800: '#991b1b',
      900: '#7f1d1d',
      950: '#450a0a',
    },
    neutral: {
      50: '#fafafa',
      100: '#f5f5f5',
      200: '#e5e5e5',
      300: '#d4d4d4',
      400: '#a3a3a3',
      500: '#737373',
      600: '#525252',
      700: '#404040',
      800: '#262626',
      900: '#171717',
      950: '#0a0a0a',
    }
  },
  
  // Typography
  typography: {
    fontFamily: {
      sans: ['Inter', 'system-ui', 'sans-serif'],
      mono: ['JetBrains Mono', 'monospace'],
    },
    fontSize: {
      xs: '0.75rem',
      sm: '0.875rem',
      base: '1rem',
      lg: '1.125rem',
      xl: '1.25rem',
      '2xl': '1.5rem',
      '3xl': '1.875rem',
      '4xl': '2.25rem',
      '5xl': '3rem',
      '6xl': '3.75rem',
      '7xl': '4.5rem',
      '8xl': '6rem',
      '9xl': '8rem',
    },
    fontWeight: {
      thin: '100',
      light: '300',
      normal: '400',
      medium: '500',
      semibold: '600',
      bold: '700',
      extrabold: '800',
      black: '900',
    },
    lineHeight: {
      tight: '1.25',
      snug: '1.375',
      normal: '1.5',
      relaxed: '1.625',
      loose: '2',
    }
  },
  
  // Spacing
  spacing: {
    px: '1px',
    0: '0px',
    0.5: '0.125rem',
    1: '0.25rem',
    1.5: '0.375rem',
    2: '0.5rem',
    2.5: '0.625rem',
    3: '0.75rem',
    3.5: '0.875rem',
    4: '1rem',
    5: '1.25rem',
    6: '1.5rem',
    7: '1.75rem',
    8: '2rem',
    9: '2.25rem',
    10: '2.5rem',
    11: '2.75rem',
    12: '3rem',
    14: '3.5rem',
    16: '4rem',
    20: '5rem',
    24: '6rem',
    28: '7rem',
    32: '8rem',
    36: '9rem',
    40: '10rem',
    44: '11rem',
    48: '12rem',
    52: '13rem',
    56: '14rem',
    60: '15rem',
    64: '16rem',
    72: '18rem',
    80: '20rem',
    96: '24rem',
  },
  
  // Border Radius
  borderRadius: {
    none: '0px',
    sm: '0.125rem',
    base: '0.25rem',
    md: '0.375rem',
    lg: '0.5rem',
    xl: '0.75rem',
    '2xl': '1rem',
    '3xl': '1.5rem',
    full: '9999px',
  },
  
  // Shadows
  boxShadow: {
    sm: '0 1px 2px 0 rgb(0 0 0 / 0.05)',
    base: '0 1px 3px 0 rgb(0 0 0 / 0.1), 0 1px 2px -1px rgb(0 0 0 / 0.1)',
    md: '0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)',
    lg: '0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)',
    xl: '0 20px 25px -5px rgb(0 0 0 / 0.1), 0 8px 10px -6px rgb(0 0 0 / 0.1)',
    '2xl': '0 25px 50px -12px rgb(0 0 0 / 0.25)',
    inner: 'inset 0 2px 4px 0 rgb(0 0 0 / 0.05)',
    glow: '0 0 20px rgb(59 130 246 / 0.5)',
    'glow-accent': '0 0 20px rgb(249 115 22 / 0.5)',
  },
  
  // Animation
  animation: {
    spin: 'spin 1s linear infinite',
    ping: 'ping 1s cubic-bezier(0, 0, 0.2, 1) infinite',
    pulse: 'pulse 2s cubic-bezier(0.4, 0, 0.6, 1) infinite',
    bounce: 'bounce 1s infinite',
    'fade-in': 'fadeIn 0.5s ease-in-out',
    'slide-up': 'slideUp 0.3s ease-out',
    'slide-down': 'slideDown 0.3s ease-out',
    'scale-in': 'scaleIn 0.2s ease-out',
  },
  
  // Transitions
  transition: {
    fast: '150ms ease-in-out',
    base: '200ms ease-in-out',
    slow: '300ms ease-in-out',
    slower: '500ms ease-in-out',
  }
}

// Component-specific styles
export const COMPONENT_STYLES = {
  // Button styles
  button: {
    primary: 'bg-primary-600 hover:bg-primary-700 text-white font-semibold py-3 px-6 rounded-lg shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2',
    secondary: 'bg-secondary-600 hover:bg-secondary-700 text-white font-semibold py-3 px-6 rounded-lg shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-secondary-500 focus:ring-offset-2',
    accent: 'bg-orange-600 hover:bg-orange-700 text-white font-semibold py-3 px-6 rounded-lg shadow-lg hover:shadow-xl transform hover:scale-105 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-orange-500 focus:ring-offset-2',
    outline: 'border-2 border-primary-600 text-primary-600 hover:bg-primary-600 hover:text-white font-semibold py-3 px-6 rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2',
    ghost: 'text-primary-600 hover:bg-primary-50 font-semibold py-3 px-6 rounded-lg transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-primary-500 focus:ring-offset-2',
  },
  
  // Card styles
  card: {
    base: 'bg-white rounded-xl shadow-lg hover:shadow-xl transition-all duration-300 border border-neutral-200',
    interactive: 'bg-white rounded-xl shadow-lg hover:shadow-xl hover:scale-105 transition-all duration-300 border border-neutral-200 cursor-pointer',
    elevated: 'bg-white rounded-2xl shadow-xl hover:shadow-2xl transition-all duration-300 border border-neutral-200',
  },
  
  // Input styles
  input: {
    base: 'w-full px-4 py-3 border border-neutral-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-primary-500 transition-all duration-200',
    error: 'w-full px-4 py-3 border border-error-500 rounded-lg focus:outline-none focus:ring-2 focus:ring-error-500 focus:border-error-500 transition-all duration-200',
    success: 'w-full px-4 py-3 border border-success-500 rounded-lg focus:outline-none focus:ring-2 focus:ring-success-500 focus:border-success-500 transition-all duration-200',
  },
  
  // Badge styles
  badge: {
    primary: 'bg-primary-100 text-primary-800 text-xs font-semibold px-2.5 py-0.5 rounded-full',
    secondary: 'bg-secondary-100 text-secondary-800 text-xs font-semibold px-2.5 py-0.5 rounded-full',
    accent: 'bg-orange-100 text-orange-800 text-xs font-semibold px-2.5 py-0.5 rounded-full',
    success: 'bg-success-100 text-success-800 text-xs font-semibold px-2.5 py-0.5 rounded-full',
    warning: 'bg-warning-100 text-warning-800 text-xs font-semibold px-2.5 py-0.5 rounded-full',
    error: 'bg-error-100 text-error-800 text-xs font-semibold px-2.5 py-0.5 rounded-full',
  }
}

// Layout styles
export const LAYOUT_STYLES = {
  container: 'max-w-7xl mx-auto px-4 sm:px-6 lg:px-8',
  section: 'py-16 lg:py-24',
  sectionSm: 'py-8 lg:py-12',
  sectionLg: 'py-24 lg:py-32',
  grid: 'grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6',
  grid2: 'grid grid-cols-1 lg:grid-cols-2 gap-8',
  grid3: 'grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6',
  flexCenter: 'flex items-center justify-center',
  flexBetween: 'flex items-center justify-between',
  flexCol: 'flex flex-col',
}

// Utility classes
export const UTILITIES = {
  text: {
    gradient: 'bg-gradient-to-r from-primary-600 to-secondary-600 bg-clip-text text-transparent',
    gradientAccent: 'bg-gradient-to-r from-orange-500 to-primary-600 bg-clip-text text-transparent',
    heading: 'text-3xl md:text-4xl lg:text-5xl font-bold text-neutral-900',
    subheading: 'text-xl md:text-2xl lg:text-3xl font-semibold text-neutral-800',
    body: 'text-base text-neutral-600 leading-relaxed',
    small: 'text-sm text-neutral-500',
  },
  background: {
    hero: 'bg-gradient-to-br from-primary-600 via-secondary-600 to-orange-600',
    section: 'bg-neutral-50',
    card: 'bg-white',
    overlay: 'bg-black/50 backdrop-blur-sm',
  },
  border: {
    base: 'border border-neutral-200',
    accent: 'border-2 border-orange-500',
    focus: 'ring-2 ring-primary-500 ring-offset-2',
  }
}
