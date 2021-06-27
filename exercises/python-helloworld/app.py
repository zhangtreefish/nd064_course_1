from flask import Flask
from flask import json
from flask import request
from flask import render_template
import logging
app = Flask(__name__)

@app.route("/")
def hello():
    app.logger.info(request.endpoint + ' has been reached')
    return "Hello 2021!"

@app.route("/status")
def checkStatus():
    app.logger.info('Inside /status endpoint')
    response = app.response_class(
        response=json.dumps({"result":"OK - healthy"}),
        status=200,
        mimetype='application/json'
    )
    app.logger.info('Status request successfull')
    return response

@app.route("/metrics")
def sayHealthy():
    app.logger.info('Inside /metrics endpoint')
    app.logger.debug('metrics request successfull again!')
    app.logger.info('metrics request successfull')
    return "{UserCount: 140, UserCountActive: 23}"
    
    
if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG, format=f'%(asctime)s  %(message)s')
    app.run(host='0.0.0.0')
