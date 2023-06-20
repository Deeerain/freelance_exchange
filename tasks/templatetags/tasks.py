from django import template
from tasks.models import Task


register = template.Library()


@register.inclusion_tag('task/task_list.html')
def draw_tasks(category=None, count=10):
    objects = Task.objects.filter(visible=True).prefetch_related('category')

    return {
        'tasks': objects
    }
