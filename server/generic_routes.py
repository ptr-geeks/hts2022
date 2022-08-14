from flask import send_from_directory

import helpers


def home():
    return helpers.uncache(send_from_directory("./templates", "index.html", cache_timeout=0))

def win():
    return helpers.uncache(send_from_directory("./templates", "win.html", cache_timeout=0))

def favicon():
    return helpers.uncache(send_from_directory("./static", "favicon.png", cache_timeout=0))

def robots():
    return helpers.uncache(send_from_directory("./static", "robots.txt", cache_timeout=0))
