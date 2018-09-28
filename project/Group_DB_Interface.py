import Users
import Group

class DB_Interface:

	def query_db(query, args=(), one=False):
		cur = get_db().execute(query, args)
		rv = cur.fetchall()
		cur.close()
		return (rv[0] if rv else None) if one else rv

	
        def deleteGroup(groupName):
            db = get_db()
            query_db( 'DELETE FROM group WHERE id = (?)', [groupName])
            db.commit()

        
            
            

    
