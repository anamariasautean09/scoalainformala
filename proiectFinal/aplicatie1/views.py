from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm

# Create your views here.
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView
from django.views.generic.detail import DetailView


from aplicatie1.models import Movie


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form':form}
    return render(request, 'aplicatie1/register.html', context)


def loginPage(request):
    context = {}
    return render(request, 'aplicatie1/login.html', context)

class MoviesView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'
    paginate_by = 8
    queryset = model.objects.filter(active=1)
    context_object_name = 'moviesList'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesView, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(active=1)
        return data


class CreateMoviesView(LoginRequiredMixin, CreateView):
    model = Movie
    fields = ['title', 'description', 'release_date', 'duration', 'budget', 'rating', 'poster', 'category', 'language', 'status', 'trailer_url']
    template_name = 'aplicatie1/movies_form.html'


    def get_success_url(self):
        return reverse('movieApplication:lista_filme')



class UpdateMoviesView(LoginRequiredMixin, UpdateView):
    model = Movie
    fields = ['title', 'description', 'release_date', 'duration', 'budget', 'rating', 'poster', 'category', 'language', 'status', 'trailer_url']
    template_name = 'aplicatie1/movies_form.html'

    def get_success_url(self):
        return reverse('movieApplication:lista_filme')



@login_required
def search_movies(request):
    if request.method == "POST":
        searched = request.POST['searched']
        movies = Movie.objects.filter(title__contains=searched)
        return render(request, 'aplicatie1/search_movies.html', {'searched': searched, 'movies': movies})
    else:
        return render(request, 'aplicatie1/search_movies.html', {})

@login_required
def delete_movies(request, pk):
    Movie.objects.filter(id=pk).update(active=0)
    return redirect('movieApplication:lista_filme')

@login_required
def activate_movies(request, pk):
    Movie.objects.filter(id=pk).update(active=1)
    return redirect('movieApplication:lista_filme')


class MoviesInactiveView(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'
    paginate_by = 8
    queryset = model.objects.filter(active=0)
    context_object_name = 'locations'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesInactiveView, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(active=0)
        return data


class MoviesTopRated(LoginRequiredMixin,ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesTopRated, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(status='TOP RATED')
        return data


class MoviesMostWatched(LoginRequiredMixin,ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesMostWatched, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(status='MOST WATCHED')
        return data

class MoviesRecentlyAdded(LoginRequiredMixin,ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesRecentlyAdded, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(status='RECENTLY ADDED')
        return data


class MovieDetail(LoginRequiredMixin, DetailView):
    model = Movie
    template_name = 'aplicatie1/movie_details.html'

    def get_context_data(self, *args, **kargs):
        data = super(MovieDetail, self).get_context_data(*args, **kargs)
        data['moviesL'] = self.model.objects.filter(active=1)
        return data




class MoviesAction(LoginRequiredMixin,ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesAction, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(category='action')
        return data


class MoviesDrama(LoginRequiredMixin,ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesDrama, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(category='drama')
        return data

class MoviesComedy(LoginRequiredMixin,ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesComedy, self).get_context_data( *args, **kargs)
        data['moviesL'] = self.model.objects.filter(category='comedy')
        return data


class MoviesRomance(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesRomance, self).get_context_data(*args, **kargs)
        data['moviesL'] = self.model.objects.filter(category='romance')
        return data


class MoviesAdventure(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesAdventure, self).get_context_data(*args, **kargs)
        data['moviesL'] = self.model.objects.filter(category='adventure')
        return data


class MoviesLove(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesLove, self).get_context_data(*args, **kargs)
        data['moviesL'] = self.model.objects.filter(category='love')
        return data

class MoviesCartoons(LoginRequiredMixin, ListView):
    model = Movie
    template_name = 'aplicatie1/movies_index.html'

    def get_context_data(self, *args, **kargs):
        data = super(MoviesCartoons, self).get_context_data(*args, **kargs)
        data['moviesL'] = self.model.objects.filter(category='cartoons')
        return data

