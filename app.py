from flask import Flask

app = Flask(__name__)

from flask import request, render_template
from textblob import TextBlob
import joblib

@app.route("/", methods=["GET","POST"])
def index():
    if request.method =="POST":
        text = request.form.get("text")
        print(text)
        r = TextBlob(text).sentiment
        return(render_template("index.html",results=r))
    else:
        return(render_template("index.html",results='2'))

if __name__ =="__main__":
    app.run()

#pip freeze requirements.txt