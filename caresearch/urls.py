from . import views
from django.urls import path

urlpatterns = [
    path('', views.CareProviderList.as_view(), name='careproviderhome')
]