# Base image: python:3.11.7-slim-bookworm
FROM python:3.11.7-slim-bookworm

# Set environment variables
ENV CLOUD_HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

# Install libgl1-mesa-glx for opencv
RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y
RUN apt-get install 'ffmpeg'\
    'libsm6'\
    'libxext6'  -y

# Setup new user named user with UID 1000
RUN useradd -m -u 1000 user

# Define working directory
WORKDIR $CLOUD_HOME/app

# Switch to user
USER user

# Copy requirements.txt to the image
COPY --chown=user:user ./requirements.txt /app/requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --user -r /app/requirements.txt

# Copy the rest of the code to the image
COPY --chown=user:user . $CLOUD_HOME/app

# Expose port 7860
EXPOSE 7860/tcp
EXPOSE 7860/udp

# Run the application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "7860"]