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
	def __init__(self,id,email,password,name,address,phone_number):
		self.id=id
		self.name=name
		self.email=email
		self.password=password
		self.address=address
		self.phone_number=phone_number

	def save(self):
		with SQLite() as db:
		cursor = db.execute(self.__get_save_query())
		self.id = cursor.lastrowid
		return self

	@staticmethod
    def create_user(user, password, email, address, phone_number):
        result = None
        with SQLite() as db:
            result = db.execute("INSERT INTO user",
                    (user_id,))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)



	

Petko = User(19,"p.dapchev09@abv.bg",generate_password_hash("pepi"),"Petko Dapchev","Sofia","088")


