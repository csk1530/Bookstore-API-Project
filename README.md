# Bookstore-API-Project
# 📚 Bookstore Management System – REST API (Django)

A fully functional **Bookstore Management System backend** built using **Python and Django REST Framework**.
This project provides secure, scalable REST APIs for managing books, users, and orders with **JWT-based authentication** and **role-based access control**.

🚀 Project Overview

The Bookstore Management System is designed to help bookstore owners manage inventory, users, and customer orders efficiently.
Customers can browse books and place orders, while admins can manage books and track all orders.

🎯 Key Features

* 🔐 JWT Authentication (Login & Register)
* 👤 Role-Based Access Control (Admin / Customer)
* 📚 Book Management (CRUD)
* 🛒 Order Management
* 📄 Swagger API Documentation
* 🗄️ Database Integration (SQLite by default)
* ⚠️ Proper Error Handling
* 🧪 Ready for Unit Testing

 🛠️ Technologies Used

* **Backend:** Python, Django, Django REST Framework
* **Authentication:** JWT (`djangorestframework-simplejwt`)
* **Database:** SQLite (can be replaced with PostgreSQL / MySQL)
* **API Docs:** Swagger (`drf-yasg`)
* **Testing:** Django TestCase / Pytest
* **Tools:** Postman, Swagger UI

📂 Project Structure

bookstore_api/
│── accounts/        # User registration & authentication
│── books/           # Book management APIs
│── orders/          # Order management APIs
│── config/          # Project settings & URLs
│── manage.py
│── requirements.txt
│── README.md


⚙️ Setup Instructions (Step by Step)

1️⃣ Clone or Extract Project

```bash
unzip Bookstore_API_Project.zip
cd bookstore_api
```


2️⃣ Create Virtual Environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / Mac**

```bash
source venv/bin/activate
```


3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

4️⃣ Apply Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

---

5️⃣ Create Admin User

```bash
python manage.py createsuperuser
```

(Admin users can manage books and view all orders)


6️⃣ Run the Development Server

```bash
python manage.py runserver
```

Server will start at:

```
http://127.0.0.1:8000/
```

📘 API Documentation (Swagger)

Open Swagger UI:

```
http://127.0.0.1:8000/swagger/
```

You can:

* View all endpoints
* Test APIs directly
* Add JWT token using **Authorize** button

---

 🔐 Authentication Flow

1. Register user
   **POST** `/api/register/`

2. Login and get JWT token
   **POST** `/api/login/`

3. Use token in requests:

```
Authorization: Bearer <your_access_token>
```

---

 🔗 API Endpoints

👤 Authentication

| Method | Endpoint         | Description     |
| ------ | ---------------- | --------------- |
| POST   | `/api/register/` | Register user   |
| POST   | `/api/login/`    | Login & get JWT |

---

### 📚 Books

| Method | Endpoint           | Access |
| ------ | ------------------ | ------ |
| GET    | `/api/books/`      | Public |
| GET    | `/api/books/{id}/` | Public |
| POST   | `/api/books/`      | Admin  |
| PUT    | `/api/books/{id}/` | Admin  |
| DELETE | `/api/books/{id}/` | Admin  |

---

### 🛒 Orders

| Method | Endpoint       | Access             |
| ------ | -------------- | ------------------ |
| GET    | `/api/orders/` | Admin              |
| POST   | `/api/orders/` | Authenticated User |

---

## ⚠️ Error Handling

* **400** – Bad Request (Validation errors)
* **401** – Unauthorized (Invalid / missing JWT)
* **403** – Forbidden (Permission denied)
* **404** – Resource not found
* **500** – Internal server error








