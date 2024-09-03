# Packages
django
python-dotenv
djangorestframework
pytest
pytest-django
django-mptt
drf-spectacular
coverage
pytest-cov
pytest-factoryboy

# Commands
python3 -m venv .venv
source .venv/bin/activate
pip install django
django-admin startproject drfecommerce .

python manage.py runserver

from django.core.management.utils import get_random_secret_key
print(get_random_secret_key())

pip install python-dotenv
pip install --upgrade pip
pip install djangorestframework
pip install pytest
pytest
pip install pytest-django
pip install django-mptt
pip install drf-spectacular
python manage.py spectacular --file schema.yaml
pip install coverage
coverage
pip install pytest-cov
pip install pytest-factoryboy