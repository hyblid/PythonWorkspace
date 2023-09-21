import shutil

def myxml(tagname, content='', **kwargs):
    attrs = ''.join([f' {key}="{value}"' for key, value in kwargs.items()])
    return f'<{tagname}{attrs}>{content}</{tagname}>'

def copyfile(origanlfile, *args):
        for num in args:
            with open(f"copt{num}", "w") as out_file:
                    for in_file in open(origanlfile):
                        out_file.write(in_file)
      
def factorial(*args):
    if not args:
        return 0

    total = args[0]
    for one_number in args[1:]:
        total *= one_number

    return total

def anyjoin(seq, glue=' '):
    return glue.join(str(one_item) for one_item in seq)
        
print(anyjoin([1,2,3]))