import json
import uuid

from flask import Flask
from flask import request
from flask import render_template


from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth


from database import SQLite
from errors import ApplicationError


app = Flask(__name__)

class User:
    def __init__(self,user_id,email,password,name,address,phone_number):
        self.user_id=user_id
        self.email=email
        self.password=password
	self.name=name
        self.address=address
        self.phone_number=phone_number
    
    @staticmethod
    def create_user(user_id, email,password,name, address, phone_number):
        result = None
        with SQLite() as db:
            result = db.execute("INSERT INTO user (username, password, email, address, phone_number) VALUES (?, ?, ?, ?, ?)",
                    (user_id,email, password,name, address, phone_number))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)
            
    @staticmethod
    def find(user_id):
        result = None
        with SQLite() as db:
            result = db.execute(
                    "SELECT username, password, id FROM user WHERE id = ?",
                    (user_id,))
        user = result.fetchone()
        if user is None:
            raise ApplicationError(
                    "Post with id {} not found".format(user_id), 404)
        return User(*user)

    
    @staticmethod
    def all():
        with SQLite() as db:
            result = db.execute(
                    "SELECT user_id,email, password,name,address,phone_number FROM user").fetchall()
            return [User(*row) for row in result]

    @staticmethod
    def delete(user_id):
        result = None
        with SQLite() as db:
            result = db.execute("DELETE FROM user WHERE id = ?",
                    (user_id,))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)

#    def save(self):
#        with SQLite() as db:
#        	cursor = db.execute(self.__get_save_query())
#        self.id = cursor.lastrowid
#        return self


#zasto mi kazva che podavam 6 argumenta kato se iskat 5(a te realno se iskat 6), a kato iztriq nqkoi ot argumentite mi kazva podal si 5 iskat se 6 ???????

	

Petko = User.create_user("33","p.dapchev09@abv.bg", generate_password_hash("pepi"), "Petko Dapchev", "Sofia","08")
print(User.find_by_id("33").id)




