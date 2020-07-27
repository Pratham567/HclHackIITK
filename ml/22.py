# This code was submitted as a solution to the competition

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import json, urllib.request

file = 'https://mettl-arq.s3-ap-southeast-1.amazonaws.com/questions/iit-kanpur/cyber-security-hackathon/round1/problem2/f1fswvsvi0/training.json'
with urllib.request.urlopen(file) as url:
    json_file = json.loads(url.read().decode('utf-8'))

df= pd.DataFrame(columns=['grade', 'score1', 'score2', 'score3', 'score4', 'score5', 'score6', 'score7', 'score8', 'score9', 'score10'])

for i in json_file:
    df = df.append(pd.DataFrame.from_dict(i).transpose())

    df.grade = pd.Categorical(df.grade).codes
    target = np.array(df.iloc[:, 0])

from sklearn.model_selection import train_test_split
# X_train, X_test, y_train, y_test = train_test_split(df, target, test_size= 0.5, random_state=5)

X_train = df
y_train = target

from sklearn.ensemble import RandomForestClassifier
rf = RandomForestClassifier(n_estimators=100)

y_train=y_train.astype('int')
rf = rf.fit(X_train, y_train)

with urllib.request.urlopen(input1) as url_t:
    json_file_t = json.loads(url_t.read().decode('utf-8'))

df_t= pd.DataFrame(columns=['grade', 'score1', 'score2', 'score3', 'score4', 'score5', 'score6', 'score7', 'score8', 'score9', 'score10'])

for i in json_file_t:
    df_t = df_t.append(pd.DataFrame.from_dict(i).transpose())

df_t.grade = pd.Categorical(df_t.grade).codes
target_t = np.array(df_t.iloc[:, 0])
X_test = df_t
y_test = target_t

from sklearn import metrics
y_pred = rf.predict(X_test)

answer = X_test.iloc[:, 0].to_dict()
count = 0
for i in answer:
    if y_pred[count] == 0:
        answer[i] = ('Poor')
    elif y_pred[count] == 1:
        answer[i] = ('Fair')
    elif y_pred[count] == 2:
        answer[i] = ('Good')
    elif y_pred[count] == 3:
        answer[i] = ('Very good')
    elif y_pred[count] == 4:
        answer[i] = ('Exceptional')
    else:
        None
    count +=1

# return answer