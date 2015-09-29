from django.shortcuts import render

from django.views.generic import View

from .models import Word


class IndexView(View):

    def get(self, request):
        return render(request, "index.html", {})
