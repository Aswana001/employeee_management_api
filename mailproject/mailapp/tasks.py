from celery import shared_task

from django.conf import settings

from django.core.mail import EmailMessage


@shared_task
def send_email_task(
    subject,
    message,
    from_email,
    to_email
):

    email = EmailMessage(

        subject,

        message,

        settings.EMAIL_HOST_USER,

        [to_email],

        reply_to=[from_email]
    )

    email.send()

    print("EMAIL SENT SUCCESSFULLY")

    return "Email Sent"
