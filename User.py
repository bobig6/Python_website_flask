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
        self.email=email
        self.password=password
        self.name=name
        self.address=address
        self.phone_number=phone_number


    def to_dict(self):
        user_data = self.__dict__
        del user_data["password"]
        return user_data

    @staticmethod
    def create_user(user, password, email, address, phone_number):
        result = None
        with SQLite() as db:
            result = db.execute("INSERT INTO user (username, password, email, address, phone_number) VALUES (?, ?, ?, ?, ?)",
                    (user, password, email, address, phone_number,))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)

    @staticmethod
    def find_by_username(username):
        result = None
        with SQLite() as db:
            result = db.execute(
                    "SELECT id, email, password, username, address, phone_number FROM user WHERE username = ?",
                    (username,))
        user = result.fetchone()
        if user is None:
            raise ApplicationError(
                    "Post with name {} not found".format(username), 404)
        return User(*user)
     
    @staticmethod
    def find_by_id(id):
        result = None
        with SQLite() as db:
            result = db.execute(
                    "SELECT id, email, password, username, address, phone_number FROM user WHERE id = ?",
                    (id,))
        user = result.fetchone()
        if user is None:
            raise ApplicationError(
                    "Post with id {} not found".format(id), 404)
        return User(*user)
	

    @staticmethod
    def edit(user_id, part_to_edit, value):
        if part_to_edit=="email" or part_to_edit=="password":
            raise ApplicationError("You can't change your email or password",404)
        elif part_to_edit=="username":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE user SET username = ? WHERE id = ?;",
                    (value, user_id,))

        elif part_to_edit=="address":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE user SET address = ? WHERE id = ?;",
                    (value, user_id,))

        elif part_to_edit=="phone_number":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE user SET phone_number = ? WHERE id = ?;",
                    (value, user_id,))   
        else:
            raise ApplicationError("{} doesnt exist".format(part_to_edit),404)
        

    @staticmethod
    def all():
        with SQLite() as db:
            result = db.execute(
                    "SELECT id, email, password, username, address, phone_number FROM user").fetchall()
            return [User(*row) for row in result]

    @staticmethod
    def delete(id):
        result = None
        with SQLite() as db:
            result = db.execute("DELETE FROM user WHERE id = ?",
                    (id,))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)







