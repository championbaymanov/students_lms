from django import forms
from . models import *

class GroupCreateForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = '__all__'

class MenteeCreateForm(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = '__all__'

class MentorCreateForm(forms.ModelForm):
    class Meta:
        model = Mentor
        fields = '__all__'

class MenteeCreateForm(forms.ModelForm):
    class Meta:
        model = Mentee
        fields = '__all__'

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class CourseCreateForm(forms.ModelForm):
    phota = forms.ImageField(widget=forms.FileInput(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Description',
        'rows': '1',
    }))
    title = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Title',
        'rows': '1',
    }))
    description = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Description',
        'rows': '8',
    }))
    price = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'md-textarea form-control',
        'placeholder': 'Price',
        'rows': '1',
    }))
    class Meta:
        model = Course
        fields = '__all__'
