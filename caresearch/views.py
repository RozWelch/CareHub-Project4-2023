from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import DetailView
from .models import CareProvider
from .forms import CareProviderCommentsForm

def IndexPage(request):
    return render(request, "index.html")

class CareProviderList(generic.ListView):
    model = CareProvider
    queryset = CareProvider.objects.filter(provider_approved_status=1).order_by('business_name')
    template_name = 'careproviders_list.html'
    paginate_by = 6

class CareProviderDetail(DetailView):
    model = CareProvider
    template_name = 'careprovider_detail.html'

    def get(self, request, pk, *args, **kwargs):
        queryset = CareProvider.objects.filter(provider_approved_status=1)
        post = get_object_or_404(queryset, pk=pk)
        careprovidercomments = post.careprovidercomments.filter(approved=True).order_by('-date_created')
        likes = False
        if post.likes.filter(id=self.request.user.id).exists():
            likes = True

        return render(
            request, 
            "careprovider_detail.html",
            {
                "business": business,
                "careprovidercomments": careprovidercomments,
                "likes": likes,
                "comment_form": CommentForm()
            },
            )