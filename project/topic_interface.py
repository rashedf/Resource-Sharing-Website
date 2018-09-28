#!/usr/bin/python3

import datetime
from project import topic


def getTopics():
    """Get all topics
        Return:
        Dictionary of all Topics
    """
    return topic.getTopics()

def getTopicName(topic_id):
    """Get topic name
        Args:
        topic_id: Int - id of topic used to search for topic name
        
        Return:
        the topic name (String) belonging to certain topic id
    """
    return topic.getTopicName(topic_id)

def getTopicIDs(created_by):
    """Get list of topic ids created by a certain user
        Args:
        created_by: String - username of user
        
        Return:
        the list of topic ids created by a user
    """
    topicIDs = list()
    return topicIDs

def getTimeCreated(topic_id):
    """Get time when topic was created
        Args:
        topic_id: Int - id of topic
        
        Return:
        the time the certain topic was created relevant to its topic id
    """
    timeCreated = datetime.datetime.now()
    return timeCreated

def getCreatedBy(topic_id):
    """Get user who created topic
        Args:
        topic_id: Int - id of topic
        Return:
        the username of user who created the topic
    """
    return "username"

def createTopic(topicName, created_by, group_id):
    """Create topic
        Args:
        topicName: String - name of topic to be created
        created_by : String - username of user creating the topic
        Return:
        Boolean Flag if createTopic was successful. True for Success. False for failure.
    """
    topic.insertTopic(topicName, created_by, group_id)
    return True

def editTopic(topic_id, topic_name):
    """Edit topic
        Args:
        topic_id: String - id of topic to be edited
        topic_name: String - name of topic to be edited
    """    
    return topic.editTopic(topic_id, topic_name)