from django import forms

from apps.models import Todo


class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description", "is_done"]
        labels = {
            "title": "Sarlavha",
            "description": "Tavsif",
            "is_done": "Bajarilgan",
        }
        widgets = {
            "title": forms.TextInput(attrs={"class": "input", "placeholder": "Masalan: Hisobotni tayyorlash", "autofocus": True}),
            "description": forms.Textarea(attrs={"class": "input", "rows": 5, "placeholder": "Vazifa haqida batafsil yozing..."}),
            "is_done": forms.CheckboxInput(attrs={"class": "check"}),
        }
