#!/bin/bash
# This hook is sourced after this virtualenv is deactivated.

unalias cd_project
unalias cd_apps

export PATH=$OLD_PATH
unset OLD_PATH
unset PROJECT_ROOT
