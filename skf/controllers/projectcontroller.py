from flask_restful import Resource, Api, reqparse, inputs
from logincontroller import Login
from models.projectmodel import *
from flask import Flask, jsonify
import json

class Project(Resource):   
    def get(self):
        #validate jwt token and check for permissions
        validate = Login()
        if validate.ValidateLogin("projects") != True:
            return validate.ValidateLogin("projects")
        project = Projects();
        #get projects from DB
        getprojects = project.GetProjects()
        projectList = []
        #append json to object array for returning
        for values in getprojects:  
            project = {"ProjectId": values[0], "projectName": values[1], "projectVersion": values[2], "projectDesc": values[3], "UserId": values[4]}
            projectList.append(project)
        return jsonify(projects = projectList)
        
    def post(self):
        validate = Login()
        #Validate token as wel as claims : projects
        if validate.ValidateLogin("projects") != True:
            return validate.ValidateLogin("projects")
        #parse and check values comming in from client
        parser = reqparse.RequestParser()
        parser.add_argument('projectName',    type=inputs.regex('^[ a-zA-Z0-9]+$'), help='projectName contains invalid chars, or was left empty')
        parser.add_argument('projectVersion', type=inputs.regex('^[ a-zA-Z0-9]+$'), help='project version was empty')
        parser.add_argument('projectDesc')
        args = parser.parse_args()
        data = Projects()
        #get current userid from jwt
        UserId = validate.SelectUserIdFromJWT()
        #pass data to model for insertion
        data.InsertProject(args['projectName'], args['projectVersion'], args['projectDesc'], UserId)        
        return {"Success": args},200
        