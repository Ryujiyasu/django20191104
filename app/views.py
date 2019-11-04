from django.shortcuts import render
from .forms import AttendanceForm
import datetime
from .models import Worker
# Create your views here.


def index(request):

    if request.method=="POST":
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance=form.save(commit=False)
            attendance.date=datetime.datetime.today()
            attendance.worker = Worker.objects.get(id=1)
            print(attendance)
            attendance.save()
    form = AttendanceForm()
    params={

        'form':form

    }
    return render(request,'app/index.html',params)