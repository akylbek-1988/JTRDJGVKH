import os
from pathlib import Path
from urllib.parse import unquote, urlparse

BASE_DIR = Path(__file__).resolve().parent.parent


def load_dotenv(path):
    """Load simple KEY=value settings without adding another dependency."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


load_dotenv(BASE_DIR / ".env")
SECRET_KEY = os.getenv("SECRET_KEY", "unsafe-development-key-change-me")
# Development may opt in with DEBUG=True in .env. Never expose Django's debug
# page when deployment variables have not yet been configured.
DEBUG = os.getenv("DEBUG", "False").lower() == "true"
default_allowed_hosts = {"127.0.0.1", "localhost", "jtrdjgvkh.onrender.com"}
configured_allowed_hosts = {
    host.strip() for host in os.getenv("ALLOWED_HOSTS", "").split(",") if host.strip()
}
# Keep the service's Render hostname even if the dashboard variable is empty.
ALLOWED_HOSTS = sorted(default_allowed_hosts | configured_allowed_hosts)
CSRF_TRUSTED_ORIGINS = [origin.strip() for origin in os.getenv(
    "CSRF_TRUSTED_ORIGINS", "https://jtrdjgvkh.onrender.com"
).split(",") if origin.strip()]

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "rest_framework",
    "drf_spectacular",
    "api",
]
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]
ROOT_URLCONF = "config.urls"
TEMPLATES = [{
    "BACKEND": "django.template.backends.django.DjangoTemplates",
    "DIRS": [BASE_DIR / "templates"],
    "APP_DIRS": True,
    "OPTIONS": {"context_processors": [
        "django.template.context_processors.request",
        "django.contrib.auth.context_processors.auth",
        "django.contrib.messages.context_processors.messages",
    ]},
}]
WSGI_APPLICATION = "config.wsgi.application"
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# PostgreSQL is used when Render's DATABASE_URL or individual connection variables
# are supplied. SQLite keeps local development usable before PostgreSQL is installed.
database_url = os.getenv("DATABASE_URL")
if database_url:
    parsed_database_url = urlparse(database_url)
    DATABASES = {"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": parsed_database_url.path.lstrip("/"),
        "USER": unquote(parsed_database_url.username or ""),
        "PASSWORD": unquote(parsed_database_url.password or ""),
        "HOST": parsed_database_url.hostname or "127.0.0.1",
        "PORT": str(parsed_database_url.port or 5432),
        "CONN_MAX_AGE": 60,
    }}
elif os.getenv("POSTGRES_DB"):
    DATABASES = {"default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ["POSTGRES_DB"],
        "USER": os.getenv("POSTGRES_USER", "postgres"),
        "PASSWORD": os.getenv("POSTGRES_PASSWORD", ""),
        "HOST": os.getenv("POSTGRES_HOST", "127.0.0.1"),
        "PORT": os.getenv("POSTGRES_PORT", "5432"),
    }}
else:
    DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": BASE_DIR / "db.sqlite3"}}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "Asia/Almaty"
USE_I18N = True
USE_TZ = True
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

REST_FRAMEWORK = {
    "DEFAULT_SCHEMA_CLASS": "drf_spectacular.openapi.AutoSchema",
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.IsAuthenticatedOrReadOnly"],
}
SPECTACULAR_SETTINGS = {
    "TITLE": "Madrasah API",
    "DESCRIPTION": "REST API for courses, teachers, news, events, library, and admissions.",
    "VERSION": "1.0.0",
    "SERVE_INCLUDE_SCHEMA": False,
}
