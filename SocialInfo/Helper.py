'''
Created on Apr 10, 2016

@author: lieyongzou
'''

from models import *
from itertools import chain
import operator

def getPosts(username):
    '''
    A method to fetch all the posts from the database according to the username
    @param username the username
    @return a list of post id
    '''
    
    # Check whether the user has been registered
    if not isRegistered(username):
        return []
    
    # Return list of all posts ordered by publish time
    user = User.objects.get(name = username)
    posts = user.post.all()
    sharedPosts = user.sharedPost.all()
    
    # Merge two list and order the list by the postTime reversely
    result = list(chain(posts, sharedPosts))
    result = sorted(result, key = operator.attrgetter('postTime'), reverse = True)
    
    return result

def isRegistered(username):
    '''
    A method to check whether the user has registered the website
    @param username the name of user
    @return True the user has been registered
            False the user has not been registered
    '''
    # Get the user from db
    users = User.objects.filter(name=username)
    
    # Check whether the user exists in the db
    # If not, then create one and return an empty list
    if not users:
        return False
    else:
        return True

def register(username):
    '''
    A method to register an account
    @param username the name of user
    '''
    
    if not isRegistered(username):
        user = User(name = username)
        user.save()
        
def write(content, username):
    '''
    A method to post something
    @param content: the content of the post
    @param username: the username of the post 
    '''
    print username + ' :' + content
    user = User.objects.get(name = username)
    post = Post(content = content, user = user)
    post.save()
    