from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.

def index(request):
    return render(request, 'gem/index.html')

def getjson(request):
    return JsonResponse({ 'foo':'bar'})
