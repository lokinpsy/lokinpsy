from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your models here.

#Post Model
class Post(models.Model):
    title = models.CharField(max_length=250 ,null=False)
    Categories = [
        ('Social Psychology', 'Social Psychology'),
        ('Psychopathology', 'Psychopathology'),
        ('General Psychology', 'General Psychology'),
        ('Authors', 'Authors'),
        ('Statistics','Statistics'),
        ('Research', 'Research'),
    ]
    tags = models.TextField(null=True)
    category = models.CharField(max_length=100,choices=Categories)
    intro = models.CharField(max_length=250)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pub_date = models.DateTimeField(timezone.now)
    images= models.ImageField(upload_to='static')
    likes = models.ManyToManyField(User, related_name='like_posts', blank=True)
    saves = models.ManyToManyField(User, related_name='save_posts', blank=True)

    def __str__(self):
        return self.title
    
    def total_likes(self):
        return self.likes.all().count()
    
    def total_saves(self):
        return self.saves.all().count()

    def get_absolute_url(self):
        return reverse('post.views.index', args=[self.slug])
    
    class Meta:
        ordering = ["-pub_date"]
    
class Ccustomer(models.Model):
    name = models.CharField(max_length= 200, null=False)
    email = models.EmailField(null=False, max_length=254)
    subject = models.CharField(max_length=200, null=False)
    content = models.TextField()
    c_date = models.DateTimeField(default=timezone.now)
    is_connect = models.BooleanField(default=False)

    def __str__(self):
        if self.is_connect:
            self.name = str(self.name+' connected')
        
        return self.name

    class Meta:
        ordering = ["-c_date"]
    

class CorUser(models.Model):
    name = models.CharField(max_length= 200, null=False)
    email = models.EmailField(null=False, max_length=254)
    post_no_or_title = models.CharField(max_length=200, null=False)
    message = models.TextField()
    cor_date = models.DateTimeField(default=timezone.now)
    is_connect = models.BooleanField(default=False)

    def __str__(self):
        if self.is_connect:
            self.name = str(self.name+' connected')
        
        return self.name

    class Meta:
        ordering = ["-cor_date"]

@receiver(post_save, sender=Post)
def send_email_to_subscribers(sender, instance, created, **kwargs):
    if created:
        subscribers = User.objects.all()

        subject = f'New Post Added'
        message = f'Title: {instance.title}'

        # Send the email to each subscriber
        for subscriber in subscribers:
            send_mail(subject, message, 'lokinpsy@gmail.com', [subscriber.email])

class DelUser(models.Model):
    email = models.EmailField(null=False)
    reason = models.CharField(null=False, max_length=250)
    message = models.TextField(default='not provided')
    del_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email
    
    class Meta:
        ordering = ['-del_date']