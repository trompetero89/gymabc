from _pydecimal import Decimal

from django.db import models
from  django.contrib.auth.models import User
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









