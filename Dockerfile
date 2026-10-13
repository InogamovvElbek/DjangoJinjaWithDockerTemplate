FROM python:3.14-alpine

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

CMD python manage.py migrate && python manage.py runserver 0.0.0.0:8003
