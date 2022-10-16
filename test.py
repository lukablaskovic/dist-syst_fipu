lista = [x for x in range(19)]

print(lista)
d = {k:v if v%3==0 else 0 for k,v in enumerate(lista)}

print(d)