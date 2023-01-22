from . import views
from django.urls import path

urlpatterns = [
    path('', views.CareProviderList.as_view(), name='careproviderhome'),
    path('care-provider-details/<pk>', views.CareProviderDetail.as_view(),
         name='careproviderdetail'),
]