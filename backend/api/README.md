# Backend
This is a Django project, tested on 3.6.9. To install using virtualenv:
```
virtualenv .venv --python=3.6.9
pip install -r requirements.txt
```

Activate the virtual environment with `source .venv/bin/activate`. Then, to 
initialize the project:
```
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

You should be able to run the server now with `python manage.py runserver`.