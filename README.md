# 🍋 Little Lemon Web Application: Backend Capstone Project

<p float="left">
    <img src="https://images.credly.com/size/340x340/images/4d81763c-b917-4ab9-92be-103af95c0a21/image.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/e98be3cedc71306d45526dda26a35558ec7fcc0d/Images/Menu/Little%20Lemon.jpg" width="300" />
</p>

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/Django_REST-FF1709?style=for-the-badge&logo=django&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Insomnia](https://img.shields.io/badge/Insomnia-4000BF?style=for-the-badge&logo=insomnia&logoColor=white)
![Unit Testing](https://img.shields.io/badge/Unit_Testing-25A162?style=for-the-badge&logo=testcafe&logoColor=white)

## 📋 Table of Contents
- [🎯 Project Overview](#-project-overview)
- [✨ Live Application Demo](#-live-application-demo)
- [📁 Project Structure](#-project-structure)
- [🔄 Project Workflow & Architecture](#-project-workflow--architecture)
- [🍽️ Key Application Features](#️-key-application-features)
- [🛠️ Technical Stack](#️-technical-stack)
- [📊 Database Schema](#-database-schema)
- [🚀 Implementation Guide](#-implementation-guide)
- [🔗 API Documentation](#-api-documentation)
- [🧪 Testing & Quality Assurance](#-testing--quality-assurance)
- [🏆 Project Achievements](#-project-achievements)
- [📝 Methodology](#-methodology)
- [🎨 Design Philosophy](#-design-philosophy)
- [👥 Acknowledgments](#-acknowledgments)
- [📄 License](#-license)

## 🎯 Project Overview

This comprehensive **Meta Back-End Developer Capstone Project** demonstrates end-to-end backend development skills through the design and implementation of the **Little Lemon Restaurant Management System**. As a Backend Developer, I built a full-featured web application with Django and Django REST Framework that handles menu management, customer reservations, user authentication, and provides a robust API for frontend integration.

<p float="left">
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Menu/127.0.0.1_9000_api_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Reservations%20and%20Registrations/127.0.0.1_9000_api_book_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Reservations%20and%20Registrations/127.0.0.1_9000_api_reservations_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Menu/127.0.0.1_9000_api_about_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Menu/127.0.0.1_9000_api_menu_item_2_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Reservations%20and%20Registrations/127.0.0.1_9000_api_register_.png" width="300" />
</p>

<p float="left">
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/API/127.0.0.1_9000_api_menu-items_1_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/API/127.0.0.1_9000_api_menu-items__page%3D8%20(1).png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/API/127.0.0.1_9000_api_menu-items__search%3DBurgers.png" width="300" />
</p>

## ✨ Live Application Preview

![View Application](https://img.shields.io/badge/🍽️_View_Application-DC2626?style=for-the-badge&logo=django&logoColor=white) ![Preview](https://img.shields.io/badge/Local_Development-10B981?style=for-the-badge&logo=server&logoColor=white)

*Note: This is a backend development project. To run the application locally, follow the installation guide below.*

## 📁 Project Structure

```
📂 Meta-Backend-Capstone-Project/
│
├── 📂 Images/
│   ├── 📂 API/
│   │   ├── Admin interface screenshots
│   │   ├── API endpoint examples
│   │   └── Search functionality examples
│   │
│   ├── 📂 Menu/
│   │   ├── Menu listing pages
│   │   ├── Individual menu item pages
│   │   └── About page screenshots
│   │
│   ├── 📂 Reservations and Registrations/
│   │   ├── Booking forms
│   │   ├── Reservation listings
│   │   └── User registration pages
│   │
│   └── Little Lemon Logo.png
│
├── 📂 littlelemon/
│   ├── 📂 littlelemon/ (Project configuration)
│   │   ├── settings.py (Django settings)
│   │   ├── urls.py (Main URL routing)
│   │   └── wsgi.py (WSGI configuration)
│   │
│   ├── 📂 restaurant/ (Main application)
│   │   ├── 📂 migrations/ (Database migrations)
│   │   ├── 📂 static/ (Static assets)
│   │   │   ├── 📂 css/ (Stylesheets)
│   │   │   └── 📂 img/ (Images)
│   │   │
│   │   ├── 📂 templates/ (HTML templates)
│   │   │   ├── 📂 partials/ (Template partials)
│   │   │   ├── about.html
│   │   │   ├── base.html
│   │   │   ├── book.html
│   │   │   ├── index.html
│   │   │   └── menu.html
│   │   │
│   │   ├── 📂 media/ (Uploaded media files)
│   │   │   └── menu_items/ (Menu item images)
│   │   │
│   │   ├── __init__.py
│   │   ├── admin.py (Admin configuration)
│   │   ├── apps.py (App configuration)
│   │   ├── forms.py (Django forms)
│   │   ├── models.py (Database models)
│   │   ├── serializers.py (API serializers)
│   │   ├── test_models.py (Model tests)
│   │   ├── test_serializers.py (Serializer tests)
│   │   ├── test_views.py (View tests)
│   │   ├── tests.py (Additional tests)
│   │   ├── urls.py (App URL routing)
│   │   └── views.py (View functions)
│   │
│   ├── 📂 .venv/ (Virtual environment - ignored)
│   ├── manage.py (Django management script)
│   ├── Pipfile (Dependencies)
│   ├── Pipfile.lock (Locked dependencies)
│   └── Database_INFO.txt (Database configuration)
│
├── 📜 LICENSE
├── 📜 README.md
└── 📜 project_structure.txt
```

## 🔄 Project Workflow & Architecture

### **Step 1: Project Setup & Configuration** ⚙️
- **Django Project Initialization**: Created project structure with proper settings
- **Virtual Environment**: Isolated Python dependencies using pipenv
- **Application Creation**: Set up `restaurant` app with MVC architecture
- **Tools**: Django CLI, pipenv, Python 3.8+

### **Step 2: Database Design & Implementation** 🗃️
- **MySQL Database**: Configured relational database for restaurant data
- **Model Creation**: Designed Menu, Booking, User, and Category models
- **Migrations**: Generated and applied database schema migrations
- **Admin Interface**: Customized Django admin for data management

### **Step 3: REST API Development** 🌐
- **Django REST Framework**: Implemented RESTful API endpoints
- **Serializers**: Created data transformation layers
- **ViewSets & Routers**: Implemented CRUD operations for all models
- **Pagination & Filtering**: Added API optimization features
- **Tools**: DRF, Insomnia for API testing

### **Step 4: User Authentication & Authorization** 🔐
- **Djoser Integration**: Implemented token-based authentication
- **User Registration**: Created signup flow with validation
- **Login/Logout**: Implemented secure session management
- **Permissions**: Configured role-based access control
- **Tools**: Djoser, Django auth system

### **Step 5: Frontend-Backend Integration** 🎨
- **Template System**: Created Django HTML templates with Bootstrap
- **Static Files**: Managed CSS, JavaScript, and images
- **Form Handling**: Implemented Django forms for user input
- **Media Uploads**: Configured file uploads for menu items
- **Tools**: Django templating, Bootstrap 5

### **Step 6: Testing & Quality Assurance** 🧪
- **Unit Tests**: Created comprehensive test suite for models
- **Integration Tests**: Tested API endpoints and views
- **Test Coverage**: Ensured critical functionality was tested
- **Continuous Testing**: Implemented test-driven development practices
- **Tools**: Django test framework, unittest

### **Step 7: Documentation & Deployment Preparation** 📚
- **API Documentation**: Documented all endpoints and usage
- **Project Documentation**: Created comprehensive README and guides
- **Deployment Configuration**: Prepared settings for production
- **Performance Optimization**: Applied database and query optimizations

## 🍽️ Key Application Features

### **Menu Management System** 📋
- **Dynamic Menu Display**: Real-time menu listing with categories
- **Search Functionality**: Filter menu items by name or category
- **Detailed Views**: Individual menu item pages with descriptions
- **Image Uploads**: Support for menu item photos
- **Admin Control**: Full CRUD operations for restaurant staff

### **Reservation System** 📅
- **Online Booking**: Customer-facing reservation form
- **Date/Time Validation**: Prevents double bookings and validates times
- **Reservation Management**: View and manage all bookings
- **Customer Notifications**: Confirmation system (stubbed for extension)
- **Capacity Management**: Restaurant seating optimization

### **User Authentication System** 👥
- **Customer Registration**: Simple signup process
- **Secure Login**: Token-based authentication
- **Profile Management**: User details and preferences
- **Session Handling**: Persistent login sessions
- **Password Security**: Hashed password storage

### **Admin Dashboard** 🛠️
- **Django Admin**: Full-featured administration interface
- **Data Management**: Edit all models through admin
- **User Management**: Control customer and staff accounts
- **Content Management**: Update menu items and categories
- **Analytics**: Basic reporting and data insights

### **RESTful API** 🔌
- **Complete CRUD API**: Full REST endpoints for all models
- **Authentication Endpoints**: Signup, login, token management
- **Pagination**: Efficient data loading for large datasets
- **Filtering & Sorting**: Advanced query capabilities
- **JSON Responses**: Standardized API responses

## 🛠️ Technical Stack

### **Backend Framework**
![Django](https://img.shields.io/badge/Django_4.2-092E20?style=for-the-badge&logo=django&logoColor=white)
![Django REST](https://img.shields.io/badge/Django_REST_Framework-FF1709?style=for-the-badge&logo=django&logoColor=white)
![Python](https://img.shields.io/badge/Python_3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)

### **Database & ORM**
![MySQL](https://img.shields.io/badge/MySQL_8.0-4479A1?style=for-the-badge&logo=mysql&logoColor=white)
![Django ORM](https://img.shields.io/badge/Django_ORM-0C4B33?style=for-the-badge&logo=django&logoColor=white)
![Database Migrations](https://img.shields.io/badge/Database_Migrations-8B5CF6?style=for-the-badge)

### **Authentication & Security**
![Djoser](https://img.shields.io/badge/Djoser_Auth-F59E0B?style=for-the-badge)
![Token Authentication](https://img.shields.io/badge/Token_Authentication-10B981?style=for-the-badge)
![Password Hashing](https://img.shields.io/badge/Password_Hashing-EF4444?style=for-the-badge)

### **Testing & Development Tools**
![Unit Testing](https://img.shields.io/badge/Unit_Testing-25A162?style=for-the-badge&logo=testcafe&logoColor=white)
![Insomnia](https://img.shields.io/badge/Insomnia_API_Client-4000BF?style=for-the-badge&logo=insomnia&logoColor=white)
![Git Version Control](https://img.shields.io/badge/Git-F05032?style=for-the-badge&logo=git&logoColor=white)

### **Frontend Integration**
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap_5-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

## 📊 Database Schema

### **Core Models**
| Model | Purpose | Key Fields | Relationships |
|-------|---------|------------|---------------|
| **User** | User authentication & profiles | username, email, password | One-to-many with Booking |
| **Category** | Menu categorization | name, slug | One-to-many with MenuItem |
| **MenuItem** | Restaurant menu items | title, price, description | ForeignKey to Category |
| **Booking** | Customer reservations | user, date, time, guests | ForeignKey to User |
| **Order** | Customer orders | user, date, total | One-to-many with OrderItem |
| **OrderItem** | Individual order items | order, menu_item, quantity | ForeignKey to Order & MenuItem |

### **Database Relationships**
```
User ────┐
         │
         ├─ has many ──→ Bookings
         │
         └─ has many ──→ Orders
                           │
                           └─ has many ──→ OrderItems
                                              │
                                              └─ belongs to ──→ MenuItem
                                                                  │
                                                                  └─ belongs to ──→ Category
```

## 🚀 Implementation Guide

### **For Backend Developers**
1. **Environment Setup**
   ```bash
   git clone https://github.com/Willie-Conway/Meta-Backend-Capstone-Project.git
   cd Meta-Backend-Capstone-Project/littlelemon
   pipenv install
   pipenv shell
   ```

2. **Database Configuration**
   ```bash
   # Update Database_INFO.txt with your MySQL credentials
   # Configure settings.py with database connection
   python manage.py migrate
   python manage.py createsuperuser
   ```

3. **Run Development Server**
   ```bash
   python manage.py runserver
   # Access at http://127.0.0.1:8000
   ```

### **For API Consumers**
1. **Explore API Endpoints**
   ```
   http://127.0.0.1:8000/api/           # API Root
   http://127.0.0.1:8000/api/menu-items/ # Menu Items
   http://127.0.0.1:8000/api/bookings/   # Bookings
   ```

2. **Test with Insomnia/Postman**
   - Import the provided API collection
   - Test authentication endpoints first
   - Explore CRUD operations on all resources

### **For Frontend Developers**
1. **API Integration**
   ```javascript
   // Example: Fetch menu items
   fetch('http://127.0.0.1:8000/api/menu-items/')
     .then(response => response.json())
     .then(data => console.log(data));
   ```

2. **Authentication Flow**
   ```javascript
   // Example: User login
   fetch('http://127.0.0.1:8000/auth/token/login/', {
     method: 'POST',
     body: JSON.stringify({username, password})
   });
   ```

## 🔗 API Documentation

### **Authentication Endpoints**
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `POST` | `/auth/users/` | Register new user | No |
| `POST` | `/auth/token/login/` | Login (get token) | No |
| `POST` | `/auth/token/logout/` | Logout (invalidate token) | Yes |
| `GET` | `/auth/users/me/` | Get current user profile | Yes |

### **Menu Endpoints**
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/menu-items/` | List all menu items | No |
| `GET` | `/api/menu-items/{id}/` | Get specific menu item | No |
| `POST` | `/api/menu-items/` | Create menu item | Admin only |
| `PUT` | `/api/menu-items/{id}/` | Update menu item | Admin only |
| `DELETE` | `/api/menu-items/{id}/` | Delete menu item | Admin only |

### **Booking Endpoints**
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/bookings/` | List user's bookings | Yes |
| `GET` | `/api/bookings/{id}/` | Get specific booking | Yes (owner) |
| `POST` | `/api/bookings/` | Create new booking | Yes |
| `PUT` | `/api/bookings/{id}/` | Update booking | Yes (owner) |
| `DELETE` | `/api/bookings/{id}/` | Delete booking | Yes (owner) |

### **Category Endpoints**
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/categories/` | List all categories | No |
| `GET` | `/api/categories/{id}/` | Get specific category | No |
| `POST` | `/api/categories/` | Create category | Admin only |

### **Order Endpoints**
| Method | Endpoint | Description | Auth Required |
|--------|----------|-------------|---------------|
| `GET` | `/api/orders/` | List user's orders | Yes |
| `POST` | `/api/orders/` | Create new order | Yes |
| `GET` | `/api/orders/{id}/` | Get specific order | Yes (owner) |

### **Query Parameters**
```
# Pagination
/api/menu-items/?page=2&page_size=10

# Filtering
/api/menu-items/?category=1
/api/menu-items/?price__gte=10&price__lte=20

# Searching
/api/menu-items/?search=pizza

# Ordering
/api/menu-items/?ordering=price
/api/menu-items/?ordering=-created_at
```

## 🧪 Testing & Quality Assurance

### **Test Suite Structure**
```
📂 tests/
├── test_models.py           # Database model tests
├── test_serializers.py     # API serializer tests
├── test_views.py          # View and API endpoint tests
└── tests.py              # Additional integration tests
```

### **Running Tests**
```bash
# Run all tests
python manage.py test

# Run specific test module
python manage.py test restaurant.tests.test_models

# Run with coverage report
coverage run manage.py test
coverage report
coverage html
```

### **Test Coverage**
- **Model Validation**: All database models have validation tests
- **API Endpoints**: CRUD operations tested for each resource
- **Authentication**: Login, registration, and token tests
- **Permissions**: Role-based access control tests
- **Edge Cases**: Error handling and boundary tests

### **Example Test Case**
```python
class MenuItemModelTest(TestCase):
    def test_create_menu_item(self):
        """Test creating a new menu item"""
        category = Category.objects.create(name="Appetizers")
        menu_item = MenuItem.objects.create(
            title="Bruschetta",
            price=8.99,
            category=category,
            description="Toasted bread with tomatoes"
        )
        self.assertEqual(menu_item.title, "Bruschetta")
        self.assertEqual(menu_item.price, 8.99)
        self.assertEqual(menu_item.category.name, "Appetizers")
```

## 🏆 Project Achievements

✅ **Complete Django Backend** with MVC architecture  
✅ **RESTful API** with full CRUD operations  
✅ **MySQL Database** with optimized schema design  
✅ **User Authentication** with token-based security  
✅ **Comprehensive Testing Suite** with high coverage  
✅ **Admin Interface** for restaurant management  
✅ **Frontend-Backend Integration** with templates  
✅ **API Documentation** for external consumers  
✅ **Scalable Architecture** for future enhancements  

## 📝 Methodology

### **Agile Development Approach**
1. **Sprint Planning**
   - User story creation
   - Task breakdown
   - Priority assignment

2. **Incremental Development**
   - Feature-by-feature implementation
   - Continuous integration
   - Regular testing

3. **Code Review & Refactoring**
   - Peer reviews
   - Code quality checks
   - Performance optimization

### **Test-Driven Development**
1. **Red Phase**: Write failing tests
2. **Green Phase**: Implement minimal code to pass tests
3. **Refactor Phase**: Improve code while maintaining tests

### **API-First Design**
1. **Contract Definition**: Define API endpoints and responses
2. **Implementation**: Build backend to match contracts
3. **Documentation**: Create comprehensive API docs
4. **Testing**: Verify API behavior matches contracts

## 🎨 Design Philosophy

### **RESTful Principles**
- **Stateless Operations**: Each request contains all necessary information
- **Resource-Based URLs**: Clear, predictable endpoint structure
- **HTTP Methods**: Proper use of GET, POST, PUT, DELETE
- **Standard Status Codes**: Meaningful HTTP response codes

### **Security-First Approach**
- **Input Validation**: Sanitize all user inputs
- **Authentication**: Secure token-based auth system
- **Authorization**: Role-based access control
- **Data Protection**: Encrypted sensitive information

### **Scalability Considerations**
- **Database Indexing**: Optimized query performance
- **Caching Strategy**: Implemented caching layers
- **Code Modularity**: Reusable, maintainable components
- **Configuration Management**: Environment-specific settings

### **User Experience**
- **Responsive Design**: Mobile-friendly interfaces
- **Intuitive Navigation**: Clear user flows
- **Error Handling**: Helpful error messages
- **Performance**: Fast loading times

## 👥 Acknowledgments

- **Meta Back-End Developer Professional Certificate** program
- **Django Software Foundation** for the excellent web framework
- **MySQL** development team for robust database tools
- **Django REST Framework** team for powerful API toolkit
- **Educational Instructors** and mentors for guidance

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details. The Little Lemon brand and concept are used for educational purposes as part of the Meta Back-End Developer Capstone Project.

---

⭐ **This project demonstrates comprehensive backend development skills using Django and modern web technologies. Feedback and contributions are welcome!** ⭐

*Project Completed: As part of Meta Back-End Developer Professional Certificate*  
*Last Updated: January 28, 2025*
