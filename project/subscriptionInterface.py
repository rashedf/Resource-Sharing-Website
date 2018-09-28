#!/usr/bin/python3
import datetime
from project import subscription

"""Subscription interface

Internal to project

The idea behind this module is for a clean seperation from the main project module and
the subscription handler module. The intended use is so that should the implementation of
the subscription handler change, the main code is uneffected. It is this modules responcibility
to make sure that the main code is receiving the return type is desires.

Functions:
    sendNotifications(str, str or int) --> None
    getNotifications(str) --> sqlite3.Row
    getNotificationTimeSent(str, int) --> datetime
    hasNotification(str) --> bool
"""

def addSubscription(user, topic_id):
    """Passes the given arguements to the subscription code and returns a sqlite3.Row object

    Args:
        user - the identifying id associated with the user
        topic_id - the identifying id associated with the topic

    Return:
        boolean - signifies successful addition to subscribers of a topic

    This method serves as a boundary to the subscription implementation module when a user subscribes to a topic.
    """

    return subscription.addToSub(user, topic_id)

def removeSubscription(user, topic_id):
    """A stub implementation that simply passes
    
    Args:
        user - the identifying id associated with the user
        topic_id - the identifying id associated with the topic
    
    The idea of this method would be to remove a notification once the user 
    views the notification. This functionality would mirror the behaviour of 
    most notification services found in the industry.
    """
    pass

def getSubscriptionDate(user, topic_id):
    """A stub implementation that returns a datetime
    
    Args
        user - the identifying id associated with the user
        topic_id - the identifying id associated with the topic
    
    This is currently a stub implementation with no proper functionality
    because the feature is not relavent. It simply returns the current
    date and time in which it is called.
    
    """
    return datetime.datetime.now()
