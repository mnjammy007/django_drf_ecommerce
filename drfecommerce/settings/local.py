# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases
from .base import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
