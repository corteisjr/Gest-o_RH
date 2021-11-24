import os
from .settings import *

DEBUG = False

SECRET_KEY = '=+pecle1kks@noj2js^x6%pth2vjs)jfkb2*3^%#%+=i%h-2ib'

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3')
    }
}