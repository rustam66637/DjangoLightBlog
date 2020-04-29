from django.shortcuts import render
from django.shortcuts import get_object_or_404, redirect

from .models import Post, Tag

class DetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        return render(request, self.template, context={
        self.model.__name__.lower(): obj
        })

class CreateMixin:
    form_model = None
    template = None

    def get(self, request):
        form = self.form_model
        return render(request, self.template, context={'form': form})


    def post(self, request):
        bound_form = self.form_model(request.POST)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})

