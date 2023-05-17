from typing import Dict, List, Any

from django.db.models import QuerySet, Q
from django.views.generic.list import MultipleObjectMixin
from django.http import HttpRequest


class SearchMixin(MultipleObjectMixin):
    search_fields: List[str] = []
    search_param_name: str = 'search'

    def get_search_param(self) -> str:
        if hasattr(self, 'request'):
            if isinstance(self.request, HttpRequest):
                request: HttpRequest = getattr(self, 'request')
                request = getattr(self, 'request')

                return request.GET.get(self.search_param_name)

        return None

    def get_search_fields(self, search_param: str) -> list[Dict[str, Any]]:
        return [{field + '__icontains': search_param}
                for field in self.search_fields]

    def generate_filter(self, search_fields: list[str]):
        q: Q = Q()

        for field in search_fields:
            q = q.__or__(Q(**field))

        return q

    def filter(self, queryset: QuerySet[Any]) -> QuerySet[Any]:
        search_param = self.get_search_param()

        if search_param:
            sf = self.get_search_fields(search_param)
            f = self.generate_filter(sf)
            print(f)
            return queryset.filter(f)

        return queryset

    def get_queryset(self) -> QuerySet[Any]:
        queryset = super().get_queryset()
        return self.filter(queryset)
