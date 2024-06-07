import requests,os

api = 'https://jsonplaceholder.typicode.com/todos/1'
getApi = requests.get(api)
jsonApi = getApi.json()
print(jsonApi)