from turtle import width
from pandas_datareader import data
from datetime import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.embed import components
from bokeh.resources import CDN

start=datetime(2022,3,1)
end=datetime(2022,4,10)
df=data.DataReader(name="AAPL", data_source="yahoo", start=start, end=end)  #stock symbols form the companies, data_source may be google,yahoo
# print(dt)


hours_12=12*60*60*1000

def inc_dec(c, o):
    if c>o:
        return "Increase"
    elif c<o:
        return "Decrease"
    else:
        return "Equals"

df["Status"]=[inc_dec(c,o) for c,o in zip(df.Close,df.Open)]
df["Middle"]=(df.Open+df.Close)/2
df["Height"]=abs(df.Open-df.Close)

p=figure(x_axis_type='datetime', width=1000, height=300, sizing_mode="scale_width")
p.title="Candlestick Chart"
p.grid.grid_line_alpha=0.3

p.segment(df.index, df.High, df.index, df.Low, color="black")

p.rect(df.index[df.Status=='Increase'], df.Middle[df.Status=='Increase'], hours_12, df.Height[df.Status=='Increase'], fill_color='green',line_color='black')
p.rect(df.index[df.Status=='Decrease'], df.Middle[df.Status=='Decrease'], hours_12, df.Height[df.Status=='Decrease'], fill_color='red',line_color='black')
p.rect(df.index[df.Status=='Equals'], df.Middle[df.Status=='Equals'], hours_12, df.Height[df.Status=='Equals'], fill_color='blue',line_color='black')

script, html = components(p)
cdnJS = CDN.js_files[0]
cdnCSS = CDN.css_files
# output_file('cs.html')
# show(p)