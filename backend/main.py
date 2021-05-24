from flask import Flask , render_template, request, jsonify 
app = Flask(__name__)

data = []

@app.route('/')
def hello_world():
    return render_template('Home.svelte')

# @app.route('/message')
# def message():
#     return render_template('Chat.svelte', text = data)

# @app.route('/receive')
# def receive():
#     data.append(request.args['whatever'])
#     return render_template('Chat.sveltel', text = data)

app.run(host='127.0.0.1', port=8080)