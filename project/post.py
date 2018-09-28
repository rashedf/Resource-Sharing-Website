#!/usr/bin/python3 
import datetime 
from project import dbInterface

    
def getPosts(topic_id):
    return dbInterface.getTopicPosts(topic_id)
    
def getPost(post_id):
    return dbInterface.getPost(post_id)  
    
def insertPost(topic_id, posted_by, title, main_body):
    dbInterface.insertPost(topic_id, posted_by, title, main_body)

def editPost(post_id,title, main_body):
    dbInterface.editPost(post_id,title, main_body)
        
