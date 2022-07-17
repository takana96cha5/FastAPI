import requests

url = 'http://jsonplaceholder.typicode.com/posts/'
params = {
    'id': 3
}

res = requests.get(url,params)
print(res.status_code)
print(res.json()[0])
