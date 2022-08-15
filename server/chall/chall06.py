from flask import request, redirect, send_from_directory

import helpers

def challenge(flag, next_challenge):
    if request.method == "POST":
        if request.form.get("flag") == flag:
            print("[INFO] chall06 solved")
            return next_challenge;
        else:
            return redirect(request.url)
    else:
        return helpers.uncache(send_from_directory("./templates", "chall06.html", cache_timeout=0))

def static(name):
    data = name.split("?")[0]
    data = data.split("/")

    if data[0] != "files":
        return helpers.serve_static(name)

    if data[-1] == "":
        del data[-1]

    paths = {
        "0001": ("Put title here", "Hello world!"),
        "0023": ("Slike!", "https://www.humanesociety.org/sites/default/files/styles/2000x850/public/2020-07/kitten-510651.jpg"),
        "0069": ("Funny number", "hehehe..."),
        "0255": ("Broadcast", "Last ip in my /24 range"),
        "0420": ("Blaze it", "Sam ne na taboru"),
        "0666": ("Oh no", "Quick, get out of here!"),
        "0946": ("Igre", "https://www.igre123.com/"),
        "1101": ("Not-a-scam", "Hello, your computer has virus!"),
        "1583": ("Rogger", "Pogger"),
        "1877": ("Random", "https://xkcd.com/221/"),
        "2181": ("Kam gres?", "Ne vem kam grem k ne vem kje sm!"),
        "2400": ("Slon", "Sadez"),
        "2869": ("WC", "Uff kok smrdi kle..."),
        "3365": ("SHA256", "https://www.youtube.com/watch?v=dQw4w9WgXcQ"),
        "3550": ("Resistance", "is futile"),
        "3890": ("Resistance2", "=U/I"),
        "4010": ("<", "3"),
        "4096": ("RSA", "Maybe 8192 for post quantum security"),
        "4767": ("2+2/2", "=2        Majkemi da je totalno prou!"),
        "5111": ("Next challenge here", "I lied."),
        "5782": ("Mikrovalovka", "mmmmmmmmmmmmmmmm"),
        "6969": ("Funny number 2", "'69' + 69"),
        "7200": ("Zmankuje mi idej", "Tuki pa tut"),
        "7412": ("Blink182", "Fak smo stari"),
        "7988": ("Najhitrejsi avto za cez grbine", "Sluzbeni."),
        "8192": ("SIKE", "https://arstechnica.com/information-technology/2022/08/sike-once-a-post-quantum-encryption-contender-is-koed-in-nist-smackdown/"),
        "8657": ("Cookies!", "I lied about having cookies."),
        "9000": ("Power", "Damn, it's so close..."),
        "9001": ("POWER", "IT'S OVER 9000"),
        "9200": ("ES", "https://discuss.elastic.co/t/what-are-ports-9200-and-9300-used-for/238578"),
        "9300": ("ES2", "https://discuss.elastic.co/t/what-are-ports-9200-and-9300-used-for/238578"),
        "9999": ("Last but not least", "May be least..."),
    }

    if len(data) == 2:
        if data[1] in paths.keys():
            ret = paths[data[1]][1]
            if ret.startswith("https://"):
                return redirect(ret)
            return ret
        elif data[1] == "4588":
            return "Return to sender"
        elif data[1] == "6432":
            return "Fuuuuuuuuuuuuuuu...zer"
        else:
            return "No data here", 404
    elif len(data) == 1:
        html = "<h1>/s/files/</h1><br/><br/>\n"

        for k in paths.keys():
            html += '<a href="' + ("/s/files/" + k + "/") + '">' + paths[k][0] + '</a><br/>\n'

        return html
    else:
        return "No data here", 404
        

