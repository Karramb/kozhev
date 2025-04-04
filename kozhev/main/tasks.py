from __future__ import absolute_import, unicode_literals
from celery import shared_task
from django.core.mail import send_mail


@shared_task
def send_application_email(email, message, subject, from_email, recipient_list):
    """
    Отправляем письмо с заявкой асинхронно.
    """
    body = f"{message}\n\nОт: {email}"
    send_mail(
        subject=subject,
        message=body,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False
    )
