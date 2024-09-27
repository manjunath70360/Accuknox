
# Question 1: By default, are Django signals executed synchronously or asynchronously?

# By default, Django signals are executed synchronously, meaning they are executed immediately after 
# the signal is sent, blocking the flow until the connected receiver is executed.


import time
import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import MyModel

logging.basicConfig(level=logging.INFO)

@receiver(post_save, sender=MyModel)
def my_signal_receiver(sender, instance, **kwargs):
    logging.info("Signal receiver started")
    time.sleep(5)  # Simulate a time-consuming task
    logging.info("Signal receiver finished")


from .models import MyModel
import logging

logging.basicConfig(level=logging.INFO)

def my_view(request):
    logging.info("View execution started")
    obj = MyModel.objects.create(name="Test")  
    logging.info("View execution finished")
