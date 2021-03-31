from django.urls import path
from . import views

urlpatterns = [
    path('' , views.index , name='index'),
    path('write' , views.ArticleWrite , name='write'),
    path('articles' , views.AllArticles , name='all'),
    path('article/<int:article_id>',views.ArticleDetails , name='article_details'),
    path('my_articles/',views.UserArticles, name='user_articles'),
    path('update/<int:article_id>',views.UpdateArticle,name='update')
]
