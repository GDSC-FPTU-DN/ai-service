FROM python:3.11.7-slim-bookworm

COPY ./requirements.txt /app/requirements.txt

RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y

RUN pip install -r /app/requirements.txt

RUN useradd -m -u 1000 user
USER user
ENV HOME=/home/user \
    PATH=/home/user/.local/bin:$PATH

WORKDIR $HOME/app

COPY --chown=user . $HOME/app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]