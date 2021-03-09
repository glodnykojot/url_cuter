from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from cuter.models import Address
from django.http import HttpResponse


class redirectView(TemplateView):

    def get(self, request, shortcut):
        try:
            ad = Address.objects.get(shortcut=shortcut)
            return redirect(ad.url)
        except:
            return HttpResponse('not exists in database',status=404) 