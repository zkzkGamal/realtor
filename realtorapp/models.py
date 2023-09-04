from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    countrys = [('Egypt','Egypt'),('Canada','Canada'),
                ('USA','USA'),('UAE','UAE'),('KSA','KSA'),
                ('UK','UK'),('Germany','Germany')]

    user = models.OneToOneField(User , on_delete=models.CASCADE , null=True)
    phone = models.CharField(max_length=11 , null=True , blank=True)
    email = models.EmailField(max_length=50 , null=True , blank=True)
    address = models.CharField(max_length=80 , null=True , blank=True)
    f_name = models.CharField(max_length=10 , null=True , blank=True)
    L_name = models.CharField(max_length=10 , null=True , blank=True)
    picture = models.FileField(upload_to='media',null=True, blank=True)
    country = models.TextField(choices=countrys , null=True , blank=True)
    status = models.CharField(default='offline' , max_length=10)
    def __str__(self):
        if self.f_name and self.L_name:
            return str(self.f_name + self.L_name)
        else:
            return str(self.user.username)
class product(models.Model):
    av_location = [('nasrcity','nasrcity') , ('madity','madity'),
                   ('elshrouk','elshrouk') , ('Giza','Giza'),
                   ('The Fifth Settlement','The Fifth Settlement') ,
                     ('badr','badr')]
    types = [('Houses','Houses') , ('Appartment','Appartment') , 
             ('Townhell','Townhell') , ('Vacation','Vacation')]
    styles = [('A-Frame','A-Frame') , ('Spanish','Spanish')]
    selling_type = [('Sell' ,'Sell') , ('Rent', 'Rent')]
    house_used = [('Vecation' , 'Vecation') , ('Normal','Normal')]
    profile_user = models.ForeignKey(profile , on_delete=models.CASCADE)
    name = models.CharField(max_length=20 , null=True , blank=True)
    Description = models.CharField(max_length=500 , null=True , blank=True)
    location = models.TextField(null=True , blank=True , choices=av_location)
    type_house = models.TextField(choices=types , null=True , blank=True)
    style_house = models.TextField(choices=styles , null=True , blank=True)
    area = models.FloatField(null=True , blank=True)
    price = models.FloatField(null=True , blank=True)
    number_kitchen = models.IntegerField(null=True , blank=True)
    number_bedroom = models.IntegerField(null=True , blank=True)
    number_bathroom = models.IntegerField(null=True , blank=True)
    pics = models.FileField(upload_to='media' , null=True )
    sell_type = models.TextField(choices=selling_type , null=True , blank=True)
    house_for = models.TextField(choices=house_used,null=True , blank=True)
    active = models.BooleanField(default=False)

    def __str__(self):
        return str('name : ' + self.profile_user.f_name + ' -product name : ' + self.name)
class produc_images(models.Model):
    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'
    
    Product = models.ForeignKey(
        product, on_delete=models.CASCADE, null=True, blank=True)
    img = models.FileField(upload_to='media' , null=True)
class messageQA(models.Model):
    email = models.EmailField(null=True , blank=True)
    qustion = models.CharField(max_length=200 , null=True , blank=True)

class saved_message(models.Model):
    sender = models.ForeignKey(profile , on_delete=models.CASCADE , related_name='sender'  , null=True , blank=True)
    reciver = models.ForeignKey(profile , on_delete=models.CASCADE , related_name='reciver' , null=True , blank=True)
    message = models.TextField( null=True , blank=True)
    time_stamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str('sender : ' + self.sender.f_name + ' ' + self.sender.L_name
                   + ' reciver : ' + self.reciver.f_name + ' ' + self.reciver.L_name )


