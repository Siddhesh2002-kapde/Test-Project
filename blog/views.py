from django.shortcuts import render,get_object_or_404
from blog.models import *
# Create your views here.

def home(request):
    queryset = Blog.objects.all()

    context = {
        'queryset':queryset
    }
    return render(request, 'home.html',context)



def category(request):
    queryset = Blog.objects.all()
    category = Category.objects.all()


    context = {
        'queryset':queryset,
        'category':category
    }
    return render(request, 'category.html',context)



def blogs(request,id):
    category = get_object_or_404(Category, id = id)
    queryset = Blog.objects.filter(category = category)


    context = {
        'category':category,
        'queryset': queryset
    }
    return render(request, 'blogs.html',context)


def Each_blog(request, id):
    queryset = Blog.objects.filter(id = id)
    context = {
        'queryset':queryset
    }
    return render(request, 'Each_blog.html',context)

