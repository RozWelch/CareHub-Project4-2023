from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
    )
from .models import CareProvider, CareProviderComments
from .forms import CareProviderCommentsForm, ProviderForm, ReviewForm
from django.urls import reverse, reverse_lazy
from django.contrib import messages


def IndexPage(request):
    return render(request, "index.html")


class CareProviderList(generic.ListView):
    model = CareProvider
    queryset = (
        CareProvider.objects.filter(provider_approved_status=1).
        order_by('business_name')
    )
    template_name = 'careproviders_list.html'
    paginate_by = 6


class CareProviderDetail(View):

    def get(self, request, pk, *args, **kwargs):
        queryset = CareProvider.objects.filter(provider_approved_status=1)
        post = get_object_or_404(queryset, pk=pk)
        comments = (
            post.careprovider_comments.filter(approved=True).
            order_by('-date_created')
        )
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
        comments = (
            post.careprovider_comments.filter(approved=True).order_by(
                '-date_created')
        )
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


class AddProvider(generic.CreateView):
    # Allows logged in users to create a Care Provider
    model = CareProvider
    success_url = reverse_lazy('careproviderhome')
    form_class = ProviderForm
    template_name = 'careproviders_add_details.html'
    success_message = (
        "Care provider created successfully and is awaiting approval"
    )

    def form_valid(self, form):
        # called when a valid form is posted, sets signed in user as author
        form.instance.author = self.request.user
        messages.success(self.request, self.success_message)
        return super().form_valid(form)


class UpdateProvider(UpdateView):
    # allows signed in Care Provider to update their details
    model = CareProvider
    success_url = reverse_lazy('careproviderhome')
    template_name = 'careproviders_edit.html'
    form_class = ReviewForm
    success_message = "Your care provider has been successfully updated"

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser()
        messages.success(self.request, self.success_message)


class DeleteProvider(DeleteView):
    # allows signed in Care Provider to delete their details
    model = CareProvider
    success_url = reverse_lazy('careproviderhome')
    template_name = 'careproviders_delete.html'
    success_message = "Your care provider has been successfully deleted"

    def test_func(self):
        return self.request.user == self.get_object().author or self.request.user.is_superuser()
        messages.success(self.request, self.success_message)
