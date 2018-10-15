#!/bin/bash

source _variables.sh

# Probar que se esta en el entorno de producción.
if [ $VIRTUALENV != $VIRTUAL_ENV_PROD ]
then
  echo "reinstall_dev.sh es solo para el entorno virtual '$VIRTUAL_ENV_PROD'"
  exit
fi

cd $PROJECT_ROOT

# Ejecutar git pull origin prod.
read -p "git pull origin $BRANCH_PROD? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  git pull origin $BRANCH_PROD
fi

# NPM/Yarn.
read -p "Ejecutar yarn? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  # Si yarn esta instalado, ejecutarlo, de lo contrario usar npm.
  if [ $PKGM_NODEJS == "yarn" ]
  then
    yarn install
  elif [ $PKGM_NODEJS == "npm" ]
  then
    npm install
  fi
fi

# Gulp siempre lo ejecuta.
eval gulp

# Actualizar pip.
read -p "¿Actualizar pip? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  pip install -r $PROJECT_ROOT/requirements/prod.txt
fi

# Backup database
read -p "¿Backup database? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $CRON_ROOT/postgres_db_backup.sh
fi

# Ejecutar migrate.
read -p "¿Ejecutar migrate? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PROJECT_ROOT/prod_manage.py migrate
fi

# Ejecutar collectstatic.
read -p "¿Ejecutar collectstatic? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  $PYTHON_EXEC $PROJECT_ROOT/prod_manage.py collectstatic --clear --noinput
fi

# Reiniciar gunicorn.
read -p "¿Reiniciar gunicorn? (y/[N]) " yn
if [ "$yn" == "y" -o "$yn" == "Y" ]
then
  sudo systemctl restart gunicorn
fi
