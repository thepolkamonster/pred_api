from flask import request, render_template
from flask_smorest import Blueprint, abort
from flask import jsonify
from flask.views import MethodView

blp = Blueprint("routes", __name__, description = "The main routes Blueprint")

#-------------------
@blp.route('/')
def index():
    return 0

@blp.route('/api/<int:id_req>', methods = ['GET', 'POST'])
def predict(id_req):
    return jsonify(id_req)

