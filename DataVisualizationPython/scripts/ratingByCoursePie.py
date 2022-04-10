import justpy as jp
import pandas, os

reviewsPath = './dataFiles/reviews.csv'
if os.path.exists(reviewsPath):
    data = pandas.read_csv(reviewsPath, parse_dates=['Timestamp'])
else:
    data = [None]


share = data.groupby(['Course Name'])['Rating'].count()

chartDef= """
{
    chart: {
        plotBackgroundColor: null,
        plotBorderWidth: null,
        plotShadow: false,
        type: 'pie'
    },
    title: {
        text: 'Browser market shares in January, 2018'
    },
    tooltip: {
        pointFormat: '{series.name}: <b>{point.percentage:.1f}%</b>'
    },
    accessibility: {
        point: {
            valueSuffix: '%'
        }
    },
    plotOptions: {
        pie: {
            allowPointSelect: true,
            cursor: 'pointer',
            dataLabels: {
                enabled: true,
                format: '<b>{point.name}</b>: {point.percentage:.1f} %'
            }
        }
    },
    series: [{
        name: 'Brands',
        colorByPoint: true,
        data: [{
            name: 'Chrome',
            y: 61.41,
            sliced: true,
            selected: true
        }, {
            name: 'Internet Explorer',
            y: 11.84
        }, {
            name: 'Firefox',
            y: 10.85
        }, {
            name: 'Edge',
            y: 4.67
        }, {
            name: 'Safari',
            y: 4.18
        }, {
            name: 'Sogou Explorer',
            y: 1.64
        }, {
            name: 'Opera',
            y: 1.6
        }, {
            name: 'QQ',
            y: 1.2
        }, {
            name: 'Other',
            y: 2.61
        }]
    }]
}
"""

def app():
    wp = jp.QuasarPage()
    h1 = jp.QDiv(a=wp, text="Analysis of course reviews", classes="text-h3 text-center q-pa-md") ## Use Quasar styling
    hc = jp.HighCharts(a=wp, options=chartDef)
    hcData = [{"name":v1, "y":v2} for v1, v2 in zip(share.index, share)]
    hc.options.series[0].data = hcData
    p1 = jp.QDiv(a=wp, text="These graphs represent course review analysis", classes="text-h6 text-center q-pa-md")
    return wp

jp.justpy(app)