#!/usr/bin/env bash

# Assuming that the shell has access to the Python virtualenv and that `python manage.py migrate` has been already executed

# Setup a few environment variables required by createsuperuser
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_EMAIL="admin@admin.it"
export DJANGO_SUPERUSER_PASSWORD="supersecretpwd"

# Create a Django superuser with the values of the environment variables just defined
python manage.py createsuperuser --no-input

# Create the other users
python manage.py shell < setup-users-dev.py

# Dump all the users as fixtures just in case we need to manually load them in the future
python manage.py dumpdata core.CustomUser --indent 4 > ./core/fixtures/users.json

# Populate the database with all the remaining fixtures' data 
find ./core/fixtures/ \
    -maxdepth 1 \
    -type f \
    -name "*.json" ! -name "users.json" \
    -exec python manage.py loaddata '{}' +
