import pandas, os
from datetime import datetime
from pytz import utc

reviewsPath = './dataFiles/reviews.csv'
if os.path.exists(reviewsPath):
    data = pandas.read_csv(reviewsPath, parse_dates=['Timestamp'])
else:
    data = [None]

print (data.head())
print ('\n')
print (data.hist('Rating'))


## Selecting data from dataframe ##
print ('\n')
print(data['Rating'])
print ('\n')
print(data.iloc[1:3])
print ('\n')
print(data[['Course Name', 'Rating']].iloc[1:3])
print ('\n')
print(data['Rating'].iloc[2])
## Selecting data from dataframe ##


## Filtering data based on conditions ##
##One condition
print('\n')
print(data[data['Rating']>4].count())
d2=data[data['Rating']>4]
print('\n')
print(d2['Rating'])

##Multiple condition
print('\n')
print(data[(data['Rating'] > 3) & (data['Course Name'] == 'The Python Mega Course: Build 10 Real World Applications')]['Rating'].mean())


##Time-based filtering
print('\n')
print(data[(data['Timestamp'] >= datetime(2020, 7, 1, tzinfo=utc)) & (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc))]['Timestamp'].head())

## Filtering data based on conditions ##


## Turning data into information ##
##Average rating
print('\n Average rating')
print(data['Rating'].mean())

##Average rating for a particular course
print('\n Average rating for a particular course')
print(data[data['Course Name']== 'The Python Mega Course: Build 10 Real World Applications']['Rating'].mean())

##Average rating for a particular period
print('\n Average rating for a particular period')
print(data[(data['Timestamp'] >= datetime(2020, 1, 1, tzinfo=utc)) & (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc))]['Rating'].mean())

##Average rating for a particular period for a particular course
print('\n Average rating for a particular period for a particular course')
print(data[(data['Timestamp'] >= datetime(2020, 1, 1, tzinfo=utc)) & 
    (data['Timestamp'] <= datetime(2020, 12, 31, tzinfo=utc)) &
    (data['Course Name']== 'The Python Mega Course: Build 10 Real World Applications')]['Rating'].mean())

##Average of uncommented ratings
print('\n Average of uncommented ratings')
print(data[data['Comment'].isnull()]['Rating'].mean())

##Average of commented ratings
print('\n Average of commented ratings')
print(data[data['Comment'].notnull()]['Rating'].mean())

##Number of uncommented ratings
print('\n Number of uncommented ratings')
print(data[data['Comment'].isnull()]['Rating'].count())

##Number of commented ratings
print('\n Number of commented ratings')
print(data[data['Comment'].notnull()]['Rating'].count())

##Number of comments containing a certain word
print('\n Number of comments containing a certain word')
print(data[data['Comment'].str.contains('accent', na=False)]['Comment'].count())

##Average of commented ratings with "accent" in comment
print('\n Average of commented ratings with "accent" in comment')
print(data[data['Comment'].str.contains('accent', na=False)]['Rating'].mean())

## Turning data into information ##