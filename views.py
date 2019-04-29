from django.shortcuts import render,redirect
from django.http import HttpResponse
from app1.models import Employee


def allData():
	emp=Employee.objects.all()
	context={'emp' : emp}
	return context

def index(request):
	return render(request,'app1/index.html')
def about(request):
	return render(request,'app1/about.html')

def contact(request):
	return render(request,'app1/contact.html')

def view(request):
    return render(request,'app1/portal.html',allData())

def add(request):
	return render(request,'app1/portal.html',{"a":'ac'})

def create(request):
    emp=Employee(eid=request.POST['eid'],ename=request.POST['ename'],contact=request.POST['contact'],designation=request.POST['designation'])
    emp.save()
    return redirect('/')
def edit(request,id):
	emp=Employee.objects.get(eid=id)
	context={'emp' : emp}
	return render(request,'app1/edit.html',context)

def update(request,id):
	emp=Employee.objects.get(eid=id)
	emp.ename=request.POST['ename']
	emp.contact=request.POST['contact']
	emp.designation=request.POST['designation']
	emp.save()
	return render(request,'app1/index.html',allData())


def delete(request,id):
	emp=Employee.objects.get(eid=id).delete()
	return render(request,'app1/portal.html',allData())