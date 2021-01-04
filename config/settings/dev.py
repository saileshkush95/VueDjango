from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = config(
    "SECRET_KEY", default="bcd92=a1w@)&uunl%^%karsf0he2&y8tm-_3&9j9&jw!k!nkb4"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config("DEBUG", default=True)

ALLOWED_HOSTS = ["127.0.0.1", "localhost"]

# https://github.com/tjwalch/django-livereload-server
LIVE_SERVER = config("LIVE_SERVER", default=False)


# Installed Apps

INSTALLED_APPS += ["debug_toolbar", "django_extensions"]


MIDDLEWARE += [
    "debug_toolbar.middleware.DebugToolbarMiddleware",
]


INTERNAL_IPS = ["127.0.0.1", "10.0.2.2"]

DEBUG_TOOLBAR_PANELS = [
    "debug_toolbar.panels.versions.VersionsPanel",
    "debug_toolbar.panels.timer.TimerPanel",
    "debug_toolbar.panels.settings.SettingsPanel",
    "debug_toolbar.panels.headers.HeadersPanel",
    "debug_toolbar.panels.request.RequestPanel",
    "debug_toolbar.panels.sql.SQLPanel",
    "debug_toolbar.panels.staticfiles.StaticFilesPanel",
    "debug_toolbar.panels.templates.TemplatesPanel",
    "debug_toolbar.panels.cache.CachePanel",
    "debug_toolbar.panels.signals.SignalsPanel",
    "debug_toolbar.panels.logging.LoggingPanel",
    "debug_toolbar.panels.redirects.RedirectsPanel",
    "debug_toolbar.panels.profiling.ProfilingPanel",
]


def show_toolbar(request):
    return True


DEBUG_TOOLBAR_CONFIG = {
    "INTERCEPT_REDIRECTS": False,
    "SHOW_TOOLBAR_CALLBACK": show_toolbar,
}


# Database Setting

USE_SQLITE = config("USE_SQLITE", default=True)

if USE_SQLITE:
    # Database
    # https://docs.djangoproject.com/en/3.0/ref/settings/#databases
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }

else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.postgresql_psycopg2",
            "NAME": config("NAME"),
            "USER": config("USER"),
            "PASSWORD": config("PASSWORD"),
            "HOST": config("HOST"),
            "PORT": config("PORT", default=5432),
        }
    }

# Email Settings
CONSOLE_EMAIL = config("CONSOLE_EMAIL", default=True)

if not CONSOLE_EMAIL:
    EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
    EMAIL_HOST = config("EMAIL_HOST")
    EMAIL_PORT = config("EMAIL_PORT")
    EMAIL_HOST_USER = config("EMAIL_HOST_USER")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD")
    EMAIL_USE_TLS = config("EMAIL_USE_TLS")

else:
    # https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
    EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
