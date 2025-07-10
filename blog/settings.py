from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = True

APP_NAME = "blog"

SECRET_KEY = "blog"

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = []

MIDDLEWARE = []

ROOT_URLCONF = "blog.urls"


TORTOISE_ORM = {
    "connections": {"default": "sqlite://blog.sqlite3"},
    "apps": {
        APP_NAME: {
            "models": ["blog.models", "aerich.models"],
            "default_connection": "default",
        },
    },
    "timezone": "Asia/Shanghai",
}

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = True


