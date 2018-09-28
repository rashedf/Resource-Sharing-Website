#!/usr/bin/python3
from flask import Flask, request, session, g
import sqlite3
import datetime
#from .project import app
from project import db

database = db.Database()

#Database Managment
def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(database.project_database)
    rv.row_factory = sqlite3.Row
    return rv
    

#User SQL Queries

def get_db():
    """Opens a new database connection if there is none yet for the
		current application context.
    """
    if not hasattr(g, 'sqlite_db'):
        g.sqlite_db = connect_db()
    return g.sqlite_db


    
def query_db(query, args=(), one=False):
    """Execute SQL commands and return the resulting table
    
    Parameters
	----------
        query: string
            The SQLite query command to execute
    
    Returns
    -------
        list
            rv: A list of dictionaries. Each dictionary is a row in the table returned by the query
    """
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv


def createUser(username, password, firstname, lastname):
    """Add new entry in the user table in the database
    
    Parameters
    ----------
        username: string
        password: string
        firstname: string
        lastname: string

    """
    g.db = connect_db()
    g.db.execute('insert into user (username, password, fname, lname) values (?, ?, ?, ?)', (username, password, firstname, lastname))
    g.db.commit()
    g.db.close()



def deleteUser(username):
    """Remove entry from the user table in the database, where username is username
    
    Parameters
    ----------
        username: string

    Notes
    -----
        This function doesn't actually remove the specific entry. As of now, it just 
        updates the username to 'RemovedAccount', which is a reserved username. This way, there
        is no record in the user table with their old username.

    """
    g.db = connect_db()
    g.db.execute('update user set username="RemovedAccount" where username=?', [username])
    g.db.commit()
    g.db.close()


    
def getUsers():
    """Get all information about all users from the user table in the database
    
    Returns
    -------
        list
            A list of tuples, where each tuple is a row in the table returned by the 
            query

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM user")
    users = cur.fetchall()
    g.db.close()
    return users



def getUserInfoDict(username):
    """Get all information about user with username = username
    
    Parameters
    ----------
    username: string

    Returns
    -------
        dict
            A dictionary where the keys are the column headers in the table returned by
            the query and the values are column data in the table.

    """
    return query_db("SELECT fname,lname FROM user where username=?", [username])



def getUserInfo(username):
    """Get all information about user with username = username
    
    Parameters
    ----------
        username: string

    Returns
    -------
        tuple
            A tuple containing all information of the user with username = username

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM user where username=?", [username])
    users = cur.fetchall()
    g.db.close()
    return users



def getUserId(username):
    """Get user ID of user with username = username
    
    Parameters
    ----------
        username: string

    Returns
    -------
        int
            ID of user with username = username

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT id FROM user WHERE username=?", [username])
    users = cur.fetchone()
    g.db.close()
    return users



def getUsernames():
    """Get usernames of all users in the user table

    Returns
    -------
        list
            A list of tuples, where each tuple is a row in the table returned by the 
            query

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT username FROM user")
    users = cur.fetchall()
    g.db.close()
    return users

#Topic SQL Queries

def insertTopic(name, created_by, group_id):
    g.db = connect_db()
    g.db.execute("INSERT INTO topic(name, time_created , created_by, group_id) VALUES(?, ?, ?, ?)", (name, datetime.datetime.now(), created_by, group_id))
    g.db.commit()
    g.db.close()

def insertPost(topic_id, posted_by, title, main_body, ):
    print("hello")
    g.db = connect_db()
    g.db.execute("INSERT INTO post(topic_id, posted_by, title, main_body, time_posted) VALUES(?, ?, ?, ?, ?)", (topic_id, posted_by, title, main_body, datetime.datetime.now()))
    g.db.commit()
    g.db.close()

