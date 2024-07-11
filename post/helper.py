from django.core.mail import send_mail
from django.core.paginator import Paginator
from . import models

# 1. Subscription mail

def sub_mail(subject,message,semail):
    subject = subject
    message = message
    from_email = "lokinpsy@gmail.com"
    recipient_list = [semail]

    # Send the email
    send_mail(subject, message, from_email, recipient_list)

def cus_paginator(request, model, no_of_post):
    paginator = Paginator(model, no_of_post)
    page_number = request.GET.get('page')
    page = paginator.get_page(page_number)
    return page

