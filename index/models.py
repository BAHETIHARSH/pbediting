from django.db import models

# Create your models here.
class Contact(models.Model):
    f_name=models.CharField(max_length=50)
    l_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phone=models.CharField(max_length=20)
    msg=models.TextField()
    date=models.DateField()

    def __str__(self):
        return self.f_name

# blog
class Blog(models.Model):
    title = models.TextField()
    des = models.TextField()
    img = models.TextField()
    url = models.URLField()
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.title
# Tutorials
class Tutorial(models.Model):
    title = models.TextField()
    descripation = models.TextField()
    type = models.CharField(max_length=10, choices=[("CS3","CS3"), ("CC", "CC"), ])
    link = models.URLField()


    def __str__(self):
        return self.title