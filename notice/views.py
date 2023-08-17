from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def notice_web01(reqeust):
    return HttpResponse('<h1> notice_web01 </h1>')

def notice_web02(reqeust):
    return HttpResponse('<h1> notice_web02 </h1>')