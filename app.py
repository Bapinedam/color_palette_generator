from flask import Flask, render_template, request

app = Flask(__name__,
            template_folder='templates')

@app.route("/dog")
def dog():
    return "WOF WOF WOF!!"

@app.route("/")
def index():
    return render_template("index.html", encoding="utf-8")

if __name__ =="__main__":
    app.run(debug=True)