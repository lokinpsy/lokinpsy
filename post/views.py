from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from . import models
from . import helper
from django.contrib import messages
from django.db.models import Q
import random

# 1. Index page / Home page
def index(request):
    posts = models.Post.objects.all()
    page = helper.cus_paginator(request,posts,10)
    context = {'posts':page}
    return render(request, 'index.html', context)

def search(request):
    if request.method == "GET":
        query = request.GET.get('searchquery')
        if query is not None:
            lookups = Q(tags__icontains = query)| Q(category__icontains=query)| Q(title__icontains = query)
            results = models.Post.objects.filter(lookups).distinct()
            page = helper.cus_paginator(request,results,10)
            data = {
                'results': page,
                'query': query
            }
            return render(request, 'results.html', data)
        return redirect('home')
    return redirect('home')

# 2. About page
def about(request):
    return render(request,'about.html')

# 3. Contact page
def contact(request):
    if request.method == 'POST':
        cname = request.POST.get('cname')
        csubject = request.POST.get('csubject')
        cemail = request.POST.get('cemail')
        cmessage = request.POST.get('cmessage')
        ccustomer = models.Ccustomer()
        ccustomer.name = cname
        ccustomer.email = cemail
        ccustomer.subject = csubject
        ccustomer.content = cmessage
        ccustomer.save()
        messages.success(request, "Message recieved successfully. We'll contact soon ")
        return redirect('contact')
    return render(request, 'contact.html')

# 4. Subscribe
        
def sotp(request):
    if request.method == "POST":
        global otp, gsemail
        otp = random.randint(100000,999999)
        gsemail = request.POST.get('semail')
        if models.Subscriber.objects.filter(email = gsemail).exists():
            return JsonResponse({'message':'Email already used'})
        else:
            emsg = f'Hey there\nYour OTP for email verification is {otp}\nEnter OTP in the correct input box and subscribe.\n\nTeam Lokin Psy'
            helper.sub_mail('Email Verification', emsg,gsemail)
            return JsonResponse({'message':'OTP sent successfully'})
    else:
        return redirect('home')

def subscribe(request):
    if request.method == "POST":
        sotp = request.POST.get('sotp')
        if int(sotp) == int(otp):
            subscriber = models.Subscriber()
            subscriber.email = gsemail
            subscriber.save()
            messages.success(request, "Subscription added successfully.")
            emsg = f'Hurray,\nYour subscription has been added\nGet email notification for every post added and stay learning.\n\nTeam Lokin Psy'
            helper.sub_mail('Subscription Added', emsg,gsemail)
            return redirect('home')
        else:
            return JsonResponse({'message':'Incorrect OTP entered'})
    else:
        return redirect('home')
        
# 5 Post view
def post(request, id):
    post = get_object_or_404(models.Post, pk=id)
    data = {"post": post}
    return render(request, 'post.html', data)

# 6. Correction Form 

def correq(request):
    if request.method == "POST":
        corname = request.POST.get('corname')
        coremail = request.POST.get('coremail')
        corpost = request.POST.get('corpost')
        cormessage = request.POST.get('cormessage')
        coruser = models.CorUser()
        coruser.name = corname
        coruser.email = coremail
        coruser.post_no_or_title = corpost
        coruser.message = cormessage
        coruser.save()
        messages.success(request, "Thank You for submitting correction form! Your request is in consideration, you'll recieve an email on regarding action")
        return redirect('correq')
    return render(request, 'correq.html')

def pp(request):
    return render(request, 'pp.html')

def disclaimer(request):
    return render(request, 'disc.html')

def tnc(request):
    return render(request, 'tnc.html')
        