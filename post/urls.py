from django.urls import path
from post import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('subscribe',views.subscribe, name='subscribe'),
    path('post/<int:id>/',views.post,name='post'),
    path('correq',views.correq,name='correq'),
    path('search/', views.search, name='search'),
    path('privacy_policy', views.pp, name='pp'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('tnc', views.tnc, name='tnc'),
    path('sotp', views.sotp, name='sotp'),
]