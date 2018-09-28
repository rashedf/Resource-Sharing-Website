#!/usr/bin/python3

"""Handles notification interactions

Internal to project

No objects are created in this module. All functions utilize the database 
interface to handle notification interactions. In order to get all of a users
notifications simply call getNotifications while providing the users id.

Sending notifications can be done by calling sendNotif, passing the type of
notification and the identifying id.

Functions:
  sendNotif(str, int or str) --> None
  getNotifications(str) --> sqlite3.Row Object 
"""
from project import dbInterface

def sendNotif(typ, identifying_id):
    """Sends a notification, depending on the type, to all users subscribed to a topic and return implicit None or pass.
    
    Args:
        type - the type of notification to be send
        identifying_id - the unique id identifying for the type of notification that will be generated

    Return:
        None or pass

    This versitile method is used to send notifiactions to one (or more) users in the event that
    a notifcation sequence of events is generated. Due to the nature of the prototype, this method will
    be exclusively used for posts. However, given the nature of its implementation, it could be used for
    other events (ie. new topics in groups, up/down votes etc) as well in the future.  
    """
    if typ == "post":

        subscribers = dbInterface.getSubscribers(str(identifying_id))
        topicName = dbInterface.getTopicName(str(identifying_id))
	
        for user in subscribers:
            user_id = user['user_id']
            title = "New Post"
            body = "A new post has been created in " + str(topicName[1])

            dbInterface.addNotification(user_id, title, body, "post", identifying_id)

    else:
        pass

def getNotifications(user):
    """Used to retrieve all notifications for the current user to be displayed and return a sqlite3.Row object.
    
    Args:
        user - the identifying id associated with the user

    Return:
        sqlite3.Row - contains (user_id, title, body, target, target_id)

    This method is used to retrieve all notifications for the desired user.
    """
    notifications = dbInterface.getNotifications(user)
    return notifications
