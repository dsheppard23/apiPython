import requests
from requests.auth import HTTPBasicAuth
import json
import xlwt
from xlwt import Workbook

#URL for fields
url = "https://api.knack.com/v1/objects/object_1/fields"

#Start excel sheet
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')

#get request
r = requests.get(url, headers={'X-Knack-Application-Id': '5ffde6eb154a84001b1ea6f6', 'X-Knack-REST-API-KEY': '5c95477a-4351-4706-b2e5-67c976dd41b1'})
f = r.json()

#create 2d array for label + key
arr = {}

sheetArray = []

#iterate through fields
for i in range(0, len(f['fields'])):
    label = f['fields'][i]['label']
    sheetArray.append(label)
    key = f['fields'][i]['key']
    arr[key]=label

for x in range(0, len(sheetArray)):
    sheet1.write(x, 0, sheetArray[x])

#RECORDS
#URL for records, get request
urlRec = "https://api.knack.com/v1/objects/object_1/records"
rec = requests.get(urlRec, headers={'X-Knack-Application-Id': '5ffde6eb154a84001b1ea6f6', 'X-Knack-REST-API-KEY': '5c95477a-4351-4706-b2e5-67c976dd41b1'})
f2 = rec.json()
f2 = f2['records'][0]

#create new arrrays
ar2 = {}
ar3 = {}

for record in f2:
    ar2[record] = f2[record]


arr['id'] = "id"

#Iterator for the loop
i = 0

#iterate through records
#print(ar2)
for key in arr.keys():
    #print(ar2[key])
    if(key in ar2.keys()):
        ar3[arr[key]] = ar2[key]
        sheet1.write(i, 1, ar3[arr[key]])
        i = i+1

wb.save('xlwt example.xls')