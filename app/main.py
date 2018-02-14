from flask import Flask, Response, request

from sphttp import Downloader

app = Flask(__name__)


@app.route('/proxy')
def proxy():
    string = request.args['host']
    hosts = string.split(',')
    d = Downloader(urls=hosts)
    gen = d.generator()
    return Response(gen, mimetype='application/octet-stream')


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True, port=8080)
