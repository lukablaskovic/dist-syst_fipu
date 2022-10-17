d1= {"valute" : ["GBP", "USD", "CZK", "Error"], "cijena" : [8,5,7,7,0.3,10.3]}
d2 = {"valute" : ["EUR", "USD", "CZK", "Error"], "cijena" : [7.5, 7.7, 0.3, 5.5]}
#Vraca novu listu u kojoj se nalaze samo elementi koji se ponavljaju u oba na istim indexima te imaju istu vrijednost

def fun(dic1, dic2):
    assert isinstance(dic1, dict)
    assert isinstance(dic2, dict)
    for lis in dic1:
        assert isinstance(lis, list)
    assert all(key in dic1.keys() for dic1 in dic1 for key in dic.keys()) 
print(fun(d1,d2))