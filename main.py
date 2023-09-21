
from collections import defaultdict
import mysql.connector
import psycopg2
from bs4 import BeautifulSoup

# Get HTML Data
response = open('./index.html')
html_doc = response.read()

soup = BeautifulSoup(html_doc, 'html.parser')

days = ["monday", "tuesday", "wednesday", "thursday", "friday"]

colorsInDays = defaultdict(list)
dayNo = 0

countAllColors = {}

for td in soup.find_all("td"):
    if td.text.lower() not in days:
        dayNo += 1
        
        splitColors = td.text.lower().split(", ")
        
        colorsInDays[dayNo].append(td.text.lower())
        for i in range(len(splitColors)):
            countAllColors[splitColors[i]] = 1 if countAllColors.get(splitColors[i]) == None else countAllColors[splitColors[i]] + 1

totalNoOfColors = 0 

for color in countAllColors:
    totalNoOfColors += countAllColors[color]

sortedCountAllColors = sorted(countAllColors.items(), key=lambda x:x[1])
countAllColors = dict(sortedCountAllColors)

# Mean
mean = (totalNoOfColors / len(countAllColors))
print("Mean of colors: " + str(mean))

key_list = list(countAllColors.keys())
val_list = list(countAllColors.values())

position = val_list.index(min(list(countAllColors.values()), key=lambda x:abs(x - mean)))
print("Mean color: " + str(key_list[position]))

# Color with the highest frequency
print("Color with the highest frequency: " + str(list(countAllColors.keys())[-1]))

# Median
lenOfColors = len(countAllColors) 
if lenOfColors % 2 == 1:
    print("Median color is: " + str(list(countAllColors.keys())[
        int(lenOfColors / 2)
    ]))
else:
    getMid = int(lenOfColors / 2)
    firstAvgColor = list(countAllColors.keys())[getMid - 1]
    secondAvgColor = list(countAllColors.keys())[getMid]
    
    avg = int(countAllColors[firstAvgColor] + countAllColors[secondAvgColor] / 2)
    
    key_list = list(countAllColors.keys())
    val_list = list(countAllColors.values())

    position = val_list.index(min(list(countAllColors.values()), key=lambda x:abs(x-avg)))
    print("Median color is: " + key_list[position])


# Calculating Variance
sqDeviationFromMean = {}
sumOfSqrsFromMean = 0
for item in countAllColors.values():
    sqDeviationFromMean[item] = pow((item - mean), 2)
    sumOfSqrsFromMean += pow((item - mean), 2)

variance = sumOfSqrsFromMean / len(countAllColors) - 1

print("Variance of colors: " + str(variance))

# Saving Colors in Postgresql

conn = psycopg2.connect(
   database="postgres", user='postgres', password='password', host='localhost', port= '5432'
)

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS color_frequencies (
        color_name VARCHAR(255) PRIMARY KEY,
        frequency INT
    )
""")

for color in countAllColors:
    cursor.execute("""
        INSERT INTO color_frequencies (color_name, frequency)
        VALUES (%s, %s)
    """, (color, countAllColors[color]))

cursor.execute("SELECT * FROM color_frequencies")
rows = cursor.fetchall()

print("Color Frequencies:")
for row in rows:
    print(f"Color: {row[0]}, Frequency: {row[1]}")

conn.commit()
#Closing the connection
cursor.close()
conn.close()
