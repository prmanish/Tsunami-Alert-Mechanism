# -*- coding: utf-8 -*-
"""Tsunami Alert Mechanism.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-49p0DNkPCqAP0OVdKiUjK0Q-DuH_yhV
"""

!pip install pandas_ml

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mp
from sklearn.preprocessing import StandardScaler
from sklearn.preprocessing import scale
from sklearn import preprocessing
import sklearn as sk
from sklearn.decomposition import PCA

from google.colab import files
uploaded=files.upload()

import io
df=pd.read_csv(io.BytesIO(uploaded['sources.csv']))

df.head()

dr=['COUNTRY','STATE/PROVINCE','LOCATION','LATITUDE','LONGITUDE']
df=df.drop(dr,axis=1)

df.head()

df.fillna(0,inplace=True)

df.head()

df.astype(int).dtypes

from sklearn.model_selection import train_test_split
X=df.iloc[:,:-1]
y=df['REGION_CODE']
scale=StandardScaler()
Xn=scale.fit_transform(X)
pca=PCA(n_components=30)
Xs=pca.fit_transform(Xn)
X_train, X_test, y_train, y_test = train_test_split(Xs, y, test_size = 0.33, random_state=42)

from sklearn import  linear_model
loreg = linear_model.LogisticRegression()
loreg.fit(X_train, y_train)
print("Accuracy",loreg.score(X_test, y_test))

y_predicted = np.array(loreg.predict(X_test))
y_prob1=loreg.predict_proba(X_test)[:,1]
y_prob2=loreg.predict_proba(X_test)[:,2]

y_predicted = np.array(loreg.predict(X_test))
y_right = np.array(y_test)
from pandas_ml import ConfusionMatrix
confusion_matrix = ConfusionMatrix(y_right, y_predicted)
print("Confusion matrix:\n%s" % confusion_matrix)
confusion_matrix.plot(normalized=True)
plt.show()
confusion_matrix.print_stats()

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
ans=mean_absolute_error(y_test,y_predicted)
ans1=mean_squared_error(y_test,y_predicted)
print("Mean Absolute Error Is:",ans)
print("Mean Squared Error Is:",ans1)

#classification report
from sklearn.metrics import classification_report
print(classification_report(y_test,y_predicted))

regions = {77:'West Coast of Africa',
            78:'Central Africa',
            73:'Northeast Atlantic Ocean',
            72:'Northwest Atlantic Ocean',
            70:'Southeast Atlantic Ocean',
            71:'Southwest Atlantic Ocean',
            75:'E. Coast USA and Canada, St Pierre and Miquelon',
            76:'Gulf of Mexico',
            74:'Caribbean Sea',
            40:'Black Sea and Caspian Sea',
            50:'Mediterranean Sea',
            30:'Red Sea and Persian Gulf',
            60:'Indian Ocean (including west coast of Australia)',
            87:'Alaska (including Aleutian Islands)',
            84:'China, North and South Korea, Philippines, Taiwan',
            81:'E. Coast Australia, New Zealand, South Pacific Is.',
            80:'Hawaii, Johnston Atoll, Midway I',
            83:'E. Indonesia (Pacific Ocean) and Malaysia',
            82:'New Caledonia, New Guinea, Solomon Is., Vanuatu',
            86:'Kamchatka and Kuril Islands',
            85:'Japan',
            88:'West Coast of North and Central America',
            89:'West Coast of South America'}


df['REGIONS'] = df['REGION_CODE'].map(regions)
df['REGIONS_FRECUENCY']=df.groupby(df.REGIONS)['REGIONS'].transform('count')

ans=[]
for i in range(len(y_predicted)):
  ans.append(regions[y_predicted[i]])
print(max(y_predicted),max(ans))

