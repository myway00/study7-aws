from django.shortcuts import render, redirect, get_object_or_404
from .models import blog
from django.utils import timezone
from .forms import blogform

# Create your views here.
def detail(request, id):
    Blog=get_object_or_404(blog, pk=id) 
    return render(request, 'detail.html', {'blog':Blog})

def home(request):
    blogs=blog.objects.all()
    return render(request, 'home.html',{'blogs':blogs})

def new(request):
    form=blogform()
    return render(request, 'new.html',{'form' : form})

def create(request): #new.html에서 오는 정보를 받아줘야 함
    form=blogform(request.POST, request.FILES)
    if form.is_valid: #유효성 검사
        new_blog=form.save(commit=False)
        #blogform엔 pub_date가 들어가지 않는데그냥 냅둔다면 빈칸으로 쌓일거기 때문에
        #commit false로 임시저장 시캬노코 pubdate 추가해야함
        new_blog.pubdate=timezone.now()
        new_blog.save() #pub도 추가했으니 최종 저장
        return redirect('detail', new_blog.id)
    return redirect('home') #form 유효안하면 home으로

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