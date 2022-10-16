"""
Zadatak 6
Funkciji se predaju dva parametra. Provjera se jesu li parametri istog tipa,
ako ne error. Provjeri se jesu li parametri liste ili dictionary, ako ne error.
Vraća se spojena lista ili dictionary.

Ispis : [1,2,1,2],[3,2] -> [1,2,1,2,3,2]
Ispis : {1:2,3:2},{5:2,4:1} -> {1: 2, 3: 2, 5: 2, 4: 1}
"""
list1 = [1,2,1,2]
list2 = [3,2]
dict1 = {1:2, 3:2}
dict2 = {5:2, 4:1}

def fun(data1, data2):
    assert type(data1) == type(data2)
    assert isinstance(data1, (list, dict))
    assert isinstance(data2, (list, dict))
    return data1 + data2 if isinstance(data1, list) else data1 | data2

print(fun(dict1, dict2))