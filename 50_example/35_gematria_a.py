import string
import json

alpahbet = {"a":1, "b":2, "c":3, "d":4 ,"e": 5,"f":6 ,"g":7 ,
            "h":8, "i":9, "j":10, "k":11, "l":12, "m":13 ,
            "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, 
            "t":20, "u":21, "v":22, "w":23, "x":24, "y":25, "z": 26}


def gematria():
    return { value:index for index, value in enumerate(string.ascii_lowercase,1)}

def read_config(filename):
    return {one_line.split('=')[0]: one_line.split('=')[1].strip()
            for one_line in open(filename)}
    
def read_config1(filename):
    return {one_line.split("=")[0]: int(one_line.split("=")[1])
            for one_line in open(filename) if one_line.split("=")[1].strip().isdigit()}

def get_city_data(filename):
    return {one_city['city']: one_city['population'] for one_city in json.load(open(filename))}

def get_city_data2(filename):
    return {(one_city['city'], one_city['state']): one_city['population'] for one_city in json.load(open(filename))}
    
print(len(get_city_data2("cities.json")))

