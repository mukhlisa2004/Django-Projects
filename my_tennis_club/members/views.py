from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic import TemplateView




def  hello (request):
    return HttpResponse('Hello World !')

def about(request):
    '''  calling from def function this  template files '''
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

class Home_Viev(TemplateView):
    template_name = 'home.html'




# Create your views here.
