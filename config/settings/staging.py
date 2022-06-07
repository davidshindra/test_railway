# emulates production environment
import dj_database_url
from decouple import config

from .settings import *

SECRET_KEY = config('SECRET_KEY')

DEBUG = False

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost'
]

DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://postgres:postgres@localhost:5432/test_railway_staging',
        conn_max_age=600
    )
}