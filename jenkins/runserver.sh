python manage.py collectstatic --noinput
python manage.py syncdb --noinput
python manage.py syncdb --noinput --database="wedding_photo_db" > /dev/null 2>&1
python manage.py syncdb --noinput --database="rsvp_db" > /dev/null 2>&1
python manage.py migrate photologue --noinput --database="wedding_photo_db"
python manage.py migrate rsvp --noinput --database="rsvp_db"
python manage.py runserver
