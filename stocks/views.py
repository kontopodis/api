from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from stocks.controllers.cacheController import CacheController

CACHE = CacheController()
CACHE.update()
def index(request):

    return HttpResponse("Hi just a long response",CACHE.controller)


def strategies(request):
    return HttpResponse("Hello, world. You're at the strategies page.")


def stock(request, stock_id):
    response = [{'msg':'Stock is not in our Database',
                'data':'none'}]
    for t in CACHE.controller:

        if str(t['id']) == str(stock_id):
            print(t['id'], " - ", stock_id)
            response[0]['data'] = t
            response[0]['msg'] = '200'
    return HttpResponse(response)