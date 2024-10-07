from django.urls import path
from blog.views import *
urlpatterns = [
    path('', home, name= 'home'),
    path('category', category,name = 'categroy'),
    path('blogs/<id>',blogs, name= 'blogs'),
    path('Each_blog/<id>',Each_blog, name = 'Each_blog')
]

