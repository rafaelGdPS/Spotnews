from django.shortcuts import render
from .models import News

# Create your views here.


# def category(request):
#     context = {"categories": Category.objects.all()}
#     return render(request, 'home.html', context)


# def user(request):
#     context = {"users": User.objects.all()}
#     return render(request, 'home.html', context)


def new(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    new_detail = News.objects.get(id=id)
    context = {"details": new_detail}
    return render(request, 'news_details.html', context)
