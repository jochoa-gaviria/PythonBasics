import pandas, os
from datetime import datetime
from pytz import utc
import matplotlib.pyplot as plt

reviewsPath = './dataFiles/reviews.csv'
if os.path.exists(reviewsPath):
    data = pandas.read_csv(reviewsPath, parse_dates=['Timestamp'])
else:
    data = [None]

## Average by day ##
data['Day']=data['Timestamp'].dt.date
dayAverage = data.groupby(['Day']).mean()
# print(dayAverage['Rating'])
plt.figure(figsize=(25,3))
plt.plot(dayAverage.index, dayAverage['Rating'])
plt.show()
# print(data['Day'])
## Average by day ##

## Average by week ##
data['Week']=data['Timestamp'].dt.strftime('%Y-%U')
print(data['Week'])
weekAverage=data.groupby(['Week']).mean()
# print(weekAverage)
plt.figure(figsize=(25,3))
plt.plot(weekAverage.index, weekAverage['Rating'])
plt.show()
## Average by week ##

## Average by month ##
data['Month']=data['Timestamp'].dt.strftime('%Y-%m')
print(data['Month'])
monthAverage=data.groupby(['Month']).mean()
# print(monthAverage)
plt.figure(figsize=(25,3))
plt.plot(monthAverage.index, monthAverage['Rating'])
plt.show()
## Average by month ##


## Average by month by course ##
monthCourseAverage= data.groupby(['Month', 'Course Name']).mean().unstack()
plt.figure(figsize=(25,3))
monthCourseAverage.plot(figsize=(25,8))
plt.show()
## Average by month by course ##


## What day are people the happiest? ##
data['Weekday'] = data['Timestamp'].dt.strftime('%A')
data['DayNumber'] = data['Timestamp'].dt.strftime('%w')
# print(data['Weekday'])
weekDayAverage = data.groupby(['Weekday', 'DayNumber']).mean()
weekDayAverage = weekDayAverage.sort_values('DayNumber')
plt.figure(figsize=(15, 3))
plt.plot(weekDayAverage.index.get_level_values(0), weekDayAverage['Rating'])
plt.show()
## What day are people the happiest? ##