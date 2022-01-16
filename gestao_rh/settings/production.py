from .settings import *

DEBUG = False

SECRET_KEY = '!2qszk_y7i(9wtiryhuow1mqmoxxqb^7^iw%50csx%nx2t=nw6'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}