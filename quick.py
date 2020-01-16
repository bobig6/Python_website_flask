import json
import uuid

from flask import Flask
from flask import request
from flask import render_template
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3 as sqlite



app = Flask(__name__)

class User:
	def __init__(self,id,email,password,name,address,phone_number):
		self.id=id
		self.email=email
		self.password=password
		self.name=name
		self.address=address
		self.phone_number=phone_number

Petko = User(19,"p.dapchev09@abv.bg",generate_password_hash("pepi"),"Petko Dapchev","Sofia","088")


