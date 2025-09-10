from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        'name': 'Randuichi Touya',
        'class': 'PBP D',
    }

    return render(request, "home.html", data)