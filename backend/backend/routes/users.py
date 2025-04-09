from backend.routes import basic_auth, token_auth
from backend.entity.user import User
from backend.extensions import db

from flask import Blueprint, jsonify, request, Response
from sqlalchemy import select

users_bp = Blueprint("users", __name__, url_prefix="/users")

@users_bp.route("", methods=["GET"])
@token_auth.login_required
def get_all_users():
    # all_users = [{"id": 1, "name": "joe"}, {"id": 2, "name": "bob"}]
    # all_users = User.query.all()


    # style 2.0
    all_users = db.session.scalars(select(User)).all()

    return jsonify(all_users)

@users_bp.route("", methods=["POST"])
@token_auth.login_required  # Changed from basic_auth to token_auth
def create_user():
    d = request.json
    print(d)
    return Response(status=204)
    # return jsonify(d), 201


@users_bp.route("/<int:user_id>", methods=["GET"])
@token_auth.login_required
def get_user(user_id):
    # 1.x styple
    # user = User.query.filter_by(id=user_id).one()

    # final though on ORM...it is crazy, it make simple thing slightly complicated
    # and make complicated thing even more complicated.
    # I will stick with raw SQL for now.


    user = db.session.get(User, user_id)
    if user:
        return jsonify(user)
    return Response(status=404)