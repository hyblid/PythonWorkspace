_list = [4, 2, 1, 3, 5]
print(_list)
print("lenght", len(_list))

_list2 = _list.copy()
print("_list2", _list2)

_list.append(6)
print("After append", _list)

_list.remove(6)
print("After remove", _list)
_list.insert(5, 6)
print("After insert", _list)

print("After pop", _list.pop())

_list.sort()
print("After sort", _list)
_list.reverse()
print("After reverse", _list)
_list.extend(_list2)
print("After extend", _list)

_list.count(5)
print("After count", _list.count(5))

_list.clear()
print("After clear", _list)
