import requests

print(requests.get('http://www.baidu.com').content.decoding())
