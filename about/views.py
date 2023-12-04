from django.shortcuts import render

# Create your views here.
def about(response):
    return render(response, 'about_index.html')