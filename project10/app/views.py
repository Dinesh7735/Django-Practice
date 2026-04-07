from django.shortcuts import render

# Create your views here.
def conditions(request):
    d = {'name':'Ashish', 'age':15}
    return render(request,'conditions.html',d)