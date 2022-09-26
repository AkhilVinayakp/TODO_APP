from flask import Flask, jsonify

class User:
    def sign_up(self):
        '''
            Returns:
                objects containing the details
                status code <int>
                    200 for success.
                    400 for failure.
            
        '''
        # user object
        user = {
            "_id": "",
            "name": "",
            "email": "",
            "password": ""
        }
        return jsonify(user), 200  # test code
    