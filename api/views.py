from django.http import HttpResponse


def index(request):
    res = ['response',"Hi thats a respomse in an object"]
    return HttpResponse(res)
