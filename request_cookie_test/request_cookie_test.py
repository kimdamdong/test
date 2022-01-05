import requests

cookie_dict = {'my_cookie': 'cookie_value'}
url = 'http://httpbin.org/cookies'

with requests.Session() as session:
    response = session.get(url, cookies=cookie_dict)

print(response)
print(response.text)

## 사용가능한 옵션들
url = '',
params = '',
data = '',
json = '',
headers = '',
cookies = '',
files = '',
auth = '',
timeout = '',
proxies = '',
hooks = '',
stream = '',
verify = '',
cert = '',
allow_redirects = ''