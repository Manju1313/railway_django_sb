# from django.db import models

# # Create your models here.
# class Article(models.Model):
#     title = models.CharField(max_length=200)
#     body = models.TextField()
#     created_on = models.DateTimeField(auto_now_add=True)
  
  
# class Comment(models.Model):
#     article = models.ForeignKey(Article, on_delete=models.CASCADE)
#     text = models.CharField(max_length=200)
#     created_on = models.DateTimeField(auto_now_add=True)


from django.db import models


class Member(models.Model):

       residing_country = models.CharField(max_length=50)
       residing_state = models.CharField(max_length=50)
       residing_city = models.CharField(max_length=50)

class Country(models.Model):

         country= models.CharField(max_length=20)

class State(models.Model):

         state=models.CharField(max_length=20)
         country = models.ForeignKey(Country,on_delete=models.DO_NOTHING,blank=True, null=True)       

class City(models.Model):

        city=models.CharField(max_length=20)
        state=models.ForeignKey(State,on_delete=models.DO_NOTHING,blank=True, null=True)