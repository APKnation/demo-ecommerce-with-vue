# Electronics Cart Backend

Django REST API for the electronics e-commerce application with role-based permissions.

## Features

- **User Roles**: Customer, Author, Admin
- **Authentication**: Token-based authentication
- **Products**: Authors can upload/manage products
- **Orders**: Customers can place orders, Admins can manage them
- **Shopping Cart**: Full cart functionality
- **CORS**: Configured for Vue.js frontend integration

## API Endpoints

### Authentication
- `POST /api/auth/register/` - User registration
- `POST /api/auth/login/` - User login
- `POST /api/auth/logout/` - User logout
- `GET /api/auth/profile/` - Get user profile
- `PUT /api/auth/profile/` - Update user profile
- `GET /api/auth/users/` - List all users (Admin only)

### Products
- `GET /api/products/` - List all products
- `GET /api/products/<id>/` - Get product details
- `POST /api/products/create/` - Create product (Author/Admin)
- `PUT /api/products/<id>/manage/` - Update product (Owner/Admin)
- `DELETE /api/products/<id>/manage/` - Delete product (Owner/Admin)
- `GET /api/products/my-products/` - Get current user's products
- `GET /api/products/categories/` - List categories
- `POST /api/products/categories/create/` - Create category (Admin)

### Orders
- `GET /api/orders/cart/` - Get cart details
- `POST /api/orders/cart/add/` - Add item to cart
- `PUT /api/orders/cart/items/<id>/` - Update cart item
- `DELETE /api/orders/cart/items/<id>/` - Remove cart item
- `POST /api/orders/create/` - Create order from cart
- `GET /api/orders/` - List user's orders
- `GET /api/orders/<id>/` - Get order details
- `GET /api/orders/admin/all/` - List all orders (Admin)
- `PUT /api/orders/admin/<id>/status/` - Update order status (Admin)

## Setup

1. Create virtual environment:
```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run migrations:
```bash
python manage.py makemigrations
python manage.py migrate
```

4. Create admin user:
```bash
python create_admin.py
```

5. Start server:
```bash
python manage.py runserver 0.0.0.0:8000
```

## Admin Access

- **URL**: http://localhost:8000/admin/
- **Username**: apk
- **Password**: apk

## User Roles

- **Customer**: Can browse products, add to cart, place orders
- **Author**: Can create and manage their own products
- **Admin**: Full access to all features and user management

## Frontend Integration

The API is configured to work with Vue.js frontend running on:
- http://localhost:3000
- http://localhost:5173
- http://127.0.0.1:3000
- http://127.0.0.1:5173

Use token-based authentication for API requests.
