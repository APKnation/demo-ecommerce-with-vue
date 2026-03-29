# KAFUKA Electronics E-commerce Platform

A complete, production-ready e-commerce platform built with Vue.js 3 and Django REST Framework, featuring multi-role support (Customer, Vendor, Admin), real-time data flow, and comprehensive order management.

## 🚀 Quick Start

### Prerequisites
- Node.js 16+
- Python 3.10+
- Django 4.0+
- Vue.js 3

### Installation

#### Backend Setup
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

#### Frontend Setup
```bash
cd frontend
npm install
npm run dev
```

## 🏗️ Architecture Overview

### Backend (Django REST Framework)
- **Authentication**: Token-based auth with role management
- **User Roles**: Customer, Vendor, Admin
- **Products**: Full CRUD with vendor management
- **Orders**: Complete order lifecycle management
- **Cart**: Persistent shopping cart system
- **Real-time**: WebSocket support for live updates

### Frontend (Vue.js 3)
- **Composition API**: Modern Vue.js patterns
- **State Management**: Composables-based state
- **Routing**: Vue Router with role-based navigation
- **UI Components**: Custom components with Tailwind CSS
- **Real-time**: WebSocket integration
- **Responsive**: Mobile-first design

## 📱 User Roles & Features

### Customer Features
- 🛍️ Browse and search products
- 🛒 Shopping cart management
- 📦 Order placement and tracking
- 👤 Profile management
- 📱 Mobile-responsive interface

### Vendor Features
- 🏪 Vendor dashboard
- 📦 Product management (add/edit/delete)
- 💰 Sales tracking and analytics
- 📊 Inventory management
- ✅ Product approval system

### Admin Features
- 🔧 Complete admin dashboard
- 👥 User management (all roles)
- 📋 Order management and oversight
- 🏪 Vendor approval system
- 📦 Product approval workflow
- 📊 System statistics and analytics

## 🔄 Data Flow Architecture

### Complete Bidirectional Data Flow
```
Customer ↔ Backend ↔ Frontend
    ↓           ↓           ↓
Orders    ←→ Database ←→ UI Updates
Products  ←→ Models    ←→ Real-time
Users     ←→ Auth      ←→ WebSocket
```

### Real-time Communication
- **WebSocket**: Live order updates, notifications
- **Polling Fallback**: Ensures connectivity
- **Role-based Channels**: Targeted updates per user type

## 🛠️ Technical Stack

### Backend Technologies
- **Django 4.0**: Web framework
- **Django REST Framework**: API development
- **SQLite**: Database (development)
- **Token Authentication**: Secure auth system
- **WebSocket**: Real-time communication

### Frontend Technologies
- **Vue.js 3**: Progressive framework
- **Vue Router**: Client-side routing
- **Tailwind CSS**: Utility-first CSS
- **Composition API**: Modern Vue patterns
- **Axios**: HTTP client
- **SweetAlert2**: User notifications

## 📊 Database Models

### User Management
- **User**: Extended Django User with roles
- **Roles**: Customer, Vendor, Admin
- **Profiles**: User preferences and settings

### Product Management
- **Category**: Product categorization
- **Product**: Product details with vendor relationships
- **Images**: Product image management

### Order Management
- **Order**: Order tracking and management
- **OrderItem**: Individual order items
- **Cart**: Shopping cart persistence

## 🔐 Authentication & Authorization

### Token-based Authentication
```javascript
// Login and get token
const response = await fetch('/api/accounts/login/', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ username, password })
})
const { token, user } = await response.json()
```

### Role-based Access Control
- **Customer**: Access to own orders and profile
- **Vendor**: Access to own products and related orders
- **Admin**: Full system access and management

## 📱 API Endpoints

### Authentication
- `POST /api/accounts/login/` - User login
- `POST /api/accounts/register/` - User registration
- `POST /api/accounts/logout/` - User logout
- `GET /api/accounts/profile/` - User profile

### Products
- `GET /api/products/` - List products
- `POST /api/products/` - Create product (vendor/admin)
- `PUT /api/products/{id}/` - Update product
- `DELETE /api/products/{id}/` - Delete product

