from urlReciever.models import URL_RECIEVED
from django import forms



class urlRecieveModelForm (forms.ModelForm):



    class Meta:
        model   = URL_RECIEVED
        fields  = ['RecievedAdress', 'ShortAdressInt']

        widgets = {
            'RecievedAdress'         : forms.TextInput(attrs={'placeholder' : 'Enter Your "URL" : ', 'class':'forminput'}),
            'ShortAdressInt'         : forms.HiddenInput(),
            
         }



