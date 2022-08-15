from flask import request, redirect, send_from_directory

from hashlib import md5
import binascii

from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Cryptodome.Util.Padding import pad, unpad

import helpers

key = md5("M4XcX94%w8ZXN$638#%425!28#B8%K$R".encode('utf8')).digest()

def challenge(_, next_challenge):
    if request.method == "POST":
        try:
            iv = request.form.get("iv", None)
            ct = request.form.get("message", None)
            if iv == None or ct == None:
                return redirect(request.uri)

            iv = binascii.unhexlify(iv.encode('utf-8'))
            ct = binascii.unhexlify(ct.encode('utf-8'))
            
            cipher = AES.new(key, AES.MODE_CBC, iv)
            pt = unpad(cipher.decrypt(ct), AES.block_size).decode('utf-8')

            if pt.split(";")[0] == "udelezenec@posta.si":
                print("[INFO] chall08 solved")
                return next_challenge
            else:
                return redirect(request.uri)

        except:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates", "chall08.html", cache_timeout=0))

def static(name):
    return helpers.serve_static(name)
