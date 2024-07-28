from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from . import models
from . import helper
from django.contrib import messages
from django.db.models import Q
import random
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
import json

# 1. Index page / Home page
def index(request):
    posts = models.Post.objects.all()
    page = helper.cus_paginator(request,posts,10)
    ran_post = helper.ran_post(num_post=3,type='index',post_id=0)
    context = {'posts':page,
               'ran_posts':ran_post}
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

        
def sotp(request):
    if request.method == "POST":
        global otp, gsemail
        type = request.POST.get('type')
        otp = random.randint(100000,999999)
        gsemail = request.POST.get('semail')
        if type=="signup":
            if User.objects.filter(email=gsemail).exists():
                return JsonResponse({'message':'Email already used'})
            else:
                emsg = f'Hey there\nYour OTP for email verification is {otp}\nEnter OTP in the correct input box and signup.\n\nTeam Lokin Psy'
                helper.sub_mail('Email Verification', emsg,gsemail)
                return JsonResponse({'message':'OTP sent successfully'})
        
        elif type == "fp":
            if User.objects.filter(email=gsemail).exists():
                emsg = f'Hey there\nYour OTP for email verification is {otp}\nEnter OTP in the correct input box and change password.\n\nTeam Lokin Psy'
                helper.sub_mail('Email Verification', emsg,gsemail)
                return JsonResponse({'message':'OTP sent successfully'})
            else:
                return JsonResponse({'message':'Email not registered'})
        elif type == "delacc":
            if User.objects.filter(email = gsemail).exists():
                emsg = f'Hey there\nYour OTP for email verification is {otp} for deleting your account\nEnter OTP in the correct input box and continue.\n\nTeam Lokin Psy'
                helper.sub_mail('Email Verification', emsg,gsemail)
                return JsonResponse({'message':'OTP sent successfully'})
            else:
                return JsonResponse({'message':'Email not registered'})
        else:
            return redirect('home')
    else:
        return redirect('home')
        
# 5 Post view
def post(request, id):
    post = get_object_or_404(models.Post, pk=id)
    ran_post = helper.ran_post(num_post=6,type='post',post_id=id)
    data = {"post": post,
            'ran_posts':ran_post}
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

def signup(request):
    if request.method == "POST":
        signotp = int(request.POST.get('sotp'))
        nuser = request.POST.get('username')
        nuser = nuser.lower()
        if User.objects.filter(username = nuser).exists():
            return JsonResponse({"msg":"Username already taken"})
        else:           
            if int(otp) == signotp:
                user = User()

                if models.DelUser.objects.filter(email = gsemail):
                    user.first_name = "renew_user"
                    preuser = models.DelUser.objects.get(email = gsemail)
                    preuser.delete()
                else:
                    user.first_name = "new_user"

                user.username = nuser
                user.email = gsemail
                user.password = request.POST.get('password')
                user.save()
                messages.success(request,'Singup successfully')
                login(request, user)
                return JsonResponse({"msg":"successfull"})
            else:
                return JsonResponse({"msg":"OTP is incorrect"})
    return render(request,'signup.html')


def signin(request):
    if request.method == "POST":
        password = request.POST.get('password')
        username_or_email = request.POST.get('username')

        try:
            user = User.objects.get(username=username_or_email)
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username_or_email)
            except User.DoesNotExist:
                messages.info(request, 'User does not exist')
                return render(request, 'login.html')

        if user.password == password:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Password is incorrect')
            return render(request, 'login.html')

    return render(request, 'login.html')


def fp(request):
    if request.method == "POST":
        sotp = int(request.POST.get('sotp'))
        if int(otp) == sotp:
            user = User.objects.get(email= gsemail)
            user.password = request.POST.get('npass')
            user.save()
            messages.info(request,'Password changes successfully')
            login(request,user)
            return JsonResponse({"msg":"successfull"})
        else:
            return JsonResponse({"msg":"OTP is incorrect"})
        
    return render(request, 'fp.html')

def signout(request):
    logout(request)
    messages.success(request,'Signout successfully')
    return redirect('home')


def me(request):
    data = request.user
    if data.is_authenticated: 
        like_post = models.Post.objects.filter(likes = data)               
        save_post = models.Post.objects.filter(saves = data)               
        user = {"data":data}
        return render(request, 'me.html', user)
    else:
        return redirect('signin')

def chu(request):
    if request.method == "POST":
        nusername = request.POST.get('nusername')
        user = request.user
        if nusername != user.username:
            if User.objects.filter(username=nusername).exists():
                return JsonResponse({"msg":"Username already taken"})
            else:
                user.username = nusername
                user.save()
                messages.success(request,"username changed successfully")
                return JsonResponse({"msg":"success"})
        return JsonResponse({"msg":"success"})


def like(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        post_id = int(data.get('post_id'))
        post = get_object_or_404(models.Post, id=post_id)
        user = request.user
        if user.is_authenticated:
            if user in post.likes.all():
                post.likes.remove(user)
                liked = False
            else:
                post.likes.add(user)
                liked = True
            return JsonResponse({'liked': liked, 'likes_count': post.likes.count()})
        else:
            return JsonResponse({'error':True, 'likes_count': post.likes.count()})

def save(request):
    if request.method == "POST":
        data = json.loads(request.body.decode('utf-8'))
        post_id = int(data.get('post_id'))
        post = get_object_or_404(models.Post, id=post_id)
        user = request.user
        if user.is_authenticated:
            if user in post.saves.all():
                post.saves.remove(user)
                saved = False
            else:
                post.saves.add(user)
                saved = True
            return JsonResponse({'saved': saved})
        else:
            return JsonResponse({'error':True})
        
def likedpost(request):
    user = request.user
    if user.is_authenticated:
        posts = models.Post.objects.filter(likes = user)
        page = helper.cus_paginator(request,posts,10)
        context = {'posts':page}
        return render(request, 'likepost.html', context)
    return redirect('signin')

def savedpost(request):
    user = request.user
    if user.is_authenticated:
        posts = models.Post.objects.filter(saves = user)
        page = helper.cus_paginator(request,posts,10)
        context = {'posts':page}
        return render(request, 'savedpost.html', context)
    return redirect('signin')

def del_acc(request):
    if request.method == "POST":
        unsubotp = int(request.POST.get('sotp'))
        password = request.POST.get('password')
        if unsubotp == int(otp):
            if User.objects.get(email = gsemail).password == password:
                unsubrsn = request.POST.get('sersn')
                unsubmsg = request.POST.get('sersnmsg')
                unsubscriber = models.DelUser()
                unsubscriber.email = gsemail
                unsubscriber.reason = unsubrsn
                unsubscriber.message = unsubmsg
                user = models.User.objects.get(email = gsemail)
                user.delete()
                unsubscriber.save()
                messages.success(request, "Account Deleted")
                emsg = f"Hey,\nYour account has been deleted.\nYou won't receive new updates, news and posts.\n\nTeam Lokin Psy"
                helper.sub_mail('Account Deleted', emsg, gsemail)
                return JsonResponse({'message':'success'})
            else:
                return JsonResponse({'message':'Incorrect Password'})
        else:
            return JsonResponse({'message':'Incorrect OTP entered'})
    if request.user.is_authenticated:
        return render(request,'delacc.html')
    else:
        return redirect('signin')