# Recruitment System

A Django-based Recruitment Management System that allows users to submit and view application data efficiently. It provides REST API endpoints for adding and retrieving applications, with CRUD functionality handled through Django’s built-in admin panel.

## Features
- Submit new applications via API  
- View all submitted applications (no authentication required)  
- Manage (create, read, update, delete) applications via the admin panel  
- SQLite database for data storage  
- Django-based backend structure  

## Tech Stack
- Backend: Python (Django)  
- Database: SQLite  
- Version Control: Git & GitHub  

## Getting Started

### 1. Clone the repository
git clone https://github.com/Tb-Gith/recruitment-system.git
cd recruitment-system



### 2. Set up a virtual environment
python -m venv venv
venv\Scripts\activate # (on Windows)



### 3. Install dependencies
pip install django



### 4. Run database migrations
python manage.py makemigrations
python manage.py migrate



### 5. Create a superuser (for admin access)
python manage.py createsuperuser



### 6. Run the development server
python manage.py runserver



Access the app at:  
- Applications API: http://127.0.0.1:8000/applications  
- Admin panel: http://127.0.0.1:8000/admin  

## Project Overview
This project demonstrates core backend concepts such as models, views, URLs, and CRUD operations using Django and SQLite. It is suitable as a beginner-level backend development project.

## Author
**Tharun Balaji**  
GitHub: [Tb-Gith](https://github.com/Tb-Gith)
