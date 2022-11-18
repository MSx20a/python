# dictionary is mutable
# it like object in other programming
x = {}
x["name"] = "Alvin"
x["age"] = 27
print(x)

scooter = {"manufacturer": "KYMCO", "name": "RacingS", "weight": "130kg"}
print(scooter.keys())
print(scooter.values())
print(scooter.items())  # something like a list of tuples
print(scooter["name"])
print("--------------------")

# sorted method（排序後不想改變原本的dictionary key，而是會直接產生一個新的dictionary key存放到新的記憶體位置）
person = {"name": "kira", "age": "18"}
y = sorted(person)
print(person)
print(y)
