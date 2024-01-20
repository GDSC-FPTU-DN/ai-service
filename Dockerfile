FROM python:3.11.7-slim-bookworm

WORKDIR /app

COPY ./requirements.txt /app

RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]