from flask import Response, jsonify, request
from backend import create_app

app = create_app()

@app.route("/health", methods=["GET"])
def health():
    return "OK", 200

@app.route("/users", methods=["POST"])
def get_all_users():
    all_users = [{"id":1, "name": "bob"}, {"id":2, "name": "foo"}]
    return jsonify(all_users), 200

@app.route("/users", methods=["POST"])
def create_user():
    d =request.json
    print(d)
    return Response(status=204)
    # return jsonify(d), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1")