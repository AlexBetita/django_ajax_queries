# CREATE ENV
python3 -m venv venv
source venv/bin/activate

pip install Django django-ajax-selects

# RUN MIGRATIONS
python manage.py makemigrations
python manage.py migrate

# RUN SERVER
python manage.py runserver

Sample pics:
![image](https://github.com/user-attachments/assets/fd7f5dac-2e09-4af7-b382-b63b40ccec11)
![image](https://github.com/user-attachments/assets/385e2b96-60db-416b-b9e8-2ed88d2d3aa2)
![image](https://github.com/user-attachments/assets/24eb73f6-8256-4e23-9e8b-0678421a5acb)
