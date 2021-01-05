import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
dd=pd.read_csv(open('./PM25city.csv',encoding='utf-8'))
data=dd[dd.AQI>0]
data=dd[dd.PM25>0]
citydict={}
aqidict={}
aqilist=[]
for index, row in data.iterrows():
    AQI=row['AQI']
    year=row['year']
    month=row['month']
    if(month<10):
        month='0'+str(month)
    day=row['day']
    if (day < 10):
        day = '0' + str(day)
    date=str(year) + str(month) + str(day)
    city=row['city']
    if (citydict.get(city)):
        aqidict=citydict.get(city)
        if (aqidict.get(date)):
            aqilist = aqidict.get(date)
            aqilist.append(AQI)
        else:
            aqilist = []
            aqilist.append(AQI)
            aqidict[date] = aqilist
    else:
            aqidict={}
            aqilist = []
            aqilist.append(AQI)
            aqidict[date] = aqilist
            citydict[city] = aqidict
for (city,aqidict) in citydict.items():
       for (date,aqilist) in aqidict.items():
            sum=0
            count=0
            for i in range(0,len(aqilist)):
                count=count+1
                sum+=aqilist[i]
            avg=sum / count
            aqilist.append(sum/count)
            write_clo = [city, date, avg, ]
            df = pd.DataFrame(columns=write_clo)
            df.to_csv('result.csv', line_terminator="\n", index=False, mode='a', encoding='utf8')
# result=pd.read_csv(open('F:/研二上/大数据hadoop/PM25city/result.csv',encoding='utf-8'))
# citydict2={}
# for index, row in result.iterrows():
#     city = row['city']
#     month=str(row['date'])[:6]
#     aqi = row['aqi']
#     if (citydict2.get(city)):
#         aqidict=citydict2.get(city)
#         if (aqidict.get(month)):
#             aqilist = aqidict.get(month)
#             if aqi <= 50:
#                 aqilist[0] = aqilist[0] + 1
#             elif aqi <= 100:
#                 aqilist[1] = aqilist[1] + 1
#             elif aqi <= 100:
#                 aqilist[2] = aqilist[2] + 1
#             elif aqi <= 100:
#                 aqilist[3] = aqilist[3] + 1
#             elif aqi <= 100:
#                 aqilist[4] = aqilist[4] + 1
#             else:
#                 aqilist[5] = aqilist[5] + 1
#         else:
#             aqilist = aqilist = [0,0,0,0,0,0]
#             if aqi <= 50:
#                 aqilist[0] = aqilist[0] + 1
#             elif aqi <= 100:
#                 aqilist[1] = aqilist[1] + 1
#             elif aqi <= 100:
#                 aqilist[2] = aqilist[2] + 1
#             elif aqi <= 100:
#                 aqilist[3] = aqilist[3] + 1
#             elif aqi <= 100:
#                 aqilist[4] = aqilist[4] + 1
#             else:
#                 aqilist[5] = aqilist[5] + 1
#             aqidict[month] = aqilist
#     else:
#             aqidict={}
#             aqilist = [0,0,0,0,0,0]
#             if aqi<=50:
#                 aqilist[0]=aqilist[0]+1
#             elif aqi<=100:
#                 aqilist[1]=aqilist[1]+1
#             elif aqi<=100:
#                 aqilist[2]=aqilist[2]+1
#             elif aqi<=100:
#                 aqilist[3]=aqilist[3]+1
#             elif aqi<=100:
#                 aqilist[4]=aqilist[4]+1
#             else:
#                 aqilist[5] = aqilist[5] + 1
#             aqidict[month] = aqilist
#             citydict2[city] = aqidict
#
# for (city,aqidict) in citydict2.items():
#     for (month, aqilist) in aqidict.items():
#          write_clo = [city, month, aqilist ]
#          df = pd.DataFrame(columns=write_clo)
#          df.to_csv('handle.csv', line_terminator="\n", index=False, mode='a', encoding='utf8')




# result=pd.read_csv(open('F:/研二上/大数据hadoop/PM25city/result.csv',encoding='utf-8'))
# citydict3={}
#
# for index, row in result.iterrows():
#     city = row['city']
#     month=str(row['date'])[:6]
#     aqi = row['aqi']
#     if (citydict3.get(city)):
#         aqilist = citydict3.get(city)
#         if aqi<=50:
#             aqilist[0]=aqilist[0]+1
#         elif aqi<=100:
#             aqilist[1]=aqilist[1]+1
#         elif aqi<=100:
#             aqilist[2]=aqilist[2]+1
#         elif aqi<=100:
#             aqilist[3]=aqilist[3]+1
#         elif aqi<=100:
#             aqilist[4]=aqilist[4]+1
#         else:
#             aqilist[5] = aqilist[5] + 1
#     else:
#             aqilist = [0,0,0,0,0,0]
#             if aqi <= 50:
#                 aqilist[0] = aqilist[0] + 1
#             elif aqi <= 100:
#                 aqilist[1] = aqilist[1] + 1
#             elif aqi <= 100:
#                 aqilist[2] = aqilist[2] + 1
#             elif aqi <= 100:
#                 aqilist[3] = aqilist[3] + 1
#             elif aqi <= 100:
#                 aqilist[4] = aqilist[4] + 1
#             else:
#                 aqilist[5] = aqilist[5] + 1
#             citydict3[city] = aqilist
#
# for (city,aqi) in citydict3.items():
#          write_clo = [city, aqi[0], aqi[1],aqi[2],aqi[3],aqi[4],aqi[5]]
#          df = pd.DataFrame(columns=write_clo)
#          df.to_csv('pie.csv', line_terminator="\n", index=False, mode='a', encoding='utf8')