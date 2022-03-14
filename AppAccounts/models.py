from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save
from AppViajes.models import Post
from django.contrib.auth.decorators import login_required

# Create your models here.

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=120, null=True, blank=True)
    apellido=models.CharField(max_length=120, null=True, blank=True)
    email=models.EmailField()
    foto=models.ImageField(upload_to='profiles', null=True, blank=True)
    descripcion=models.CharField(max_length=350, null=True, blank=True)
    web=models.URLField(max_length=200, null=True, blank=True)
    def __str__(self):
        return self.user.username
      

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()