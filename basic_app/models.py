from _pydecimal import Decimal

from django.db import models
from  django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.



class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username



class Payments(models.Model):
    PaymentsId = models.IntegerField()
    id_afiliado = models.ForeignKey(UserProfileInfo, on_delete=models.CASCADE)
    months = models.IntegerField()
    amount = models.BigIntegerField()
    payment_date = models.DateTimeField()


class Menu(models.Model):
    name = models.CharField(max_length=256)
    provider = models.CharField(max_length=256)
    location = models.CharField(max_length=256)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("basic_app:detail",kwargs={"pk":self.pk})


class Alimento(models.Model):
    name = models.CharField(max_length=256)
    preparacion = models.CharField(max_length=256)
    menu = models.ForeignKey(Menu,related_name='alimentos',on_delete=models.CASCADE)

    def __str__(self):
        return self.name








