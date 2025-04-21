#!/bin/bash

# Apply database migrations
python manage.py migrate

# Collect static files
python manage.py collectstatic --noinput

# Create a superuser (optional; consider using fixtures for production)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

# Authenticate with jprq and expose port 8000 using the environment variable
jprq auth $JPRQ_AUTH_KEY
jprq http 8000 &

# Set the webhook
python manage.py setwebhook

# Start the Uvicorn ASGI server
uvicorn core.asgi:application --host 0.0.0.0 --port 8000 --reload
