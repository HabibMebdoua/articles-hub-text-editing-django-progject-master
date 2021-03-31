from django.shortcuts import render,redirect,get_object_or_404
from .forms import ArticleForm
from .models import Article
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView
# Create your views here.

def index(request):

    return render(request , 'articles/index.html')

@login_required
def ArticleWrite(request):
    form = ArticleForm()
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.owner = request.user
            article.save()
            return redirect('index')
        else :
            ArticleForm()
    context = {
        'form':form
    }

    return render(request , 'articles/write.html' , context)

def AllArticles(request):
    articles = Article.objects.all()
    title =None
    if 'searchname' in request.GET:
        title = request.GET['searchname']
        if title : 
            articles = articles.filter(title__icontains=title)
    
    context = {
        'article':articles
    }

    return render(request , 'articles/all.html' , context)
    
@login_required
def ArticleDetails(request , article_id):
    article = get_object_or_404(Article,pk=article_id)

    article.views =+1
    article.save()
    
    context = {
        'article':article
    }
    return render(request , 'articles/article_details.html' , context)

@login_required
class UpdateArticle(UpdateView):
    model = Article
    fields = ['title','content']
    template_name = 'articles/update_article.html'
    pk_url_kwarg = 'article_id'
    context_object_name = 'article'

    def form_valid(self , form):
        post = form.save()
        post.save()


@login_required
def UserArticles(request):
    article = Article.objects.all()
   
    context = {
        'article':article
    }
    return render(request , 'articles/user_articles.html' , context)



