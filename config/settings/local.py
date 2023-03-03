from .base import *

DEBUG = True
SECRET_KEY = SECRET_KEY or \
             'django-insecure-tf^+mft-c2^#fa)m(ysvyuj7fc6&ypzbxs1xdl_6$bnp7&y22c'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
