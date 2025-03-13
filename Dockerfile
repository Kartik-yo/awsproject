# Stage 1: Build Dependencies
FROM python:3.9 AS builder

WORKDIR /app

# Copy the dependencies file
COPY requirements.txt .

# Install dependencies in a virtual environment
RUN python -m venv venv && \
    . venv/bin/activate && \
    pip install --no-cache-dir -r requirements.txt

# Stage 2: Production Image
FROM python:3.9-slim

WORKDIR /app

# Copy only necessary files from builder stage
COPY --from=builder /app/venv /app/venv
COPY . .

# Set environment variable for virtual environment
ENV PATH="/app/venv/bin:$PATH"

# Expose port (Dynamic)
ARG SERVICE_PORT=5000
EXPOSE ${SERVICE_PORT}

# Set default service (User Service)
ARG SERVICE_NAME=user

CMD ["python", "user_service.py"]  # Default to user service

