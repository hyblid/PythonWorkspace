nest_dict = [
    {"name": "howard", "age": 34},
    {"name": "jeniffer", "age": 14},
    {"name": "james", "age": 20},
]

nest_dict1 = {
   1: {"name": "howard1", "age": 1000},
   2: {"name": "jeniffer1", "age": 1400},
   3: {"name": "james1", "age": 2000},
}

people = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}

for d in nest_dict:
    for key, value in d.items():
        print(key,value, end="\n")

for key in nest_dict1.keys():
        print(nest_dict1[key].get("name"), nest_dict1[key].get("age"))