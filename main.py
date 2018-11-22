from flask import Flask, render_template

app = Flask(__name__)


@app.route("/profile/<name>")
def profile(name):
    return render_template("profile.html", name=name)
#this is not what you think

if __name__ == "__main__":
    app.debug = True
    app.run()
