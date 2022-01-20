import math

def gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums):
    telpas_izmers = math.ceil(telpas_garums) * math.ceil(telpas_platums)
    izmaksa = cena * telpas_izmers / linoleja_platums
    return izmaksa

cena = int(input("ievadi linoleja cenu eur uz kvadratmetru: "))
linoleja_platums = int(input("ievadi linoleja ruļļa platumu metros: "))
telpas_platums = int(input("ievadi telpas platumu metros: "))
telpas_garums = int(input("ievadi telpas garumu metros: "))

print("izklājot garumā:")
print(str(gridas_izmaksa(cena, linoleja_platums, telpas_platums, telpas_garums)) + " euro")
print("izklājot platumā")
print(str(gridas_izmaksa(cena, linoleja_platums, telpas_garums, telpas_platums)) + " euro") 