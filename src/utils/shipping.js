// Shipping Cost Calculation System for Tanzania
export const SHIPPING_ZONES = {
  // Tanzania Mainland Zones
  dar_es_salaam: {
    name: 'Dar es Salaam',
    code: 'DAR',
    baseCost: 5000,
    freeShippingThreshold: 50000,
    deliveryTime: '1-2 business days',
    regions: ['dar_es_salaam', 'ilala', 'kinondoni', 'temeke', 'ubungo']
  },
  
  major_cities: {
    name: 'Major Cities',
    code: 'MAJOR',
    baseCost: 8000,
    freeShippingThreshold: 75000,
    deliveryTime: '2-3 business days',
    regions: ['arusha', 'mwanza', 'dodoma', 'mbeya', 'tanga', 'morogoro', 'zanzibar']
  },
  
  other_regions: {
    name: 'Other Regions',
    code: 'OTHER',
    baseCost: 12000,
    freeShippingThreshold: 100000,
    deliveryTime: '3-5 business days',
    regions: ['kagera', 'kigoma', 'tabora', 'singida', 'manyara', 'njombe', 'katavi', 'simiyu', 'geita', 'lindi', 'mtwara', 'ruvuma', 'iringa', 'rukwa']
  },
  
  // International Shipping
  east_africa: {
    name: 'East Africa',
    code: 'EAST_AFRICA',
    baseCost: 25000,
    freeShippingThreshold: 200000,
    deliveryTime: '5-7 business days',
    regions: ['kenya', 'uganda', 'rwanda', 'burundi', 'south_sudan']
  },
  
  international: {
    name: 'International',
    code: 'INTL',
    baseCost: 50000,
    freeShippingThreshold: 500000,
    deliveryTime: '7-14 business days',
    regions: ['other_international']
  }
}

// Shipping Methods
export const SHIPPING_METHODS = {
  standard: {
    name: 'Standard Delivery',
    code: 'STD',
    multiplier: 1.0,
    description: 'Regular delivery service',
    tracking: true
  },
  
  express: {
    name: 'Express Delivery',
    code: 'EXP',
    multiplier: 1.5,
    description: 'Fast delivery service',
    tracking: true
  },
  
  pickup: {
    name: 'Store Pickup',
    code: 'PICKUP',
    multiplier: 0,
    description: 'Pick up from our store',
    tracking: false
  }
}

// Product-specific shipping rules
export const PRODUCT_SHIPPING_RULES = {
  // Heavy items
  heavy_items: {
    threshold: 5, // kg
    additionalCost: 3000 // per kg over threshold
  },
  
  // Fragile items
  fragile_items: {
    categories: ['cameras', 'electronics'],
    additionalCost: 2000,
    insurance: 0.02 // 2% of product value
  },
  
  // Bulk items
  bulk_items: {
    threshold: 3, // quantity
    discount: 0.1 // 10% discount on shipping
  }
}

// Shipping cost calculation class
export class ShippingCalculator {
  constructor() {
    this.zones = SHIPPING_ZONES
    this.methods = SHIPPING_METHODS
    this.rules = PRODUCT_SHIPPING_RULES
  }
  
  // Determine shipping zone based on region
  getShippingZone(region) {
    for (const [zoneKey, zone] of Object.entries(this.zones)) {
      if (zone.regions.includes(region.toLowerCase())) {
        return { key: zoneKey, ...zone }
      }
    }
    return this.zones.international
  }
  
  // Calculate base shipping cost
  calculateBaseCost(zone, cartTotal) {
    // Check for free shipping
    if (cartTotal >= zone.freeShippingThreshold) {
      return 0
    }
    
    return zone.baseCost
  }
  
  // Apply shipping method multiplier
  applyShippingMethod(baseCost, method) {
    const methodConfig = this.methods[method] || this.methods.standard
    return Math.round(baseCost * methodConfig.multiplier)
  }
  
