import azure.functions as func
from flask import Flask

from flask_cors import CORS

from routes import register_blueprints
from .config import Config

app = Flask(__name__)
CORS(app)
app = register_blueprints(app)

main = func.WsgiMiddleware(app.wsgi_app).main


@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
    response.headers['Content-Type'] = 'application/json'
    return response


if __name__ == '__main__':
    app.run(debug=Config.DEBUG)
