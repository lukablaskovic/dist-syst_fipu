"""
Zadatak 1
Kreirajte dvije asinkrone funkcije te funkciju main. 

Prva funkcija vraća
listu dictionary-a u kojem se nalaze artikli.
[{“artikl”:“Kava”},{“artikl”:“Voda”}]

Druga funkcija prima listu dictionary-a artikala, te svakom artiklu dodaje
random cijenu u range-u od 1 do 10. Prvo provjeri radi li se o listi, te jesu
li svi njeni elementi dictionary. Funkcija main poziva obije funkcije, te
njenim zavrsetkom zavrsava i program.
"""
import asyncio
import numpy as np
async def fun1():
    return [{"artikl" : v} for v in ["Kava", "Voda"]]

async def fun2(x):
    assert isinstance(x, list) and all([isinstance(d, dict)] for d in x)
    return [{**d, **{"cijena": np.random.randint(1,10)}} for d in x]

async def main():
    artikli = await fun1()
    final = await fun2(artikli)
    print(final)

if __name__ == "__main__":
    asyncio.run(main())