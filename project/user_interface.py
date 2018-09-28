#!usr/bin/python3
"""User interface module for interacting with other modules

This module is designed to be used with the COMP_2005_Project package. 
The module provides users of other modules simple methods to add, edit, retrieve or
delete data from the database of the project. 

Notes
-----
	Must include: from project import user

Functions
---------
	For use outside this module:	
		createUser()
		deleteUser()
		getUsers()
		getUserInfo()
		getUserInfoDict()
		getUserId()
		isUsernameTaken()
		isReserved()
		authenticate()
		logout()
		getLoggedInUser()

"""

from project import user

def createUser(username, password, firstname, lastname):
    """Create new user account

    Parameters
    ----------
        username: string
        password: string
        firstname: string
        lastname: string

    """
    user.createUser(username, password, firstname, lastname)

def deleteUser(username):
    """Delete user account with Username = username

    Parameters
    ----------
        username: string

    """
    user.deleteUser(username)
    
def getUsers():
    """Retrieve all information about all users

    Returns
    -------
        list
            A list of tuples where each tuple contains data about
            a specific user.

    Examples
    --------
        An example of what the function returns:
            [(10, 'jdoe', 'rmvy793', 'John', 'Doe'), (11, 'jadoe', 'rmjk5644', 'Jane', 'Doe')]

    """
    return user.getUsers()

def getUserInfo():
    """Get logged-in  user's information from the database

    Notes
    -----
        This essentially retrieves the same informationa as getUserInfoDict().
        The difference is in the data-type of the return.

    Returns
    -------
        tuple
            A tuples containing user data where each tuple contains data about a user.

    Example
    -------
        Below is an example of what this function returns:
            (10, 'jdoe', 'rmvy793', 'John', 'Doe')
		
    """
    return user.getUserInfo()

def getUserInfoDict():
    """Get logged-in  user's information from the database database

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
    return user.getUserInfoDict()

def getUserId():
    """Get current user's user ID

    Returns
    -------
        int
            Logged-in user's user ID
		
    """
    return user.getUserId()


def getIDFromUsername(username):
    """Get user ID by username

    Returns
    -------
        int
            User's user ID
		
    """
    return user.getIDFromUsername(username)


    
def isUsernameTaken(username):
    """Check if a username already exists in the database

    Parameters
    ----------
        username: string

    Returns
    -------
        bool
            True if the username exists, False otherwise.
		
    """
    return user.isUsernameTaken(username)

def isReserved(username):
    """Check if a username is reserved

    Parameters
    ----------
        username: string

    Returns
    -------
        bool
            True if the username has a match with one of the reservedUsernames
            entries, False otherwise.
		
    """
    return user.isReserved(username)
    
def authenticate(username, password):
    """Match username and password

    Also check if the username provided is in the reservedUsernames list

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
    return user.authenticate(username, password)
    
def logout():
    """Log user out of the session

    Notes
    -----
        This function uses the pop method for python dicts. The second argument (None) is 
        necessary so that it doesn't throw an exception if the key being popped doesn't 
        exist.

        This function doesn't care if the user is logged in.
    """
    user.logout()
    
def getLoggedInUser():
    """Get the username of the user currently logged in

    Returns
    -------
        string
            Username of user logged in to current session

    """
    return user.getLoggedInUser()
    
