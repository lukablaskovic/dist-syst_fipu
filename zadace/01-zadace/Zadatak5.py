"""
Zadatak 5

Funkcija prima listu tuple-a o studentima (id, ime, prezime). Vraća novu
sortiranu po id-u (manji->veci) listu dictionary-a o studentima kojima ime
i prezime počinje istim slovom. (One-liner u return-u)

Ispis : [(121,“Ivan”,“Ivic”),(431,“Pero”,“Horvat”),(31,“Marija”,“Maric”)]

-> [{"id": 31, "ime": "Marija", "prezime": "Maric"}, {"id": 121, "ime":
"Ivan", "prezime": "Ivic"}]

"""
list_of_tuples = [
    (121, "Ivan", "Ivic"),
    (431, "Pero", "Horvat"),
    (31, "Marija", "Maric")
]
def fun(tuple_list):
    return sorted([{"id" : t[0], "ime" : t[1], "prezime" : t[2]} for t in tuple_list if t[1][0] == t[2][0]],key= lambda x: x["id"])

print(fun(list_of_tuples))