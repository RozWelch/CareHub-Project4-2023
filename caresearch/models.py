from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

PROVIDER_APPROVED_STATUS = ((0, "Pending"), (1, "Approved_careprovider"))

class CareProvider(models.Model):
    careprovider_username = models.CharField(max_length=200, unique=True, primary_key=True)
    password = models.CharField(max_length=20)
    business_name = models.CharField(max_length=200, unique=True)
    main_contact_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=250)
    address_line_2 = models.CharField(max_length=250, blank=True)
    address_line_3 = models.CharField(max_length=250, blank=True)
    postcode = models.CharField(max_length=8)
    phone_number = models.IntegerField()
    outofhours_phone = models.IntegerField()
    email = models.EmailField()
    disabled_parking = models.BooleanField()
    provider_image = CloudinaryField('image', default='placeholder')
    provider_approved_status = models.IntegerField(choices=PROVIDER_APPROVED_STATUS, default=0)
    likes = models.ManyToManyField(User, realated_name='provider_likes', blank=True)