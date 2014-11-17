echo $WORKSPACE
export PROJECT_NAME=kyleandemily
export APP_VERSION=`git rev-parse HEAD | cut -c -12`
export VENV_VERSION=`sha1sum ./requirements.txt | cut -c -12`
export ROOT="/usr/local/$PROJECT_NAME"
export APP_DIR="$ROOT/app_versions/$APP_VERSION"
export VENV_DIR="$ROOT/venv_versions//$VENV_VERSION"
export ACTIVE_APP_DIR="$ROOT/app_prod"
export ACTIVE_VENV_DIR="$ROOT/app_venv"
export MEDIA_DIR="$ROOT/media"
export DB_DIR="$ROOT/db"

mkdir -p "$MEDIA_DIR"
mkdir -p "$DB_DIR"

mkdir -p "$APP_DIR"
cp -rv "./." "$APP_DIR"

if [[ ! -e "$VENV_DIR/bin/activate" ]]
then
  virtualenv "$VENV_DIR"
  . "$VENV_DIR/bin/activate"
  pip install -r "./requirements.txt"
else
  . "$VENV_DIR/bin/activate"
fi

cd "$APP_DIR"
python manage.py collectstatic --noinput
python manage.py migrate --noinput

ln -snf "$APP_DIR" "$ACTIVE_APP_DIR"
ln -snf "$VENV_DIR" "$ACTIVE_VENV_DIR"

cp -f "`pwd`/jenkins/nginx.conf" "/etc/nginx/site-enabled/$PROJECT_NAME.conf"
cp -f "`pwd`/jenkins/wsgi.conf" "/usr/local/uwsgi/confs/$PROJECT_NAME.conf"
