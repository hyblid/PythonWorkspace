fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print("After add", fruits)

fruits.discard("apple")
print("After discard", fruits)

fruits.pop()
print("After pop", fruits)

fruits.update({"chicken", "beef"})
print("After update", fruits)