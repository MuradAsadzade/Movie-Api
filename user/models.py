from django.db import models
from django.contrib.auth.models import User
from movie.models import Studio,Movie
# Create your models here.

class Director(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    studio=models.ForeignKey(Studio,on_delete=models.SET_NULL,blank=True,null=True)
    
    def __str__(self):
        return self.user.username
    
class Customer(models.Model):
    user=models.OneToOneField(User,on_delete=models.PROTECT)
    
    def __str__(self):
        return self.user.username
    
    
class Review(models.Model):
    customer=models.ForeignKey(Customer,on_delete=models.CASCADE)
    movie=models.ForeignKey(Movie,on_delete=models.CASCADE)
    point=models.IntegerField()
    comment=models.TextField()
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f'{self.movie.title}-{self.customer.user.username}'