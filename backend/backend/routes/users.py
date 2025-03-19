
from flask import Blueprint, Response, jsonify, request


users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["POST"])
def get_all_users():
    all_users = [{"id":1, "name": "bob"}, {"id":2, "name": "foo"}]
    return jsonify(all_users), 200

@users_bp.route("", methods=["POST"])
def create_user():
    d =request.json
    print(d)
    return Response(status=204)
    # return jsonify(d), 201