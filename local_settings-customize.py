# coding=UTF-8
from os.path import abspath, dirname

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Your Name', 'name@email.com'),
)

MANAGERS = ADMINS

DATABASE_ENGINE = 'mysql'
DATABASE_NAME = 'bigua'
DATABASE_USER = 'user'
DATABASE_PASSWORD = 'password'

TIME_ZONE = 'America/Montevideo'

USE_I18N = True

# MEDIA
PROJECT_ABSOLUTE_DIR = dirname(abspath(__file__))
MEDIA_ROOT = PROJECT_ABSOLUTE_DIR + "/media/"
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin_media/'

CSS_PATH = '%scss/' % MEDIA_URL
JS_PATH = '%sjs/' % MEDIA_URL
