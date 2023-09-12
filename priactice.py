peoples = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]

def format_sort_record1(list_of_tuples):
    template = "{1:10} {0:10} {2:5.2f}"
    for person in peoples:
        print("{1:10} {0:10} {2:5.2f}".format(*person))
format_sort_record1(peoples)