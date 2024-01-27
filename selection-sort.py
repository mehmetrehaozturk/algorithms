import random

def selectionSort(numbers_list : list):
    for i in range(len(numbers_list)):
        min_index = i
        for j in range(i+1, len(numbers_list)):
            if numbers_list[j] < numbers_list[min_index]:
                min_index = j

        numbers_list[i], numbers_list[min_index] = numbers_list[min_index], numbers_list[i]

    print(numbers_list) 

def create_random_list(min_value: int, max_value: int, size: int):

    random_numbers_list = [random.randint(min_value, max_value) for _ in range(size)]

    return random_numbers_list


selectionSort(numbers_list= create_random_list(min_value=-10, max_value=10, size=10))