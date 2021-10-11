from django.http import HttpResponse 
from django.shortcuts import render
from django.template.loader import get_template
from .forms import ContactForm
from blog.models import BlogPost
"""
	template_name = "title.txt"
	template_obj = get_template(template_name)
	rendered_item = template_obj.render(context)
	rendered_string = template_obj.render(context)
	print(rendered_string)# terminal
	#doc = "<h1>{title}</h1>".format(title=my_title)
	#django_rendered_doc = "<h1>{{title}}</h1>".format(title=my_title)
	return render(request,"hello_world.html",{"title":rendered_string})
	
	
		if request.user.is_authenticated:
		context = {"title":my_title,"my_list":[1,2,3,4,5]}
	"""
def home_page(request):
	my_title = "Hello there ..."
	qs = BlogPost.objects.all()[:5]
	context = {"title":"Welcome to try django",'blog_list':qs}
	return render(request,"home.html",context)


def about_page(request):
	return render(request,"about.html",{"title":"About us"})

def contact_page(request):
	#return HttpResponse("<h1> Contact Us <h1>")
	#print(request.POST)
	form = ContactForm(request.POST or None)
	if form.is_valid():
		print(form.cleaned_data)
		form=ContactForm()
	context = {
		"title": "Contact us", "form": form
	}
	return render(request,"form.html",context)

def example_page(request):
	context       = {"title":"Exemple"}
	template_name = "hello_world.html"
	template_obj  = get_template(template_name)
	rendered_item = template_obj.render(context)
	return HttpResponse(template_obj.render(context))