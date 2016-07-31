from config.sqlite import * 

class Projects:
        
    def GetProjects(self):
	    db = database_con()
	    cur = db.execute('SELECT ProjectId, ProjectName, ProjectVersion, ProjectDescription, UserId FROM Projects')
	    return cur.fetchall()
    
    def InsertProject(self, projectName, projectVersion, projectDescription, UserId):
        db = database_con()
        db.execute('INSERT INTO projects (ProjectName, ProjectVersion, ProjectDescription, UserId) VALUES (?, ?, ?, ?)',
								[projectName, projectVersion, projectDescription, UserId])
        db.commit()