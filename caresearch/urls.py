from . import views
from django.urls import path
from .views import (
    AddProvider, CareProviderDetail, UpdateProvider, DeleteProvider
)

urlpatterns = [
    path('', views.IndexPage, name='home'),
    path('list', views.CareProviderList.as_view(), name='careproviderhome'),
    path('care-provider-details/<pk>', views.CareProviderDetail.as_view(),
         name='careproviderdetail'),
    path('addcareprovider/', AddProvider.as_view(), name='add_provider'),
    path('editcareprovider/<pk>', UpdateProvider.as_view(), name='update_provider'),
    path('deletecareprovider/<pk>', DeleteProvider.as_view(), name='delete_provider')
]
