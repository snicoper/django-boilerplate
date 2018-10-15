#!/bin/bash

# Elimina una instalación y la reinstala en un entorno de desarrollo.
# Elimina la base de datos y la restaura.

source _variables.sh

# Probar que se esta en el entorno de desarrollo.
if [ $VIRTUALENV != $VIRTUAL_ENV_DEV ]
then
  echo "reinstall_dev.sh es solo para el entorno virtual '$VIRTUAL_ENV_DEV'"
  exit
fi

cd $PROJECT_ROOT

# Restaurar permisos de directorios y archivos.
read -p "¿Restaurar permisos? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $BIN_ROOT/permissions.sh
fi

# Reinstalar node_modules.
read -p "¿Reinstalar Node? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  if [ -d $PROJECT_ROOT/node_modules ]
  then
    rm -rf $PROJECT_ROOT/node_modules
  fi

  # Si yarn esta instalado, ejecutarlo, de lo contrario usar npm.
  if [ $PKGM_NODEJS == "yarn" ]
  then
    yarn install
  elif [ $PKGM_NODEJS == "npm" ]
  then
    npm install
  fi
fi

# Ejecutar Gulp?
read -p "¿Ejecutar Gulp? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  gulp
fi

# Reinstalar la base de datos, requiere ~/.pgpass
read -p "¿Restaurar la base de datos? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  psql -U postgres -c "DROP DATABASE IF EXISTS $DATABASE_NAME"
  echo "Eliminada base de datos $DATABASE_NAME"
  psql -U postgres -c "CREATE DATABASE $DATABASE_NAME WITH OWNER $DATABASE_USER"
  echo "Creada base de datos $DATABASE_NAME WITH OWNER $DATABASE_USER"

  # Eliminar directorios migrations, quitar cuando se pasa a prod.
  read -p "¿Eliminar directorios migrations? (y/[N]) " yn
  if [ "$yn" == "y" -o "$yn" == "Y" ]
  then
    source $BIN_ROOT/delete_migrations.sh
  fi

  $PROJECT_ROOT/manage.py makemigrations
  $PROJECT_ROOT/manage.py migrate
fi

# Restore Media?
read -p "¿Restaurar Media local? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  rm -rf $SRC_ROOT/media
  cp -r $PROJECT_ROOT/compose/media $SRC_ROOT/media
fi

# Load fixtures
read -p "¿Load Fixtures? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  source django_loaddata.sh
fi

# Eliminar logs
read -p "¿Eliminar logs? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  count_logs=$(find $PROJECT_ROOT/logs/ ! -name '.*' -type f | wc -l)
  if [ "$count_logs" -gt "0" ]
  then
    find $PROJECT_ROOT/logs/* ! -name ".keep" -exec rm -r {} \;
    echo "Eliminado archivos en $PROJECT_ROOT/logs/"
  else
    echo "No hay logs para eliminar en $PROJECT_ROOT/logs/"
  fi

fi

# Comprueba si hay algún print() en el código python.
grep --exclude=*.pyc -rnw $PROJECT_ROOT/src/apps $PROJECT_ROOT/tests -e 'print'

# Comprueba si hay algún console.log() en el código javascript.
grep -rnw $PROJECT_ROOT/src/static/src/js -e 'console.log'

# Iniciar el servidor
read -p "¿Iniciar el servidor? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PROJECT_ROOT/manage.py runserver $SITE_DOMAIN
fi
