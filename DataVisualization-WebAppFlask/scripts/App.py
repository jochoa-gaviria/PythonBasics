from flask import Flask, render_template
import os
from dataAnalysis import stockAnalysis

app=Flask(__name__, template_folder="../templates", static_folder="../static" )

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/about/')
def about():
    return render_template("about.html")


@app.route('/plot/')
def plot():
    return render_template("plot.html", script=stockAnalysis.script, html = stockAnalysis.html, cdnCSS= stockAnalysis.cdnCSS, cdnJS = stockAnalysis.cdnJS )

if __name__ == "__main__":
    app.run(debug=True)