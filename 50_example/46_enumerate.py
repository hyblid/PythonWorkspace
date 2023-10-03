class MyEnumerate():
    # def __init__(self, start=0):
        # self.data = data
        # self.start = start

    def __iter__(self):
        #return MyEnumerateIterator(self.data) 
        return self
    
    def my_enumerate(data, start=0):
        index = start
        for one_item in data:
            yield (index, one_item)
            index += 1
        

# class MyEnumerateIterator:
#     def __init__(self, data, start):
#         self.data = data
#         self.index = start

#     def __next__(self):
#         if self.index >= len(self.data):
#             raise StopIteration
#         value = (self.index, self.data[self.index])
#         self.index += 1
#         return value

e = MyEnumerate.my_enumerate('abc')

print('** A **')
for index, one_item in e:
    print(f'{index}: {one_item}')
    
print('** B **')
for index, one_item in e:
    print(f'{index}: {one_item}')