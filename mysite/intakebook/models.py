from django.db import models

# Create your models here.
class McType(models.Model):
        name =  models.CharField(max_length=20)
        def __str__(self):
                return self.name

class Rank(models.Model):
        name =  models.CharField(max_length=20)
        def __str__(self):
                return self.name

class Academy(models.Model):
        name =  models.CharField(max_length=100)
        def __str__(self):
                return self.name

class Role(models.Model):
        name = models.CharField(max_length = 20)
        def __str__(self):
                return self.name

class Soldier(models.Model):
        mc_type = models.ForeignKey(McType, on_delete= models.CASCADE)
        mc = models.IntegerField(unique=True)
        rank = models.ForeignKey(Rank, on_delete=models.CASCADE)
        name =  models.CharField(max_length=20)
        position = models.CharField(max_length = 200)
        unit = models.CharField(max_length=200)
        academy = models.ForeignKey(Academy, on_delete= models.CASCADE)
        intake = models.IntegerField()
        phone_no = models.CharField(max_length = 20)
        password = models.CharField(max_length = 200)
        role = models.ForeignKey(Role, on_delete= models.CASCADE)
        def __str__(self):
                return self.name

