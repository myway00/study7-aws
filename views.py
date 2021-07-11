from django.shortcuts import render, get_object_or_404
from .models import blog
# Create your views here.
def detail(request, id):
    Blog=get_object_or_404(blog, pk=id) 
    return render(request, 'detail.html', {'blog':Blog})

def home(request):
    blogs=blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

