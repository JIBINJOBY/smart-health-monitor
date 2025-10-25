# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy all files
COPY . /app

# Install dependencies
RUN pip install -r app/requirements.txt

# Expose port
EXPOSE 5000

# Run app
CMD ["python", "app/app.py"]
