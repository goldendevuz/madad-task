#!/bin/bash

# Apply database migrations
make mig
# Collect static files
make collect

# Create a superuser (optional; consider using fixtures for production)
# echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell

# Authenticate with jprq and expose port 8000 using the environment variable
jprq auth $JPRQ_AUTH_KEY
jprq http 8000 -s local &

# Set the webhook
python3 manage.py setwebhook # not make webhook

# Start the Uvicorn ASGI server
make run
