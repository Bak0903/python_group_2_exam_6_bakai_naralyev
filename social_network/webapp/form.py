from django import forms
from webapp.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'created_at')
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control col-sm-10'}),
            'text': forms.Textarea(attrs={'class': 'form-control col-sm-10'}),
            'created_at': forms.SelectDateWidget(attrs={'class': 'form-control col-sm-10'}),
        }
