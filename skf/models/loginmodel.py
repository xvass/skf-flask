from config.sqlite import * 

class users:

    def __init__(self, _username, _password):
        self._username = _username
        self._password = _password
    
    def GetUsers(self):
	    db = database_con()
	    cur = db.execute('SELECT UserId, UserName, Password FROM Users WHERE UserName=?',
	                      					  [self._username])
	    return cur.fetchall()
