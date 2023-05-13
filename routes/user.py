from flask import Blueprint, jsonify, make_response, request, redirect, flash
from config.server_conf import db
from controllers.User import User_belongs_to_Community
from datetime import datetime

meetings = Blueprint("belong", __name__)

@meetings.route("/new", methods=['POST'])
def new_meet():
    User_belongs_to_Community.create_belong()
    return redirect("/")


