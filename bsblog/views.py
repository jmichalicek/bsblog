# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views.decorators.cache import cache_control, cache_page
from django.http import Http404

from taxonomy import models as taxonomy
from models import Post, Category


from time import strptime

@cache_control(max_age=3600)
@cache_page(60 * 15)
def index(request,page=0):
    start_index = int(page) * 5;
    end_index = start_index + 5;
    post_list = Post.objects.filter(published=True).order_by('-created_date')[start_index:end_index]

    next_page = int(page) + 1
    previous_page = int(page) - 1
    if previous_page == -1:
        previous_page = 0

    return render_to_response(
        'cms/index.html',
        {'post_list': post_list,
         'next_page': next_page,
         'previous_page': previous_page},
        context_instance=RequestContext(request)
        )

@cache_control(max_age=3600)
@cache_page(60 * 15)
def item(request,year,month,day,slug):
    post = get_object_or_404(Post,slug=slug)

    previous = Post.objects.filter(id__lt=post.id).order_by('-id')[:1]
    next_post = Post.objects.filter(id__gt=post.id).order_by('id')[:1]
    
    return render_to_response(
        'cms/detail.html',
        {'post': post, 'previous': previous, 'next': next_post},
        context_instance=RequestContext(request)
        )

def list_posts(request,year,month):
    posts = Post.objects.filter(created_date__year=year,created_date__month=strptime(month,'%b').tm_mon).order_by('-created_date')

    return render_to_response(
        'cms/list.html',
        {'posts':posts},
        context_instance=RequestContext(request)
        )

def posts_by_category(request, category):
    category = get_object_or_404(Category, name=category)
    posts = Post.objects.filter(category=category, published=True)


def projects(request):
    category = Category.objects.get(name="Projects")
    projects = Post.objects.filter(published=1, category=category)
    taxonomy_group = taxonomy.TaxonomyGroup.objects.get(name="Programming Languages")
    
    return render_to_response(
        'cms/projects.html',
        {'projects': projects,
         'taxonomy_group': taxonomy_group},
        context_instance=RequestContext(request)
        )    
