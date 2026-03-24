# Demo E-commerce Platform

Full-stack e-commerce application with Vue.js frontend and Django REST API backend.

## Project Structure

```
demo-ecommerce/
├── frontend/          # Vue.js frontend application
├── backend/           # Django REST API backend
└── README.md          # This file
```

## Frontend (Vue.js)

- **Technology**: Vue 3, Vite, TailwindCSS
- **Location**: `frontend/` directory
- **Start**: `cd frontend && npm run dev`
- **Port**: Usually 5173

## Backend (Django)

- **Technology**: Django, Django REST Framework
- **Location**: `backend/` directory
- **Start**: `cd backend && source venv/bin/activate && python manage.py runserver`
- **Port**: Usually 8000

## Features

### User Roles
- **Customer**: Browse products, add to cart, place orders
- **Author**: Upload and manage products
- **Admin**: Manage users, products, and orders

### API Endpoints
- **Authentication**: `/api/auth/`
- **Products**: `/api/products/`
- **Orders**: `/api/orders/`

## Quick Start

### Frontend
```bash
cd frontend
npm install
npm run dev
```

### Backend
```bash
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Admin Access
- **URL**: http://localhost:8000/admin/
- **Username**: apk
- **Password**: apk

## Development
- Frontend runs on http://localhost:5173
- Backend runs on http://localhost:8000
- API available at http://localhost:8000/api/
