# django-boilerplate

Estructura que utilizo para crear practicas con Django con una base ya hecha.

Django >= 2 y Python 3.6

## Instalación

Crear un entorno virtual con `virtualenvwrapper` y crear el proyecto.

Clonando el proyecto.

```bash
cd ~/projects
git clone git@github.com:snicoper/django-boilerplate.git
```

De esta manera se ha de generar [secret_key](http://www.miniwebtool.com/django-secret-key-generator/)
en los archivos `src/config/settings/(local,prod,test).py`

Usando `startproject --template=`.

```bash
django-admin.py startproject --template=https://github.com/snicoper/django-boilerplate/archive/master.zip nombre_proyecto
cd nombre_proyecto/
```

Requirements.

```bash
# requirements
pip install -r requirements/(local|prod).txt
```

Renombrar `src/apps/utils/templatetags/utils_tags.py.txt` a `src/apps/utils/templatetags/utils_tags.py`

```bash
mv src/apps/utils/templatetags/utils_tags.py.txt src/apps/utils/templatetags/utils_tags.py
```

Al usar `startproject`, con `utils_tags.py` siempre me da el error `django.template.exceptions.TemplateSyntaxError: Invalid filter: 'markdown'`.
No he sabido solucionarlo y renombrar a `.txt` me ha solucionado el problema.

## Añadir postactivate y postdeactivate al env (opcional)

Esto es para comodidad, para los scripts dentro del directorio `bin`

Activar el entorno virtual y editar `postactivate` y `postdeactivate`.

### postactivate

```bash
workon django-boilerplate

vim $VIRTUAL_ENV/bin/postactivate

# Añadir
source ~/projects/django-boilerplate/bin/postactivate.sh

#export NODE_ENV="production"
export NODE_ENV="development"

deactivate
workon django-boilerplate
```

### postdeactivate

```bash
vim $VIRTUAL_ENV/bin/postdeactivate

# Añadir
source ~/projects/django-boilerplate/bin/postdeactivate.sh

unset NODE_ENV
```

## Lista de archivos bin

Luego cualquier archivo en `./bin` se podrá ejecutar desde cualquier ruta.

* `cloc_project.sh`: Cuanta lineas del proyecto.
* `delete_migrations.sh`: Elimina migraciones, para primeras etapas de desarrollo.
* `delete_pycache.sh`: Eliminar directorios `__pycache__`
* `django_dumpdata.sh`: Vuelca los datos actuales en `./fixtures`, para desarrollo.
* `django_loaddata.sh`: Igual que `django_dumpdata.sh`, pero los lee, para desarrollo.
* `gunicorn_start.sh`: Para producción.
* `permissions.sh`: Establecer permisos en el proyecto.
* `postactivate.sh`: Archivo que carga cuando se entra al entorno virtual con `workon`.
* `postdeactivate.sh`: Archivo que carga cuando se sale al entorno virtual con `deactivate`.
* `reinstall_dev.sh`: Rápida re-instalación en desarrollo.
* `reload_prod.sh`: Actualizar servidor de producción con tareas comunes.
* `runserver.sh`: Alias de `python -Wd manage.py runserver $command`

Una vez entrado al entorno, se podrá hacer `cd_project` para ir al directorio raíz del
proyecto o `cd_apps` para ir al directorio raíz de las **apps**.

## Migración y súper usuario (desarrollo)

Por defecto usa **SQLite**, editar `./src/config/settings/local.py` para editar los datos de conexión.

```bash
./manage.py migrate
./manage.py createsuperuser
```

## manage_prod.py y manage_test.py

Para no tener que estar cambiando con `./manage.py command --settings=archivo.settings`, hay 3
archivos `manage`, cada uno de ellos apunta al archivo `settings` que corresponde.

* `manage.py`: Para desarrollo.
* `prod_manage.py`: Para producción.
* `test_manage.py`: Para tests.

## Node

Editar `./package.json` para los paquetes de **nodejs**

```bash
npm install
```

### gulpfile.js

* `gulp`: Unifica y minifica los archivos `.js` y `.scss` desarrollo y producción.
* `gulp watch`: Unifica, minifica y escucha archivos `.js` y `.scss` en desarrollo locales.

## Reinstalar en desarrollo

Para una re-instalación rápida en la etapa de desarrollo (**solo PostgreSQL**).

Editar `src/config/settings/local.py` la conexión a **PostgreSQL**

Editar las variables del archivo `bin/_variables.sh`.

Ejecutar `reinstall_dev.sh`.

## Reload prod

En desarrollo usar, `reload_prod.sh`
