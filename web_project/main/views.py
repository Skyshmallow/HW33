from django.shortcuts import render

# Create your views here.
# Можно и без индекса
def index(request):
    return render(request, 'main/index.html')

def about(request):
    return render(request, 'main/about.html')