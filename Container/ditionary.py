car1 = { "brand": "Ford", "model": "Mustang", "year": 1964}

print("After items()->", car1.items())
print("After keys()->", car1.keys())
print("After values()->", car1.values())

car2 = car1.copy()
print("After copy1()->", car2)
print("After get()->", car1.get("brand"))

car1.pop("brand")
print("after pop()->",car1)

car1.update({"brand" : "Ford", "price": 100})
print("after update()->",car1)

#pop last item
car1.popitem()
print("after pop()-> item",car1)

x = ('key1', 'key2', 'key3')
y = 0
thisdict = dict.fromkeys(x, y)
print("After formkeys()->", thisdict)
#After formkeys {'key1': 0, 'key2': 0, 'key3': 0}
thisdict.clear()
print("After clear()->", thisdict)

""" How to aceess Dictionary of Dictionary"""
fields = {
    "Date": {'req': True, 'values':10000},
    "Time": {'req': True, 'values': ['8:00', '12:00', '16:00', '20:00']}}

for t in fields["Time"].get("values"):
    print(f"time {t}")
    
print(fields.keys())