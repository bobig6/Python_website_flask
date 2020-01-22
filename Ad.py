import json
import uuid

from flask import Flask
from flask import request
from flask import render_template


from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth


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
        # put authentication here
        #-->
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


#ad = Ad("Prodavam moskvi4", "prodavam moskvi4. Pipnal sum go. Slojil sum mu v8 TDI i 22 colovi janti. 550 konq. VDIGA 250!!!!", 35000.0, "e predi malko", True, "Kolyo pi4a")
#obqva = Ad.create_ad("kolyo", "Obi4amKotki124", ad)
find = Ad.all()
print(find[0].title)
print(find[0].description)