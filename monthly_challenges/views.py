
from django.http import Http404


def not_found(_):
    raise Http404()