### Orders
- `GET /api/orders/` - User orders
- `POST /api/orders/create/` - Create order
- `GET /api/orders/{id}/` - Order details
- `PUT /api/orders/{id}/status/` - Update order status

### Cart
- `GET /api/orders/cart/` - Cart contents
- `POST /api/orders/cart/add/` - Add to cart
- `PUT /api/orders/cart/items/{id}/` - Update cart item
- `DELETE /api/orders/cart/items/{id}/` - Remove cart item

### Admin
- `GET /api/accounts/users/` - All users
- `GET /api/accounts/admin/vendors/` - Vendor management
- `PUT /api/accounts/admin/vendors/{id}/approve/` - Approve vendor
- `GET /api/orders/admin/all/` - All orders

## 🎨 UI Components

### Custom Components
- **ProductCard**: Product display with actions
- **ShoppingCart**: Cart management interface
- **SearchFilter**: Product search and filtering
- **NotificationSystem**: Real-time notifications
- **OrderTracking**: Order status visualization

### Responsive Design
- **Mobile-first**: Optimized for all devices
- **Breakpoints**: Tailwind CSS responsive utilities
- **Touch-friendly**: Mobile interaction patterns

## 🔄 Real-time Features

### WebSocket Integration
```javascript
// Real-time order updates
const ws = new WebSocket('ws://localhost:8000/ws/ecommerce/')
ws.onmessage = (event) => {
  const data = JSON.parse(event.data)
  handleRealTimeUpdate(data)
}
```

### Live Notifications
- **Order Status**: Real-time order updates
- **Product Approval**: Vendor notifications
- **System Messages**: Admin announcements

## 📊 Analytics & Reporting

### Vendor Analytics
- **Sales Tracking**: Revenue and order metrics
- **Product Performance**: Best-selling products
- **Customer Analytics**: Purchase patterns

### Admin Dashboard
- **System Statistics**: Overall platform metrics
- **User Activity**: Registration and engagement
- **Order Analytics**: Processing and fulfillment

## 🚀 Deployment

### Production Setup
```bash
# Backend
export DEBUG=False
export ALLOWED_HOSTS=yourdomain.com
python manage.py collectstatic
python manage.py runserver 0.0.0.0:8000

# Frontend
npm run build
# Deploy dist/ to web server
```

### Environment Variables
```bash
# Backend
DEBUG=False
SECRET_KEY=your-secret-key
ALLOWED_HOSTS=localhost,127.0.0.1,yourdomain.com

# Frontend
VITE_API_BASE_URL=http://yourdomain.com/api
```

## 🧪 Testing

### Backend Tests
```bash
python manage.py test
python manage.py test accounts.tests
python manage.py test products.tests
python manage.py test orders.tests
```

### Frontend Tests
```bash
npm run test
npm run test:e2e
```

## 📝 Development Guidelines

### Code Style
- **Python**: PEP 8 compliance
- **JavaScript**: ESLint configuration
- **Vue.js**: Composition API patterns
- **CSS**: Tailwind CSS utilities

### Git Workflow
```bash
git add .
git commit -m "feat: add new feature"
git push origin main
```

## 🐛 Troubleshooting

### Common Issues

#### Backend Issues
- **Migration Errors**: `python manage.py migrate --fake`
- **Static Files**: `python manage.py collectstatic --noinput`
- **Database**: Delete `db.sqlite3` and re-migrate

#### Frontend Issues
- **Dependencies**: `npm install --force`
- **Build Errors**: Clear `node_modules` and reinstall
- **API Connection**: Check backend server status

### Debug Mode
```bash
# Backend debug
python manage.py runserver --debug

# Frontend debug
npm run dev --debug
```

## 📞 Support

### Documentation
- **API Docs**: `/api/docs/` (when enabled)
- **Admin Panel**: `/admin/`
- **API Testing**: Use Postman or curl

### Contact
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Email**: support@kafuka-electronics.com

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- **Vue.js Team**: For the amazing framework
- **Django Team**: For the robust backend
- **Tailwind CSS**: For the utility-first CSS framework
- **Open Source Community**: For the incredible ecosystem

---

**KAFUKA Electronics E-commerce Platform** - Complete e-commerce solution for modern businesses.
