import operator
from collections import namedtuple

PEOPLES = [('Donald', 'Trump', 7.85),
          ('Vladimir', 'Putin', 3.626),
          ('Jinping', 'Xi', 10.603)]
def format_sort_record1(list_of_tuples):
    output = []
    template = "{1:10} {0:10} {2:5.2f}"
    for person in sorted(list_of_tuples,key=operator.itemgetter(1,0)):
        output.append(template.format(*person))
    return output
#-----------------------------------------------------------------------------#
Person = namedtuple('Person', ['first', 'last', 'distance'])
PEOPLE = [Person('Donald', 'Trump', 7.85),
          Person('Vladimir', 'Putin', 3.626),
          Person('Jinping', 'Xi', 10.603)]
def format_sort_records(list_of_tuples):
    output = []
    template = '{last:10} {first:10} {distance:5.2f}'
    for person in sorted(list_of_tuples, key=operator.attrgetter('last', 'first')):
        output.append(template.format(*(person._asdict())))
    return output

#---------------------------------------------------------------------------------------#
MOVIES = [('Parasite', 132, 'Bong Joon-ho'),
          ('Ford v Ferrari', 152, 'James Mangold'),
          ('The Irishman', 209, 'Martin Scorsese'),
          ('Jojo Rabbit', 108, 'Taika Waititi'),
          ('Joker', 122, 'Todd Phillips'),
          ('Little Women', 135, 'Greta Gerwig'),
          ('Marriage Story', 137, 'Noah Baumbach'),
          ('1917', 119, 'Sam Mendes'),
          ('Once Upon a Time in Hollywood', 161, 'Quentin Tarantino')
          ]

FIELDS = {'name': 0,
          'length': 1,
          'director': 2}
#---------------------------------------------------------------------------------------#
def sort_movies1():
    sort_by = input("Enter sort field (name/length/director): ").strip()
    if sort_by in FIELDS:
        output = []
        template = '{0:30} {1:3} {2:20}'
        for one_movie in sorted(MOVIES, key=operator.itemgetter(FIELDS[sort_by])):
            output.append(template.format(*one_movie))
        return output
    print(f'No such field {sort_by}')
#----------------------------------------------------------------------------------#    
def sort_movies2():
    sort_by = input("Enter sort fields (name/length/director): ").split()
    if all(field_name in FIELDS
           for field_name in sort_by):
        output = []
        template = '{0:30} {1:3} {2:20}'
        for one_movie in sorted(MOVIES, key=operator.itemgetter(*[FIELDS[field_name]
                                                               for field_name in sort_by])):
            output.append(template.format(*one_movie))
        return output
    print(f'No such field {sort_by}')


print(sort_movies2())