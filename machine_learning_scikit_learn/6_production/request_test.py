import requests

url = "http://127.0.0.1:8080/predict"
obj = {"age": 52, "sex": 1, "cp": 0, "trestbps": 125, "chol": 212, "fbs": 0, "restecg": 1, "thalach": 168,
       "exang": 0, "oldpeak": 1, "slope": 2, "ca": 2, "thal": 3}
x = requests.post(url, json=obj)

print(x.text)
