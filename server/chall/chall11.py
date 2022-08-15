from flask import request, redirect, send_from_directory, make_response

import os
import subprocess

import helpers

def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            print("[INFO] chall11 solved")
            return next_challenge;
        else:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates", "chall11.html", cache_timeout=0))

def static(name):
    if name == "webfetch":
        url = request.args.get("website", None)
        if request.method == "GET" and url != None:
            if url.startswith("http://") or url.startswith("https://") or (url.startswith("file:///proc/") and ".." not in url):
                proc_env = os.environ.copy()
                proc_env["chall10secret"] = "[REDACTED]"
                proc = subprocess.run(["curl", url], env=proc_env, capture_output=True)
                if proc.returncode != 0:
                    return "Error? Does the website exist? :O", 500
                res = make_response(proc.stdout, 200)
                res.headers["Content-Type"] = "text/plain"
                return helpers.uncache(res)
            else:
                return "Bad website 2", 400
        else:
            return "Bad website 1", 400
    return helpers.serve_static(name)
