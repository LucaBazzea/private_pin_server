# Use the official Alpine Python image
FROM python:3.12-alpine

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the container
COPY requirements.txt .

# Install the dependencies
RUN apk add --no-cache build-base \
    && pip install --no-cache-dir -r requirements.txt \
    && apk del build-base

# Copy the rest of the application code to the container
COPY . .

# Set the environment variables from the .env file
COPY .env /app/.env

# Make the .env file readable
RUN chmod +r /app/.env

# Expose the port that Django will run on
EXPOSE 8000

# Run the Django development server when the container starts
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
