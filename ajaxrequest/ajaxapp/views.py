from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from .models import Task
from django.views import View


class PostFbView(View):
    def post(self, request):
        print(request.POST)
        title=request.POST.get('title')
        dec=request.POST.get('description')

        task = Task.objects.create(title=title,description=dec)

        data = {}
        data['title'] = task.title
        data['description'] = task.description
        data['id'] = task.id

        

        return JsonResponse(data)

    def get(self, request):
        tasklist=Task.objects.all()
        return render(request,'index.html',{'task':tasklist})



