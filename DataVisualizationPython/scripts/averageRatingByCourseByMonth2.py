import justpy as jp
import pandas, os
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

reviewsPath = './dataFiles/reviews.csv'
if os.path.exists(reviewsPath):
    data = pandas.read_csv(reviewsPath, parse_dates=['Timestamp'])
else:
    data = [None]

data['Month']=data['Timestamp'].dt.strftime('%Y-%m')
monthCourseAverage= data.groupby(['Month', 'Course Name']).count().unstack()

charDef = """
{
    chart: {
        type: 'streamgraph',
        marginBottom: 30,
        zoomType: 'x'
    },

    title: {
        floating: true,
        align: 'left',
        text: 'Average by course by month'
    },
    

    xAxis: {
        maxPadding: 0,
        type: 'category',
        crosshair: true,
        categories: [],
        labels: {
            align: 'left',
            reserveSpace: false,
            rotation: 270
        },
        lineWidth: 0,
        margin: 20,
        tickWidth: 0
    },

    yAxis: {
        visible: false,
        startOnTick: false,
        endOnTick: false
    },

    legend: {
        enabled: false
    },

    annotations: [{
        labels: [{
            point: {
                x: 5.5,
                xAxis: 0,
                y: 30,
                yAxis: 0
            },
            text: 'course launche'
        }, {
            point: {
                x: 18,
                xAxis: 0,
                y: 90,
                yAxis: 0
            },
            text: 'python got popular'
        }],
        labelOptions: {
            backgroundColor: 'rgba(255,255,255,0.5)',
            borderColor: 'silver'
        }
    }],

    plotOptions: {
        series: {
            label: {
                minFontSize: 5,
                maxFontSize: 15,
                style: {
                    color: 'rgba(255,255,255,0.75)'
                }
            }
        }
    },

    // Data parsed with olympic-medals.node.js
    series: [{
        name: "Finland",
        data: [
            0, 11, 4, 3, 6, 0, 0, 6, 9, 7, 8, 10, 5, 5, 7, 9, 13, 7, 7, 6, 12, 7, 9, 5, 5
        ]
    }],

    exporting: {
        sourceWidth: 800,
        sourceHeight: 600
    }

}
"""



def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md")
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis")

    hc = jp.HighCharts(a=wp, options=charDef)
    hc.options.xAxis.categories = list(monthCourseAverage.index)
    hcData = [{"name":v1, "data":[v2 for v2 in monthCourseAverage[v1]]} for v1 in monthCourseAverage.columns]
    hc.options.series = hcData
    return wp

jp.justpy(app)