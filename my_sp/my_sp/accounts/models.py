from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Patrner(models.Model):
    slug = models.SlugField(max_length=100, unique=True)
    name = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        self.slug = self.name.replace(" ", "-").lower()
        super().save(*args, **kwargs)



class User(AbstractUser):
    partner = models.ForeignKey(Patrner, on_delete=models.CASCADE)
    
