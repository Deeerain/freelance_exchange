from django.views.generic import TemplateView, ListView
from accounts.models import User

from .mixins import SearchMixin


class HomeView(TemplateView):
    template_name = 'burse/index.html'


class Freelancers(ListView, SearchMixin):
    model = User
    template_name = 'freelancers/list.html'
    search_fields = ['user__username']
