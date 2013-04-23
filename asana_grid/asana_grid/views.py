import sys

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response, redirect
from django.template import loader, Context, RequestContext
from django.core.urlresolvers import reverse

def home(request):
    return HttpResponse("hello world")
