#!/bin/bash

# Curiosidad para contar lineas
# Requiere de cloc dnf install cloc

source _variables.sh

cloc $PROJECT_ROOT \
--exclude-dir=\
__pycache__,\
.git,\
.idea,\
.tox,\
.vscode,\
compose,\
dist,\
docs,\
fixtures,\
font-awesome,\
htmlcov,\
locale,\
logs,\
media,\
migrations,\
node_modules,\
requirements,\
 \
--exclude-ext=json,coverage
