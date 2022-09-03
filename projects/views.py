from django.shortcuts import render,redirect
from .models import Project
from .forms import *
from django.contrib.auth.decorators import login_required
from .utils import searchProjects


def projects(request):
    projects, search_query = searchProjects(request)
    context={'projects':projects,'search_query': search_query}
    return render(request,'projects/projects.html',context)



def project(request,pk):
    projectobj=Project.objects.get(id=pk)
    context={'project':projectobj}
    return render(request,'projects/single_project.html',context)



@login_required(login_url='loginpage')
def createproject(request):
    profile=request.user.profile
    form=ProjectForm()
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES)
        if form.is_valid:
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/forms.html',context)



@login_required(login_url='loginpage')
def updateproject(request,pk):
    profile=request.user.profile
    project=profile.project_set.all().first()
    form=ProjectForm(instance=project)
    if request.method=='POST':
        form=ProjectForm(request.POST,request.FILES,instance=project)
        if form.is_valid:
            project=form.save(commit=False)
            project.owner=profile
            project.save()
            return redirect('projects')
    context={'form':form}
    return render(request,'projects/forms.html',context)



@login_required(login_url='loginpage')
def deleteproject(request,pk):
    profile=request.user.profile
    project=profile.project_set.all().first()
    if request.method=='POST':
        project.delete()
        return redirect('projects')
    context={'projectt':project}
    return render(request,'delete.html',context)
# Create your views here.
