from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(
    request: str
)-> HttpResponse:
    return HttpResponse('<h1>Hello ali</h1>')