"""
1. Kreirajte jednu asinkronu (afun1) i jednu sinkronu (fun2) funkciju, te
funkciju main. Unutar funkcije main, kreiraju se tri datoteke u radnom
direktoriju te se nazivi spremaju u listu.

[“datoteka1”, “datoteka2”, “datoteka3”]

Nakon toga poziva se afun1 koja uzima parametar lista naziva datoteka.
Čeka 0.2 sekunde i vraća listu dictionary-a, gdje svaki dictonary sadrži
naziv datoteke te njenu veličinu u byte-ovima.

[{“naziv”:“datoteka1”, “velicina”:1212},{“naziv”:“datoteka2”, “velicina”:8912},{“naziv”:“datoteka3”, “velicina”:2212}]

Odmah nakon afun1, unutar main-a poziva se fun2 koja prima listu naziva
datoteka. Unutar nje, u svaku datoteku upisuje brojeve od 1 do 10 000.
Na kraju main-a čeka se rezultat iz afun1 koji se ispisuje u konzolu.

(Hint: os package)
"""

import asyncio
import os

main_directory = os.getcwd()
current_directory = main_directory+"/zadace/03-zadace/"

async def afun1(file_names):
    await asyncio.sleep(0.2)
    return [{"naziv" : f, "velicina" : os.path.getsize(current_directory+f)} for f in file_names]

def fun2(file_names):
    for file in file_names:
        f = open(current_directory+file, "a")
        for n in range(1,10000+1):
            f.write(str(n)+ "\n")
    pass

async def main():
    names = []
    for x in range(3):
        open(current_directory+"datoteka{}".format(x+1), "w")
        names.append("datoteka{}".format(x+1))
    result = await afun1(names)
    fun2(names)
    result = await afun1(names)
    print(result)

if __name__ == "__main__":
    asyncio.run(main())