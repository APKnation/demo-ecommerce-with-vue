# KAFUKA E-commerce Store - Vue.js Version

A modern e-commerce application built with Vue.js 3, Vue Router, and Tailwind CSS. This is a complete rewrite of the original HTML/CSS/JavaScript version using modern Vue.js composition API.

## Features

- **Product Catalog**: Browse products with advanced filtering and search
- **Shopping Cart**: Add items to cart with quantity controls
- **Wishlist**: Save favorite products for later
- **Product Comparison**: Compare up to 3 products side by side
- **Order Management**: View order history and order details
- **Admin Panel**: Manage products and view store statistics
- **Responsive Design**: Mobile-first design with Tailwind CSS
- **Local Storage**: Persistent cart, wishlist, and order data

## Technology Stack

- **Vue.js 3** - Progressive JavaScript framework
- **Vue Router 4** - Official routing library for Vue.js
- **Tailwind CSS** - Utility-first CSS framework
- **Vite** - Fast build tool and development server
- **LocalStorage API** - Client-side data persistence

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd electronics-cart-main
```

2. Install dependencies:
```bash
npm install
```

3. Start the development server:
```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:3000`

## Project Structure

```
src/
├── main.js              # Application entry point
├── App.vue              # Root component with layout and global state
├── style.css            # Global styles and Tailwind imports
└── views/               # Page components
    ├── Home.vue         # Product catalog with filtering
    ├── Cart.vue         # Shopping cart management
    ├── Admin.vue        # Admin panel for product management
    ├── Orders.vue       # Order history
    └── Order.vue        # Individual order details
```

## Key Features Implementation

### State Management
- Uses Vue 3 Composition API with `ref`, `computed`, and `provide/inject`
- Global state managed in App.vue and provided to child components
- LocalStorage integration for data persistence

### Routing
- Vue Router for single-page application navigation
- Dynamic routes for order details (`/order/:id`)
- Programmatic navigation for better user experience

### Styling
- Tailwind CSS for utility-first styling
- Custom component classes for consistent design
- Responsive design with mobile-first approach
- Smooth transitions and hover effects

### Component Architecture
- Each page is a separate Vue component
- Reusable patterns for modals, cards, and forms
- Proper component communication using props and provide/inject

## Data Persistence

The application uses LocalStorage to persist:
- Shopping cart items
- Wishlist items
- Compare list
- Order history
- Product catalog (admin-managed)

## Development Commands

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Browser Compatibility

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

MIT License - see LICENSE file for details
# demo-ecommerce-with-vue
