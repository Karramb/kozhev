FROM python:3.9

WORKDIR /app

COPY kozhev/requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "kozhev", "worker", "--loglevel=info", "--pool=solo"]

# Убедитесь, что your_app - это имя вашего Python модуля с Celery приложением