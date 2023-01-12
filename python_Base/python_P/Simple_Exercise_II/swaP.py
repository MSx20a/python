def swap(x:str):
    z=""
    for i in x:
        if i == i.upper():
            z+=i.lower()
        else:
            z+=i.upper()    
    return z

print(swap("Aloha"))
print(swap("Love you."))