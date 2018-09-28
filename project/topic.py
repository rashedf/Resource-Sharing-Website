#!/usr/bin/python3 
import datetime 
from project import dbInterface

    
    
def insertTopic(name, created_by, group_id):
    dbInterface.insertTopic(name, created_by, group_id)
    
def getTopics():
    return dbInterface.getTopics();    
    
def getTopicName(topic_id):
    return dbInterface.getTopicName(topic_id)

def editTopic(topic_id, topic_name):
    return dbInterface.editTopic(topic_id, topic_name)
        
