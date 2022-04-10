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
        type: 'spline'
    },
    title: {
        text: 'Average by month by course'
    },
    legend: {
        layout: 'vertical',
        align: 'left',
        verticalAlign: 'top',
        x: 150,
        y: 100,
        floating: false,
        borderWidth: 1,
        backgroundColor:
            '#FFFFFF'
    },
    xAxis: {
        categories: [
            'Monday',
            'Tuesday',
            'Wednesday',
            'Thursday',
            'Friday',
            'Saturday',
            'Sunday'
        ],
        plotBands: [{ // visualize the weekend
            from: 4.5,
            to: 6.5,
            color: 'rgba(68, 170, 213, .2)'
        }]
    },
    yAxis: {
        title: {
            text: 'Average'
        }
    },
    tooltip: {
        shared: true,
        valueSuffix: ' '
    },
    credits: {
        enabled: false
    },
    plotOptions: {
        areaspline: {
            fillOpacity: 0.5
        }
    },
    series: [{
        name: 'John',
        data: [3, 4, 3, 5, 4, 10, 12]
    }, {
        name: 'Jane',
        data: [1, 3, 4, 3, 3, 5, 4]
    }]
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