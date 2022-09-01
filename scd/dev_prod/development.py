import environ

env = environ.Env()
environ.Env.read_env()
SECRET_KEY = env('SECRET_KEY')
ALLOWED_HOSTS = []
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': str(env('NAME')),
        'USER': str(env('USER')),
        'PASSWORD': str(env('PASSWORD')),
        'HOST': str(env('HOST')),
        'DATABASE_PORT': str(env('DATABASE_PORT')),

    }
}