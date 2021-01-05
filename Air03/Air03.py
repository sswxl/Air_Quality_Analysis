#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif']=['SimHei']


# In[16]:


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
    day=row['day']
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
        if (aqidict.get(date)):
            aqilist = aqidict.get(date)
            aqilist.append(AQI)
        else:
            aqidict={}
            aqilist = []
            aqilist.append(AQI)
            aqidict[date] = aqilist
            citydict[city] = aqidict


# In[17]:


data.head()


# In[79]:


data.describe()


# In[77]:


data.city.value_counts()


# for (city,aqidict) in citydict.items():
#        for (date,aqilist) in aqidict.items():
#             sum=0
#             count=0
#             for i in range(0,len(aqilist)):
#                 count=count+1
#                 sum+=aqilist[i]
#             aqilist.append(sum/count)

# In[21]:


result=pd.read_csv(open('./result.csv',encoding='utf-8'),header=None)
result.columns = ['city','date','AQI']
result['date'] = result['date'].apply(str)


# In[19]:


result.head()#12个城市每天的平均AQI


# In[24]:


handle=pd.read_csv(open('./handle.csv',encoding='utf-8'))


# In[25]:


handle.head()#12个城市每月的空气质量等级天数


# In[26]:


pie=pd.read_csv(open('./pie.csv',encoding='utf-8',),header=None)
pie.columns = ['city','Excellent','Good','Lightly Polluted','Moderately Polluted','Heavily Polluted','Severely Polluted']


# In[27]:


pie.head()#12个城市总的空气质量的天数统计


# In[83]:


sns.distplot(data["AQI"])


# In[84]:


sns.scatterplot(x='经度', y='纬度', hue='AQI', palette=plt.cm.RdYlGn_r, data=data[data['city']=='成都'])


# In[85]:


corrdata=data[['AQI','PM25','PM10','CO','NO2','O3-1','SO2','O3-8h','纬度','经度']]
corr=corrdata.corr()
plt.figure(figsize=(12,12))
# 绘制相关系数热力图
plt.subplots(figsize=(8, 8))
sns.heatmap(corr, annot=True, vmax=1, square=True, cmap="Blues")
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
sns.set(font='LiSu')
plt.show()


# In[89]:


plt.figure(figsize=(8,4))
sns.scatterplot(x="city", y="AQI",hue="AQI", data=result)


# In[98]:


plt.figure(figsize=(8,4))
sns.barplot(x="city", y="Excellent", data=pie)


# In[91]:


plt.figure(figsize=(8,4))
sns.countplot(x='city',hue='等级',data=data)


# In[99]:


pie.values.tolist()[0][1:]


# In[100]:


plt.pie(x=pie.values.tolist()[8][1:],labels=['Excellent','Good','Lightly Polluted','Moderately Polluted','Heavily Polluted','Severely Polluted'],autopct='%1.2f%%',colors=['green','red','skyblue','blue','yellow'],pctdistance=0.6)


# In[3]:


from sklearn.linear_model import LinearRegression,BayesianRidge
from sklearn.model_selection import train_test_split

x = data.drop(['city','站号','AQI','year','month','day','hour'], axis=1) #删除city等字段
y = data['AQI']
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


# In[74]:


x_train.head()


# In[101]:


x_train.describe()


# In[4]:


reg = LinearRegression()
reg.fit(x_train, y_train)
print('训练集R2score：', reg.score(x_train, y_train))
print('测试集R2score：', reg.score(x_test, y_test))


# In[15]:


y_hat = reg.predict(x_test[:200])
plt.figure(figsize=(15,5))
plt.plot(y_test[:200].values,'-r', label='真实值', marker='o')
plt.plot(y_hat, color='#054E9F', label='预测值', marker='D')
plt.legend(loc='upper left')
plt.xlabel("样本")
plt.ylabel("AQI")
plt.title('LinearRegression结果',fontsize=20)


# In[ ]:




