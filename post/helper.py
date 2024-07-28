from django.core.mail import send_mail
from django.core.paginator import Paginator
from .models import Post
import random

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

def ran_post(num_post, type, post_id=None):
    total_posts = Post.objects.count()
    num_posts = min(num_post, total_posts)
    ran_ind = random.sample(range(1, total_posts + 1), num_posts)
    ran_posts = Post.objects.filter(pk__in=ran_ind)
    if type == 'index':
        return ran_posts

    elif type == 'post':
        current_post = Post.objects.get(pk=post_id)
        current_tags = current_post.tags.split(",") if current_post.tags else []
        related_posts = Post.objects.filter(tags__icontains=current_tags).exclude(pk=post_id)[:6]
        if len(related_posts) <6:
            ran_posts = ran_posts.exclude(pk=post_id)
            return ran_posts
        else:
            return related_posts
    else:
        return None