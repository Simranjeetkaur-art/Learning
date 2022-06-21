from django.http import HttpResponse

# Create your views here.
def login(request):
    return HttpResponse("H. world")
def login1(request):
    return HttpResponse("H1. world")