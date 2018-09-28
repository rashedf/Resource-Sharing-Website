from project import Group


def createGroup(name, created_by):
        """Creates a group
        Args:
                name - String - Name of the group
                created_by  -String  - Usename of the group creator
        Return:
                None
        Rasies:

        """
        Group.createGroup(name, created_by)
        

def getGroupName(Id):
        """Get the group name when given the id
                Args:
                        id - int - Group idenitification number
                Return:
                        Group name

                Rasies:

        """
        return "Group name"

def getGroupSize(Id):
        """Gets the amount of users in a group
                Args:
                        id - int - Group idenitification number
                Return:
                        number of users in a group 
        """
        return "Number of groups"

def Group_created_by(Groupname):
        """Gets the name of the user that created the group
                Args:
                        Groupname - String - the name of the group
                Return:
                        Usename of the group creator 
        """
        return Group.Group_created_by(Groupname)

def getGroups():
        """Gets the all the groups in the database
                Args:
                        None
                Return:
                        List of groups created 
                        
        """
        return Group.getGroups()


def deleteGroup(groupName):
        """Delete a group from the database
                Args:
                        Groupname - String - the name of the group
                Return:
                        None 
        """
        Group.deleteGroup(groupName)


def getGroupTopics(group_id):
        """Gets the id, name, created_by attributes of a group
                Args:
                        Groupid - int - the group id number
                Return:
                        id, name, created_by of the group 
        """       
        return Group.getGroupTopics(group_id)

def getAGroupInfo(group_id):
        """Gets the id, name, created_by attributes of a group
                Args:
                        Groupid - int - the group id number
                Return:
                        id, name, created_by of the group 
        """
        return Group.getAGroupInfo(group_id)

def AddMemberToGroup(group_id,user_id):
        """This function adds a user to a group

                args:
                        group_id    Int     the group id number
                        user_id     Int     the user id number
    
                Return:
                        None
        """
        Group.AddMemberToGroup(group_id,user_id)

def getGroupId(groupName):
        """This function gets a group id number
    
                args:
                        name    String      the group name

                Return:
                        GroupId     Int     the group id number
        """
        return Group.getGroupId(str(groupName))

def getGroupMembers(group_id):
        """This function gets the user_id of a members of a particular group

                args:
                        group_id    int     the group id number

                Return:
                        members     List    A list containing (membership_id, user-id, group_id) attributes of a user
    
    """
        return Group.getGroupMembers(group_id)

