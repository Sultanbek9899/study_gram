set -e

# Apply database migrations
echo "Applying database migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Django development server
echo "Starting development server..."
exec gunicorn -w 4 --bind 0.0.0.0:8000 config.wsgi --reload
