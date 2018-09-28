#!/usr/bin/python3
from project import notification

"""Notification interface

Internal to project

The idea behind this module is for a clean seperation from the main project module and
the notification handler module. The intended use is so that should the implementation of
the notification handler change, the main code is uneffected. It is this modules responcibility
to make sure that the main code is receiving the return type is desires.

Functions:
    sendNotifications(str, str or int) --> None
    getNotifications(str) --> sqlite3.Row
    getNotificationTimeSent(str, int) --> datetime
    hasNotification(str) --> bool
"""

def sendNotifications(typ, identifying_id):
    """Passes the given arguements to the subscription code and returns implicit None.
    
    Args
        type - the type of notification to be send.
        id - the identifying id associated with the type of notification.

    Return:
        None

    This function provides supports flexability if notifications are to extend past just new posts.
    """
    notification.sendNotif(typ, identifying_id)

def getNotifications(user):
    """Passes the given arguements to the notification code and returns a sqlite3.Row object.
    
    Args
        user - the identifying id associated with the user.

    Returns:
        sqlite3.Row - conatins (title, user_id, body, target, target_id).

    This method simply passes control to the proper method to retrieve all
    of the notificaiton information for the user.
    """
    notifications = notification.getNotifications(user)
    return notifications

def getNotificationTimeSent(user, notify_id):
    """A stub implementation that returns a datetime.
    
    Args
        user - the identifying id associated with the user.
        notify_id - the identifying id associated with the notification.

    This sub implementation method merely exists for further functionality that may
    be used in the future.
    """
    return datetime.datetime.now()

def hasNotification(user):
    """A stub implementation that returns a boolean.
    
    Args
        user - the identifying id associated with the user
    
    This is currently a stub implementation with no proper functionality
    because the feature is not relavent. It simply returns True as if a 
    user has a notification.

    Uses of the functionality could include displaying a notification badge should
    development shift into a menu implementation.
    """

    return True
