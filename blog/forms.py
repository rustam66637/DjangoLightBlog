from django import forms
from .models import Tag, Post
from django.core.exceptions import ValidationError

class TagForm(forms.ModelForm):
    '''Форма создания тега'''
    # title = forms.CharField(max_length=50) # виджеты input
    # slug = forms.CharField(max_length=50)
    #
    # title.widget.attrs.update({'class': 'form-control'})
    # slug.widget.attrs.update({'class': 'form-control'})
    class Meta:
        model = Tag
        fields = ['title', 'slug']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
        }


    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        # проверка на создание тега 'create'
        if new_slug == 'create':
            raise ValidationError('Тег не может иметь название "create"')

        # проверка на создание существующего тега
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError(f'Тег {new_slug} уже имеется')

        return new_slug


    # # переопределение метода save
    # def save(self):
    #     new_tag = Tag.objects.create(
    #         title=self.cleaned_data['title'],
    #         slug=self.cleaned_data['slug']
    #     )
    #     return new_tag

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'text', 'tags']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            'tags': forms.SelectMultiple(attrs={'class': 'form-control'}),
        }

    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()

        if new_slug == 'create':
            raise ValidationError('Пост не может иметь название "create"')
        return new_slug
