from django.shortcuts import render
from .models import Mark
from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf
# Create your views here.
def index(request):
    if request.method == "POST":
        if request.POST['sname'] and request.POST['rno'] and request.POST['sub1'] and request.POST['sub2'] and request.POST['sub3'] :
            obj = Mark()
            obj.name = request.POST['sname']
            obj.Roll = request.POST['rno']
            obj.sub_1 = request.POST['sub1']
            obj.sub_2 = request.POST['sub2']
            obj.sub_3 = request.POST['sub3']
            obj.percent = (int(obj.sub_1) + int(obj.sub_2) + int(obj.sub_3))/3

            obj.save()

    return render(request, 'index.html')


def pdf(request):

    obj = Mark.objects.all()
    return render(request,'details.html',context={'items':obj})


def get(request):
    if request.method == "POST":
        obj = Mark.objects.all().filter(name=request.POST['name'])
        if obj:
            pdf = render_to_pdf('details.html', context_dict={'items':obj})
            return HttpResponse(pdf, content_type='application/pdf')
        return HttpResponse("name not found")
    return render(request,'form.html')
