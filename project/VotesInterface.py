#!/usr/bin/python3
from project import Votes



## Getter

def getUpVotes(postID):
	"""Retreives the number of up votes for a given post

	Args:
	postID:Votes - the post ID from which the up votes is required

	Return:
	number of upvotes

	Raises:

	"""
	return Votes.get_uv(postID)

def getDownVotes(postID):
	"""Retreives the number of down votes for a given post

	Args:
	    postID:Votes - the post ID from which the down votes is required

	Return:
	    number of upvotes

	Raises:

	"""
	return Votes.get_dv(postID)

def getVotedUsers(postId):
	"""Gives a list of all the users who voted for a particular post

	Args:
	    postID:Votes - the post ID from which the voted users must be seen

	Return:
	    number of upvotes

	Raises:

	"""
	return Votes.votedUsers(postID)

## Do things

def callUpVote(userID,postID):
    """Increases number of up votes(if feasable)

    Args:
        postID:Votes - The id of the post which is being up voted on
        userID:Votes - The id of the user who upvoted

    Return:
        N/A

    Raises:

        when this method is called, calls on the upVote method from Votes class
	"""
    Votes.upvote(userID,postID)
    print(0)

def callDownVote(userID,postID):
    """Increases number of down votes(if feasable)

    Args:
        postID:Votes - The id of the post which is being down voted on
        userID:Votes - The id of the user who down voted

    Return:
        N/A

    Raises:

        when this method is called, calls on downVote method from Votes class
	"""
    Votes.downvote(userID,postID)


