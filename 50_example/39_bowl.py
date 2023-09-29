class Scoop():
    def __init__(self, flavor):
        self.flavor = flavor
        
class Bowl():
    def __init__(self):
        self.scoops = []
        
    def add_scoops(self, *new_scoops):
        for one_scoop in new_scoops:
            self.scoops.append(one_scoop)
            
    def __repr__(self):
        return '\n'.join(s.flavor for s in self.scoops)

class TooManyBookOnShelfError(Exception):
    pass
       
class Book():
    def __init__(self, title, author, price, width):
        self.title=title
        self.author=author
        self.price=price
        self.width=width

class Shelf:
    def __init__(self):
        self.books = []
        self.width=500

    def add_books(self, *args):
        for new_book in args:
            if self.total_width() + new_book.width > self.width:
                raise TooManyBookOnShelfError('Too many books!')
            self.books.append(new_book)    

    def total_price(self):
        return sum(one_book.price
                   for one_book in self.books)
    
    def total_width(self):
        return sum(one_book.width
                   for one_book in self.books)        
            
    def has_book(self, title):
        #The list is dynamic, whereas the tuple has static characteristics. 
        #This means that lists can be modified whereas tuples cannot be modified,
        #The tuple is faster than the list because of static in nature.
        return title in (one_book.title for one_book in self.books)
    
 
b1 = Book("a", "aa", 1000, 100)       
b2 = Book("b", "bb", 2000, 200)       
b3 = Book("c", "cc", 3000, 300)
s = Shelf()
s.add_books(b1,b2,b3)
print(s.total_price())
       