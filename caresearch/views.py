from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import DetailView
from .models import CareProvider
from .forms import CareProviderCommentsForm

class CareProviderList(generic.ListView):
    model = CareProvider
    queryset = CareProvider.objects.filter(provider_approved_status=1).order_by('business_name')
    template_name = 'careproviders_list.html'
    paginate_by = 6

class CareProviderDetail(DetailView):
    model = CareProvider
    template_name = 'careprovider_detail.html'
    # def get(self, request, business_name, *args, **kwargs):
    #     queryset = CareProvider.objects.filter(provider_approved_status)
    #     business = get_object_or_404(queryset, business_name=business_name)
    #     careprovidercomments = business.careprovidercomments(approved=True).order_by('-date_created')
    #     likes = False
    #     if business.like.filter(id=self.request.user.id).exists():
    #         likes = True

    #     return render(
    #         request, 
    #         "careprovider_detail.html",
    #         {
    #             "business": business,
    #             "careprovidercomments": careprovidercomments,
    #             "likes": likes
    #         },
    #         )