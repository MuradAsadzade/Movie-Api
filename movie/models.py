from django.db import models
# from user.models import Director
# Create your models here.

class Studio(models.Model):
    title=models.CharField(max_length=100)
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Genre(models.Model):
    title=models.CharField(max_length=100)
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
class Movie(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()
    released=models.DateField()
    # imdb=models.IntegerField()
    # studio=models.ForeignKey(Studio,on_delete=models.SET_NULL,blank=True,null=True)
    image = models.ImageField(upload_to="movie/images/",null=True,blank=True)
    director=models.ForeignKey('user.Director',on_delete=models.SET_NULL,blank=True,null=True)
    genres=models.ManyToManyField(Genre)
    updated=models.DateField(auto_now=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.title