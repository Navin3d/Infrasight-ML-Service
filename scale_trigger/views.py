from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
from configurations import eureka
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

eureka.register()

data = pd.read_csv('https://navin3d.github.io/Infrasight-Staticfiles/InfraDataSet_final.csv')
X = data[['cpu', 'disk', 'ram','load','uptime']]
y = data['output']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a random forest classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)
print(clf.predict([[100, 79, 6, 4, 10]]))
@api_view(["GET"])
def scale_decision(request,cpu,disk,ram,load,uptime):
    if request.method == "GET":
        scaling_decision = clf.predict([[cpu, disk, ram, load, uptime]])
        return Response(scaling_decision[0], status=status.HTTP_200_OK)
