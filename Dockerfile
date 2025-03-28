# Use the official Python base image
FROM python:3.9-slim

# Install required packages using pip
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set working directory to /app
WORKDIR /app

# Copy source code into container
COPY . .

# Run application
CMD ["python", "app.py"]