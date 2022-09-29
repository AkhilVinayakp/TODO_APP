from this import d
from flask import Flask, jsonify, request, session, redirect
import uuid
from passlib.hash import pbkdf2_sha256
from pymongo import MongoClient


class User:
    
    def __init__(self) -> None:
        self._mongoclient =  MongoClient('mongodb://localhost:27017/')
        self._database = self._mongoclient['Sample']
        self._user_collection = self._database['todo_users']

    def _create_session(self):
        '''creating session upon sucessfull sign in'''
        session['logged_in'] = True
        del self._user['password']
        session['user'] = self._user
        return 200
    


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
           self._user_collection.insert_one(self._user)
        except Exception as e:
            return 400
        return self._create_session()
    
    @property
    def get_user_name(self):
        return self._name
    @property
    def get_user_email(self):
        return self._email
    
