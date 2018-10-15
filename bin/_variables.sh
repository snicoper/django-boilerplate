#!/bin/bash

# Variables para usar en el resto de archivos ./bin.
# Requiere postactivate y postdeactivate (que .bin este en el PATH)

# PROJECT_ROOT la obtiene de bin/postactivate.sh.
# Por lo que si no existe, no esta en el entorno virtual.
if [ ! $PROJECT_ROOT ]
then
    echo "Es necesario estar un entorno virtual"
    exit
fi

###########################################################
# branch en producción

BRANCH_PROD='prod'

# npm o yarn para nodejs
PKGM_NODEJS="yarn"

###########################################################
# Entornos virtuales

# Producción
VIRTUAL_ENV_PROD="myenvprod"

# Desarrollo
VIRTUAL_ENV_DEV="django-boilerplate"

# Obtener el nombre del entorno virtual.
VIRTUALENV=$(basename "$VIRTUAL_ENV")

###########################################################
# PATHS

BACKUPS_DIR="$HOME/backups/SITENAME.COM"

# Ruta absoluta al directorio src.
SRC_ROOT="$PROJECT_ROOT/src"

# Ruta absoluta al directorio documentos.
DOCS_ROOT="$PROJECT_ROOT/docs"

# Ruta absoluta al directorio apps.
APPS_ROOT="$SRC_ROOT/apps"

# Ruta absoluta a directorio cron.
CRON_ROOT="$PROJECT_ROOT/cron"

# Ruta absoluta al directorio bin.
BIN_ROOT="$PROJECT_ROOT/bin"

# Ruta absoluta al ejecutable de python.
PYTHON_EXEC="$VIRTUAL_ENV/bin/python"

###########################################################
# Database desarrollo "PostgreSQL".
# El usuario ha de estar creado en postgresql.
# La contraseña ha de estar en ~/.pgpass.
# Editar "./src/config/settings/local.py"

# Nombre db desarrollo
DATABASE_NAME="namedbdev"

# Usuario db
DATABASE_USER="userdbdev"

###########################################################
# Database producción "PostgreSQL" para backups.
# El usuario ha de estar creado en postgresql.
# La contraseña ha de estar en ~/.pgpass.
# Editar "./src/config/settings/prod.py"

# Nombre db producción
PROD_DATABASE_NAME="namedbprod"

# Usuario db
PROD_DATABASE_USER="userdbprod"

# Numero de días que conservara los backups
PROD_DATABASE_NUMBER_OF_DAYS=7

# Location to place backups.
PROD_BACKUP_DIR="$HOME/backups/db/$PROD_DATABASE_NAME/"

# String to append to the name of the backup files.
PROD_DATABASE_BACKUP_DATE=`date +%Y-%m-%d_%H-%M`

###########################################################
# Fixtures DIR, directorio donde creara los fixtures.

FIXTURESDIR=~/Downloads/fixtures

###########################################################
# Añadir las apps que requieren load fixtures. (El orden importa).

APPS=(
  accounts
  authentication
  contact
)
