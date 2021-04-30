from flask import Blueprint

hello_world_bp = Blueprint("hello_world", __name__)

@hello_world_bp.route("/hello-world", methods=["GET"])
def say_hello_world():
    response_body = "Hello, Kaylyn!"
    return response_body

@hello_world_bp.route("/hello-world-json", methods=["GET"])
def say_hello_json():
    return {
        "name": "MEEEEE",
        "message": "sup",
        "hobbies": ["Eating bread", "Killing plants", "Watching Bake-Off"]
    }