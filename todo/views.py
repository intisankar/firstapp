from django.shortcuts import render

from .models import sample

# Create your views here.
def index(request):
	todo_items = sample.objects.order_by('id')
	context = {'todo_items':todo_items}
	return render(request,'todo/sample.html',context)
