import struct


class Book:
    # bigend, 64byte char[],pad,64byte char[],pad,short,short
    packer = struct.Struct(">64sx64sx2h")

    def __init__(self, title="", author="", pages=0, pages_read=0):
        self.title = title
        self.author = author
        self.pages = pages
        self.pages_read = pages_read

    def update_progress(self, pages_read):
        self.pages_read = min(pages_read, self.pages)

    def serialize(self):
        #encode to UTF-8
        return self.packer.pack(
            self.title.encode(),
            self.author.encode(),
            self.pages,
            self.pages_read
        )

    """ 
    bits = Book.packer.size()
    """
    @classmethod
    def deserialize(cls, bits):
        title, author, pages, pages_read = cls.packer.unpack(bits)
        title = title.decode()
        author = author.decode()
        return cls(title, author, pages, pages_read)
