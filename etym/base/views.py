import time
import os

from django.shortcuts import render, redirect
from django.views.generic import View, TemplateView
from django.views.generic.edit import CreateView

from utils import get_random_word
from models import Word


class IndexView(View):

    def get(self, request):

        if 'w' in request.GET:
            search_word = request.GET.get("w")
            words = Word.objects.filter(name__iexact=search_word)
            found = bool(len(words))

            return render(request, "index.html" if found else "notfound.html" , {
                "word": words[0] if found else search_word,
            })

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


class WordCreateView(CreateView):
    template_name = "add.html"
    model = Word
    fields = ['name', 'description', 'origin', 'type']
    redirect_to = "/add/success/"


class SuccessView(TemplateView):
    template_name = "success.html"
