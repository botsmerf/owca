import random

gracze = ["A", "B","C","D","E","F", "H","J","G","K"]

def genTeam(lista):
    random.shuffle(lista)
    polowaListy = len(lista) //2
    team1 = lista [0 : polowaListy]
    team2 = lista [ polowaListy : ] 
    return team1,team2



genTeam([1,2,3,4,5,6,7,8,9])


print(a[0])
print(a[1])