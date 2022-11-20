from flask import Flask

def create_app():
    app = Flask("abc")

    @app.route('/')
    def hello_world():
        return 'Hello, World!'