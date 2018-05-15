from django.db.models import Q


def propositions_filter(self, queryset):
    query = self.request.GET.get('query')
    try:
        query_int = int(query)
    except (ValueError, TypeError):
        query_int = -1

    if query:
        queryset = queryset.filter(
            Q(abstract__contains=query) |
            Q(number__contains=query) |
            Q(proposition_type__contains=query) |
            Q(proposition_type_initials__contains=query) |
            Q(year=query_int)
        )

    return queryset
