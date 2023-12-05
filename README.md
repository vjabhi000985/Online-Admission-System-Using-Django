# Online-Admission-System-Using-Django

## Introduction

This project is a web-based Online Admission System developed using Django, a high-level Python web framework. The system utilizes SQLite3 as the database, Bootstrap for styling, and Jinja2 syntax for templates.

## Features

- *User Authentication*: Secure registration and login functionality.
- *Admission Process*: Streamlined admission process for students.
- *Database Integration*: SQLite3 used for efficient data management.
- *Responsive Design*: Bootstrap ensures a mobile-friendly user interface.

## Installation

### 1. Install Django
```bash
pip install django
```

### 2. Clone the Repository
```bash
git clone https://github.com/vjabhi000985/Online-Admission-System-Using-Django.git
cd admission
```

### 3. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate
```

### 4. Install Dependencies
```bash
pip install django sqlite3 jinja2
```

### 5. Run Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run Development Server
```bash
python manage.py runserver
```

### 7. Access the Application
Open your browser and go to http://127.0.0.1:8000/

## Project Structure

The project follows a structured layout to organize its components and files. Below is an overview of the main directories and files:

- *`admission_system/`*
  - *`admissions/`*
    - `admin.py`: Admin configuration for models.
    - `models.py`: Definition of database models.
    - `views.py`: Implementation of views and controllers.
    - `urls.py`: URL patterns for the application.
    - `templates/`: HTML templates using Bootstrap and Jinja2 syntax.
  - `settings.py`: Django project settings.
  - `urls.py`: Project-level URL patterns.
  - `manage.py`: Django management script.

 ## Credits
 Developed by *Pandey Abhishek Nath Roy [me] and my team consisting of Shashi Oraon, Abhijit Kumar, Bineet Kumar and Bittu Kumar.*
