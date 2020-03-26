from django.shortcuts import render
from .models import Mark

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
            obj.percent = (obj.sub_1 + obj.sub_2 + obj.sub_3)/3

            obj.save()

    return render(request, 'index.html')

