# Base image
FROM python:3.12-slim


ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1


WORKDIR /app


RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    nodejs \
    npm \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt .
RUN pip install --upgrade pip && pip install -r requirements.txt


COPY . .

RUN npm install
RUN npm run build


CMD ["sh", "-c", "\
  python manage.py collectstatic --noinput && \
  python manage.py migrate && \
  python manage.py createsuperuser --noinput || true && \
  gunicorn Appointpro.wsgi:application --bind 0.0.0.0:8000 \
"]

EXPOSE 8000