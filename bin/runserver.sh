#!/usr/bin/env bash

# Para ejecutar el servidor en desarrollo.
# Los argumentos serán pasados después de ./manage.py runserver *args

source _variables.sh

$PYTHON_EXEC -Wd $PROJECT_ROOT/manage.py runserver $*
