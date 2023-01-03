from django import template
from django.db.models import Count
from news.models import Category


register = template.Library()


@register.simple_tag(name='get_list_categories')
def get_categories():
    return Category.objects.all()


@register.inclusion_tag('news/list_categories.html')
def show_categories():
    # Get all categories which contains news (without empty categories)
    categories = Category.objects.annotate(qty=Count('news')).filter(qty__gt=0)
    return {'categories': categories}
