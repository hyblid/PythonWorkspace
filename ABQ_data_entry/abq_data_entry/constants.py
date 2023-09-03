from enum import Enum, auto
'''
assign the numerical values (INTEGER) automatically to the class attributes by using this method
[<FieldTypes.string: 1>, <FieldTypes.string_list: 2>, <FieldTypes.short_string_list: 3>,
<FieldTypes.iso_date_string: 4>, <FieldTypes.long_string: 5>, <FieldTypes.decimal: 6>, 
<FieldTypes.integer: 7>, <FieldTypes.boolean: 8>]

print(FielTypes.string.value)
'''

class FieldTypes(Enum):
  string = auto()
  string_list = auto()
  short_string_list = auto()
  iso_date_string = auto()
  long_string = auto()
  decimal = auto()
  integer = auto()
  boolean = auto()
  
  