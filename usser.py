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
    def __init__(self,id,email,password,nama,address,phone_number):
		self.id=id
		self.email=email
		self.password=password
		self.nama=nama
		self.address=address
		self.phone_number=phone_number

    @staticmethod
    def create_user(id, email,password,nama, address, phone_number):
        result = None
        with SQLite() as db:
            result = db.execute("INSERT INTO user (id, email, password,nama, address, phone_number) VALUES (?, ?, ?, ?, ?, ?)",
                    (id,email, password,nama, address, phone_number))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)
            
    @staticmethod
    def find(id):
        result = None
        with SQLite() as db:
            result = db.execute(
                    "SELECT username, password, id FROM user WHERE id = ?",
                    (id,))
        user = result.fetchone()
        if user is None:
            raise ApplicationError(
                    "Post with id {} not found".format(id), 404)
        return User(*user)

    
	

	@staticmethod
	def edit(part_you_wish_to_edit):
		part_you_want_to_edit=raw_input("Enter the part you wish to edit:" )
	if part_you_wish_to_edit=="email" or part_you_wish_to_edit=="password":
		raise ApplicationError("You can't change your email or password",404)
	elif part_you_wish_to_edit=="nama":
		new_name=raw_input("Enter the nama you want:" )
		User.nama=new_name
	elif part_you_wish_to_edit=="address":
		new_address=raw_input("Enter your new address:" )
		User.address=new_address
	elif part_you_want_to_edit=="phone number":
		new_phone_number=raw_input("Enter your new number:")
		User.phone_number=new_phone_number


    @staticmethod
    def delete(id):
        result = None
        with SQLite() as db:
            result = db.execute("DELETE FROM user WHERE id = ?",
                    (id,))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)

#    def save(self):
#        with SQLite() as db:
#        	cursor = db.execute(self.__get_save_query())
#        self.id = cursor.lastrowid
#        return self


#zasto mi kazva che podavam 6 argumenta kato se iskat 5(a te realno se iskat 6), a kato iztriq nqkoi ot argumentite mi kazva podal si 5 iskat se 6 ???????
#dali edit raboti vupreki hamalskoto izpulnenie
#	

Petko = User.create_user("33","p.dapchev09@abv.bg", generate_password_hash("pepi"), "Petko Dapchev", "Sofia","08")
print(User.find_by_id("33").id)

