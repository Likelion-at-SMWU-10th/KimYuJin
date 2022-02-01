from key import apikey
import requests
import json

city = "Seoul"
lang = "kr"
units = "metric"
api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&lang={lang}&units={units}"

result = requests.get(api)
# print(result.text)

data = json.loads(result.text)
# print(data)

print(data["name"] + "�� �����Դϴ�.")
print("������", data["weather"][0]["description"], "�Դϴ�.")
print("���� �µ���", data["main"]["temp"], "�Դϴ�.")
print("������ ü�� �µ���",  data["main"]["feels_like"], "�Դϴ�.")
print("���� �����",data["main"]["temp_min"], "�Դϴ�.")
print("�ְ� �����", data["main"]["temp_max"], "�Դϴ�.")
print("������", data["main"]["humidity"], "�Դϴ�.")
print("�����", data["main"]["pressure"], "�Դϴ�.")
print("ǳ����", data["wind"]["deg"], "�Դϴ�.")
print("ǳ����", data["wind"]["speed"], "�Դϴ�.")