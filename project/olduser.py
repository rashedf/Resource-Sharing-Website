#!/usr/bin/python3
"""User module for interacting with the database

This module is designed to be used with the COMP_2005_Project package. 
The module acts as a bridge between the data persistence code in dbInterface.py 
and the interface code in user_interface.py. Most functions in this module 
just retrieve and pass-along data by referencing the dbInteface functions and 
returning the data. The data is then passed to the user_interface module functions.

Notes
-----
    Ideally, the functions in this module need not be modified/referenced by 
    other users/modules. Only the user_interface module should reference the functions 
    in this module.

Attributes
----------
    reservedUsernames: list
        This is a list of all the usernames that cannot be used to login or signup. 
        They are reserved for the following reasons:
        'RemovedAccount': Deleted accounts are assigned this username
        'admin': This username can be misleading. It's also used for debugging
        'defaul': Used for debugging
        'user': This username can be misleading. 
"""
from flask import session
from project import dbInterface

reservedUsernames = ['RemovedAccount', 'admin', 'default', 'user']



def createUser(username, password, firstname, lastname):
    """Function to create new user account

    Parameters
    ----------
        username: string
        password: string
        firstname: string
        lastname: string

    """
    dbInterface.createUser(username, password, firstname, lastname)



def deleteUser(username):
    """Function to delete a user account

    Parameters
    ----------
        username: string

    """
    dbInterface.deleteUser(username)


    
def getUsers():
    """Function to retrieve all information about all users

    Returns
    -------
        list
            A list of tuples where each tuple contains data about
            a specific user.

    """
    return dbInterface.getUsers()


    
def isUsernameTaken(username):
    """Function to check if a username already exists in the database

    Parameters
    ----------
        username: string

    Returns
    -------
        bool
            True if the username exists, False otherwise.
		
    """
    users = dbInterface.getUsernames()
    for user in users:
        if(str(user['username']) == str(username)):  
            return True
    return False



def isReserved(username):
    """Function to check if a username is reserved

    Parameters
    ----------
        username: string

    Returns
    -------
        bool
            True if the username has a match with one of the reservedUsernames
            entries, False otherwise.
		
    """
    if username in reservedUsernames:
        return True
    return False



def getUserInfoDict():
    """Function to retrieve logged-in  user's information from the database database

    Notes
    -----
        This essentially retrieves the same informationa as getUserInfo().
        The difference is in the data-type of the return.

    Returns
    -------
        dict
            A dictionary containing the column headers as keys,
            and the column data as values.

    Example
    -------
        Below is an example of what this function returns:
            {'id': 10, 'username': 'jdoe', 'password': 'qkbl987', 'fname': 'John', 'lname': 'Doe'}
		
    """
    return dbInterface.getUserInfoDict(session['loggedInUser'])



def getUserId():
    """Function to retrieve current user's user ID

    Returns
    -------
        int
            Logged-in user's user ID
		
    """
    return dbInterface.getUserId(username=session['loggedInUser'])



def getIDFromUsername(username):
    """Function to retrieve user's user ID

    Returns
    -------
        int
            User's user ID
		
    """
    return dbInterface.getUserId(username)



def getUserInfo():
    """Function to retrieve logged-in  user's information from the database

    Notes
    -----
        This essentially retrieves the same informationa as getUserInfoDict().
        The difference is in the data-type of the return.

    Returns
    -------
        tuple
            A tuple containing user data where each tuple contains data about a user.

    Example
    -------
        Below is an example of what this function returns:
            (10, 'jdoe', 'rmvy793', 'John', 'Doe')
		
    """
    return dbInterface.getUserInfo(session['loggedInUser'])
 

   
def authenticate(username, password):
    """Function to match username and password

    Also checks if the username provided is in the reservedUsernames list

    Parameters
    ----------
        username: string
        password: string
	
    Returns
    -------
        bool
            True if username and password match and username is not in the reservedUsernames
            list, False otherwise

    """
    users = dbInterface.getUsers()
    if not isReserved(username):
        for user in users:
            if((str(user['username']) == str(username)) and (str(user['password']) == str(password))):
                session['loggedIn'] = True
                session['loggedInUser'] = username  
                return True
    return False



def logout():
    """Function to log user out of the session

    Notes
    -----
        This function uses the pop method for python dicts. The second argument (None) is 
        necessary so that it doesn't throw an exception if the key being popped doesn't 
        exist.

        This function doesn't care if the user is logged in.
    """
    session.pop('loggedIn', None)
    session.pop('loggedInUser', None)



def getLoggedInUser():
    """Function to get the username of the user currently logged in

    Returns
    -------
        string
            Username of user logged in to current session

    """
    return  session['loggedInUser']
       
