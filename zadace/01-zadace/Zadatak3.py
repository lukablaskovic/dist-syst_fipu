"""
Zadatak 3
Funkcija uzima listu dictionary-a o artiklima. Provjerava je li parametar
lista, ak ne error. Provjerava jesu li svi elementi dictionary, ako ne error.
Provjerava imaju li svi dictionary odgovarajuća 3 ključeva, ako ne error.
(“cijena”,“naziv”,“kolicina”) (Moze i u dvije linije) 
Vraća novi nested dictionary s ključem “ukupno” i dictionary sa ključem “artikli” i listom
svih odabranih artikala te “cijena” s ukupnom cijenom računa.
(Ne treba biti One-liner)

[{"cijena":8,"naziv":"Kruh","kolicina":1}, 
{"cijena":13,"naziv":"Sok","kolicina":2}, 
{"cijena":7,"naziv":"Upaljac","kolicina":1}] 

-> {'ukupno': {'artikli': ['Kruh', 'Sok', 'Upaljac'], 'cijena': 41}}
"""
artikli = [
    {"cijena":8,"naziv":"Kruh","kolicina":1}, 
    {"cijena":13,"naziv":"Sok","kolicina":2}, 
    {"cijena":7,"naziv":"Upaljac","kolicina":1} 
]
def fun(list_p):
    assert isinstance(list_p, list)
    for dic in list_p:
        assert isinstance(dic, dict)
    assert all(key in dic.keys() for dic in list_p for key in dic.keys())
    for dic in list_p:
        return {"ukupno" : {"artikli": [dic["naziv"] for dic in list_p], "cijena" : sum([dic["kolicina"] * dic["cijena"] for dic in list_p])}}
print(fun(artikli))




