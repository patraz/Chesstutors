python manage.py makemigrations
python manage.py migrate
gunicorn chesstutors.wsgi --bind=0.0.0.0:80