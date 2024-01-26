from django.shortcuts import render
#from django.http import HttpResponse
#test1 virtual env

posts = [
    {
        'name': 'kru',
        'school': 'bit',
        'college': 'mit',
        'dob': '18th jan 2000',
    },
    {
        'name': 'pru',
        'school': 'ait',
        'college': 'yit',
        'dob': '19th jan 1999',
    }
]


# Create your views here.

def home(request):
    context = {
        'title': 'Home',
        'posts': posts,
    }
        
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html',{'title':'About'})



