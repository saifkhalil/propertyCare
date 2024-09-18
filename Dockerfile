# Use Python 3.10-slim as the base image
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory
WORKDIR /app

# Copy the requirements file
COPY ./requirements.txt /app/requirements.txt

# Install the dependencies
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy the project
COPY . /app/

# Run UVicorn
CMD ["uvicorn", "django_project.asgi:application", "--host", "0.0.0.0", "--port", "8000", "--reload"]
