import requests,os

dPrimos = []
dNoPrimos = []

folderName = 'Downloads'
folderPath = '/home/gorra/Escritorio/Gorra/ITR/Programacion/EXAMENES/Examen 2/'

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
        
        os.makedirs(folderPath, exist_ok=True)
        
        if(jsonApi['id'] % 2 == 0):
            dNoPrimos.append(jsonApi)
            noPrim = open('dlXNotPrimes.json', 'w') 
            with noPrim as folderPath:
                noPrim.write(str(dNoPrimos))
                
        else:
            dPrimos.append(jsonApi)
            Prim = open('dlXPrimes.json', 'w') 
            with Prim as folderPath:
                Prim.write(str(dPrimos))
#print()
#print(dNoPrimos)
#print()
#print(dPrimos