from django_filters import FilterSet, DateFilter
from django import forms
from .models import Post

class PostFilter(FilterSet):
    search_data = DateFilter(field_name='timeDateCreation', widget = forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),lookup_expr='gt', label='Дата')

    class Meta:
        model = Post
        fields = {
            'title': ['icontains'],
            'author': ['exact'],
            'postCategory': ['exact'], 
            }
        

