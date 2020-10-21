from django.shortcuts import render
from django.http import HttpResponse
from se.documents import CarDocument


# def index(request):
#     return HttpResponse("Hello, world. You're at the search engine index.")


def se(request):
    q = request.GET.get('q')
    if q:
        cars = CarDocument.search().query("match", description=q)
    else:
        cars = ''
    return render(request, 'se/se.html', {'cars': cars})
