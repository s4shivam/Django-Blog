from django.db.models.signals import post_save  #operation after object is saved
from django.contrib.auth.models import User    #sender
from django.dispatch import receiver   #receiver
from .models import Profile    #import profile to tie everything together


#create profile object with user=instance of the user
@receiver(post_save,sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user = instance)

#Saves our profile everytime user objects gets saved
@receiver(post_save,sender=User)
def save_profile(sender,instance,**kwargs):
    instance.profile.save()
