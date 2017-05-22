from django.conf.urls import *
from myapp.views import place
from django.contrib import admin
from django.views.generic import TemplateView

admin.autodiscover()
urlpatterns = [url(r'^connection/',TemplateView.as_view(template_name = 'places.html')),
               url(r'^place/', place, name = 'place'),]
