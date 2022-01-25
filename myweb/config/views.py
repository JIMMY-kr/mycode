from django.shortcuts import render

def home(request):
    # template => html code
    return render(request, 'index.html')