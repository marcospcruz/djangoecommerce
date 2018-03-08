from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
def index(request):
	#return HttpResponse('Hello World!!!')
	texts = [
		'Marcos ',
		'Pereira ',
		'da ',
		'Cruz '
	]
	context = {
		'title':'Django E-commerce Rendered Title',
		'texts': texts
	}
	return render(request,'index.html',context)
"""
def index(request):
	return render(request,'index.html')
	
def contact(request):
	return render(request, 'contact.html')
	
def product_list(request):
	return render(request,'product_list.html')					  

def product(request):
	return render(request,'product.html')
	

	