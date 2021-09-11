from flask import Flask, render_template
import os 

# instance relative config tells app that there are config files or secret files relative to instance path outside of 'website'
def create_app(test_config=None):
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    return app