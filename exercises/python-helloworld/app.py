from flask import Flask
from flask import json
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello 2021!"

@app.route("/status")
def checkStatus():
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def sayHealthy():
    return "{UserCount: 140, UserCountActive: 23}"
    
    
if __name__ == "__main__":
    app.run(host='0.0.0.0')
