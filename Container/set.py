fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print("After add()->", fruits)
#After add {'cherry', 'banana', 'orange', 'apple'}

fruits.discard("apple")
print("After discard()->", fruits)
#After discard {'cherry', 'banana', 'orange'}

fruits.pop()
print("After pop()->", fruits)
#After pop {'banana', 'orange'}

fruits.update({"chicken", "beef"})
print("After update()->", fruits)
#After update {'banana', 'orange', 'chicken', 'beef'}
#just modify