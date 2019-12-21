# -*- coding: utf-8 -*-

from django.core.mail import send_mail

from pizzapp.settings import EMAIL_HOST_USER

SUBJECT_STR = 'Yumpizza Delivery Service'
MESSAGE_STR = 'Order was placed successfully. Delivery would take {0} min.'


def send_mail_on_order(delivery_time: int, customer_email: str) -> None:
    """Sends email with order info to customer address."""
    send_mail(
        SUBJECT_STR,
        MESSAGE_STR.format(delivery_time),
        EMAIL_HOST_USER,
        [customer_email],
    )
