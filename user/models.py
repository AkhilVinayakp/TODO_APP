from flask import Flask, jsonify, request
import uuid
from config import logging

class User:
    def sign_up(self):
        '''
            Returns:
                objects containing the details
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
        return jsonify(self._user), 200    
    
    @property
    def get_user_name(self):
        return self._name
    @property
    def get_user_email(self):
        return self._email
    
