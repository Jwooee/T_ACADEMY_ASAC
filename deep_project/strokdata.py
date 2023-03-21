#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
get_ipython().run_line_magic('matplotlib', 'inline')

import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam


from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder,MinMaxScaler


# In[2]:


import os
os.getcwd()


# In[2]:


df = pd.read_csv('healthcare-dataset-stroke-data.csv')
df.head(10)


# In[3]:


a = df[df['gender']=='Other'].index
df.drop(a,inplace=True)


# In[4]:


df[df['gender']=='Other']


# In[ ]:


'gender':1,0 
'ever_married':1,0
'Residence_type':1,0
'work_type':공기업 0 prvate 1 selfempy 2 


# In[5]:


df['smoking_status'].head(5)


# In[6]:


df['smoking_status'].replace({'formerly smoked':1,
                              'never smoked':0,
                              'smokes':2,
                              'Unknown':0
                              },inplace=True)


# In[7]:


df.head()


# In[ ]:


# 'gender':1,0 
# 'ever_married':1,0
# 'Residence_type':1,0
# 'work_type':공기업 0 prvate 1 selfempy 2 


# In[8]:


features=['age','gender','hypertension','heart_disease', 'ever_married',
          'work_type', 'Residence_type' , 'avg_glucose_level','bmi','smoking_status']#데이터와 관련없는 id 제거
x=df[features]
y_before=df['stroke']
y=pd.DataFrame(y_before)
y.columns=['target_y']


# 결측치 : 중앙값 대치 

# In[9]:



x.info()
x.fillna(x['bmi'].median(), inplace=True)


# In[10]:



from imblearn.over_sampling import SMOTENC
oversample = SMOTENC(random_state=312, categorical_features=[1,2,3,4,5,6])
x_over, y_over = oversample.fit_resample(x, y)
print(y_over.value_counts())


# In[11]:



x_over['gender'].replace({'Male':1,
                              'Female':0,
                              },inplace=True)
x_over['ever_married'].replace({'Yes':1,
                              'No':0,
                              },inplace=True)
x_over['Residence_type'].replace({'Urban':1,
                              'Rural':0,
                              },inplace=True)
x_over['work_type'].replace({'Private':1,
                              'Self-employed':2,
                              'Govt_job':0,
                              'children':0,
                              'Never_worked':0
                              
                              },inplace=True)


# In[12]:


scaleF = MinMaxScaler()
x_over = scaleF.fit_transform(x_over)


# In[14]:


x_over1 = pd.DataFrame(x_over)


# In[19]:


x_over1.info()


# In[22]:


import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False 


# In[23]:


sns.heatmap(x_over1.corr(method='pearson'),
            annot=True)
plt.title('독립변수간 상관계수', fontsize=20)
#plt.xlabel('성별',	'나이',	'고혈압',	'심장병'	,'결혼','직업형태',	'거주형태',	'혈당',	'비만도'	,'흡연', fontsize=14)
#plt.ylabel('성별',	'나이',	'고혈압',	'심장병'	,'결혼','직업형태',	'거주형태',	'혈당',	'비만도'	,'흡연', fontsize=14)
plt.show()


# eda

# In[11]:


var = x.groupby('gender')['gender'].count()
plt.title('gender', fontsize=20)
plt.bar(var.index, var) 
plt.xticks([0, 1, 2])
plt.show()


# In[12]:


var = x.groupby('work_type')['work_type'].count()
plt.title('work_type', fontsize=20)
plt.bar(var.index, var) 
plt.xticks([0, 1, 2, 3, 4])
plt.show()


# In[17]:


def pie_graph(df,title,values):   
    labels = df[values].value_counts().index
    values = df[values].value_counts()

    fig = go.Figure(data = [
        go.Pie(
        labels = labels,
        values = values,
        hole = .5)
    ])

    fig.update_layout(title_text = title)
    fig.show()
pie_graph(x_train, 'Hypertension Distribution','hypertension')


# In[39]:


# oh_encoder = OneHotEncoder()
# oh_encoder.fit(x_over)
# oh_labels = oh_encoder.transform(x_over)
# print(oh_labels.shape)


# In[ ]:





# In[40]:


from tensorflow import keras
from tensorflow.keras import layers 


# In[41]:


#데이터 파티셔닝
x_train, x_test, y_train, y_test = train_test_split(x_over, y_over, train_size=0.7, test_size=0.3, random_state=77)


# In[42]:


x_train.shape


# In[45]:


model = keras.Sequential()
model.add(layers.Dense(units = 64, input_dim = 10, activation = "relu")) # 784x64 b:64
model.add(layers.Dense(units = 32, input_dim = 64, activation = "relu" )) # 64x32 b:32
model.add(layers.Dense(units = 1, input_dim = 32, activation = 'sigmoid' )) # 64x10 b:10
model.compile(loss= 'binary_crossentropy', optimizer= "adam", metrics=["acc"])

model.fit(x_train,y_train, epochs=2000)


# In[48]:



#f1_score
pred = (model.predict(x_train)>0.5) +0
f1_score(y_train,pred)


# In[49]:


#f1_score
pred1 = (model.predict(x_test)>0.5) +0
f1_score(y_test,pred1)


# In[50]:


#accuracy_score
accuracy_score(y_train,pred)


# In[51]:


#accuracy_score
accuracy_score(y_test,pred1)


# In[52]:


import matplotlib
matplotlib.rcParams['font.family']='Malgun Gothic'
matplotlib.rcParams['axes.unicode_minus'] = False 


# In[54]:


#train confusion_matrix
c = confusion_matrix(y_train,pred)
sns.heatmap(c,annot=True,fmt='d',linewidths=0.2,cmap='seismic',
           vmin = 0 , vmax=400,xticklabels = ['비뇌졸증예측','뇌졸증예측'],
           yticklabels=['비위험','위험'])
plt.show()


# In[55]:


#test confusion_matrix
c = confusion_matrix(y_test,pred1)
sns.heatmap(c,annot=True,fmt='d',linewidths=0.2,cmap='seismic',
           vmin = 0 , vmax=400,xticklabels = ['비뇌졸증예측','뇌졸증예측'],
           yticklabels=['비위험','위험'])
plt.show()


# In[ ]:





# In[ ]:




