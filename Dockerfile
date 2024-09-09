# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /code

# Copy the requirements file into the container
COPY requirements.txt /code/

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install wkhtmltopdf for generating PDFs/Images
RUN apt-get update && apt-get install -y wkhtmltopdf

# Copy the current directory contents into the container at /code
COPY . /code/

# Command to run on container start
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
