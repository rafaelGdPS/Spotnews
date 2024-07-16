from django.shortcuts import redirect, render
from .models import News, Category
from .forms import NewCategoryForm

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


def create_new_category(request):
    form = NewCategoryForm()

    if request.method == 'POST':
        form = NewCategoryForm(request.POST)

        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect("home-page")
    context = {"form": form}
    return render(request, "categories_form.html", context)
