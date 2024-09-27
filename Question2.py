# Question 2: Do Django signals run in the same thread as the caller?

# Yes, by default, Django signals run in the same thread as the caller.


import threading
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

logging.basicConfig(level=logging.INFO)

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    logging.info(f"Signal receiver running in thread: {threading.current_thread().name}")


from .models import MyModel
import threading
import logging

logging.basicConfig(level=logging.INFO)

def my_view(request):
    logging.info(f"View running in thread: {threading.current_thread().name}")
    obj = MyModel.objects.create(name="Test")  
    return HttpResponse("Done")
