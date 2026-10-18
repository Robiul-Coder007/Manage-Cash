# Manage Cash - Personal Cash Management Web App

A Python Django web application designed to help users track income, expenses, and overall financial stability.

## Features

- User Authentication (Login & Register)
- Profile Management
- Dashboard for Income, Expenses, and Net Balance Calculation
- Add/Track Cash and Expenses

## Installation & Setup

**Clone the repository:**
   ```bash
bash
git clone https://github.com/Robiul-Coder007/Manage-Cash.git .
cd Manage Cash

**Create and activate a virtual environment:**

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install dependencies:

Bash
pip install django
Run migrations:

Bash
python manage.py makemigrations
python manage.py migrate
Create a superuser:

Bash
python manage.py createsuperuser
Run the development server:

Bash
python manage.py runserver