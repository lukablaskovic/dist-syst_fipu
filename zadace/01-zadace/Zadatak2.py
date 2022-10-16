"""
Zadatak 2

Funkcija uzima listu i dictionary. Provjeri jesu li lista i dictionary, ako ne
error. Provjeri imaju li isti broj elemenata. Provjeri jesu li svi elementi
liste tipa integer. Vraća novi dictionary, gdje je value element iz liste na
tom indexu ako se nalazi unutar [5,10] ako ne upisuje -1.

Ispis : [8,7,1], {1:2,2:1,3:2} -> {1: 8, 2: 7, 3: -1}
"""
some_list = [8,7,1]
some_dict = {1 : 2, 2 : 1, 3 : 2}

def fun(list_p, dict_p):
    assert isinstance(list_p, list)
    assert isinstance(dict_p, dict)
    assert len(list_p) == len(dict_p)
    assert [el for el in list_p if isinstance(el, int)]
    return {k:v if v in range(5,10) else -1 for k,v in zip(dict_p, list_p)}

new_dict = fun(some_list,some_dict) 
print(new_dict)