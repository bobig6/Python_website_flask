import json
import uuid

from flask import Flask
from flask import request
from flask import render_template


from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth

import basic_auth

from database import SQLite
from errors import ApplicationError
#import basic_auth

class Ad:
    def __init__(self, title, description, price, date, isActive, buyer):
        self.title = title
        self.description = description
        self.price = price
        self.date = date
        self.isActive = isActive
        self.buyer = buyer


    @staticmethod
    def create_ad (user, password, newAd):
        result = None
        with SQLite() as db:
            result = db.execute("INSERT INTO ads (title, description, price, date, isActive, buyer) VALUES (?, ?, ?, ?, ?, ?)",
                    (newAd.title, newAd.description, newAd.price, newAd.date, newAd.isActive, newAd.buyer,))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)
        


            
    @staticmethod
    def find_by_id(id):
        result = None
        with SQLite() as db:
            result = db.execute(
                    "SELECT title, description, price, date, isActive, buyer FROM ads WHERE id = ?",
                    (id,))
        ad = result.fetchone()
        if ad is None:
            raise ApplicationError(
                    "Ad with id {} not found".format(ad), 404)
        return Ad(*ad)

    @staticmethod
    def all():
        with SQLite() as db:
            result = db.execute(
                    "SELECT title, description, price, date, isActive, buyer FROM ads").fetchall()
            return [Ad(*row) for row in result]


    @staticmethod
    def edit(ad_id, part_to_edit, value):
        if part_to_edit=="title":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE ads SET title = ? WHERE id = ?;",
                    (value, ad_id,))

        elif part_to_edit=="description":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE ads SET description = ? WHERE id = ?;",
                    (value, ad_id,))

        elif part_to_edit=="price":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE ads SET price = ? WHERE id = ?;",
                    (value, ad_id,)) 

        elif part_to_edit=="date":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE ads SET date = ? WHERE id = ?;",
                    (value, ad_id,))  

        elif part_to_edit=="isActive":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE ads SET isActive = ? WHERE id = ?;",
                    (value, ad_id,)) 

        elif part_to_edit=="buyer":
            with SQLite() as db:
                result = db.execute(
                    "UPDATE ads SET buyer = ? WHERE id = ?;",
                    (value, ad_id,))  
        else:
            raise ApplicationError("{} doesnt exist".format(part_to_edit),404)
        

    @staticmethod
    def delete(id):
        result = None
        with SQLite() as db:
            result = db.execute("DELETE FROM ads WHERE id = ?",
                    (id,))
        if result.rowcount == 0:
            raise ApplicationError("No value present", 404)








