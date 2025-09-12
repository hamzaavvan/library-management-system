# Base Image
FROM python:3.11-slim

# WORK DIR
WORKDIR /app

# Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy File
COPY . .

# Expose Port
EXPOSE 5000

# Environment Variables
ENV FLASK_APP=app.py
ENV FLASK_ENV=development

# Run
CMD [ "flask", "run", "--host=0.0.0.0", "--port=5000"  ]
