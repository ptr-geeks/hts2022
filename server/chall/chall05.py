from flask import request, redirect, send_from_directory

import helpers

def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            print("[INFO] chall05 solved")
            return next_challenge;
        else:
            return redirect(request.url)
    else:
        res = helpers.uncache(send_from_directory("./templates", "chall05.html", cache_timeout=0))
        res.headers["X-Date"] = "I was headed in that direction"
        return res

def static(name):
    return helpers.serve_static(name)
