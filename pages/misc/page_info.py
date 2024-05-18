import random
from site_setting.models import Contact, Salon


def get_random_salon():
    salons = Salon.objects.all()
    return random.choice(salons)


def get_contact_info(salon):
    return Contact.objects.filter(salon__pk=salon['pk']).first()