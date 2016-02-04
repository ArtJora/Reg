from django.http.response import HttpResponse, Http404
from django.template.loader import get_template
from django.shortcuts import render_to_response, redirect
from news.models import Article, Comments
from django.core.exceptions import ObjectDoesNotExist
from forms import CommentForm, NewsForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.utils import timezone




# Create your views here.


def news(request):
    news_form = NewsForm
    args = {}
    args.update(csrf(request))
    args['form'] = news_form
    args['articles'] = Article.objects.all()
    args['user'] = auth.get_user(request)
    return render_to_response('articles.html', args)

def addnews(request):
    news_form = NewsForm
    args = {}
    args.update(csrf(request))
    args['form'] = news_form
    args['articles'] = Article.objects.all()
    args['user'] = auth.get_user(request)
    return render_to_response('addnews.html', args)

    # return render_to_response('articles.html', {'articles': Article.objects.all(), 'user': auth.get_user(request) })



def news_item(request, article_id=1):
    comment_form = CommentForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['form'] = comment_form
    args['user'] = auth.get_user(request)
    return render_to_response('article.html', args)

def addlike(request, article_id):
    try:
        if article_id in request.COOKIES:
            redirect('/')
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(article_id,"test")
            return response
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/news/')

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/news/%s/' % article_id)

def savenews(request):
    if request.POST and ("pause" not in request.session):
        form = NewsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            now = timezone.now()
            comment.article_date = now

            # comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            # request.session.set_expiry(60)
            # request.session['pause'] = True
    return redirect('/news/')

