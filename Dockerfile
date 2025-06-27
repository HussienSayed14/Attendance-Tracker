# Use slim Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app


# add system libs
RUN apt-get update && apt-get install -y gcc libpq-dev build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy project files
COPY ./app ./app
COPY ./alembic.ini .
COPY ./alembic ./alembic

# Expose the port
EXPOSE 8000

# Run FastAPI app (remove --reload in production)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]