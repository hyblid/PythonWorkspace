
import sys
 
sys.path.append('../PythonWorkspace')
from freedonia import calculate_tax
from freedonia import tax_brackets
from freedonia import analyze_string
from freedonia import from_keys

brackets = [{'start': 0, 'end': 1000, 'tax': 0},
            {'start': 1000, 'end': 10000, 'tax': .1},
            {'start': 10000, 'end': 20000, 'tax': .2},
            {'start': 20000, 'end': 999999999999, 'tax': .5}]

def char_to_int(ch):
    return ord(ch) 

print(from_keys("abc", char_to_int))
