"""Test module for project

Includes at least 3 test methods for each module in project
"""

import os
import project
from project import db, user, topic, Group, post, notification, subscription, Votes
import unittest
import tempfile

class ProjectTestCase(unittest.TestCase):
    
    def setUp(self):
        """Setup new databse for test methods
           Populate the database with at least one record per table for testing
        """
        self.db_fd, project.app.config['DATABASE'] = tempfile.mkstemp()
        project.app.testing = True
        self.app = project.app.test_client()
        with project.app.app_context():
            db.Database().create_tables()
            user.createUser('adminTest', 'tcg1134', '', '')
            user.createUser('adminTest2', 'gct2334', '', '')
            Group.createGroup('TestGroup', 'adminTest2')
            topic.insertTopic('TestTopic', 'adminTest2', '1')
            post.insertPost(1, 'adminTest2', 'TestPost', 'Some random text')
            subscription.addToSub(1,1)
            notification.sendNotif("post", 1)
            Votes.upvote(1, 1)
            
            
    def tearDown(self):
        """
        Close database connection
        """
        os.close(self.db_fd)
        os.unlink(project.app.config['DATABASE'])


    def convertRowObjectsToLists(rowObjects):
        allRows = []
        for aRow in rowObjects:
            allRows.append(list(aRow))
        return allRows



#---------------------------    
#test methods for project.py
#---------------------------
    def test_empty_db(self):
        """Test if the database is empty

        Notes
        -----
            Since the topic and post table have been populated in the 
            setup method, this test method tests if those tables are NOT empty.
            This method can also be used to check if they ARE empty by changing 
            'not in' to in, and removing the lines that add posts and topics in
            the setup method. When there are no posts, the page should display
            'Start a discussion'.
        """
        rv = self.app.get('/')
        assert b'Start A Discussion' not in rv.data


    def login(self, username, password):
        """
        Helper method for test_login()
        """
        return self.app.post('/login', data=dict(
            username=username,
            password=password
        ), follow_redirects=True)


    def logout(self):
        """
        Helper method for test_logout()
        """
        return self.app.get('/logout', follow_redirects=True)


    def test_login(self):
        """
        Tests if the login function works with an existing account
        """
        rv = self.login('adminTest2', 'gct2334')
        assert b'Interesting Topics' in rv.data

    def test_logout(self):
        """
        Tests if the logout function works
        """
        rv = self.logout()
        assert b'You were logged out' in rv.data

#------------------------    
#test methods for user.py
#------------------------
    def test_isUsernameTaken(self):
        """
	Tests the isUsernameTaken function to see if a username already exists
        """
        with project.app.app_context():
            self.assertTrue(user.isUsernameTaken('adminTest2'))


    def test_isReserved(self):
        """
	Tests the isReserved function to see if the function returns True if
        provided a reserved username
        """
        with project.app.app_context():
            self.assertTrue(user.isReserved('RemovedAccount'))


    def test_authenticate(self):
        """
        Tests the authenticate function to see if it returns False when an 
        unregistered username is entered
        """
        with project.app.app_context():
            self.assertFalse(user.authenticate('Random', 'password'))


    def test_get_ID_from_username(self):
        """
        Tests the getIDFromUSername function to see if it returns the correct ID
        """
        with project.app.app_context():
            self.assertEqual(user.getIDFromUsername('adminTest2')[0], 2)

#-------------------------    
#test methods for topic.py
#-------------------------
    def test_getTopicName(self):
        """
	Tests the getTopicName function to see if it returns the correct topic name
        """
        with project.app.app_context():
            self.assertEqual(topic.getTopicName(1)[1], 'TestTopic')


    def test_getTopics(self):
        """
	Tests the getTopics function to see if it returns the correct list of topics
        """
        with project.app.app_context():
            allTopics = []
            for atopic in topic.getTopics():
                allTopics.append(list(atopic))
            self.assertEqual(allTopics, [[1, 'TestTopic', 1]])


#-------------------------    
#test methods for Group.py
#-------------------------
    def test_Group_created_by(self):
        """
	Tests the Group_created_by function to see if it returns the correct username
        """
        with project.app.app_context():
            self.assertEqual(Group.Group_created_by('TestGroup')[0], 'adminTest2')

    
    def test_getGroupId(self):
        """
	Tests the getGroupId function to see if it returns the correct id
        """
        with project.app.app_context():
            self.assertEqual(Group.getGroupId('TestGroup')[0], 1)


    def test_getGroupTopics(self):
        """
	Tests the getGroupTopics function to see if it returns the correct list of topics
        """
        with project.app.app_context():
            allTopics = []
            for atopic in Group.getGroupTopics(1):
                allTopics.append(list(atopic))
            self.assertEqual(allTopics, [[1, 'TestTopic', 1]])



#------------------------    
#test methods for post.py
#------------------------
    def test_getPost(self):
        """
	Tests the getPost function to see if it returns the correct post information
        given a post id
        """
        with project.app.app_context():
            self.assertEqual(post.getPost(1)[3], 'TestPost')


    def test_getPosts(self):
        """
	Tests the getPosts function to see if it returns the correct list of posts
        given a topic id
        """
        with project.app.app_context():
            allPosts = []
            for aPost in post.getPosts(1):
                desc = list(aPost)
                allPosts.append([desc[0], desc[2], desc[3]])
            self.assertEqual(allPosts, [[1, 'TestPost', 'Some random text']])


    def test_editPost(self):
        """
	Tests the editPost function to see if it correctly edits a post given its
        post id
        """
        with project.app.app_context():
            post.editPost(1, "TestPost", "Edited")
            allPosts = []
            for aPost in post.getPosts(1):
                desc = list(aPost)
                allPosts.append([desc[0], desc[2], desc[3]])
            self.assertEqual(allPosts, [[1, 'TestPost', 'Edited']])


#--------------------------------    
#test methods for notification.py
#--------------------------------
    def test_getNotifications(self):
        """
	Tests the getNotifications function to see if it correctly retrieves all
        notifications for the user with the given user id
        """
        with project.app.app_context():
            allnotif = []
            for aNotif in notification.getNotifications(1):
                desc = list(aNotif)
                allnotif.append([desc[2]])
            self.assertEqual(allnotif, [['A new post has been created in TestTopic']])

    



#------------------------    
#test methods for Votes.py
#------------------------
    def test_ifEmpty(self):
        """
	Tests the ifEmpty function to see if a certain post has been voted up/down
        by any user yet
        """
        with project.app.app_context():
            self.assertFalse(Votes.ifEmpty(1))


    def test_checkvotevalue(self):
        """
	Tests the checkvotevalue function to see if it correctly restricts a user
        from casting the same vote (up/down) on a particular post, more than once
        """
        with project.app.app_context():
            self.assertTrue(Votes.checkvotevalue(1, 1, 'up'))


    def test_get_uv(self):
        """
	Tests the get_uv function to see if the function returns the correct number
        up votes for a given post
        """
        with project.app.app_context():
            self.assertEqual(Votes.get_uv(1), 1)


    def test_get_dv(self):
        """
	Tests the get_dv function to see if the function returns the correct number
        down votes for a given post
        """
        with project.app.app_context():
            self.assertEqual(Votes.get_dv(1), 0)


        
if __name__ == '__main__':
    unittest.main()
        
    
