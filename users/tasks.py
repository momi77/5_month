from celery import shared_task
from django.core.mail import send_mail
from datetime import datetime

@shared_task
def add(x, y):
    print(f"args: {x}, {y}")
    return x + y


@shared_task
def daily_report():
    now = datetime.now()
    print(f"Daily report generated at {now}")
    return f"Report at {now}"


@shared_task
def send_welcome_email(to_email):
    subject = "Welcome to Show API"
    message = "Thank you for registering. We're glad to have you on board!"
    from_email = "momi@gmail.com"  
    send_mail(subject, message, from_email, [to_email])
    print(f"Email sent to {to_email}")
    return f"Email sent to {to_email}"
