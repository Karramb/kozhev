Сайт для знакомого кожевника, в стадии разработки

Настройки nginx для сервера sudo nano /etc/nginx/sites-enabled/default
server {

    listen 80;
    allow 158.160.145.122;
    client_max_body_size 20M;

    location / {
        proxy_set_header Host $http_host;
        proxy_pass http://127.0.0.1:8000;
    }
}

При установке celery + rabbitmq на win10 запускать workera celery командой celery -A kozhev worker -l info --pool=solo