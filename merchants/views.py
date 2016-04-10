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
	template = "step2.html"
	return render(request,template)

def declarations(request):
	template = "declarations.html"
	return render(request,template)

def confirmation(request):
	template = "confirmation.html"
	return render(request,template)

def getkit(request):
	template = "download.html"
	return render(request,template)
