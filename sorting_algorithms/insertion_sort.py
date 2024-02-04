from convenience.utilities import evaluate_performance, create_random_list

@evaluate_performance
def insertionSort(numbers_list: list):
    for i in range(1, len(numbers_list)):
        key = numbers_list[i]
        j = i - 1

        while key < numbers_list[j] and j >= 0:
            numbers_list[j + 1] = numbers_list[j]
            j -= 1

        numbers_list[j + 1] = key

    return numbers_list


if __name__ == "__main__":
 sorted_list = insertionSort(create_random_list(min_value=-10, max_value=100, size=30))
 print(sorted_list)