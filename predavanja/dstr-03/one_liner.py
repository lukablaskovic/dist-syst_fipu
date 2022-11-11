studenti = [
    {
        "name" : "Marko",
        "kolegiji" : ["RS"]
    },
    {
        "name" : "Ana",
        "kolegiji" : ["RS", "WA"]
    },
    {
        "name" : "Hrvoje",
        "kolegiji" : ["PI"]
    }
]

# rez = ["Marko", "Ana", "Hrvoje"]

rez = []
for student in studenti:
    rez.append(student["name"])

#print(rez)

rez2 = [student["name"] for student in studenti ]

#print(rez2)

"""
rez3 = {
    "Marko" : True,
    "Ana" : True,
    "Hrvoje" : True
}
"""
rez3 = {}
for s in studenti:
    print("s=", s)
    ime = s["name"]
    rez3[ime] = True

rez4 = { s["name"] : True for s in studenti}

print("rez4", rez4)