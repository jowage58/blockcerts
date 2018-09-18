from flask import Flask, Response, request

app = Flask(__name__)


@app.before_request
def log_request_info():
    app.logger.debug('Headers: %s', request.headers)
    app.logger.debug('Body: %s', request.get_data())


@app.route("/intro", methods=['GET', 'POST'])
def intro():
    return Response("ok", mimetype="text/text")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
