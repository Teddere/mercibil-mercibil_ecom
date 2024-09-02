import logging
from django.conf import settings
from concurrent.futures import ThreadPoolExecutor
from django.template.loader import render_to_string
from django.core.mail import send_mail

logger = logging.getLogger(__name__)

def send_email(subject:str,receivers:list,template:str,context:dict):
    "This function help to send a customized mail template"
    try:
        message = render_to_string(template, context)
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            receivers,
            fail_silently=False
        )
        with ThreadPoolExecutor() as executor:
            future = executor.submit(send_mail)
            future.result()
        return True
    except Exception as e:
        logger.error(e)

    return False

