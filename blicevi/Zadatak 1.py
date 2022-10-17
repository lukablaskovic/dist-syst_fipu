"""
"""

def fun(li):
    assert isinstance(li, list)
    assert [el for el in li if isinstance(el, str)]

    return {k:v[::-1] for k,v in enumerate(li)}

lis = ["Stol", "Stolica", "Krevet", "Fotelja"]
print(fun(lis))