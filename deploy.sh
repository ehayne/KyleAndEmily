echo $WORKSPACE
export PROJECT_NAME=kyleandemily
export VENV_ROOT=/www/.virtualenvs/${PROJECT_NAME}/
export WEB_ROOT=/www/${PROJECT_NAME}

rm -rvf ${WEB_ROOT}
mkdir ${WEB_ROOT}
cp -rv ./* ${WEB_ROOT}
cd ${WEB_ROOT}

ln -s ${VENV_ROOT} ./.virtualenv
. ./.virtualenv/bin/activate
pip install --upgrade -r ./requirements.txt

rm -f /etc/uwsgi/apps-enabled/${PROJECT_NAME}.ini
mv ./wsgi.ini /etc/uwsgi/apps-enabled/${PROJECT_NAME}.ini

rm -f /etc/nginx/conf.d/${PROJECT_NAME}.conf
mv ./nginx.conf /etc/nginx/conf.d/${PROJECT_NAME}.conf

python manage.py collectstatic --noinput