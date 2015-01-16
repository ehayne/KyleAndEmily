echo $WORKSPACE
export PROJECT_NAME=kyleandemily
export ROOT="/usr/local/$PROJECT_NAME"
export DB_DIR="$ROOT/db_$APP_ENV"
export DB_BACKUP_DIR="$ROOT/db_backup/"

mkdir -p "$DB_BACKUP_DIR"

cp -r $DB_DIR $DB_BACKUP_DIR$BUILD_ID
