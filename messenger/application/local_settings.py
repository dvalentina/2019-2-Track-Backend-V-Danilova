DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '&vjz95og59qv1cn6640!#4+wstvss#9!n9(ux4t%7&1nepqz(u'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'quack_db',
	'USER': 'quack',
	'PASSWORD': 's3cr3t',
	'HOST': '127.0.0.1',
	'PORT': '5432',
    }
}
