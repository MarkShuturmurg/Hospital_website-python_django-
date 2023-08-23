from django.shortcuts import render

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'MEDC/home.html', context)

def profile(request):
    return render(request, 'MEDC/profile.html')

def appointment(request):
    return render(request, 'MEDC/appointment.html')

def account(request):
    return render(request, 'MEDC/account.html')

# Create your views here.
