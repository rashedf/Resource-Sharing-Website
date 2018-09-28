import datetime
from project import dbInterface
def createGroup(Groupname, created_by):
    """Creates a group
    Args:
            name - String - Name of the group
            created_by  -String  - Usename of the group creator
    Return:
            None
    Rasies:

    """
    dbInterface.createGroup(Groupname, created_by)

def getGroups():
    """Gets the all the groups in the database
            Args:
                    None
            Return:
                    List of groups created 
    """
    return dbInterface.getGroups();

def Group_created_by(Groupname):
    """Gets the name of the user that created the group
            Args:
                    Groupname - String - the name of the group
            Return:
                    Usename of the group creator 
    """
    return dbInterface.Group_created_by(GroupName)

def deleteGroup(groupName):
    """Delete a group from the database
            Args:
                    Groupname - String - the name of the group
            Return:
                    None 
    """
    dbInterface.deleteGroup(groupName)


def getGroupTopics(group_id):
    """Gets the id, name, created_by attributes of a group
            Args:
                    Groupid - int - the group id number
            Return:
                    id, name, created_by of the group 
    """ 
    return dbInterface.getGroupTopics(group_id)

def getAGroupInfo(group_id):
    """Gets the id, name, created_by attributes of a group
            Args:
                    Groupid - int - the group id number
            Return:
                    id, name, created_by of the group 
    """
    return dbInterface.getAGroupInfo(group_id)

def AddMemberToGroup(group_id,user_id):
    """This function adds a user to a group
        args:
             name    String      the group name
        Return:
             GroupId     Int     the group id number
    """
    dbInterface.AddMemberToGroup(group_id,user_id)

def getGroupId(groupName):
        return dbInterface.getGroupId(str(groupName))

def getGroupMembers(group_id):
        return dbInterface.getGroupMembers(group_id)