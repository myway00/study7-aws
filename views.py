from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from django.utils import timezone
# Create your views here.
def detail(request, id):
    Blog=get_object_or_404(blog, pk=id) 
    return render(request, 'detail.html', {'blog':Blog})

def home(request):
    blogs=blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def new(request):
    return render(request, 'new.html')

def create(request): #new.html에서 오는 정보를 받아줘야 함
    new_blog=blog()
    new_blog.title=request.POST['title']
    new_blog.writer=request.POST['writer']
    new_blog.body=request.POST['body']
    new_blog.pub_date=timezone.now()
    new_blog.save()
    return redirect('detail', new_blog.id)

def edit(request, id):
    edit_blog=blog.objects.get(id=id)
    return render(request, 'edit.html',{'blog': edit_blog})

def update(request, id):
    update_blog=blog.objects.get(id=id)
    update_blog.title=request.POST['title']
    update_blog.writer=request.POST['writer']
    update_blog.body=request.POST['body']
    update_blog.pub_date=timezone.now()
    update_blog.save()
    return redirect('detail', update_blog.id)

def delete(request, id):
    delete_blog=blog.objects.get(id=id)
    delete_blog.delete()
    return redirect('home')