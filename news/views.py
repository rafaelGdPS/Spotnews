from django.shortcuts import redirect, render
from rest_framework import viewsets
from .models import News, Category, User
from .forms import NewCategoryForm, NewsForm
from .serializers import CategorySerializer, NewsSerializer, UserSerializer


def new(request):
    context = {"news": News.objects.all()}
    return render(request, 'home.html', context)


def news_details(request, id):
    new_detail = News.objects.get(id=id)
    context = {"details": new_detail}
    return render(request, 'news_details.html', context)


def create_new_category(request):
    form = NewCategoryForm()

    if request.method == 'POST':
        form = NewCategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "categories_form.html", context)


def create_new_news(request):
    form = NewsForm()

    if request.method == "POST":
        form = NewsForm(request.POST, request.FILES)

        if form.is_valid():
            data = form.cleaned_data.pop("categories")
            news = News.objects.create(**form.cleaned_data)
            print(data)
            news.categories.set(data)
            return redirect("home-page")
    print(form)
    context = {"form": form}
    return render(request, "news_form.html", context)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
