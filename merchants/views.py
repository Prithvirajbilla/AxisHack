from django.shortcuts import render
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse,HttpResponseRedirect,Http404,HttpResponseNotFound
import json
import datetime
import urllib


def index(request):
	template = "index.html"
	return render(request,template)

def details(request):
	template = "index.html"
	return render(request,template)

def declarations(request):
	template = "index.html"
	return render(request,template)

def confirmation(request):
	template = "index.html"
	return render(request,template)

def getkit(request):
	template = "index.html"
	return render(request,template)
