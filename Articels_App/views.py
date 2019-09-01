from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from Articels_App.forms import (ArticleForm , UserForm, CommentForm)
from Articels_App.models import (Article , Comment , Sys_user)
from django.views.generic import (TemplateView , DeleteView ,
                                  DetailView ,ListView,
                                  CreateView , UpdateView)
from django.urls import reverse_lazy , reverse
from django.contrib.auth import authenticate, login as dj_login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# Create your views here.
class index(TemplateView):
    template_name = 'Home/index.html'

class ArticleListView(ListView):
    template_name = 'Articles/article_list_temp.html'
    queryset = Article.objects.all()
    model = Article
    context_object_name = 'articles'

class ArticleCreateView(CreateView):
    template_name = 'Articles/create_article_temp.html'
    model = Article
    form_class = ArticleForm


class ArticleDetailView(DetailView):
    template_name = 'Articles/article_detail_temp.html'
    queryset = Article.objects.all()
    model = Article
    context_object_name = 'articles_detail'



def comment_to_article(request , pk):
    art = get_object_or_404(Article , pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save(commit = False)
            form.art = art
            form.save()
            return HttpResponseRedirect(reverse('Art:ArticleList'))
    else:
        form = CommentForm()
    return render(request , 'Articles/comment_temp.html' , {'form' : form})
