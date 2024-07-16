from django import forms
from .models import Category, News


class NewCategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["name"]
        labels = {
            "name": "Nome"
        }


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"
        labels = {
            "title": "Título",
            "content": "Conteúdo",
            "author": "Autoria",
            "created_at": "Criado em",
            "image": "URL da Imagem",
            "categories": "categoria",
        }
        widgets = {
            "content": forms.Textarea(),
            "categories": forms.CheckboxSelectMultiple(),
            "created_at": forms.DateInput(
                attrs={"type": "date"}
            )
        }
