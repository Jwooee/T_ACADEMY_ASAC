import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import Adam
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, OneHotEncoder,MinMaxScaler
from imblearn.over_sampling import SMOTENC
from sklearn import datasets
import joblib

def meodel(age, bmi, gender, hypertension, heart_disease,
        ever_married, Residence_type, work_type, avg_glucose_level,
        smoking_status):
# def meodel():
    df = pd.read_csv('healthcare-dataset-stroke-data.csv')

    a = df[df['gender']=='Other'].index
    df.drop(a,inplace=True)

    df[df['gender']=='Other']

    df['smoking_status'].replace({'formerly smoked':1,
                                'never smoked':0,
                                'smokes':2,
                                'Unknown':0
                                },inplace=True)

    features=['age','gender','hypertension','heart_disease', 'ever_married',
            'work_type', 'Residence_type' , 'avg_glucose_level','bmi','smoking_status']#데이터와 관련없는 id 제거
    x=df[features]
    y_before=df['stroke']
    y=pd.DataFrame(y_before)
    y.columns=['target_y']

    x.info()
    x.fillna(x['bmi'].median(), inplace=True)

    oversample = SMOTENC(random_state=312, categorical_features=[1,2,3,4,5,6])
    x_over, y_over = oversample.fit_resample(x, y)

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

    scaleF = MinMaxScaler()
    x_over = scaleF.fit_transform(x_over)

    x_over1 = pd.DataFrame(x_over)

    from tensorflow import keras
    from tensorflow.keras import layers 

    x_train, x_test, y_train, y_test = train_test_split(x_over, y_over, train_size=0.7, test_size=0.3, random_state=77)

    # model = keras.Sequential()
    # model.add(layers.Dense(units = 64, input_dim = 10, activation = "relu")) # 784x64 b:64
    # model.add(layers.Dense(units = 32, input_dim = 64, activation = "relu" )) # 64x32 b:32
    # model.add(layers.Dense(units = 1, input_dim = 32, activation = 'sigmoid' )) # 64x10 b:10
    # model.compile(loss= 'binary_crossentropy', optimizer= "adam", metrics=["acc"])

    # model.fit(x_train,y_train, epochs=2000)
    
    # 

    loaded_model = joblib.load(r'deep_model.pkl')
    # pred = (loaded_model.predict(x_train)>0.5) +0
    # print(pred)
    # score = loaded_model.score(X,y)
    # print('정확도: {score:.3f}'.format(score=score))
    # #f1_score
    res = (loaded_model.predict([[age, gender, hypertension, heart_disease,ever_married, work_type, Residence_type, avg_glucose_level, bmi, smoking_status]])>0.5)+0
    # res = (loaded_model.predict([[73.11150146,0,0,0,1,2,1,75.266532,26.1113258,0]])>0.5)+0
    # res = loaded_model.predict([[73.11150146,0,0,0,1,2,1,75.266532,26.1113258,0]])>0.5)+0
    # int(res)
    # pred = (model.predict(x_train)>0.5) +0
    # f1_score(y_train,pred)

    # #f1_score
    # pred1 = (model.predict(x_test)>0.5) +0
    # f1_score(y_test,pred1)

    # #accuracy_score
    # accuracy_score(y_train,pred)

    # #accuracy_score
    # accuracy_score(y_test,pred1)
    # joblib.dump(model, './model.pkl')
    if res == 1:
        string = "뇌줄중 위험이 있습니다."
    elif res==0:
        string = "뇌줄중 위험이 적습니다."
    print("아아아아")
    print(res)
    return string
# meodel()