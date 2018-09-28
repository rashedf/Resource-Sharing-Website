import Users
import membership
import Group
import db


class DB_Interface:

	def query_db(query, args=(), one=False):
		cur = get_db().execute(query, args)
		rv = cur.fetchall()
		cur.close()
		return (rv[0] if rv else None) if one else rv

	def addNewMember(Mem):
            query_db('INSERT into membership (membership_id, group_id, user_id)  VALUES (?, ?, ?)',
                     [Mem.(), Mem.getGroupID(), Mem.getUserid()])

        def removerMember(Mem):
            db = get_db()
            query_db( 'DELETE FROM membership WHERE id = (?)', [Mem.getMemId()])
            db.commit()
