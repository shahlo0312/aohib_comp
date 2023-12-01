from django import forms
# from ckeditor.widgets import CKEditorWidget
from .models import News


class AddNewsForms(forms.ModelForm):
    class Meta:
        model = News
        fields = ['title', 'img', 'body', 'category', 'tags']
    
