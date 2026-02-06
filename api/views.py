from django.http import HttpResponse


def index(request):
    res = ["Hi thats a respomse in an object"]
    return HttpResponse(res)
