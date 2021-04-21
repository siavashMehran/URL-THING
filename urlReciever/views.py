

from urlShortner.settings import MEDIA_ROOT
from .utils import make_my_QRcode_bitch
from urlReciever.models import URL_RECIEVED

from urlReciever.forms import urlRecieveModelForm
from django.http.response import Http404
from django.shortcuts import redirect, render

def ss(s):
    print('*'*30)
    print(s)
    print('*'*30)




# Create your views here.


def home(request, *args, **kwargs):

    def adressRandomizer():
        from random import randint
        randomInteger = 1
        while (URL_RECIEVED.objects.filter(ShortAdressInt=randomInteger).exists()):
            randomInteger = randint(1, 5000)
        return  randomInteger

    randomInteger   = adressRandomizer()  
    

    form = urlRecieveModelForm(initial={'ShortAdressInt':randomInteger})
    if (request.method == 'POST') and ('RecievedAdress' in request.POST):
        
        form = urlRecieveModelForm(request.POST or None)
        
        if form.is_valid():
            form.save()
            saved_randint = form.cleaned_data.get('ShortAdressInt')
            form = urlRecieveModelForm()
            return redirect('resultPage', shortUrldRandint=saved_randint)

        else: return redirect('/')


    
    context = {
        'title'     : 'Siavash Urlify Thing That Shortens URLS  (duhhh.....)',
        'form'     : form,
        
    }

    return render(request, 'index.html', context)
    


def short_redirect(request, shorturl):
    
    recieved_url_instance = URL_RECIEVED.objects.filter(ShortAdressInt=shorturl).first()
    recieved_url = recieved_url_instance.RecievedAdress
    


    return redirect(f'http://{recieved_url}')










def result_page(request, shortUrldRandint, *args, **kwargs):
    
    def relativeLinkMaker(shortUrldRandint):
        link = f"http://localhost:899/{shortUrldRandint}"
        return link
    
    instance = URL_RECIEVED.objects.filter(ShortAdressInt=shortUrldRandint).first()
    relative_link = relativeLinkMaker(instance.ShortAdressInt)
    
    


    make_my_QRcode_bitch(relative_link, f"{MEDIA_ROOT}/QRcodes/{shortUrldRandint}.png", saveit=True)
    generatedQRcodeAdress = f"QRcodes/{shortUrldRandint}.png"
    instance.qr = generatedQRcodeAdress
    instance.save()
    
    context = {
        'link' : relative_link,

        'instance'   : instance
    }

    

    return render(request, 'result.html', context)
    

