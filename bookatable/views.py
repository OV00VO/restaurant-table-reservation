from django.shortcuts import render
#from django.http import generic
from . models import Post

# Create your views here.
def index(request):
    context = {}
    return render(request, 'index.html', context)

def menu(request):
    context = {}
    return render(request, 'menu.html', context)

def reservation(request):
    context = {}
    return render(request, 'reservation.html', context)

def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

# class PostList(generic.ListView):
#    queryset = Post.objects.filter(status=1)
#    template_name = "restaurant/index.html"
#    paginate_by = 6