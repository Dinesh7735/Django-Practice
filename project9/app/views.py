from django.shortcuts import render

# Create your views here.
def jinjaPrint(request):
    d = {'Name' : 'Ashok', 'age' : 24}
    return render(request,'jinjaPrint.html',d)