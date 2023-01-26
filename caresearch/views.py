from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import DetailView
from .models import CareProvider, CareProviderComments
from .forms import CareProviderCommentsForm


def IndexPage(request):
    return render(request, "index.html")


class CareProviderList(generic.ListView):
    model = CareProvider
    queryset = CareProvider.objects.filter(provider_approved_status=1).order_by('business_name')
    template_name = 'careproviders_list.html'
    paginate_by = 6


class CareProviderDetail(View):

    def get(self, request, pk, *args, **kwargs):
        queryset = CareProvider.objects.filter(provider_approved_status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.careprovider_comments.filter(approved=True).order_by('-date_created')
        likes = False
        if post.likes.filter(id=self.request.user.id).exists():
            likes = True

        return render(
            request,
            "careprovider_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "likes": likes,
                "comment_form": CareProviderCommentsForm()
            },
            )

    def post(self, request, pk, *args, **kwargs):
        queryset = CareProvider.objects.filter(provider_approved_status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = post.careprovider_comments.filter(approved=True).order_by('-date_created')
        likes = False
        if post.likes.filter(id=self.request.user.id).exists():
            likes = True

        comment_form = CareProviderCommentsForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.careprovider = post
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CareProviderCommentsForm()

        return render(
            request,
            "careprovider_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "likes": likes,
                "comment_form": CareProviderCommentsForm()
            },
            )
