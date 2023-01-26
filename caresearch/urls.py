from . import views
from django.urls import path

urlpatterns = [
    path('', views.IndexPage, name='home'),
    path('list', views.CareProviderList.as_view(), name='careproviderhome'),
    path('care-provider-details/<pk>', views.CareProviderDetail.as_view(),
         name='careproviderdetail'),
]
