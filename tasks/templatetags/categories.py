from django import template
from django.db.models import Count

from tasks.models import Category

register = template.Library()


@register.inclusion_tag('task/category_list.html')
def draw_categories():
    category_list = Category.objects.all().annotate(count=Count('task'))

    return {
        'categories': category_list
    }
