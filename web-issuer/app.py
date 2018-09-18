from flask import Flask, Response, request

app = Flask(__name__)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


@app.route("/intro")
def intro():
    return Response("ok", mimetype="text/text")


app.run(debug=True)
