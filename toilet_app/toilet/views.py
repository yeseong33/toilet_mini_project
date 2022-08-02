from http.client import HTTPResponse
from django.shortcuts import render

def welcome(request):
    return HTTPResponse('Welcome!')
