# CREATE ENV
python3 -m venv venv
source venv/bin/activate

pip install Django django-ajax-selects

# RUN MIGRATIONS
python manage.py makemigrations
python manage.py migrate

# RUN SERVER
python manage.py runserver
