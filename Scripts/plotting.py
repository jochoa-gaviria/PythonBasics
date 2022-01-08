from motionDetector import df
from bokeh.plotting import figure, show, output_file
from bokeh.models import HoverTool, ColumnDataSource


viewsPath='./views/graps/'

# df["Start_string"]=df["Start"].dt.srtftime("%Y-%m-%d %H:%M:%S")
# df["End_string"]=df["End"].dt.srtftime("%Y-%m-%d %H:%M:%S")
df["Start_string"]=df["Start"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
df["End_string"]=df["End"].apply(lambda x: x.strftime("%Y-%m-%d %H:%M:%S"))
cds=ColumnDataSource(df)

f=figure(x_axis_type='datetime', height=100, width=500,sizing_mode='scale_width', title="Motion graph")
f.yaxis.minor_tick_line_color=None
f.yaxis.ticker.desired_num_ticks=1

hover=HoverTool(tooltips=[("Start ","@Start_string"), ("End ", "@End_string")])
f.add_tools(hover)



q=f.quad(left="Start",right="End",bottom=0, top=1, color="green", source=cds)
output_file(viewsPath+'motionDetector.html')
show(f)