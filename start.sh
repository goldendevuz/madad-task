#!/bin/bash

set -e  # Exit on any error

# Apply database migrations
make mig

# Collect static files
make collect

echo ""
echo "========== Starting Tunnels =========="

if [ "$ENV" = "production" ]; then
  # Start jprq tunnel
  if [ -n "$JPRQ_AUTH_KEY" ]; then
    echo "Authenticating jprq..."
    jprq auth "$JPRQ_AUTH_KEY"
    echo "Starting jprq tunnel on port 1025..."

    PIPE=$(mktemp -u)
    mkfifo "$PIPE"
    jprq http 1025 -s "$JPRQ_URL" > "$PIPE" 2>&1 &
    read -r LINE < "$PIPE"
    JPRQ_URL=$(echo "$LINE" | grep -o 'https://[a-zA-Z0-9.-]*\.jprq\.site')
    rm "$PIPE"
  fi

  # Start ngrok tunnel
  NGROK_URL=""
  if [ -n "$NGROK_AUTH_TOKEN" ]; then
    echo "Authenticating ngrok..."
    ngrok config add-authtoken "$NGROK_AUTH_TOKEN"
    echo "Starting ngrok tunnel on port 1025..."
    ngrok http --url=positively-big-kingfish.ngrok-free.app 1025 > /dev/null &
    sleep 2
    NGROK_URL=$(curl --silent http://localhost:1026/api/tunnels \
      | grep -o 'https://[a-zA-Z0-9.-]*\.ngrok-free\.app' | head -n1)
  fi

  # Show tunnel URLs
  echo ""
  echo "========== Public URLs =========="
  [ -n "$JPRQ_URL" ] && echo "🌀 jprq  → $JPRQ_URL"
  [ -n "$NGROK_URL" ] && echo "🚀 ngrok → $NGROK_URL"
  echo "================================="
else
  echo "ENV != production; skipping tunnels."
fi

# Start the Uvicorn ASGI server
echo "Starting Uvicorn ASGI server..."
make run-asgi
