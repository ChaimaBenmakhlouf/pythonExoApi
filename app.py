from flask import Flask, jsonify, request
import overpass
api = overpass.API()


app = Flask(__name__)
# def settings():
#     return 'settings'

@app.route('/')
def hello():
    return 'hello world'

@app.route("/api/")
def api_root():
    return jsonify({"restos": "http://127.0.0.1:5000//api/restos/"})


@app.route("/api/restos/")
def restos():
    return 'Hello world'

@app.route("/api/restos/<city>", methods=["GET", "PUT"])
def store(city):
    if request.method == "GET":
        response = api.get(f"""area[name={city}]; node[amenity=restaurant](area);""")
        return response