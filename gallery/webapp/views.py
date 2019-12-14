from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PhotoForm
from webapp.models import Photo


class PhotosView(ListView):
    template_name = 'index.html'
    model = Photo
    context_object_name = 'photos'


class PhotoDetail(DetailView):
    template_name = 'photo_detail.html'
    model = Photo
    context_object_name = 'photo'


class PhotoCreateView(CreateView):
    template_name = 'photo_create.html'
    model = Photo
    form_class = PhotoForm

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('webapp:index')


class PhotoUpdateView(UpdateView):
    model = Photo
    class_form = PhotoForm
    template_name = 'photo_update.html'
    context_object_name = 'photo'
    fields = ['photo', 'note']

    def get_success_url(self):
        return reverse('webapp:index')


class PhotoDeleteView(DeleteView):
    model = Photo
    success_url = reverse_lazy('webapp:index')


def login_view(request):
    context = {}
    next_page = request.GET.get('next')
    url = request.session.setdefault('url', next_page)
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if url:
                return redirect(url)
            return redirect('webapp:index')
        else:
            context['has_error'] = True
    return render(request, 'login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('webapp:index')
