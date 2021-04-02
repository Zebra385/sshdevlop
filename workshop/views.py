from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.

class AccueilView(TemplateView):
    """ That class to get the accueil page"""
    template_name = "workshop/accueil.html"

class AboutView(TemplateView):
    """ That class to get the about page"""
    template_name = "workshop/about.html"

class WorkView(TemplateView):
    """ That class to get the work page"""
    template_name = "workshop/work.html"

class Work01View(TemplateView):
    """ That class to get the work01 page"""
    template_name = "workshop/work01.html"

class Work02View(TemplateView):
    """ That class to get the work02 page"""
    template_name = "workshop/work02.html"

class Work03View(TemplateView):
    """ That class to get the work03 page"""
    template_name = "workshop/work03.html"
