import time
import os

from django.shortcuts import render
from django.views.generic import View, TemplateView

from utils import get_random_word


class IndexView(View):

    def get(self, request):
        word = get_random_word()
        return render(request, "index.html", {
            "word": word,
        })


class AboutView(TemplateView):
    template_name = "humans.txt"

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context["last_update"] = time.ctime(os.path.getmtime(__file__))
        return context

    def render_to_response(self, context, **kwargs):
        return super(AboutView, self).render_to_response(
            context,
            content_type='text/plain',
            **kwargs
        )