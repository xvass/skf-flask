from flask_restful import Resource, Api
from models.loginmodel import *
from flask.ext.bcrypt import Bcrypt
from flask import Flask, request
from datetime import date, datetime, timedelta
import jwt


app = Flask(__name__)
bcrypt = Bcrypt(app)

#When supplied with valid credentials it returns a JWT
class Login(Resource):
    def get(self):
        #Variables will be get from angular same goes for password
        user = users("Riiecco", "")
        #if it returns true set session
        data = user.GetUsers()
    	for validate in data:
    		#validate password
            password = validate[2]
            if(bcrypt.check_password_hash(password, 'Welkom01') == True):
                #set claims and other information into jwt token
                payload = {
            # subject
            'UserId': validate[0],
            # userid
            'sid': validate[1],
            #issued at
            'iat': datetime.utcnow(),
            #expiry
            'exp': datetime.utcnow() + timedelta(minutes=50),
            #claims temp hardcoded
            'claims': 'projects, dashboard'
            }
            token = jwt.encode(payload, 'drol', algorithm='HS256')
            #temp token print for copy pasting into postman
            print token
            return jwt.decode(token, 'drol', algorithms='HS256')
    
    #Validates the JWT and permissions
    def ValidateLogin(self, restriction):
        if not request.headers.get('Authorization'):
            return {"error":"Missing autentication header"}, 401
        try:
            token = request.headers.get('Authorization').split()[1]
            checkClaims = jwt.decode(token, 'drol', algorithms='HS256')
        except jwt.exceptions.DecodeError:
			return {"error":"token could not be decoded"}, 401
        except jwt.exceptions.ExpiredSignature:
            return {"error":"token is expired"}, 401
        #check the users permissions    
        permissions = checkClaims['claims'].split(',')
        for value in permissions:
            if value == restriction:
                return True
        return {"error":"Invalid permissions"}, 403
    
    #function for returning the users id
    def SelectUserIdFromJWT(self):
        token = request.headers.get('Authorization').split()[1]
        checkClaims = jwt.decode(token, 'drol', algorithms='HS256')
        return checkClaims['UserId']
        