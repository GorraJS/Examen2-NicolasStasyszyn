import requests,os

dPrimos = []
dNoPrimos = []

folderName = 'Downloads'
folderPath = os.path.join(os.getcwd())

api = 'https://jsonplaceholder.typicode.com/todos/'

print('Seleccione catidad de posts (max 100)')
nPosts = input() #3 

i = 0
while(int(nPosts) > i ):
    i+=1
    if(int(nPosts) > 100 or int(nPosts) < 0):
        print('La cantidad debe ser de 0 a 100')
    else:
        api2 = api + str(i)
        getApi = requests.get(api2)
        jsonApi = getApi.json()
        
        if(jsonApi['id'] % 2 == 0):
            dNoPrimos.append(jsonApi) 
        else:
            dPrimos.append(jsonApi)
#print()
#print(dNoPrimos)
#print()
#print(dPrimos)
if not os.path.exists(folderPath):
    os.makedirs(folderPath,folderName)
    
#with open(fileName, 'wb') as:
    
