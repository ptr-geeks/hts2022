from flask import request, redirect, send_from_directory

import helpers

def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            print("[INFO] chall03 solved")
            return next_challenge;
        else:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates", "chall03.html", cache_timeout=0))

def static(name):
    if name == "main.js":
        return helpers.uncache(send_from_directory("./chall/chall03", "main.js", cache_timeout=0))
    return helpers.serve_static(name)
