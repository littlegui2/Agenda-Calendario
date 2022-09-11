# Agenda-Calendario

cd event-calendar

python3 -m venv venv
source env/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
