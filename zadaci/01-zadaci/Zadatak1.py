"""
Zadatak 1

Kreiraj funkciju koja uzima listu brojeva i vraca novu listu brojeva koji
su višekratnici broja 4, ako nisu ih korjenuje i zaokruzi na 2 decimale.
(One-liner u return-u)

Ispis: [213,14,12,6543,232] -> [14.59, 3.74, 12, 80.89, 232]
"""
list = [213,14,12,6543,232]
def fun(x):
    return [y if y%4==0 else round(y**0.5,2) for y in x]
print(fun(list))