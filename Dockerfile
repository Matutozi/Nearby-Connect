# Use the official Python image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port that your app will run on
EXPOSE 6379

# Command to run your app
CMD ["python3", "redis_test.py"]
