#!/usr/bin/python3

"""Handles subscription interactions

Internal to project

No objects are created in this module. All functions utilize the database 
interface to handle the addition/removal of subscriptions. In order to add 
or remove a user as a subcription holder to a topic simply call addToSub or 
removeFromSub respectively. Simply pass the user id and topic id.

Functions:
    addToSub(user, topic) --> bool
    removeFromSub(user, topic) --> bool
"""
from project import dbInterface

def addToSub(user, topic):
    """Calls the database interface to add the information into the database returns implicit None.

    Args:
      topic - the topic in which the user wishes to subscribe
      user - the key attribute designated to identify the user

    Return:
      None
    """
    
    dbInterface.addSub(user, topic)

def removeFromSub(user, topic):
    """A stub implementation that simply passes
    
    Args:
      topic - the id of the topic in which the user wishes to subscribe to
      user - the key attribute (id) designated to identify the user
    
    The idea of this method would be to remove a user from the subscribers to a topic so that a user
    can stop receiving notifications (and/or other functionality) for a topic.  
    """
    pass
