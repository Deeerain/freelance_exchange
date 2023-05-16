from django.http import HttpRequest

from tasks.models import Task

from .models import Category, Account


def categories(request: HttpRequest):
    categories = Category.objects.all()

    for category in categories:
        setattr(category, 'count', Task.objects.filter(categories=category, visible=True).count())

    return {
        'categories': categories
    }

def account(request: HttpRequest):
    account = Account.objects.filter(user=request.user).first()

    return {
        'account': account
    }