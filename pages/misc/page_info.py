import random
from site_setting.models import Contact, Salon, SalonSocial


def get_random_salon():
    salons = Salon.objects.all()
    return random.choice(salons)


def get_contact_info(salon):
    data = {
        "contact": Contact.objects.filter(salon__pk=salon["pk"]).first(),
        "socials": SalonSocial.objects.filter(salon__pk=salon["pk"]),
    }
    return data
