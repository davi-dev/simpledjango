from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	return HttpResponse('Welcome to the website. <a href="about">Go To About Page.</a>')

def about(request):
	return HttpResponse('Here is the about page. <a href="/rango">Go To Home Page.</a>')