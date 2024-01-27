import random

def bubbleSort(numbers_list : list):
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list) - 1 - i):
            if numbers_list[j] > numbers_list[j+1]:
                numbers_list[j], numbers_list[j+1] = numbers_list[j+1], numbers_list[j]

    print(numbers_list) 

def create_random_list(min_value: int, max_value: int, size: int):

    random_numbers_list = [random.randint(min_value, max_value) for _ in range(size)]

    return random_numbers_list


bubbleSort(numbers_list= create_random_list(min_value=-10, max_value=0, size=9))