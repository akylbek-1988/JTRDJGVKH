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

## Deploying to Render

The repository includes `render.yaml` for a Render web service. For an existing
service, set its commands in the Render dashboard to:

```text
Build command: pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate
Start command: gunicorn config.wsgi:application
```

Set `SECRET_KEY` to a strong value, `DEBUG=False`, and set `ALLOWED_HOSTS` to
your Render hostname (for example, `your-service.onrender.com`). The Blueprint
creates a Render PostgreSQL database and provides its connection as
`DATABASE_URL`. Do not use `py manage.py` on Render: `py` is the Windows
launcher and is unavailable on the Linux deployment environment.
