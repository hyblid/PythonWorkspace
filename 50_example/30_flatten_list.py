import operator

def flatten(list):
    return [val for sublist in list for val in sublist]

def flatten_odd_ints(mylist):
    return [int(str(one_element))
            for one_sublist in mylist
            for one_element in one_sublist
            if str(one_element).strip().isdigit() and int(one_element) % 2 == 1]

def grandchildren_names1(d1):
    return [one_grandchild
            for grandchild_list in d.values()
            for one_grandchild in grandchild_list]
    
def sorted_grandchildren(d):
    grandchildren = [one_grandchild
                     for one_grandchild_list in d.values()
                     for one_grandchild in one_grandchild_list]

    return [one_grandchild['name']
            for one_grandchild in sorted(grandchildren,
                                         key=operator.itemgetter('age'))]

   
d1= {'A':['B', 'C', 'D'], 'E':['F', 'G']}
d_age= {'A':[{"name":'B', "age":12}, 
          {"name":'C', "age":21}, 
          {"name":'D', "age":14}],
     'E':[{"name":'F', "age": 11}, 
          {"name":'G', "age": 17}]}
lst = [["1","2"],["3","4"]]
print(sorted_grandchildren(d_age))