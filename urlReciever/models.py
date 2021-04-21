
from django.db import models
from django.db.models.fields import DateField
from.utils import media_upload_path
# Create your models here.


class URL_RECIEVED (models.Model):



    RecievedAdress = models.CharField(max_length=300, blank=False)
    ShortAdressInt = models.CharField(max_length=25 ,blank=True, null=True, unique=True)
    qr             = models.ImageField(upload_to=media_upload_path, blank=True)

    timestamp = DateField(auto_now_add=True)


    def __str__(self):
        return self.RecievedAdress