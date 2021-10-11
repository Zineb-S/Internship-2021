from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, get_object_or_404,redirect
from django.http import Http404 
# Create your views here.
from .models import BlogPost
from .forms import BlogPostForm, BlogPostModelForm
from django.contrib.auth.decorators import login_required
#from django.utils import timezone
# request -> django -> response

# CRUD

# GET -> Retrieve / list

# POST -> Create / Update / DELETE

# Create Retrieve Update Delete


def blog_post_list_view(request):
	#list out objects
	# search
	#now = timezone.now()
	qs = BlogPost.objects.all().published() # queryset -> list of python objects # published is cutom query set cant do all.published
	#qs = BlogPost.objects.filter(publish_date__lte=now)
	# qs = BlogPost.objects.filter(title__icontains='hello')
	if request.user.is_authenticated:
		my_qs = BlogPost.objects.filter(user=request.user)
		qs = (qs | my_qs).distinct()
	template_name = 'blog/list.html'
	context = { 'object_list' :qs}
	return render(request, template_name, context)


@login_required
@staff_member_required
def blog_post_create_view(request):
	#create objects
	# ? use forms
	form= BlogPostModelForm(request.POST or None,request.FILES or None)
	if form.is_valid():
		# print(form.cleaned_data)
		# title = form.cleaned_data['title']
		obj = form.save(commit=False)
		obj.title = form.cleaned_data.get("title")#+"0"
		obj.user = request.user
		obj.save()
		form = BlogPostModelForm()
	template_name = 'form.html'
	context = {'form': form}
	return render(request, template_name, context)


"""
obj = BlogPost.objects.create(**form.cleaned_data)
obj = BlogPost.objects.create(title=title)
#obj2= OtherModel.objects.create(title=title)
=======
obj = BlogPost()
obj.title = title
obj.save() 
"""
def blog_post_detail_view(request,slug): #retrieve
	# 1 object -> detail view
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/detail.html'
	context = {"object": obj}  # {"title":obj.title}
	return render(request, template_name, context)

@staff_member_required
def blog_post_update_view(request,slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	form = BlogPostModelForm(request.POST or None,instance=obj)
	if form.is_valid():
		form.save()
	template_name = 'form.html'
	context = {"title":f"Update{obj.title}","form": form,}  # {"title":obj.title}
	return render(request, template_name, context)

@staff_member_required
def blog_post_delete_view(request,slug):
	obj = get_object_or_404(BlogPost, slug=slug)
	template_name = 'blog/delete.html'
	if request.method == "POST":
		obj.delete()
		return redirect("/blog")
	context = {"object": obj}  # {"title":obj.title}
	return render(request, template_name, context)


"""
def blog_post_detail_page(request,slug):
	#print("DJANGO SAYS " , request.method,request.path,request.user)
	#print(post_id.__class__)
	obj = get_object_or_404(BlogPost,slug=slug)
	template_name = 'blog_post_detail.html'
	context = {"object": obj}  # {"title":obj.title}
	return render(request, template_name, context)
"""
"""
slug=slug was id=post_id
try:
	obj = BlogPost.objects.get(slug=slug) # query -> database -> data -> django renders it
except BlogPost.DoesNotExist:
	raise Http404
except ValueError:
	raise Http404


querySet = BlogPost.objects.filter(slug=slug)
if querySet.count() == 0:
	raise Http404
obj = querySet.first()

"""

# change models -> makemigrations -> migrate