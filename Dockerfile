FROM python:3.8.0rc1-buster

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV MODE prod

CMD ["python", "app.py"]
