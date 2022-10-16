"""
Zadatak 1

Funkcija uzima listu string-ova. Provjeri dal su sve stringovi, ako ne error.
Vraća novu listu, gdje su string-ovi duži od 4 znaka. (Funkcija od dvije
linije)

Ispis: [“Pas”, “Macka”, “Stol”] -> [“Macka”]
"""

list = ["Pas", "Macka", "Stol"]
def fun(list):
    for item in list: assert isinstance(item, str)
    return [item for item in list if len(item)>4]

new_list = fun(list)
print(new_list)