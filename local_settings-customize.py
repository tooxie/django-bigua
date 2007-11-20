# coding=UTF-8
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

AUTH_PROFILE_MODULE = 'canchas.Socio'
