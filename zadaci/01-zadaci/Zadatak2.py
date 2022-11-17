"""
Zadatak 2

Funckija uzima dvije liste, ako su liste iste duljine vraca dictionary gdje
su key vrijednost iz prve list, a value vrijednosti iz druge liste. Ako nisu
vraca prazan dictionary. (One-liner u return-u)

Ispis: [1,2,3], [4,3,2] -> {1: 4, 2: 3, 3: 2}
"""
list1 = [1,2,3]
list2 = [4,3,2]
def fun(list1, list2):
    return {k : v for k,v in zip(list1,list2) if len(list1) == len(list2)}
print(fun(list1, list2))