class FlexibleDict(dict):
    def __getitem__(self, key):
        try:
            if key in self:
                pass
            elif str(key) in self:
                key =str(key)
            elif int(key) in self:
                key = int(key)
        except ValueError:
            pass
        return dict.__getitem__(self,key)

class Stringdict(dict):
    def __setitem__(self, key, value):
        return dict.__setitem__(self,str(key), value)
    
class RecentDict(dict):
    def __init__(self, maxsize):
        super().__init__()
        self.maxsize = maxsize

    def __setitem__(self, key, value):
        dict.__setitem__(self, str(key), value)

        if len(self) > self.maxsize:
            self.pop(list(self.keys())[0])
            
class FlatList(list):
    def append(self, new_value):
        try:
            for one_item in new_value:
                list.append(self, one_item)
        except TypeError:
            list.append(self, new_value)

f = FlatList()
f.append([10,20,30])
print(f)