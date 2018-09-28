#!/usr/bin/python3

from project import dbInterface

def ifEmpty(postID):
    """Calls on the database interface method to see if a post is in the table

    Args:
        postID:Votes - the post ID to see if is in the table

    Return:
        True, if it's not in the table, and False if it is

    Raises:

    """
    x= dbInterface.getvoteid(postID)
    if x is False:
        return True

    else:
        return False
 


            


def checkvotevalue(userID,voteID,vValue):
    """Calls on the database interface method to see if a given vote is equivalent to the one in the table( for a given user and post)

    Args:
        postID:Votes - the post ID to select in the table
        userID:Votes - the user ID to select in the table
        vValue:Votes - the vote value for which the user voted on the post

    Return:
        True, if the user voted the same vote on the post, and False if it differs

    Raises:

    """
    votevalue= dbInterface.get_voteValue(userID,voteID)

    if votevalue == vValue :
        return True

    else:
        return False




def check_if_UserVote(userID,postID):
    """Calls on the database interface method to see if a given user has voted on a post

    Args:
        postID:Votes - the post ID to select in the table
        userID:Votes - the user ID to select in the table

    Return:
        True, if the user voted the on the given post. 

    Raises:

    """
    voteID = dbInterface.getvoteid(postID)
    allofVT= dbInterface.getall_votertype()
    for voter in allofVT :
        if((str(voter['user_id']) == str(userID)) and (str(voter['vote_id']) == str(voteID))):
            return True
        else:
            print("Im about to return false after my vote check")
            



def upvote(userID,postID):
    """Increases up vote by 1 (if user has already down voted, decrease down vote by 1)

        Args: 
                postID:Votes - The id of the post which is being up voted on
                userID:Votes - The id of the user who upvoted

        Return: 
                N/A

        Raises:
        
        """

    if ifEmpty(postID) ==True :
        type='1'
        dbInterface.makeVote(type, postID, 1, 0)
        addUser(postID,"up",userID)

    else:
        voteID = dbInterface.getvoteid(postID)
        print(voteID)
        upvote= dbInterface.get_upvote(postID) 
        downvote=dbInterface.get_downvote(postID) 

        if check_if_UserVote(userID,postID) == True :
            if str(dbInterface.get_voteValue(userID,voteID))== "down":
                upvote=upvote+1
                downvote=downvote-1
                dbInterface.set_downvote(str(upvote),str(downvote),postID)
                dbInterface.updateVotetype(userID,voteID,"up")

        else: 
                downvote=downvote
                upvote=upvote+1
                dbInterface.set_upvote(str(upvote),str(downvote),postID)
                dbInterface.updateVotetype(userID,voteID,"up")
                addUser(postID,"up",userID)

	
	


def downvote(userID,postID):
    """Increases down vote by 1 (if user has already up voted, decrease down vote by 1

    Args:
        postID:Votes - The id of the post which is being down voted on
        userID:Votes - The id of the user who down voted

    Return: 
        N/A

    Raises:

    
    """

    if ifEmpty(postID) ==True :
        type='1'
        dbInterface.makeVote(type, postID, 0, 1)
        addUser(postID,"down",userID)

    
    else:
        voteID = dbInterface.getvoteid(postID)
        upvote= dbInterface.get_upvote(postID) 
        downvote=dbInterface.get_downvote(postID) 

        if check_if_UserVote(userID,postID) == True :
            if str(dbInterface.get_voteValue(userID,voteID))== "up":
                upvote=upvote-1
                downvote=downvote+1
                dbInterface.set_downvote(str(upvote),str(downvote),postID)
                dbInterface.updateVotetype(userID,voteID,"down")

        else: 
                upvote=upvote
                downvote=downvote+1
                dbInterface.set_downvote(str(upvote),str(downvote),postID)
                dbInterface.updateVotetype(userID,voteID,"down")
                addUser(postID,"down",userID)



def addUser(postID,type_vote,userID):
    """ Whenever a user votes (for the first time), the post to which they voted on is recorded, and their username is added to the table

        Args:
        postID:Votes - The id of the post which is voted on
        type_vote:Votes - The starting vote ID ( "up","down")
        userID:Votes - The id of the user who voted

    Return: 
        N/A

    Raises: 

    """
    dbInterface.set_userID(postID,type_vote,userID)


def votedUsers(postID):
    """ Returns a list of all the voted users

    Args: 
        postID:Votes- id of post , which all the voted users need to be viewed

    Return:
        list of users who voted on the post

    Raises:

    """
    return dbInterface.get_ALL_users(postID)

def get_uv(postID):
    """ Returns the total upvotes from the database

    Args: 
        postID:  id which to get the up votes for

    Return:
        total number of up votes for a post

    Raises:
  
    """
    return dbInterface.get_upvote(postID)

def get_dv(postID):
    """ Returns the total down votes from the database

    Args: 
        postID:  id which to get the down votes for

    Return:
        total number of down votes for a post

    Raises:

    """
    return dbInterface.get_downvote(postID)











