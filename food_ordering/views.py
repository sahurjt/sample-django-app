from django.shortcuts import render
from django.http import HttpResponse


# test view
def test(request):
    return HttpResponse('Server is Up')


def index(req):
    return render(req, 'index.html')
