from django.shortcuts import render
from .models import Post
# from django.http import HttpResponse

# Create your views here.
# def hello(request):
# 	return HttpResponse("<h1>Hello world !</h1>")

def hello(request):
	#query data from model
	data = Post.objects.all()  # เป็นการ query ข้อมูลจากตัว model Post
	return render(request, 'index.html', {'posts': data})

def page1(request):
	return render(request, 'page1.html')
 
def createForm(request):
	return render(request, 'form.html')

def addBlog(request):
	# name = request.GET['name']
	# description = request.GET['description']   # วิธีการส่งค่ามาแสดงผลนะ0
	name = request.POST['name']
	description = request.POST['description']   # วิธีการส่งค่ามาแสดงผลนะ
	return render(request, 'result.html', {'name': name, 'description':description})

 

