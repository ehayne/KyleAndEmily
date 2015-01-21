echo $WORKSPACE
export PROJECT_NAME=kyleandemily
export APP_VERSION=`git rev-parse HEAD | cut -c -12`
export VENV_VERSION=`sha1sum ./requirements.txt | cut -c -12`
export ROOT="/usr/local/${PROJECT_NAME}"
export VERSION_DIR="${ROOT}/versions/${APP_VERSION}"
export APP_DIR="${VERSION_DIR}/app"
export MEDIA_DIR="${ROOT}/media_${APP_ENV}"
export DB_DIR="${ROOT}/db_${APP_ENV}"
export VENV_DIR="${ROOT}/venv_versions/${APP_ENV}_${VENV_VERSION}"
export SOURCE_ENVDIR="${ROOT}/envdir"
export ENVDIR="${VERSION_DIR}/envdir"
export LINKED_VENV_DIR="${VERSION_DIR}/venv"
export SMOKETEST_APP_DIR="${ROOT}/smoketest"
export LINKED_APP_DIR="${ROOT}/${APP_ENV}"
export LINKED_VENV_DIR="${VERSION_DIR}/venv"
export LINKED_MEDIA_DIR="${VERSION_DIR}/media"
export LINKED_DB_DIR="${VERSION_DIR}/db"

mkdir -p "${MEDIA_DIR}"
mkdir -p "${DB_DIR}"

if [[ ! -e "${VERSION_DIR}" ]]
then
  mkdir -p "${APP_DIR}"
  cp -rv "./." "${APP_DIR}"
fi

cp -rv "${SOURCE_ENVDIR}" "${ENVDIR}"
echo "${APP_ENV}" > "${ENVDIR}/APP_ENV"

if [[ ! -e "${VENV_DIR}/bin/activate" ]]
then
  virtualenv "${VENV_DIR}"
  . "${VENV_DIR}/bin/activate"
  pip install -r "./requirements.txt"
else
  . "${VENV_DIR}/bin/activate"
fi

ln -snf "${APP_DIR}" "${SMOKETEST_APP_DIR}"
cd "${SMOKETEST_APP_DIR}"
python manage.py collectstatic --noinput

ln -snf "${APP_DIR}" "${LINKED_APP_DIR}"
ln -snf "${VENV_DIR}" "${LINKED_VENV_DIR}"
ln -snf "${MEDIA_DIR}" "${LINKED_MEDIA_DIR}"
ln -snf "${DB_DIR}" "${LINKED_DB_DIR}"

cd "${LINKED_APP_DIR}"

python manage.py migrate
python manage.py migrate rsvp --database="rsvp_db"

cp -f "${WORKSPACE}/jenkins/nginx.conf" "/etc/nginx/sites-enabled/${PROJECT_NAME}.conf"
cp -f "${WORKSPACE}/jenkins/uwsgi_$APP_ENV.ini" "/usr/local/uwsgi/confs/${PROJECT_NAME}_${APP_ENV}.ini"
cp -f "${WORKSPACE}/jenkins/celeryd.conf" "/usr/local/supervisor/confs/${PROJECT_NAME}_celery.conf"
