from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'npm' : '2406350021',
        'name': 'Randuichi Touya',
        'class': 'PBP D'
    }

    return render(request, "home.html", data)