#!/bin/sh

# Collect all admin files
python3 manage.py collectstatic --no-input


python3 manage.py migrate authentication
# Apply database migrations
echo "Applying database migrations"
python3 manage.py migrate 



# Create a SuperUser
python3 manage.py initadmin

# Start server
echo "Starting server"
gunicorn core.wsgi -w 2 -b :8000 --reload