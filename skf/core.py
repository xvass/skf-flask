from controllers.dashboardcontroller import *
from controllers.projectcontroller import *
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

#Define api routes
api.add_resource(Login, '/')
api.add_resource(Dashboard, '/dashboard')
api.add_resource(Project, '/project')

if __name__ == '__main__':
    app.run(debug=True)