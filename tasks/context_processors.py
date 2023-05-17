from django.http import HttpRequest

from tasks.models import Task

from .models import Category


def categories(request: HttpRequest):
    categories = Category.objects.all()

    for category in categories:
        setattr(category, 'count', Task.objects.filter(categories=category,
                                                       visible=True).count())

    return {
        'categories': categories
    }
