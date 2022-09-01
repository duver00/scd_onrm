import environ
from scd.dev_prod.development import DATABASES, SECRET_KEY

env = environ.Env()
environ.Env.read_env()
ALLOWED_HOSTS = ['127.0.0.0.1','scd.onrm.minem.cu']