  // Calculate product-specific additional costs
  calculateProductAdditionalCosts(products) {
    let additionalCost = 0
    let totalWeight = 0
    let fragileItemsValue = 0
    let totalQuantity = 0
    
    products.forEach(product => {
      totalWeight += (product.weight || 1) * product.quantity
      totalQuantity += product.quantity
      
      // Check for fragile items
      if (this.rules.fragile_items.categories.includes(product.category)) {
        fragileItemsValue += product.price * product.quantity
        additionalCost += this.rules.fragile_items.additionalCost
      }
    })
    
    // Heavy items surcharge
    if (totalWeight > this.rules.heavy_items.threshold) {
      const overweight = totalWeight - this.rules.heavy_items.threshold
      additionalCost += overweight * this.rules.heavy_items.additionalCost
    }
    
    // Fragile items insurance
    if (fragileItemsValue > 0) {
      additionalCost += fragileItemsValue * this.rules.fragile_items.insurance
    }
    
    // Bulk items discount
    if (totalQuantity >= this.rules.bulk_items.threshold) {
      additionalCost *= (1 - this.rules.bulk_items.discount)
    }
    
    return Math.round(additionalCost)
  }
  
  // Main shipping calculation
  calculateShipping(options) {
    const {
      region,
      cartTotal = 0,
      products = [],
      method = 'standard'
    } = options
    
    // Get shipping zone
    const zone = this.getShippingZone(region)
    
    // Calculate base cost
    const baseCost = this.calculateBaseCost(zone, cartTotal)
    
    // Apply shipping method
    const methodCost = this.applyShippingMethod(baseCost, method)
    
    // Calculate product-specific costs
    const additionalCosts = this.calculateProductAdditionalCosts(products)
    
    // Total shipping cost
    const totalCost = methodCost + additionalCosts
    
    return {
      zone: zone,
      method: this.methods[method],
      baseCost,
      methodCost,
      additionalCosts,
      totalCost,
      freeShipping: baseCost === 0,
      estimatedDelivery: zone.deliveryTime,
      tracking: this.methods[method].tracking
    }
  }
  
  // Get all available regions
  getAllRegions() {
    const regions = []
    
    Object.values(this.zones).forEach(zone => {
      zone.regions.forEach(region => {
        regions.push({
          name: region.charAt(0).toUpperCase() + region.slice(1).replace('_', ' '),
          code: region.toUpperCase(),
          zone: zone.name,
          zoneCode: zone.code
        })
      })
    })
    
    return regions.sort((a, b) => a.name.localeCompare(b.name))
  }
  
  // Get shipping estimate for display
  getShippingEstimate(region, cartTotal, products = []) {
    const shipping = this.calculateShipping({ region, cartTotal, products })
    
    if (shipping.freeShipping) {
      return {
        cost: 0,
        message: 'FREE Shipping!',
        type: 'free',
        delivery: shipping.estimatedDelivery
      }
    }
    
    const freeShippingRemaining = shipping.zone.freeShippingThreshold - cartTotal
    if (freeShippingRemaining > 0 && freeShippingRemaining < 20000) {
      return {
        cost: shipping.totalCost,
        message: `Add Tsh ${freeShippingRemaining.toLocaleString()} more for FREE shipping`,
        type: 'almost_free',
        delivery: shipping.estimatedDelivery
      }
    }
    
    return {
      cost: shipping.totalCost,
      message: `Standard shipping - ${shipping.estimatedDelivery}`,
      type: 'standard',
      delivery: shipping.estimatedDelivery
    }
  }
}

// Create singleton instance
export const shippingCalculator = new ShippingCalculator()

// Helper functions
export const getShippingZones = () => {
  return Object.entries(SHIPPING_ZONES).map(([key, zone]) => ({
    key,
    ...zone
  }))
}

export const getShippingMethods = () => {
  return Object.entries(SHIPPING_METHODS).map(([key, method]) => ({
    key,
    ...method
  }))
}

export const validateShippingAddress = (address) => {
  const errors = []
  
  if (!address.region) errors.push('Region is required')
  if (!address.city) errors.push('City is required')
  if (!address.address) errors.push('Street address is required')
  if (!address.postalCode && address.region !== 'dar_es_salaam') {
    errors.push('Postal code is required')
  }
  
  return {
    isValid: errors.length === 0,
    errors
  }
}
