from flask import Flask, jsonify, request
import uuid
from passlib.hash import pbkdf2_sha256
from main import database

class User:
    def sign_up(self):
        '''
            Returns:
                status code <int>
                    200 for success.
                    400 for failure.
            
        '''
        # user
        self._user = {
            "_id": uuid.uuid4().hex,        # generating the unique id using
            "name": request.form.get('name'),
            "email": request.form.get('email'),
            "password": request.form.get('password')
        }
        self._email = self._user.get('email')
        self._name = self._user.get('name')
        # encrypting the user password.
        self._user['password'] = pbkdf2_sha256.encrypt(self._user['password'])
        # inserting documents
        try: 
            database['todo_users'].insert_one(self._user)
        except Exception as e:
            return 400
        return 100    
    
    @property
    def get_user_name(self):
        return self._name
    @property
    def get_user_email(self):
        return self._email
    
