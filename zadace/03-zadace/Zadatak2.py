"""
2. Kreirajte dvije asinkrone funkcije (afunc1, afunc2) i funkciju main. 
Unutar funkcije main pozivaju se obje funkcije jedna za drugom. 

Afunc1 kreira 10 Normalnih distribucija s 1M sample-ova i nakon svake čeka 0.9
sekundi. 
Afunc2 prati iskorištenost CPU-a u vremenskom razmaku od 10
sekundi. 

Na kraju funkcije main, čeka se rezultat afunc2 te se u konzolu
ispisuje iskorištenost CPU-a.

(Hint: numpy, psutils package)

Iskorištenost CPU u 10 sekundi iznosi : 3.8
"""

import asyncio
import numpy as np
import psutil as ps

async def afunc1():
    np.random.normal(size=(10,1000000))
    await asyncio.sleep(0.9)
    pass

async def afunc2():
    return ps.cpu_percent(10)

async def main():
    asyncio.create_task(afunc1())
    cpu_usage = await afunc2()
    print('Iskorištenost CPU-a u 10 sekundi iznosi: ', str(cpu_usage) + "%")
    pass

if __name__ == "__main__":
    asyncio.run(main())