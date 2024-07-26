from django.urls import path
from post import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about',views.about, name='about'),
    path('contact',views.contact, name='contact'),
    path('post/<int:id>/',views.post,name='post'),
    path('post/like',views.like,name='post_like'),
    path('post/save',views.save,name='post_save'),
    path('correq',views.correq,name='correq'),
    path('search/', views.search, name='search'),
    path('privacy_policy', views.pp, name='pp'),
    path('disclaimer', views.disclaimer, name='disclaimer'),
    path('tnc', views.tnc, name='tnc'),
    path('sotp', views.sotp, name='sotp'),
    path('signup',views.signup, name='signup'),
    path('signin',views.signin, name='signin'),
    path('signout',views.signout, name='signout'),
    path('fp',views.fp, name='fp'),
    path('me',views.me, name='me'),
    path('me/chu',views.chu, name='chu'),
    path('me/likedpost',views.likedpost, name='lpost'),
    path('me/savedpost',views.savedpost, name='spost'),
    path('me/delete_account',views.del_acc, name='del_acc'),
]