# Little Lemon Web Application

<p float="left">
    <img src="https://tinypic.host/images/2024/10/26/Meta-Back-End-Developer.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Database-Capstone-Project/blob/main/Images/Little%20Lemon%20Logo.png" width="300" />
</p>

## 📖Table of Contents
- [Introduction](#introduction)
- [Project Overview](#project-overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Unit Testing](#unit-testing)
- [Exercises](#exercises)
- [Contributing](#contributing)
- [License](#license)

  
## Introduction
This README provides an overview of the steps taken to develop the Little Lemon Web Application as part of the **Meta Back-End Developer Capstone** Project. The application serves as a restaurant management system, featuring menu and reservation functionalities.

## Project Overview📁
The Little Lemon Web Application is built using `Django` and `Django REST Framework`. It allows users to interact with the restaurant's menu and make reservations through a simple web interface and `RESTful API`.
<p float="left">
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Menu/127.0.0.1_9000_api_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Reservations%20and%20Registrations/127.0.0.1_9000_api_book_.png" width="300" />
    <img src="https://github.com/Willie-Conway/Meta-Backend-Capstone-Project/blob/main/Images/Reservations%20and%20Registrations/127.0.0.1_9000_api_reservations_.png" width="300" />
</p>

## ⚙️Features
- User authentication with token support
- CRUD operations for menu items
- CRUD operations for reservations
- Admin interface for managing menu and reservations
- Unit tests to ensure code reliability

## ⚙️Technologies Used
- **Programming Language:** `Python`
- **Frameworks:** `Django`, `Django REST Framework`
- **Database:** `MySQL`
- **Authentication:** `Djoser`
- **Testing:** Django’s built-in testing framework
- **Development Tools:** `Insomnia`, `Git`, `GitHub`

## Installation🔃
1. **Clone the repository:**
   
   ```bash
   git clone https://github.com/Willie-Conway/Meta-Backend-Capstone-Project.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd LittleLemon
   ```
3. **Set up Python virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
4. **Install Django and other dependencies:**
   ```bash
   pip install django mysqlclient djangorestframework djoser
   ```
5. **Create a new Django project:**
   ```bash
   django-admin startproject LittleLemon
   cd LittleLemon
   ```
6. **Create a new Django app:**
   ```bash
   python manage.py startapp restaurant
   ```
7. **Configure the MySQL database in `settings.py`.**

8. **Migrate the database:**
   ```bash
   python manage.py migrate
   ```
9. **Create a superuser:**
   ```bash
   python manage.py createsuperuser
   ```
10. **Run the server:**
    ```bash
    python manage.py runserver
    ```

## 👨🏿‍💻Usage
- Access the application at `http://localhost:8000`.
- Use **`Insomnia`** or **`Postman`** to test the API endpoints.

## 📍API Endpoints

### Authentication
- POST `/api/auth/signup/` - Register a new user
- POST `/api/auth/login/` - Log in a user
  
### Menu
- GET `/api/menu/` - Retrieve all menu items
- POST `/api/menu/` - Create a new menu item
- GET `/api/menu/:id/` - Retrieve a specific menu item
- PUT `/api/menu/:id/` - Update a menu item
- DELETE `/api/menu/:id/` - Delete a menu item
  
### Reservations
- GET `/api/reservations/` - Retrieve all reservations
- POST `/api/reservations/` - Create a new reservation
- GET `/api/reservations/:id/` - Retrieve a specific reservation
- PUT `/api/reservations/:id/` - Update a reservation
- DELETE `/api/reservations/:id/` - Delete a reservation

## 👨🏿‍💻Unit Testing
- Unit tests for models and views can be found in the `tests` folder.
- To run the tests:
  
  ```bash
  python manage.py test 
  ```

## Exercises🏋🏿‍♂️
This section provides a series of exercises that guide you through the development process of the Little Lemon Web Application. Each exercise is designed to help you implement key features step-by-step.


1. [Setting up the project](#)
2. [Setting up the MySQL database and users](#)
3. [Implementing the Django REST Framework](#)
4. [Installing Djoser and testing with Insomnia](#)
5. [Creating the unit tests](#)

## Contributing
Contributions are welcome! Please follow these steps:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

