from urllib import request

from django.shortcuts import render, redirect
from .models import Trainee
from .forms import TraineeFormModel
from django.views.generic import DeleteView
from django.views import View

# Create your views here.

def TraineeList(request):
    trainees = Trainee.objects.all()
    return render(request, 'trainee/list.html', {'trainees': trainees})

def TraineeDetail(request, id):
    trainee = Trainee.objects.get(id=id)
    return render(request, 'trainee/detail.html', {'trainee': trainee})

class TraineeCreate(View):
    def get(self, request):
        form = TraineeFormModel()
        return render(request, 'trainee/create.html', {'form': form})  
    
    def post(self, request):
        form = TraineeFormModel(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('traineeList')
        return render(request, 'trainee/create.html', {'form': form})


class TraineeUpdate(View):
    def get(self, request, id):
        trainee = Trainee.objects.get(id=id)
        form = TraineeFormModel(instance=trainee)
        return render(request, 'trainee/update.html', {'form': form})  
    
    def post(self, request, id):
        trainee = Trainee.objects.get(id=id)
        form = TraineeFormModel(request.POST, instance=trainee)
        if form.is_valid():
            form.save()
            return redirect('traineeList')
        return render(request, 'trainee/update.html', {'form': form})
    

class TraineeDelete(DeleteView):
    model = Trainee
    template_name = 'trainee/delete.html'
    success_url = '/trainee/'