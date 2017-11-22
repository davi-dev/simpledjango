from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
	context_dict = {'boldmessage': 'Some bold message here...'}
	return render(request, 'rango/index.html', context= context_dict)


def about(request):
	return HttpResponse('Here is the about page. <a href="/rango">Go To Home Page.</a>')