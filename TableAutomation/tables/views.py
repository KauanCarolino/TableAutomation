from django.shortcuts import render
from django.views.generic import ListView

from .models import Person

class IndexView(ListView):
    template_name = 'tables/base.html'
    model = Person

    def get_queryset(self):
        return Person.objects.filter(status=0)
    
    def get_field_person(self):
        fields_verbose_name = [field.verbose_name for field in Person._meta.fields]
        fields_name = [field.name for field in Person._meta.fields]

        fields_verbose_name.remove('ID')
        fields_name.remove('id')
        
        return fields_verbose_name, fields_name
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["fields_verbose_name"], context["fields_name"] = self.get_field_person()
        return context
    