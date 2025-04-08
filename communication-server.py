from flask import Flask, request

app = Flask(__name__)

@app.route('/stage', methods=['GET', 'POST'])
def stage():
    if request.method == 'GET':
        return request.args