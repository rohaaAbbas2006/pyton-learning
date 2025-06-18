list = [1,'Apple',True,34.4,43]
print(list[2])
print(list[2:5])
print(list[1:3])

list.append("New Item")
print(list)

list.extend([100, 200, 300])
print(list)

list.insert(2, "Inserted Item")
print(list)

list.remove(34.4)
print(list)

list.pop(1)
print(list)

print(len(list))
print(list.index("Inserted Item"))