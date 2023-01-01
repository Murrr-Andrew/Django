from django import forms
from .models import Category


class NewsForm(forms.Form):
    title = forms.CharField(max_length=150, label='Title:', widget=forms.TextInput(attrs={'class': 'form-control'}))
    content = forms.CharField(required=False, label='Content:', widget=forms.Textarea(attrs={'class': 'form-control'}))
    is_published = forms.BooleanField(required=False, initial=True, label='Published:',
                                      widget=forms.CheckboxInput(attrs={'class': 'form-check-input'}))
    category = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label=None, label='Category',
                                      widget=forms.Select(attrs={'class': 'form-select'}))
