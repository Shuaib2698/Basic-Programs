'''Merge Two Dictionaries ⭐⭐

Given:

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 40}

Merge them.

If a key exists in both dictionaries, add the values.
Expected:

{
    "a": 10,
    "b": 25,
    "c": 45,
    "d": 40
}'''

dict1 = {"a": 10, "b": 20, "c": 30}
dict2 = {"b": 5, "c": 15, "d": 40}

def merge_two_dic(dict1, dict2):
    result = {}

    for keys, values in dict1.items():
        if keys in dict2:
            result[keys] = dict1[keys] + dict2[keys]
        else:
            result[keys] = values

    for keys, values in dict2.items():
        if keys not in dict1:
            result[keys] = values

    return result

print(merge_two_dic(dict1, dict2))