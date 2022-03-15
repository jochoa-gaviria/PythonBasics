from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim
import pandas


templateDir = 'templates'
staticDir = 'static'
app=Flask(__name__, template_folder=templateDir, static_folder=staticDir)


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/successTable", methods=['POST'])
def successTable():
    if request.method=="POST":
        file = request.files['file']
        df=pandas.read_csv(file)
        gc=Nominatim(user_agent="geogrphy")
        df['coordinates']=df["Address"].apply(gc.geocode)
        df['Latitude']=df['coordinates'].apply(lambda x: x.latitude if x != None else None)
        df['Longitude']=df['coordinates'].apply(lambda x: x.longitude if x != None else None)
        df=df.drop('coordinates',1)
        df.to_csv('uploads/geocoded.csv',index=None)
        return render_template("index.html", text=df.to_html, btn='download.html')
    else:
        return render_template("index.html")

@app.route("/downloadFile")
def download():
    return send_file('uploads/geocoded.csv', attachment_filename='yourfile.csv', as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)