from django.shortcuts import render

from models import Note

def home(request):
    context = {
        'notitas': Note.objects.all(),
    }
    return render(request, 'home.html', context)