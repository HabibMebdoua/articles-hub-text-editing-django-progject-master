from django.urls import path
from . import views
urlpatterns = [
    path('' , views.Blog , name='blog'),
    path('blogs' , views.AllBlogs , name='all_blogs'),
    path('blog/<int:blog_id>' , views.BlogDetails , name='blog_details')
]