def getTPosts(topic_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT id, title, posted_by, main_body, time_posted FROM post WHERE topic_id =?", [topic_id])
    posts = cur.fetchall()
    g.db.close()
    return posts

def getTopics(created_by):
    g.db = connect_db()
    cur = g.db.execute("SELECT id, name, FROM topic WHERE created_by =?", [created_by])
    topics = cur.fetchall()
    g.db.close()
    return topics
    
def getTopics():
    g.db = connect_db()
    cur = g.db.execute("SELECT id, name, group_id FROM topic ")
    topics = cur.fetchall()
    g.db.close()
    return topics    

def getTopicIDs(created_by):
    g.db = connect_db()
    cur = g.db.execute("SELECT id FROM topic WHERE created_by =?", [created_by])
    topicIDs = cur.fetchall()
    g.db.close()
    return topitopicIDscs

def getCreatedBy(topic_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT created_by FROM topic WHERE topic_id =?", [topic_id])
    user = cur.fetchone()
    g.db.close()
    return user

def getTopicTimeCreated(topic_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT time_created FROM topic WHERE topic_id=?", [topic_id])
    time = cur.fetchone()
    g.db.close
    return time

def getTopicName(topic_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT id, name, created_by FROM topic WHERE id=?", [topic_id])
    topic_name = cur.fetchone()
    g.db.close
    return topic_name

def editTopic(topic_id, topic_name):
    print('in topic edit')
    g.db = connect_db()
    g.db.execute("UPDATE topic set name=? WHERE id=?", (topic_name, topic_id))
    g.db.commit()
    g.db.close()    

#Post SQL Queries
def getPostIDs(topic_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT id FROM post WHERE topic_id =?", [topic_id])
    postIDs = cur.fetchall()
    g.db.close()
    return postIDs


def getTopicPosts(topic_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT id, topic_id, title, main_body, time_posted FROM post WHERE topic_id=?", [topic_id])
    posts = cur.fetchall()
    g.db.close
    return posts

def getPosts(created_by):
    g.db = connect_db()
    cur = g.db.execute("SELECT id, topic_id,title, main_body, time_posted FROM post WHERE created_by=?", [created_by])
    posts = cur.fetchall()
    g.db.close
    return posts

def getPostIDsbyUser(created_by):
    g.db = connect_db()
    cur = g.db.execute("SELECT id FROM post WHERE created_by=?", [created_by])
    postIDs = cur.fetchall()
    g.db.close
    return postIDs

def getPost(post_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT id, topic_id, posted_by, title, main_body, time_posted FROM post WHERE id=?", [post_id])
    post = cur.fetchone()
    g.db.close
    return post

def getPostTitle(post_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT title FROM post WHERE post_id=?", [post_id])
    title = cur.fetchone()
    g.db.close
    return title

def isPostEdited(post_id):
    g.db = connect_db
    cur = g.db.execute("SELECT edited FROM post WHERE post_id=?", [post_id])
    edited = cur.fetchone()
    g.db.close()
    return edited

def getEditedPost(post_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT topic_id, posted_by, title, main_body, time_edited FROM post WHERE post_id=?", [post_id])
    post = cur.fetchone()
    g.db.close
    return post

def getPostTimePosted(post_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT time_posted FROM post WHERE post_id=?", [post_id])
    timePosted = cur.fetchone()
    g.db.close
    return timePosted

def getPostTimeEdited(post_id):
    g.db = connect_db()
    cur = g.db.execute("SELECT time_edited FROM post WHERE post_id=?", [post_id])
    timeEdited = cur.fetchone()
    g.db.close
    return timeEdited

def editPost(post_id,title, main_body):
    print('in db edit')
    edited = True
    g.db = connect_db()
    g.db.execute("UPDATE post set title=?, main_body=?, edited=?, time_edited=? WHERE id=?", (title, main_body, edited, datetime.datetime.now(), post_id))
    g.db.commit()
    g.db.close()

#Group SQL Queries   

def createGroup(Groupname, createdby):
   """This function takes in two parameters and stores in them in the groups tables

   args:
        Groupname   String      Name of the group
        created_by  String      the name of the creator

    Return:
        None

    Rasies:


   """
   g.db = connect_db()
   cur = g.db.execute("INSERT into groups (name, created_by) VALUES (?, ?)", [Groupname, createdby])
   g.db.commit()
   g.db.close()
	

def getAGroupInfo(group_id):
    """The function takes in one parameter and returns the group information from the group tables

    args:
        group_id    Int     the group identification number
    
    Return:
        Id          Int         Group Id number
        name        String      The group name
        created_by  String      the name of the creator

    Rasies:

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT id, name, created_by FROM groups WHERE id=?", [group_id])
    groupInfo = cur.fetchone()
    g.db.close
    return groupInfo
    
def getGroups():
    """This function gets all the created groups from the group table

    args:
        None

    Return:
        Allgroups   List    the attributes of all the groups(id, name, created_by)

    Rasises:

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT id, name, created_by FROM groups")
    allgroups = cur.fetchall()
    g.db.close()
    return allgroups

def getUserId(username):
    """This function get a user's Id

    args: 
        usename     String  The user's name

    Returns:
        UserId      Int     user id number

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT id FROM user WHERE username=?", [username])
    users = cur.fetchone()
    g.db.close()
    return users

def deleteGroup(groupName):
    """This function delete a created group from the database

    args:
        groupName   String  the name of the group

    Return:
        None
    """
    g.db = connect_db()
    cur = g.db.execute( 'DELETE FROM groups WHERE name =?', [groupName])
    g.db.commit()
    g.db.close()

def Group_created_by(GroupName):
    """
    This function gets the name of the creator(Adminstrator) of a group

    args: 
        Groupname   String  The name of the group

    Return:
        The name of the creator of the group

    """
    g.db = connect_db()
    cur = g.db.execute("SELECT created_by FROM groups WHERE name=?", [GroupName])
    Admin = cur.fetchone()
    g.db.close
    return Admin

def getGroupTopics(group_id):
    """This function gets all the topics associated with a particular group

    args:
        group_id    Int     group id number

    Return:
        topics     List     A list of topics in a group
    """
    g.db = connect_db()
    cur = g.db.execute("SELECT id, name, group_id FROM topic WHERE group_id =?", [group_id])
    topics = cur.fetchall()
    g.db.close()
    return topics

def AddMemberToGroup(group_id,user_id):
    """This function adds a user to a group

    args:
        group_id    Int     the group id number
        user_id     Int     the user id number
    
    Return:
        None
    """
    g.db = connect_db()
    g.db.execute("INSERT INTO membership (group_id, user_id) VALUES(?, ?)", (group_id,user_id))
    g.db.commit()
    g.db.close()

def getGroupId(name):
    """This function gets a group id number
    
    args:
        name    String      the group name

    Return:
        GroupId     Int     the group id number
    """
    g.db = connect_db()
    cur = g.db.execute("SELECT id FROM groups WHERE name=?", [name])
    GroupId = cur.fetchone()
    g.db.close()
    return GroupId

def getGroupMembers(group_id):
    """This function gets the user_id of a members of a particular group

    args:
        group_id    int     the group id number

    Return:
        members     List    A list containing (membership_id, user-id, group_id) attributes of a user
    
    """
    g.db = connect_db()
    cur = g.db.execute("SELECT membership_id, user_id, group_id FROM membership WHERE group_id=?", str(group_id))
    members = cur.fetchall()
    g.db.close()
    return members



#Vote Related SQL Queries 

def get_upvote(postID):
    """Gets total number of up votes from the vote table

    Args:
        postID:Votes - the ID from a given post, that the total number of up votes is required for

    Return:
        The total number of up votes if the table isn't empty.If it's empty, return 0

    Raises:

    """
    g.db = connect_db()
    cur=g.db.execute('''SELECT upvote FROM vote WHERE type_id=?''', [postID])
    x= cur.fetchone()
    if not x :
        return 0
    else:
        return x[0]
    g.db.close()

def get_downvote(postID):
    """Gets total number of down votes from the vote table

    Args:
        postID:Votes - the ID from a given post, that the total number of down votes is required for

    Return:
        The total number of down votes if the table isn't empty.If it's empty, return 0

    Raises:

    """
    g.db = connect_db()
    cur=g.db.execute('''SELECT downvote FROM vote WHERE type_id=?''',[postID])
    x= cur.fetchone()
    if not x :
        return 0
    else:
        return x[0]
    g.db.close()
        
def get_upORdown(userID,postID):
    """Gets whether a users vote on a prticular post is a "up" vote, or "down" vote from the votertype table

    Args:
        postID:Votes - the ID from a given post, that the user voted on 
        userID:Votes - the ID of the user who voted

    Return:
        "up","down",or "null", dependant on the user's vote/non existence of a vote

    Raises:

    """
    g.db=connect_db()
    voteID=getvoteid(postID)
    cur=g.db.execute(''' SELECT type FROM votertype WHERE user_id,vote_id = ?''',[userID,voteID])
    updown= cur.fetchone()[0]
    g.db.close()
    return updown



def get_type(post_type):
    """Gets the type ID from the string submitted ( a type of decoder)

    Args:
        post_type:Votes - String indicating the type of thread (e.g "post","discussion",etc.)

    Return:
        Int encoding for the string
        
    Raises:

    """
    g.db=connect_db()
    cur=g.db.execute(''' SELECT id FROM type WHERE type_name = ? ''',[post_type])
    str_type= cur.fetchone()[0]
    g.db.close()
    return str_type
    
def get_ALL_users(postID):
    """ Returns a list of all the users who have voted on a post
    Args:
        postID:Votes - the ID from a selected post

    Return:
        a list of all the users who voted on the post

    Raises:

    """

    g.db=connect_db()
    conn.row_factory = sqlite3.Row
    voteID=getvoteid(postID)
    cur=conn.execute('''SELECT user_id FROM votertype WHERE vote_id = ? ''',[voteID])
    g.db.close()
    
    users = []
    for tablerow in cur.fetchall():
        user = tablerow['user_id'] 
        users.append(user)
    return users

    
      
def getvoteid(postID):
    """Gets matching primary id from the post id ( vote table).This is utilized as the vote id in the votertype table

    Args:
        postID:Votes - the ID from a given post, that the vote id is required for

    Return:
        The total number of matching vote id if the table isn't empty.If it's empty, return False

    Raises:

    """
    g.db=connect_db()
    cur=g.db.execute('''SELECT id FROM vote WHERE type_id=? ''',[postID])
    voteID=cur.fetchone()
    if not voteID :
        return False
    else:
        return voteID[0]
 

def getall_votertype() :
    """Gets all of the users who voted on the same post

    Args:
        N/A

    Return:
        All the users who voted, and all the posts which have been voted on.Formatted as (voteid,userid) ,from each row

    Raises:

    """
    g.db=connect_db()
    cur=g.db.execute(''' SELECT vote_id , user_id FROM votertype''')
    allVT = cur.fetchall()
    g.db.close()
    return allVT

def updateVotetype(userid,voteid,votetype):
    """Updates the votertype table, if the user has changed their vote

    Args:
        userid:Votes - The id of the user who is currently logged in
        voteid:Votes - The vote id which came from a given post
        votetype: Votes - The vote type to which the current entry will be changed. e.g("up")

    Return:
        N/A

    Raises:

    """
    g.db=connect_db()
    g.db.execute(''' UPDATE votertype set votetype=? WHERE user_id=? AND vote_id=?''', (votetype,userid,voteid))
    g.db.commit()
    g.db.close()
    

def getall_postID():
    """Gets all the current post ID's in the vote table

    Args:
        N/A

    Return:
        All posts currently in the vote table

    Raises:

    """
    g.db=connect_db()
    cur=g.db.execute(''' SELECT type_id FROM vote''')
    postid=cur.fetchall()
    g.db.close()
    return postid

def get_voteValue(userID,voteID):
    """Gets the matching votetype (e.g "up") from the given userID and voteID. If there's no mathing entries, returns false

    Args:
        userID:Votes - the user id of a user who may or may not have voted
        voteId:Votes - the vote id(comes from post id) to check

    Return:
        A matching vote type if the table isn't empty.If it's empty, return False 

    Raises:

    """
    
    g.db=connect_db()
    cur=g.db.execute("SELECT votetype FROM votertype WHERE user_id=? AND vote_id=?",(userID,voteID))
    votevalue=cur.fetchone()
    if not votevalue :
        return False
    else:
        return votevalue[0]

def checkifemptyVote():
    """Checks if the vote table is empty. If it's empty, it returns True, else False

    Args:
       N/A

    Return:
        A matching vote type if the table isn't empty.If it's empty, return False 

    Raises:

    """
    g.db=connect_db()
    cur=g.db.execute("SELECT * FROM vote")
    if cur.fetchall() is None:
        return True
    else:
        return False
    g.db.close()


## setter methods to put data into the tables

def set_upvote(new_upvote,new_downvote,postID):
    """Sets the new total number of up votes & down votes

    Args:
        new_upvote:Votes - the updated upvotes value
        new_downvote: Votes - the updated downvoets value
        postID:Votes - the post ID from which the upvotes, must be updated

    Return:
        N/A

    Raises:

    """
    g.db=connect_db()
    g.db.execute('''UPDATE vote SET upvote = ? WHERE type_id= ?''',(new_upvote,postID))
    g.db.commit()
    g.db.close()

def makeVote(type,type_id, upvote, downvote):
    """If a post has no votes on it, a new entry is made

    Args:
        type:Votes - the type value of the post (e.g "post" is 1, "discussion" is 2 etc.)
        type_id:Votes - the post id which is being newly voted upon
        upvote:Votes - the instantiated upvote value
        downvote: Votes - the instantiated downvote value
    Return:
        N/A

    Raises:

    """
    g.db = connect_db()
    g.db.execute("INSERT INTO vote(kind, upvote, downvote, type_id) VALUES(?, ?, ?, ?)",  (type, upvote, downvote, type_id))
    g.db.commit()
    g.db.close()

def set_downvote(new_upvote,new_downvote,postID):
    """Sets the new total number of up votes & down votes

    Args:
        new_upvote:Votes - the updated upvotes value
        new_downvote: Votes - the updated downvote value
        postID:Votes - the post ID from which the down votes, must be updated

    Return:
        N/A

    Raises:

    """
    g.db=connect_db()
    g.db.execute(''' UPDATE vote set upvote=?, downvote=? WHERE type_id=?''', (new_upvote,new_downvote,postID))
    g.db.commit()
    g.db.close()

def set_userID(postID,typeVote,userID):
    """Adds a new user to the table

    Args:
        postID:Votes - the post ID is used to get the vote ID
        typeVote:Votes - the vote value, "up","down", or "null"
        userID:Votes - the ID of the user being added

    Return:
        N/A

    Raises:

    """
 
    g.db=connect_db()
    voteID=getvoteid(postID)
    g.db.execute(' INSERT INTO votertype (vote_id, user_id,votetype) VALUES(?,?,?)',(str(voteID),str(userID),typeVote)) 
    g.db.commit()
    g.db.close()



#Notification SQL Queries 

def getUserId(username):
    """Get user_id from database through the database interface and returns an sqlite3.Row object.

    Args:
        username - the identifying username of the session holder.

    Simply retrieves the information from the database.
    """
    g.db = connect_db()
    cur = g.db.execute("SELECT id FROM user WHERE username=?", [username])
    users = cur.fetchone()
    g.db.close()
    return users

def addSub(user_id, topic_id):
    """Add user to list of subs to a topic with no return type.

    Args:
        topic_id - the identifying id of the topic in which the user wishes to subscribe.
        user_id - the key attribute designated to identify the user.


    Simply inserts the information into the database.
    """
    g.db = connect_db()
    g.db.execute("INSERT INTO subscription (user_id, topic_id) VALUES (?,?)", (user_id, topic_id))
    g.db.commit()
    g.db.close()

def removeSub(user_id, topic_id):
    """*Stub Implementation Only*

    Args:
        topic_id - the topic in which the user wishes to subscribe.
        user_id - the key attribute designated to identify the user.


    Only a stub implementation since no functionality has been given.
    """
    return

def addNotification(user_id, title, body, target, target_id):
    """Add the notification for the specified user into the database with no return type.

    Args:
        user_id - the key attribute designated to identify the user.
        title - the title text of the notification to be displayed.
        body - the body text of the notification to be displayed.
        target - the type of notification.
        target_id - the identifying id of the notification trigger.


    Simply inserts the information into the database.
    """
    g.db = connect_db()	
    cur = g.db.execute("INSERT INTO notification(title,user_id,body,target,target_id) VALUES(?,?,?,?,?)", (title,user_id,body,target,target_id))
    g.db.commit()
    g.db.close()

def getSubscribers(topic_id):
    """Retrieves all of the subscribers to a topic and returns an sqlite3.Row object.

    Args:
        topic_id - the identifying id of the topic in which the user wishes to subscribe

    Return:
        sqlite3.Row - contains (user_id)

    Calls the database to retrieve row objects of all subscribers to a topic.
    """
    g.db = connect_db()
    cur = g.db.execute("SELECT user_id FROM subscription WHERE topic_id=?", [topic_id])
    userIDs = cur.fetchall()
    g.db.close()

    return userIDs

def getNotifications(user_id):
    """Retrieves all of the notifications for a particular user and returns an sqlite3.Row object.

    Args:
        user_id - the key attribute designated to identify the user.

    Return:
        sqlite3.Row - contains (user_id, title, body, target, target_id)

    Calls the database to retrieve row objects of all notifications for a user.
    """
    g.db = connect_db()
    cur = g.db.execute("SELECT user_id,title,body,target,target_id FROM notification WHERE user_id=?", [user_id])
    notifications = cur.fetchall()
    g.db.close()

    return notifications















