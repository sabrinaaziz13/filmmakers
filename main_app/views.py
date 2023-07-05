from django.shortcuts import render, redirect
from django.views import View 
from .models import Director, Movie
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.base import TemplateView 
from django.views.generic import DetailView
from django.urls import reverse


class DirectorCreate(CreateView):
    model = Director
    fields = ['name', 'img', 'bio', 'verified_director']
    template_name = "director_create.html"
    def get_success_url(self):
        return reverse('director_detail', kwargs={'pk': self.object.pk})
    
class DirectorUpdate(UpdateView):
    model = Director
    fields = ['name', 'img', 'bio', 'verified_director']
    template_name = "director_create.html"
    def get_success_url(self):
        return reverse('director_detail', kwargs={'pk': self.object.pk})
    
class DirectorDelete(DeleteView):
    model = Director
    template_name = "director_delete_confirmation.html"
    success_url = "/directors/"

class MovieCreate(View):

    def post(self, request, pk):
        title = request.POST.get("title")
        year = request.POST.get("year")
        director = Director.objects.get(pk=pk)
        Movie.objects.create(title=title, year=year, director=director)
        return redirect('director_detail', pk=pk)
    
class MovieUpdate(UpdateView):
    model = Movie
    fields = ['title', 'img', 'year', 'synopsis', 'director']
    template_name = "movie_update.html"
    def get_success_url(self):
        return reverse('movie_detail', kwargs={'pk': self.object.pk})
    
class MovieDelete(DeleteView):
    model = Movie
    template_name = "movie_delete_confirmation.html"
    success_url = "/movies/"

class Home(View):
    def get(self, request):
        return HttpResponse("Filmmakers Home")
    
class About(View):
    def get(self, request):
        return HttpResponse("Filmmakers About")
    
class Home(TemplateView):
    template_name = "home.html"
    
class About(TemplateView):
    template_name = "about.html"

class MovieList(TemplateView):
    template_name = "movie_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        title = self.request.GET.get("title")
        if title != None:
            context["movies"] = Movie.objects.filter(title__icontains=title)
            context["header"] = f"Searching for {title}"
        else:
            context["movies"] = Movie.objects.all() 
            context["header"] = "Trending Movies"

        return context


class DirectorList(TemplateView):
    template_name = "director_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context["directors"] = Director.objects.filter(name__icontains=name)
            context["header"] = f"Searching for {name}"
        else:
            context["directors"] = Director.objects.all() 
            context["header"] = "Trending Directors"

        return context

class DirectorDetail(DetailView):
    model = Director
    template_name = "director_detail.html"

class MovieDetail(DetailView):
    model = Movie
    template_name = "movie_detail.html"