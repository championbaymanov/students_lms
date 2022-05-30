from django import forms
from videos.models import Comments, VideoContent


class CreateVideoContentForm(forms.ModelForm):
    class Meta:
        model = VideoContent
        fields = '__all__'


class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'comment here ...',
        'rows': '4',
    }))

    class Meta:
        model = Comments
        fields = ('content', )

class VideoCreateForm(forms.ModelForm):
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    vidoe_url = forms.URLField(widget=forms.URLInput(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '8',
    }))
    class Meta:
        model = VideoContent
        fields = '__all__'




