import json
import uuid

from flask import Flask
from flask import request
from flask import render_template


from User import User
from Ad import Ad

from basic_auth import generate_password_hash
from basic_auth import init_basic_auth


app = Flask(__name__)
auth = init_basic_auth()

@app.route("/api/users", methods = ["POST"])
def create_user():
    user_data = request.get_json(force=True, silent=True)
    if user_data == None:
        return "Bad request", 400
    hashed_password = generate_password_hash(user_data["password"])
    User.create_user(user_data["username"], hashed_password, user_data["email"],user_data["address"],user_data["phone_number"])
    return "Success", 200

@app.route("/api/users/<user_id>", methods = ["GET"])
def get_user(user_id):
    return json.dumps(User.find_by_id(user_id).to_dict())


@app.route("/api/users", methods = ["GET"])
def all_users():
    result = {"result": []}
    for user in User.all():
        result["result"].append(user.to_dict())
    return json.dumps(result)


@app.route("/api/users/<user_id>", methods = ["PATCH"])
def update_user(user_id):
    user_data = request.get_json(force=True, silent=True)
    if user_data == None:
        return "Bad request", 400

    if "username" in user_data:
        User.edit(user_id, "username", user_data["username"])
    if "address" in user_data:
        User.edit(user_id, "address", user_data["address"])
    if "phone_number" in user_data:
        User.edit(user_id, "phone_number", user_data["phone_number"])

    return "Success", 200


@app.route("/api/users/<user_id>", methods = ["DELETE"])
def delete_user(user_id):
    User.delete(user_id)
    return "Success", 200





@app.route("/api/ads", methods = ["POST"])
@auth.login_required
def create_ad():
    ad_data = request.get_json(force=True, silent=True)
    if ad_data == None:
        return "Bad request", 400
    user_id = User.find_by_username(auth.username()).id
    ad = Ad(user_id, ad_data["title"], ad_data["description"], ad_data["price"], ad_data["date"], ad_data["isActive"], ad_data["buyer"])
    Ad.create_ad(ad)
    return json.dumps(ad.to_dict()), 201

@app.route("/api/ads/<ad_id>", methods = ["GET"])
def get_ad(ad_id):
    return json.dumps(Ad.find_by_id(ad_id).to_dict())


@app.route("/api/ads", methods = ["GET"])
def all_ads():
    result = {"result": []}
    for ad in Ad.all():
        result["result"].append(ad.to_dict())
    return json.dumps(result)


@app.route("/api/ads/<ad_id>", methods = ["PATCH"])
@auth.login_required
def update_ad(ad_id):
    ad_data = request.get_json(force=True, silent=True)
    if ad_data == None:
        return "Bad request", 400

    if(User.find_by_username(auth.username()).id == Ad.find_by_id(ad_id).user_id):
        if "title" in ad_data:
            Ad.edit(ad_id, "title", ad_data["title"])
        if "description" in ad_data:
            Ad.edit(ad_id, "description", ad_data["description"])
        if "price" in ad_data:
            Ad.edit(ad_id, "price", ad_data["price"])
        if "date" in ad_data:
            Ad.edit(ad_id, "date", ad_data["date"])
        if "isActive" in ad_data:
            Ad.edit(ad_id, "isActive", ad_data["isActive"])
        if "buyer" in ad_data:
            Ad.edit(ad_id, "buyer", ad_data["buyer"])
        return "Success", 200
    else:
        return "Permission Denied", 550


@app.route("/api/ads/<ad_id>", methods = ["DELETE"])
@auth.login_required
def delete_ad(ad_id):
    if(User.find_by_username(auth.username()).id == Ad.find_by_id(ad_id).user_id):
        Ad.delete(ad_id)
        return "Success", 200
    else:
        return "Permission Denied", 550




