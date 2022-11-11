from flask import Flask, jsonify
import requests

app = Flask(__name__)

@app.route("/service")

def get():
    r = requests.get("http://google.com")
    print(r.content)
    return jsonify({"status" : "OK", "length" : len(r.content)})