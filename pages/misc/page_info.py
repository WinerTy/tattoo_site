import random
from site_setting.models import Contact, Salon, SalonSocial
from database.models import Master, Appointment


def get_random_salon():
    salons = Salon.objects.all()
    return random.choice(salons)


def get_contact_info(salon):
    data = {
        "contact": Contact.objects.filter(salon__pk=salon["pk"]).first(),
        "socials": SalonSocial.objects.filter(salon__pk=salon["pk"]),
    }
    return data


def get_master_info(user):
    data = {}
    master = Master.objects.filter(user=user).first()
    if master:
        appointments = Appointment.objects.filter(master=master).order_by(
            "-created_at"
        )[:5]
        data["appointments"] = appointments
        return data


def check_groups(request, name):
    is_master = request.user.groups.filter(name=name).exists()
    return is_master
