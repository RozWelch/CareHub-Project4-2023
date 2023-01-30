from django.db import models
from django.contrib.auth.models import User, AbstractUser
from cloudinary.models import CloudinaryField

PROVIDER_APPROVED_STATUS = ((0, "Pending"), (1, "Approved_careprovider"))


class CareProvider(models.Model):
    careprovider_username = models.CharField(max_length=200, unique=True, primary_key=True)
    password = models.CharField(max_length=20)
    business_name = models.CharField(max_length=200, unique=True)
    type_of_care = models.CharField(max_length=250, null=True)
    main_contact_name = models.CharField(max_length=100)
    address_line_1 = models.CharField(max_length=250)
    county = models.CharField(max_length=100)
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


class CareSeeker(models.Model):
    careseeker_username = models.CharField(max_length=200, unique=True, primary_key=True)
    password = models.CharField(max_length=20)
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    phone_number = models.IntegerField()
    email = models.EmailField()
    needs_assistance = models.BooleanField()
    disabled_parking = models.BooleanField()

    def __str__(self):
        return self.careseeker_username


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
