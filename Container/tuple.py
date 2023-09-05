tuple1 = (10, "John", "Howard", 3.3)
print(tuple1)

print("After count()->", tuple1.count(10))
print("After len()->", len(tuple1))

print("After index()->", tuple1.index("Howard"))
print("After acess()->", tuple1[1])

#copy
tuple2 = tuple1    
print("After copy()->", tuple2)

#augement assignment
tuple1 += (20,30)
print("Augument assigment", tuple1)

#tuple can be muttable
student_tuple= ("Howard", [10,20,30])
student_tuple[1][2] = 100
print("Tuple can Mutualbe", student_tuple)

colors= ["red", "yellow", "blue"]
for index, color in enumerate(colors): 
    print(f"index:{index}, color{color}") 
