import json


numbers = {}


def max_repeated_number_from_array(array):
    for item in array:
        if hasattr(item, "__len__"):
            max_repeated_number_from_array(item)
        else:
            if numbers.get(item):
                numbers[item] += 1
            else:
                numbers[item] = 1
    return max(numbers, key=numbers.get)


array = []
with open("input.txt", "r") as file:
    array = json.load(file)

with open("output.txt", "w") as file:
    file.write(str(max_repeated_number_from_array(array)))
