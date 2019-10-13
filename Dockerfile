FROM python:3.8.0rc1-buster

COPY . .

RUN pip install -r requirements.txt

CMD ["python", "app.py"]
