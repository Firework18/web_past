from django.shortcuts import render
from django.views.generic import *
from .models import *


class CategoryList(ListView):
    model = Category
    context_object_name = "obj"

    def get_template_names(self):
        if self.request.headers.get("Hx-Request") == "true":
            return ["fragments/category_fragment.html"]
        return ["panel_admin/categoria.html"]


def category_save(request):
    context = {}
    template_name = "panel_admin/category-list.html"

    if request.method == "POST":
        i = request.POST.get("id")
        d = request.POST.get("descript")

        o = Category.objects.create(descript=d)
    obj = Category.objects.all().order_by("descript")
    context["obj"] = obj

    return render(request, template_name, context)


def category_delete(request, pk):
    context = {}
    template_name = "panel_admin/category-list.html"

    o = Category.objects.filter(id=pk).first()
    o.delete()

    obj = Category.objects.all().order_by("descript")
    context["obj"] = obj

    return render(request, template_name, context)
