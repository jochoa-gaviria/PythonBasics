## Installing bokeh for graps.
## pip3 install bokeh


##import bokeh and pandas ##
from bokeh.plotting import figure
from bokeh.io import output_file, show
import pandas, os
##import bokeh and pandas ##

## Preparing data ##
x=[1,2,3,4,5]
y=[6,7,8,9,10]
viewsPath='./views/graps/'
## Preparing data ##

## Prepare the output file ##
output_file(viewsPath+"Line.html")
#Create figure object
f=figure()
#Create line plot
f.line(x,y)
#show(f)
## Prepare the output file ##


## Exercise - plotting triangles and circles ##
output_file(viewsPath+"triangle.html")
f=figure()
f.triangle(x,y)
#show(f)

output_file(viewsPath+"circle.html")
f=figure()
f.circle(x,y)
#show(f)

## Exercise - plotting triangles and circles ##


## Using bokeh with pandas ##
grapsDataPath="./Files/csv/GrapsData1.csv"
if os.path.exists(grapsDataPath):
    df=pandas.read_csv(grapsDataPath)
    x=df['x']
    y=df['y']
else:
    x=[None]
    y=[None]
output_file(viewsPath+"LinePandas.html")
f=figure()
f.line(x,y)
#show(f)
## Using bokeh with pandas ##


## Exercise - Plotting education data ##
bachelorsDataPath="./Files/csv/bachelors.csv"
if os.path.exists(bachelorsDataPath):
    df=pandas.read_csv(bachelorsDataPath)
    year=df["Year"]
    engineering=df["Engineering"]
else:
    year=[None]
    engineering=[None]
output_file(viewsPath+"EducationData.html")
f=figure(plot_width=500, plot_height=400)
f.title.text="Engineering"
f.title.text_color="Gray"
f.title.text_font="times"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color=None
f.yaxis.minor_tick_line_color=None
f.xaxis.axis_label="Date"
f.yaxis.axis_label="Number of bacherlors"
f.line(year, engineering)
show(f)
## Exercise - Plotting education data ##


## Exercise - Plotting weather data ##
weatherDataPath="./Files/csv/verlegenhuken.xlsx"
if os.path.exists(weatherDataPath):
    df=pandas.read_excel(weatherDataPath, sheet_name=0)
    temperature=df["Temperature"]/10
    pressure=df["Pressure"]/10
else:
    temperature=[None]
    pressure=[None]
output_file(viewsPath+"Weather.html")
f=figure(plot_width=500, plot_height=400)
f.title.text="Temperature and air pressure"
f.title.text_color="Gray"
f.title.text_font="arial"
f.title.text_font_style="bold"
f.xaxis.minor_tick_line_color="Yellow"
f.yaxis.minor_tick_line_color="Black"
f.xaxis.axis_label="Temperature (°C)"
f.yaxis.axis_label="Pressure (hPa)"
f.circle_cross(temperature, pressure, size=0.5)
#f.line(temperature, pressure)
show(f)
## Exercise - Plotting weather data ##

## Creating a time-series plot ##
googleCsvLink='https://www.google.com/finance/quote/ADBE:NASDAQ?startdate=Jan+01,+2009&enddate=Aug+2,+2012&output=csv'
adbeFilePath="./Files/csv/adbe.csv"
if os.path.exists(adbeFilePath):
    df=pandas.read_csv(adbeFilePath, parse_dates=["Date"])
    date=df["Date"]
    close=df["Close"]
else: 
    date=[None]
    close=[None]
f=figure(width=500, height=250,x_axis_type="datetime")
f.line(date, close, color='Black', alpha=0.5)
output_file(viewsPath+'timeSeries.html')
show(f)
## Creating a time-series plot ##