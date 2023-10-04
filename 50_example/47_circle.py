
class CircleIterator():
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0
            
    def __next__(self):
        if self.index >= self.max_times:
            raise StopIteration
        value = self.data[self.index % len(self.data)]
        self.index += 1
        return value
    
    def __iter__(self):
        return self

class Circle(CircleIterator):
    def __init__(self, data, max_times):
        self.data = data
        self.max_times = max_times
        self.index = 0

def circle(data, max_times):
    for index in range(max_times):
        yield data[index % len(data)]   

class MyRange:
    def __init__(self, start, stop=None, step_size=1):
        if stop is None:
            self.current = 0
            self.stop = start
        else:
            self.current = start
            self.stop = stop
        self.step_size = step_size

    def __iter__(self):
        return self
    """
    __iter__() call __next__()
    __next__ dont need loop becuase __next__ always iterate before "raise StopIteration"
    
    """  
    def __next__(self):
        if self.current >= self.stop:
            raise StopIteration

        value = self.current
        self.current += self.step_size
        return value       

c = circle('abc', 5)
print(list(c))

r = MyRange(0,5,1)
print(list(r))