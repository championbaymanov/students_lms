from django import forms
from blog.models import Comment, Post

class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comment
        fields = ('content', )

class PostCreateForm(forms.ModelForm):
    thumbnail = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'md-textarea form-control',
        'rows': '1',
    }))
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    overview = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '8',
    }))
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '8',
    }))
    class Meta:
        model = Post
        fields = '__all__'


