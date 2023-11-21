from django.shortcuts import render

# Create your views here.

def snow(request):
    return render(request,'snow.html')
