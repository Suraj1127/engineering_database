from django.shortcuts import render
from .models import Record

# Create your views here.
def data(request):
	posts = Record.objects.order_by('name')
	return render(request, 'database/list.html', {'posts':posts})