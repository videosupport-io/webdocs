FROM python:3.8

EXPOSE 8080

WORKDIR /app

COPY src .
COPY main.py .

RUN pip install -r requirements.txt

CMD ["python", "main.py"]