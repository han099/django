from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib import messages #진행상태를 메시지로 폼에서 출력하고 싶을 때 사용
from .models import Post
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def create_post(request):
    if request.method  =='GET':
       context= {'form':PostForm()} #model 같은 폼태그형식을 속성으로 만들어서 클래스안에 Meta에 지정된 값을 리턴
       return  render(request,'blog/post_form.html',context)
    elif request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts')
        else:
            return render(request, 'blog/post_form.html', {'form': form})
@login_required
def edit_post(request,id):
    #원본 post = get_object_or_404(Post, id=id) #URL 패턴과 일치하지 않으면 404로 리디렉션을 하겠다.
    queryset = Post.objects.filter(author = request.user)
    post = get_object_or_404(queryset, id=id)

    if request.method == "GET":
        context = {'form': PostForm(instance=post), 'id': id}
        return render(request, 'blog/post_form.html', context)  #'blog/post_form.html'주소로 템플릿을 랜더링한다.
    elif request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            #https://docs.djangoproject.com/en/4.2/ref/contrib/messages/#displaying-messages 내용확인 및 추가.
            messages.success(request, 'The post has been updated successfully')
            return redirect('posts')
        else:
            messages.error(request,'Please correct the following errors:')
            return render(request, 'blog/post_form.html', {'form':form})

@login_required
def delete_post(request,id):
    queryset = Post.objects.filter(author = request.user)
    post = get_object_or_404(queryset, pk=id)

    # 원본
    # post = get_object_or_404(Post, pk=id)
    # context = {'post': post}

    if request.method == "GET":
        return render(request, 'blog/post_confirm_delete.html', context)

    elif request.method == 'POST':
        post.delete()
        messages.success(request, 'The post has been updated successfully')
        return redirect('posts')



#보기 페이지 요청하게 되면 출력되는 내용을 기재한다.
def home(request):
    posts = Post.objects.all()  #selectall _QuerySet
    context = {'posts': posts}
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')

def web01(request):
    return HttpResponse('<h1> web01 page </h1>')

def web02(request):
    return HttpResponse('<h1> web02 page </h1>')

def web03(request):
    return HttpResponse('<h1> web03 page </h1>')