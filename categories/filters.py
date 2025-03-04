import django_filters
from django.db import models
from .models import Category

class CategoryFilter(django_filters.FilterSet):
    class Meta:
        model = Category
        fields = {
            'name' : ['iexact','contains']
        }
        filter_overrides = {
        models.CharField: {
            'filter_class': django_filters.CharFilter,
            'extra': lambda f: {
                'lookup_expr': 'icontains',
            },
        },}
