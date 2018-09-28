import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash
from project import topic_interface, post_interface, user_interface, Group_interface, VotesInterface, subscriptionInterface, notificationInterface
from project import db



app = Flask(__name__) # create the application instance :)
app.config.from_object(__name__)
app.secret_key = "secretkey"
database = db.Database()
app.config.update(dict(
    DATABASE=os.path.join(app.root_path, database.project_database)
))
app.config.from_envvar('PROJECT_SETTINGS', silent=True)
@app.route('/')
def index():
    topics = topic_interface.getTopics()
    return render_template('home.html', topics = topics)
    
@app.route('/topic/<int:topic_id>/posts')
def show_topicPosts(topic_id):
    posts = post_interface.getPosts(str(topic_id))
    topic = topic_interface.getTopicName(str(topic_id))
    return render_template('posts.html', posts=posts, topic=topic)
    
@app.route('/topic/<int:topic_id>/post/<int:post_id>/')
def show_post(topic_id, post_id):
    post = post_interface.getPost(str(post_id))
    topic = topic_interface.getTopicName(str(topic_id))
    upvotes=VotesInterface.getUpVotes(str(post_id))
    downvotes=VotesInterface.getDownVotes(str(post_id))
    return render_template('post.html', post=post, topic=topic,upvote=upvotes,downvote=downvotes)
    
@app.route('/createtopic/', methods=['GET', 'POST'])
def createtopic():
    if request.method == 'POST': 
        group_id = str(0)
        topic_interface.createTopic(request.form['topic'], user_interface.getLoggedInUser(), group_id)
        return redirect(url_for('index'))
    return render_template('createtopic.html')

@app.route('/topic/<int:topic_id>/edittopic', methods=['GET', 'POST'])
def editTopic(topic_id):
    print("edit topic")
    topic = topic_interface.getTopicName(str(topic_id))
    if request.method == 'POST':
        print("inside edit post Topic")
        topic_interface.editTopic(str(topic_id), request.form['topicname'])
        #post_interface.editPost("10", "new title", "new body")
        return redirect(url_for('show_topicPosts', topic_id=topic_id))

    return render_template('editTopic.html', topic=topic)   


@app.route('/topic/<int:topic_id>/createpost', methods=['GET', 'POST'])
def createpost(topic_id):
    if request.method == 'POST': 
        post_interface.createPost(topic_id, user_interface.getLoggedInUser(), request.form['title'], request.form['body'])
        notificationInterface.sendNotifications("post", topic_id)
        return redirect(url_for('index'))
    return render_template('createpost.html', topic_id=topic_id)

@app.route('/topic/<int:topic_id>/post/<int:post_id>/editpost', methods=['GET', 'POST'])
def editPost(topic_id, post_id):
    post = post_interface.getPost(str(post_id))
    if request.method == 'POST':
        print("inside edit post POST")
        post_interface.editPost(str(post_id), request.form['title'], request.form['body'])
        #post_interface.editPost("10", "new title", "new body")
        return redirect(url_for('show_post', topic_id=topic_id, post_id=post_id))
    return render_template('editPost.html', post=post)  
    
      
@app.route('/Addmember/<int:group_id>',methods=['GET','POST'])
def memberAdd(group_id):

    if user_interface.getIDFromUsername(request.form['uname']):
        if request.method == 'POST':
            userid = user_interface.getIDFromUsername(request.form['uname'])
            Group_interface.AddMemberToGroup(group_id,userid[0])
    else:
        flash("User Invalid")

    return redirect(url_for('creategroup'))


@app.route('/showgroup/<int:group_id>',methods=['GET', 'POST'])
def displaygroup(group_id):

    groupInfo = Group_interface.getAGroupInfo(str(group_id))
    print (groupInfo['created_by'])

    groupTopic =Group_interface.getGroupTopics(str(group_id))
    groupInfo = Group_interface.getAGroupInfo(str(group_id))

    if groupInfo['created_by'] == user_interface.getLoggedInUser():
        admin = True
    else:
        admin = False

    loggUser = user_interface.getIDFromUsername(user_interface.getLoggedInUser())
    loggedUserId = loggUser[0]

    if request.method == 'POST':
        topic_interface.createTopic(request.form['topic'], user_interface.getLoggedInUser(), group_id)
       

        return redirect(url_for('creategroup'))
    grouptopic = Group_interface.getGroupTopics(str(group_id))


    Members = Group_interface.getGroupMembers(group_id)



    return render_template('creategrouptopic.html',grouptopic=grouptopic,groupInfo=groupInfo, admin= admin,Members=Members,loggedUserId=loggedUserId)    
   


    


