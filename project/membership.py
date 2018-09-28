import Group

class membership:

    def __init__(self, membershipid, groupid, userid):
        self.membershipid = membershipid
        self.groupid = groupid
        self.userid = userid
        Groupmembers = {} #Dictionary for groupid: userid


    def getMemId(self):
        return self.membershipid
    
    def setMemId(self, membershipid): 
        self.membershipid = membershipid
         
    def getGroupID(self):
        return self.groupid
    
    def setGroupId(self, idn): 
        self.groupid = groupid

    def getUserid(self):
        return self.userid = userid

    def setUserid(self, idn):
        self.userid = userid


    def getMembers(self, groupid, userid):
        for membership in query_db('SELECT * from membership'):
            Groupmembers ['groupid'] = ['userid']

    
    @approute('/members_Of_A_Group')
    def AddUsers(self):
        db = get_db()
        db.execute('INSERT into membership (groupid, userid) values(?,?)',
                   [groupid, userid])

    @approute ('Remove member')    
    def removeUsers(self, userid):
        db.get_db()
        db.execute('DELETE FROM  membershp WHERE ID = ?', userid)
        


    
            
            
        
