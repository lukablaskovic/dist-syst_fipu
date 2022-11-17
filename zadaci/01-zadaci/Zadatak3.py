"""
Zadatak 3

Funkcija prima listu dictionary-a IP adresa, kreira set od vrijednosti.
(One-liner u return-u)

Ispis: [{“ip”:“192.168.3.1”}, {“ip”:“10.0.0.0”}, {“ip”:“127.0.0.0”},
{“ip”:“192.168.3.1”}] -> {"10.0.0.0", "192.168.3.1", "127.0.0.0"}
"""
ipaddr = [
    {
        "ip": "192.168.3.1"
    },
    {
        "ip": "10.0.0.0"
    },
    {
        "ip": "127.0.0.0"
    },
    {
        "ip": "192.168.3.1"
    }
]
def fun(x):
    return{y for d in x for _,y in d.items()}
print(fun(ipaddr))
