from django.db import models
from django.contrib.auth.models import User
#from tinymce.models import HTMLField
from django.dispatch import receiver
from django.db.models.signals import post_save
from AppViajes.models import Post

# Create your models here.

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	descripcion = models.CharField('Subtitulo',max_length=120)
#    web = models.CharField ('web',max_length=30)
#    foto = models.ImageField(null=True, upload='fotos')
    

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()