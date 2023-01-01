from django import forms
from .models import News
from django.core.exceptions import ValidationError
import re


class NewsForm(forms.ModelForm):

    class Meta:
        model = News
        fields = ['title', 'content', 'is_published', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }

    def clean_title(self):
        """
        Creation of custom validator for any fields.
        Method name should start with 'clean_FIELDNAME', and only works with cleaned_data['FIELDNAME']
        """
        title = self.cleaned_data['title']

        if re.match(r'\d', title):
            raise ValidationError('The title should not starts with a number')

        return title
