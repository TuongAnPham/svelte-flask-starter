from flask import Flask , render_template, request, jsonify 
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

data = []

@app.route('/')
def hello_world():
    return 'server'

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