# Stage 1: Build dependencies
FROM python:3.11-slim AS builder
WORKDIR /app

RUN pip install --no-cache-dir --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir fastapi uvicorn sqlalchemy "psycopg[binary]"

# Stage 2: Learn production image
# Copy application source code
COPY . /app

EXPOSE 8080

# Run uvicorn via python module to ensure it's always in the path
CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]