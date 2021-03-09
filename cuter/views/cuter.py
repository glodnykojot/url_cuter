from django.shortcuts import render
from django.views.generic import TemplateView
from cuter.models import Address
from django.http import HttpResponse
import validators

def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

def elf_hash(s):
    h = 0
    for c in s:
        h = (h << 4) + ord(c)
        t = (h & 0xF0000000)
        if t != 0:
            h = h ^ (t >> 24)
        h = h & ~t
    return h
    
alphabet=["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]


class cuterView(TemplateView):

    template_name = 'cut.html'
    def get_context_data(self, **kwargs):
        context = super(cuterView, self).get_context_data(**kwargs)
        context['title'] = 'cuter'
        return context
   
    def post(self, request):
        url = request.POST.get('URL')
        tmp = url.split(".")
        if validators.url(url):
            if 'www' in url:
                domain = tmp[1]
            else:
                domain = tmp[0][8:]
            
            shortcut = domain + '-' +''.join([alphabet[x] for x in numberToBase(elf_hash(url), 62)])  
            


            try:
                if not Address.objects.filter(url=request.POST.get('URL')).exists():
                    address = Address(url=url, shortcut=shortcut)
                    address.save()
                    return HttpResponse(f'<h1>Your shortcut is:{shortcut}</h1>')
                else:
                    return HttpResponse('object exists',status=400)       
            except:    
                return HttpResponse('sth went wrong',status=404)
        else:
            return HttpResponse('not valid url',status=400)