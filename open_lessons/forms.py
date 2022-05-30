from django import forms
from open_lessons.models import *


class CreateOpen_lessonsForm(forms.ModelForm):
    class Meta:
        model = Open_lessons
        fields = '__all__'


class RedisterForm(forms.ModelForm):
    full_name = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Full Name',
        'rows': '1',
    }))
    phone = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Phone Number',
        'rows': '1',
    }))

    class Meta:
        model = Register
        fields = ('full_name', 'phone', )

class OpenCreateForm(forms.ModelForm):
    phota = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'md-textarea form-control',
        'rows': '1',
    }))
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    additional = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '5',
    }))
    spiker = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    address = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    destination = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '3',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '8',
    }))
    for_information = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    date_of_the_event = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    class Meta:
        model = Open_lessons
        fields = '__all__'




