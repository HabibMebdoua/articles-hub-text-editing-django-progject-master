from django import forms
from ckeditor.widgets import CKEditorWidget
from .models import Article


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=CKEditorWidget(),label='')
    class Meta:
        model = Article
        fields = ['title','content','save_for_you']
