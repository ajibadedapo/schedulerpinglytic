import requests

url = "https://uptimebackend.herokuapp.com/api/monitor/v1"

payload = "------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"files\"; filename=\"20180215-033512.mp4\"\r\nContent-Type: video/mp4\r\n\r\n\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"ip_address\"\r\n\r\n10.10.10.110\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW\r\nContent-Disposition: form-data; name=\"date\"\r\n\r\n2018-02-14 18:27:20\r\n------WebKitFormBoundary7MA4YWxkTrZu0gW--"
headers = {
    'content-type': "multipart/form-data; boundary=----WebKitFormBoundary7MA4YWxkTrZu0gW",
    'Accept': "application/json",
    'Content-Type': "application/x-www-form-urlencoded",
    'Cache-Control': "no-cache",
    'Postman-Token': "50de5d50-e0f9-d2ab-6b37-aee8aa127bf3"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)