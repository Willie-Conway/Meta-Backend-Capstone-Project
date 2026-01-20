# Use slim Python image
FROM python:3.10-slim

# Environment settings
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# System dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY Pipfile Pipfile.lock ./
RUN pip install pipenv && pipenv install --system --deploy

# Copy project files
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput

# Start server
CMD ["gunicorn", "littlelemon.wsgi:application", "--bind", "0.0.0.0:8000"]
