def unique_elements(input_list):
    """Возвращает список уникальных элементов"""
    return list(set(input_list))

print(unique_elements([1, 2, 2, 3, 4, 4, 4])) 



def merge_dicts(dict1, dict2):
    """Объединяет два словаря, суммируя значения при совпадении ключей"""
    result = dict1.copy()
    for key, value in dict2.items():
        result[key] = result.get(key, 0) + value
    return result

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
print(merge_dicts(dict1, dict2)) 




def count_frequency(input_list):
    """Возвращает словарь с частотой каждого элемента"""
    frequency = {}
    for item in input_list:
        frequency[item] = frequency.get(item, 0) + 1
    return frequency

print(count_frequency(['a', 'b', 'a', 'c', 'b', 'a'])) 