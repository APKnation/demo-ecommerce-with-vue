// Electronics Store Categories Configuration
export const ELECTRONICS_CATEGORIES = {
  // Mobile Devices
  smartphones: {
    name: 'Smartphones',
    icon: '📱',
    description: 'Latest smartphones and mobile devices',
    subcategories: {
      android: 'Android Phones',
      iphone: 'iPhone',
      basic: 'Basic Phones',
      accessories: 'Phone Accessories'
    },
    specifications: ['storage', 'ram', 'camera', 'battery', 'screen_size']
  },
  
  // Computing
  laptops: {
    name: 'Laptops',
    icon: '💻',
    description: 'Laptops and notebook computers',
    subcategories: {
      gaming: 'Gaming Laptops',
      business: 'Business Laptops',
      ultrabook: 'Ultrabooks',
      chromebook: 'Chromebooks'
    },
    specifications: ['processor', 'ram', 'storage', 'graphics', 'screen_size', 'weight']
  },
  
  computers: {
    name: 'Desktop Computers',
    icon: '🖥️',
    description: 'Desktop computers and all-in-one PCs',
    subcategories: {
      gaming: 'Gaming PCs',
      office: 'Office PCs',
      workstation: 'Workstations',
      allinone: 'All-in-One'
    },
    specifications: ['processor', 'ram', 'storage', 'graphics', 'form_factor']
  },
  
  // Audio
  headphones: {
    name: 'Headphones & Audio',
    icon: '🎧',
    description: 'Headphones, earphones, and audio equipment',
    subcategories: {
      wireless: 'Wireless Headphones',
      wired: 'Wired Headphones',
      earbuds: 'Earbuds',
      speakers: 'Speakers'
    },
    specifications: ['type', 'connectivity', 'battery_life', 'noise_cancelling', 'frequency_response']
  },
  
  // Wearables
  wearables: {
    name: 'Wearables',
    icon: '⌚',
    description: 'Smart watches and wearable technology',
    subcategories: {
      smartwatch: 'Smart Watches',
      fitness: 'Fitness Trackers',
      bands: 'Smart Bands',
      glasses: 'Smart Glasses'
    },
    specifications: ['display', 'battery_life', 'water_resistance', 'compatibility', 'health_features']
  },
  
  // Photography
  cameras: {
    name: 'Cameras & Photography',
    icon: '📷',
    description: 'Digital cameras and photography equipment',
    subcategories: {
      dslr: 'DSLR Cameras',
      mirrorless: 'Mirrorless Cameras',
      compact: 'Compact Cameras',
      accessories: 'Camera Accessories'
    },
    specifications: ['sensor_type', 'megapixels', 'lens', 'video_resolution', 'connectivity']
  },
  
  // Gaming
  gaming: {
    name: 'Gaming',
    icon: '🎮',
    description: 'Gaming consoles and accessories',
    subcategories: {
      consoles: 'Gaming Consoles',
      controllers: 'Controllers',
      accessories: 'Gaming Accessories',
      vr: 'VR Equipment'
    },
    specifications: ['platform', 'storage', 'resolution', 'connectivity', 'accessories']
  },
  
  // Home & Office
  accessories: {
    name: 'Accessories',
    icon: '🔌',
    description: 'Computer and electronic accessories',
    subcategories: {
      cables: 'Cables & Adapters',
      storage: 'Storage Devices',
      networking: 'Networking',
      power: 'Power & Charging'
    },
    specifications: ['compatibility', 'capacity', 'speed', 'connectivity']
  }
}

// Category helper functions
export const getCategoryById = (categoryId) => {
  return ELECTRONICS_CATEGORIES[categoryId] || null
}

export const getAllCategories = () => {
  return Object.keys(ELECTRONICS_CATEGORIES).map(key => ({
    id: key,
    ...ELECTRONICS_CATEGORIES[key]
  }))
}

export const getCategorySpecifications = (categoryId) => {
  const category = getCategoryById(categoryId)
  return category ? category.specifications : []
}

export const getSubcategoriesByCategory = (categoryId) => {
  const category = getCategoryById(categoryId)
  return category ? Object.keys(category.subcategories).map(key => ({
    id: key,
    name: category.subcategories[key]
  })) : []
}
