from flask import Flask , render_template, request, jsonify, send_from_directory
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

data = []

# Path for our main Svelte page
@app.route("/")
def base():
    return send_from_directory('public', 'index.html')

@app.route("/about")
def about():
    return render_template('home.html')

# Path for all the static files (compiled JS/CSS, etc.)

@app.route("/<path:path>")
def home(path):
    return send_from_directory('public', path)

# @app.route('/message')
# def message():
#     return render_template('Chat.svelte', text = data)

@app.route('/receive')
def receive():
    data.append(request.args['whatever'])
    return jsonify(data)

@app.route('/get')
def get():
    return jsonify(data)

app.run(host='127.0.0.1', port=8080)