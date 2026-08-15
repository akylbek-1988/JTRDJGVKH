# Django REST Framework backend

This project now uses Django REST Framework with PostgreSQL support.

1. Create a PostgreSQL database and user.
2. Copy `.env.example` to `.env`, enter your database credentials, then load those variables in your shell.
3. Install packages: `py -m pip install -r requirements.txt`
4. Create tables: `py manage.py makemigrations api` and `py manage.py migrate`
5. Create an administrator: `py manage.py createsuperuser`
6. Start it: `py manage.py runserver`

Swagger UI: `http://127.0.0.1:8000/api/docs/`  
OpenAPI schema: `http://127.0.0.1:8000/api/schema/`  
Django admin: `http://127.0.0.1:8000/admin/`

Public read endpoints are `/api/teachers/`, `/api/courses/`, `/api/news/`, `/api/events/`, `/api/gallery/`, `/api/books/`, and `/api/faqs/`. Authenticated users can create, edit, and delete their content. Public submissions use `POST /api/applications/` and `POST /api/contact-messages/`.
