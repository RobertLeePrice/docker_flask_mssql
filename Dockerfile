FROM python:3.8.5

COPY ./src /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "/app/main.py"]