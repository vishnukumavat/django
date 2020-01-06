from django.shortcuts import render
from django.http import HttpResponse
from resume.settings import BASE_DIR
import os
from django.urls import resolve
from .models import User_Data
from django.views.generic import View
from builder.utils import render_to_pdf
from django.template.loader import get_template


# Create your views here.

# Global varialble
path = BASE_DIR+'\HTML_files\Templates'
dirListing = os.listdir(path)
resumeTemplates = []
selected_template = []
printer = []
for item in dirListing:
    if ".html" in item:
        resumeTemplates.append(item)


class d_creat():
    def __init__(self,tname,nme,ag):
        dictionary = {'template_name':tname , 'name':nme , 'age':ag}
        printer.append(dictionary)

def index(request):
    return render(request, 'index.html')


def choose_templates(request):
    return render(request, 'ChooseTemplates.html',{'list':resumeTemplates})


def Collector(request):
    for items in resumeTemplates:
        if items in request.POST:
            selected_template.append(items)
    return render(request, 'Base.html')

def view_resume(request):

    i = 0
    while i <= len(selected_template)-2:
        selected_template.pop(i)
    template_selector = 'Templates/'+selected_template[0]

    nm = request.POST['name']
    ag = request.POST['age']

    dcreate = d_creat(template_selector,nm,ag)

    d = User_Data(name=nm,age=ag)
    d.save()
    
    return render(request, template_selector, {'name':nm , 'age':ag})

def generate_view(request, *args, **kwargs):

    i = 0
    while i <= len(printer)-2:
        printer.pop(i)

    dic = printer[0]
    context = {'name':dic['name'], 'age':dic['age']}

    pdf = render_to_pdf(dic['template_name'], context)
    return pdf
