from django.shortcuts import render, redirect, HttpResponse
from .forms import ArticlesForms
from .models import ArticlesModel

def index(request):
    if request.method == "POST":
        form = ArticlesForms(request.POST)
        if form.is_valid():
            Articles = ArticlesModel()    
            title = request.POST.get('title')
            link = request.POST.get('URL')
            content = request.POST.get('content')
            is_published =request.POST.get('is_published')
            category =request.POST.get('category')
            if is_published == 'on':
                is_published = True
            else:
                is_published = False
            ArticlesModel.objects.create(title=title,URL=link,content = content,is_published=is_published,category=category)
            return redirect('articles/')
        else:
            form = ArticlesForms() 
            return render(request,'index.html',{'form':form})
    else:
        form = ArticlesForms() 
        return render(request,'index.html',{'form':form})
def articles(request):
    article = ArticlesModel.objects.all()
    return render(request,'articles.html', {'article':article,})
def delete(request,num):
    delete_articles = ArticlesModel.objects.filter(id = num)
    if not delete_articles:
        return HttpResponse('IT DOESN`T EXIST')
    else:
        delete_articles[0].delete()
    return redirect('../articles/')
def change(request,num):
    try:
        articles = ArticlesModel.objects.get(id=num)
        if request.method == "POST":
            form = ArticlesForms(request.POST)
            if form.is_valid():
                articles.title = request.POST.get('title')
                articles.link = request.POST.get('URL')
                articles.content = request.POST.get('content')
                is_published =request.POST.get('is_published')
                if is_published == 'on':
                    is_published = True
                else:
                    is_published = False
                articles.category =request.POST.get('category')
                articles.is_published = is_published
                articles.save()
                return redirect("../articles/")
            else:
                return HttpResponse('no_valid form')
        else:
            form = ArticlesForms() 
            return render(request,'change.html',{'form':form})
    except articles.DoesNotExist:
        return HttpResponse("<h2>NOT found</h2>")
     