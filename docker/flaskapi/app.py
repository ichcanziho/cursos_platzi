from flask import Flask, request
from json import loads as decode_json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, Docker!'


@app.route("/api_saludar", methods=["POST"])
def saludar():
    args = decode_json(request.data)
    nombre = args["nombre"]
    return f"Hola {nombre}!"


# flask --app app run -p 8181
