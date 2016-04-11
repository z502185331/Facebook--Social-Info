from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse
from django.http.response import HttpResponse, Http404
from models import *
from Helper import *

# Create your views here.

def index_mypost(request):
    '''
    A function to login and redirect to index page
    Showing all the personal posts including the shared posts
    '''
    if not 'username' in request.POST or not request.POST['username']:
        raise Http404;
    
    username = request.POST['username']
    
    # Check the username has been registered
    if not isRegistered(username):
        return HttpResponse('Sorry, ' + username + ' has not been registered!')
    
    # Get the posts of the current user {@link Helper.py}
    posts = getPosts(username)
    
    context = {}
    context["username"] = username
    context["posts"] = posts
    
    return render(request, 'pages/index.html', context)


def index_global(request):
    '''
    A function to login and redirect to index page
    Showing all the posts including other posts
    '''
    
    # Get all the posts
    posts = Post.objects.all().order_by('-postTime')
    context = {"posts": posts}
    
    return render(request, 'pages/index.html', context);


def onRegister(request, username):
    '''
    A function to register an account in website
    @param username: the name of user 
    '''
    register(username)
    
    return redirect(reverse('global'))


def writePost(request):
    '''
    A function to write a post
    '''
    if not 'content' in request.POST or not request.POST['content'] or not 'username' in request.POST or not request.POST['username']:
        return HttpResponse("Please input your post content!")
    
    content = request.POST['content']
    username = request.POST['username']
    
    write(content, username)
    return redirect(reverse('global'))
    
    