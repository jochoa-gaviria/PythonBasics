from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sendEmail import sendEmail

app = Flask(__name__, template_folder="template", static_folder="static")


db=SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres@localhost/height_collector'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

class Data(db.Model):
    __tablename__="data"
    id=db.Column(db.Integer, primary_key=True)
    email_=db.Column(db.String(120), unique=True)
    height_=db.Column(db.Integer)

    def __init__(self, email_, height_):
        self.email_=email_
        self.height_=height_


def calculateAverage():
    average_ = db.session.query(func.avg(Data.height_)).scalar()
    average_=round(average_,1)
    return average_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods=['POST', 'GET'])
def success():
    if request.method=='POST':
        email=request.form["email"]
        height= request.form["height"]
        if db.session.query(Data).filter(Data.email_==email).count() <= 0:
            data=Data(email,height)
            db.session.add(data)
            db.session.commit()
            averageHeight = calculateAverage()
            sendEmail(email, height, averageHeight)
            return render_template("success.html")

    return render_template("index.html", text="Seems like we've got something from thah email address already!")


if __name__ == '__main__':
    app.debug=True
    app.run()
