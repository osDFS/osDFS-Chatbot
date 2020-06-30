from flask import Flask, render_template 

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/community")
def community():
    return render_template("community.html")

@app.route("/ccp")
def cpp():
    return render_template("ccp.html")

@app.route("/partners")
def partners():
    return render_template("partners.html")

@app.route("/events")
def events():
    return render_template("events.html")

@app.route("/opportunities")
def opportunities():
    return render_template("oppertunities.html")

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/test")
def test():
    return render_template("child.html")
    
if __name__ == "__main__" :
	app.run(host="0.0.0.0")