from django import forms
from .models import Post, Category

#This is how dropdown works/coded I cant do anything about it :(
#choices = [('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')]

choices = Category.objects.all().values_list('name', 'name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'author', 'category', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.TextInput(attrs={'class': 'form-control'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(choices=[('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')], attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }

class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'title_tag', 'body')
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter title here'}),
            'title_tag': forms.TextInput(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            #'author': forms.Select(attrs={'class': 'form-control'}),
            #'category': forms.Select(choices=[('coding', 'coding'), ('sports', 'sports'), ('entertainment', 'entertainment')], attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }