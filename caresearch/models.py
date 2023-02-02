from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField

PROVIDER_APPROVED_STATUS = ((0, "Pending"), (1, "Approved_careprovider"))

COUNTY_CHOICES = (
    ("CARLOW", "Carlow"), ("CAVAN", "Cavan"),
    ("CLARE", "Clare"), ("CORK", "Cork"),
    ("DONEGAL", "Donegal"), ("DUBLIN", "Dublin"),
    ("GALWAY", "Galway"), ("KERRY", "Kerry"),
    ("KILDARE", "Kildare"), ("KILKENNY", "Kilkenny"),
    ("LAOISE", "Laois"), ("LEITRIM", "Leitrim"),
    ("LIMERICK", "Limerick"), ("LONGFORD", "Longford"),
    ("LOUTH", "Louth"), ("MAYO", "Mayo"),
    ("MEATH", "Meath"), ("MONAGHAN", "Monaghan"),
    ("OFFALY", "Offaly"), ("ROSCOMMON", "Roscommon"),
    ("SLIGO", "Sligo"), ("TIPPERARY", "Tipperary"),
    ("WATERFORD", "Waterford"), ("WESTMEATH", "Westmeath"),
    ("WEXFORD", "Wexford"), ("WICKLOW", "Wicklow"),
)

SPECIALITY_CHOICES = (
    ("ELDERLYCARE", "Elderly Care"), ("GP", "General Practioner"),
    ("CAREWORKER", "Care Worker"), ("HOMECARER", "Home Carer"),
    ("ORTHOPEDICS", "Orthopedics"), ("OCCUPATIONAL", "Occupational Therapist"),
    ("CHIROPODISTS", "Chiropodists"), ("PHYSIOTHERAPY", "Physiotherapy"),
    ("SWIFTCARE", "Swift Medical Care"), ("DEMENTIA", "Dementia Support"),
)

class CareProvider(models.Model):
    careprovider_username = models.CharField(max_length=200, unique=True, primary_key=True)
    business_name = models.CharField(
        max_length=100, blank=False, default="add_business_name"
        )
    type_of_care = models.CharField(max_length=25,
                  choices=SPECIALITY_CHOICES,
                  default="ELDERLY CARE")
    main_contact_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=250)
    county = models.CharField(max_length=9,
                  choices=COUNTY_CHOICES,
                  default="DUBLIN")
    phone_number = models.IntegerField()
    email = models.EmailField()
    disabled_parking = models.BooleanField()
    provider_image = CloudinaryField('image', default='placeholder')
    provider_approved_status = models.IntegerField(choices=PROVIDER_APPROVED_STATUS, default=0)
    likes = models.ManyToManyField(User, related_name='provider_likes', blank=True)

    def __str__(self):
        return self.careprovider_username

    def number_of_likes(self):
        return self.likes.count()


class CareProviderComments(models.Model):

    careprovider = models.ForeignKey(CareProvider, on_delete=models.CASCADE,
                             related_name="careprovider_comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    comment = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date_created']

    def __str__(self):
        return f"Comment {self.comment} by {self.name}"
