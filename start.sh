#!/bin/bash

# Get port from environment variable or use default
PORT=${PORT:-8000}

# Start gunicorn with the specified port
exec gunicorn \
    --bind "0.0.0.0:${PORT}" \
    --workers 2 \
    --timeout 120 \
    --access-logfile - \
    --error-logfile - \
    api:app


