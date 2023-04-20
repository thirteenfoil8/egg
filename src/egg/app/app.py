from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random



def create_app():
    app = Flask(__name__, static_url_path='/static')
    # Register blueprints here
    from egg.app.main import bp as main_bp
    app.register_blueprint(main_bp)
    return app
if __name__ == "__main__":
    app = create_app()
    app.run(port="5000")