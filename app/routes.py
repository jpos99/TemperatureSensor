from flask import render_template, request
from app import app

request_data = {}

@app.route('/')
def visualizer_data():
    print('data = ', request_data)
    return render_template('index.html', data=request_data)


@app.route('/receive_data', methods=['POST'])
def receive_from_esp():
    global request_data
    content_type = request.headers.get('Content-Type')
    if content_type == 'application/json':
        request_data = request.json
        return "ok"

    else:
        return "notOk"
