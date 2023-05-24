from django import template

from tasks.models import Category

register = template.Library()


@register.inclusion_tag('task/category_list.html')
def draw_categories():
    category_list = Category.objects.prefetch_related()

    return {
        'categories': category_list
    }