@app.route('/startgroup', methods=['GET', 'POST'])
def creategroup():
    if request.method == 'POST':
        if request.form['Group name']:
            groupName = request.form['Group name']
            Group_interface.createGroup(groupName, user_interface.getLoggedInUser())

            group_id = Group_interface.getGroupId(str(groupName))[0]

            userid = user_interface.getIDFromUsername(user_interface.getLoggedInUser())
            Group_interface.AddMemberToGroup(group_id,userid[0])


            print (user_interface.getLoggedInUser())

        
    groups = Group_interface.getGroups()
    
    
    return render_template('creategroup.html', groups=groups)







@app.route('/userProfile', methods=['GET', 'POST'])
def userProfile():
    user = user_interface.getUserInfoDict()
    if request.method == 'POST':
        username = user_interface.getLoggedInUser()
        logout()
        user_interface.deleteUser(username)
        return redirect(url_for('index'))
    return render_template('userInfo.html', user=user)
    
@app.route('/signup', methods=['GET', 'POST'])
def signup():
    """
    Let users create new username and password if username doesn't already exist
    """
    error = None
    if request.method == 'POST':
        username = request.form['username']
        if user_interface.isReserved(username):
            error = "You can't use that username."
        #print(user_interface.isUsernameTaken(request.form['username']))
        elif user_interface.isUsernameTaken(username):
            print("username already exists")
            error = 'Username already exists'
        else:        
            user_interface.createUser(username, request.form['password'], request.form['fname'], request.form['lname'])
            flash('Your account was successfully created. Please sign in to continue.')
            return render_template('login.html', error=None)
    return render_template('signup.html', error=error) 
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    Let users login
    """
    error = None
    if request.method == 'POST':
        if user_interface.authenticate(request.form['username'], request.form['password']):
            return redirect(url_for('index'))
        error = "Wrong username & password combination" 
    return render_template('login.html', error=error) 

@app.route('/logout')
def logout():
    user_interface.logout()
    flash('You were logged out')
    return redirect(url_for('index'))


#Voting
@app.route('/topic/<int:topic_id>/post/<int:post_id>/upvote/user/<string:username>')
def up_vote(topic_id,post_id,username):

    userId = user_interface.getUserId()[0]
    print(userId)
    VotesInterface.callUpVote(str(userId),str(post_id))
    ##return render_template(url_for('show_post', topic_id=topic_id, post_id=post_id))
    return redirect(url_for('show_post',post_id=post_id,topic_id=topic_id))   

@app.route('/topic/<int:topic_id>/post/<int:post_id>/downvote/user/<string:username>')
def down_vote(topic_id,post_id,username):

    userId = user_interface.getUserId()[0]
    print("downvote")
    VotesInterface.callDownVote(str(userId),str(post_id))
    ##return render_template(url_for('show_post', topic_id=topic_id, post_id=post_id))
    return redirect(url_for('show_post',post_id=post_id,topic_id=topic_id)) 

#Notifications
@app.route('/notifications')
def notifications():
    """Gets all notifications for a user to be rendered."""
    userId = user_interface.getUserId()[0]
    notifications = notificationInterface.getNotifications(str(userId))
    
    return render_template('notifications.html', notifications=notifications)

@app.route('/topic/<int:topic_id>/subscribe')
def subscribe(topic_id):
    """Adds user to subscription table."""
    userId = user_interface.getUserId()[0]
    subscriptionInterface.addSubscription(str(userId), str(topic_id))
    
    flash("You are now subscribed")
    return redirect(url_for('show_topicPosts', topic_id=topic_id))

if __name__ == '__main__':
    app.run(debug=True)
    
    
    
    
    
    
    
    
    
    
    
    
