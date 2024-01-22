# Base image: python:3.11.7-slim-bookworm
FROM python:3.11.7-slim-bookworm

# Set environment variables
ENV HOME=/home/user \
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
WORKDIR $HOME/app

# Switch to user
USER user

# Copy requirements.txt to the image
COPY --chown=user:user ./requirements.txt /app/requirements.txt

# Install python dependencies
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --user -r /app/requirements.txt

# Copy the rest of the code to the image
COPY --chown=user:user . $HOME/app

# Expose port 8000
EXPOSE 8000/tcp
EXPOSE 8000/udp

# Run the application
CMD ["uvicorn", "main:app", "--port", "8000"]