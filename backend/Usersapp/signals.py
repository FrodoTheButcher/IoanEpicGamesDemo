from .models import Profile,User
from django.db.models import signals
from django.db.models.signals import post_delete,post_save,pre_save
from django.dispatch import receiver
@receiver(post_save,sender=User)
def create_OrUpdateProfileWhenUserCreated(sender,instance,created,**kwargs):
    if created:
        instance.username = instance.email
        instance.save()
        Profile.objects.create(
            user = instance,
            email = instance.email,
        )


#folosesti pre_save si verifici daca created e false,updatezi profilul dupa user
#update profile when user updated

@receiver(post_delete,sender=Profile)
def deleteUserWhenProfileGotDeleted(sender,instance,**kwargs):
    user =  instance.user
    user.delete()
