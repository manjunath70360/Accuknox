# Question 3: By default, do Django signals run in the same database transaction as the caller?

# Yes, Django signals are executed in the same database transaction as the caller, particularly the post_save signal.



import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

logging.basicConfig(level=logging.INFO)

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    logging.info("Signal receiver: saving related model")
    instance.related_model.create(related_name="test")  # Save something related


from django.db import transaction
from .models import MyModel
import logging

logging.basicConfig(level=logging.INFO)

def my_view(request):
    with transaction.atomic():
        logging.info("Creating object in transaction")
        obj = MyModel.objects.create(name="Test")  
        raise Exception("Error in the view") 
