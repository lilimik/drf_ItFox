FROM python:3.9
ENV PYTHONUNBUFFERED 1
ENV SECRET_KEY=test
ENV DEBUG=True


WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py migrate && ["gunicorn", "--bind", ":8000", "--workers", "3", "mysite.wsgi:application"]