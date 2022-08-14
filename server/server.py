from flask import Flask, make_response, redirect
import yaml
try:
    from yaml import CLoader as Loader
except ImportError:
    from yaml import Loader
import importlib

import helpers
import generic_routes

# Load config
with open("config.yaml") as f:
    config = yaml.load(f.read(), Loader=Loader)

# Create app
app = Flask(__name__)

app.config.update(
    SEND_FILE_MAX_AGE_DEFAULT=0,
)

# Route home
@app.route("/")
def home():
    return generic_routes.home()

@app.route("/favicon.png")
def favicon():
    return generic_routes.favicon()

@app.route("/robots.txt")
def robots():
    return generic_routes.robots()

# Route challenges
@app.route("/challenge", methods=["GET", "POST"])
def challenge():
    chall, flag, _ = helpers.get_challenge(config)
    if chall == "_win":
        return generic_routes.win()

    module_name = "chall." + chall
    module = importlib.import_module(module_name, package=__package__)
    return module.challenge(flag, helpers.next_challenge(config))

# Route static files
@app.route("/s/<path:name>", methods=["GET"])
def static_route(name):
    chall, _, _ = helpers.get_challenge(config)
    if chall == "_win":
        return helpers.serve_static(name)

    module_name = "chall." + chall
    module = importlib.import_module(module_name, package=__package__)
    return module.static(name)

