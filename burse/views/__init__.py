from django.views.generic import TemplateView, ListView

from burse.models import Account

from .mixins import SearchMixin


class HomeView(TemplateView):
    template_name = 'burse/index.html'


class Freelancers(ListView, SearchMixin):
    model = Account
    template_name = 'freelancers/list.html'
    search_fields = ['user__username']
