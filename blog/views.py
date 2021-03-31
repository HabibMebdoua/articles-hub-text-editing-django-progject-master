from django.shortcuts import render,get_object_or_404
from .models import BlogModel
# Create your views here

def Blog(request):
    return render(request , 'blog/blog.html')


def AllBlogs(request):
    blogs = BlogModel.objects.all()
    context = {
            'blog':blogs
        }

    return render(request , 'blog/all_blogs.html' , context)

def BlogDetails(request , blog_id):
    blog = get_object_or_404(BlogModel , pk=blog_id)
    blog.views =+1
    blog.save()

    context={
        'blog':blog
    }

    return render(request , 'blog/blog_details.html' , context)
