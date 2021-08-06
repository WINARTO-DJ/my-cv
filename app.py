from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/<name>")
def index(name=None):
    if name is None:
        return render_template("index.html")
    else:
        return render_template("index.html", name=name)

    

if __name__ == "__main__":
    app.run()