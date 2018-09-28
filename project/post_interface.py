#!/usr/bin/python3

import datetime
from project import post
    
def getPostIDs(username):
    """Get list of posts Ids created by a certain user
    Args:
        username - String - username of User
    Return:
        list of post ids that were created by User
    """
    postIds = list();
    return postIds;

def getPosts(topic_id):
    """Get list of posts that belong to a certain topic
    Args:
        topic_id - Int - topic id of topic
    Return:
        list of posts that belong to topic id
    """
    return post.getPosts(topic_id)
    
def getPost(post_id):
    """Get  full post that belong to a certain post id
    Args:
        post_id - Int -  id of post
    Return:
         post that belong to post id
    """
    return post.getPost(post_id)

def getPostTitle(post_id):
    """Get title of post
    Args:
        post_id - Int - Post id of post
    Return:
        Title of post that belong to post id
    """
    return "Post Title"

def getPostBody(post_id):
    """Get body of post
    Args:
        post_id - Int - Post id of post
    Return:
        Body of post that belong to post id
    """
    return "Post Body"

def getTimePosted(post_id):
    """Get time post was made
    Args:
        post_id - Int - Post id of post
    Return:
        Time the post was posted
    """
    time = datetime.datetime.now()
    return  time

def isEdited(post_id):
    """Check if post has been edited
    Args:
        post_id - Int - Post id of post
    Return:
        Boolean if post has been edited.
    """
    return True

def getTimeEdited(post_id):
    """Get time the post was edited
    Args:
        post_id - Int - Post id of post
    Return:
        Time the post was edited
    """
    editedTime = datetime.datetime.now()
    return editedTime

def getPostedBy(post_id):
    """Get username of User who made post
    Args:
        post_id - Int - Post id of post
    Return:
        Username of user who made the post
    """
    return "username"

def createPost(topic_id, posted_by, title, main_body):
    """Create Post
    Args:
        topic_id - Int - Topic id of topic
        posted_by - String - username of User
        title - String - title of post to be created
        main_body - String - main body of post to be created
    Return:
        Boolean True if creating post was successful. False if failed.
    """
    post.insertPost(topic_id, posted_by, title, main_body)

def editPost(post_id, title, main_body):
    """Edit Post
        Args:
        post_id - Int - Id of Post
        title - String - title of post to be edited
        main_body - String - main body of post to be edited
        Return:
        Boolean True if editing post was successful. False if failed.
        """
    post.editPost(post_id,title, main_body)

    




    
    
