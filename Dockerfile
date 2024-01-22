# Base image: python:3.11.7-slim-bookworm
FROM python:3.11.7-slim-bookworm

# Copy requirements.txt to the image
COPY ./requirements.txt /app

# Install libgl1-mesa-glx for opencv
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install -r /app/requirements.txt

# Setup new user named user with UID 1000
RUN useradd -m -u 1000 user

# Set environment variables
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Define working directory
WORKDIR $HOME/app

# Switch to user
USER user

# Copy the rest of the code to the image
COPY --chown=user . $HOME/app

# Expose port 80
EXPOSE 80

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]