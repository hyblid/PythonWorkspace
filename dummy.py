def combine_dicts(dict_list):
    combined_dict = {}
    
    for d in dict_list:
        for key, value in d.items():
            if key in combined_dict:
                if isinstance(combined_dict[key], list):
                    combined_dict[key].append(value)
                else:
                    combined_dict[key] = [combined_dict[key], value]
            else:
                combined_dict[key] = value
    
    return combined_dict

# Example usage:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 4, 'c': 5, 'd': 6}
dict3 = {'e': 7}

list_of_dicts = [dict1, dict2, dict3]
result = combine_dicts(list_of_dicts)
print(result)