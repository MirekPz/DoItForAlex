import requests

req = requests.get("http://numbersapi.com/random/year")

print(req)
print(req.text)
print(req.content)
print(req.cookies)
print(req.encoding)
print(req.history)
print(req.status_code)
print(req.headers)
