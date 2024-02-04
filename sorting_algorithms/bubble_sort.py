from convenience.utilities import evaluate_performance, create_random_list

@evaluate_performance
def bubbleSort(numbers_list: list):
    for i in range(len(numbers_list)):
        for j in range(len(numbers_list) - 1 - i):
            if numbers_list[j] > numbers_list[j + 1]:
                numbers_list[j], numbers_list[j + 1] = (
                    numbers_list[j + 1],
                    numbers_list[j],
                )

    return numbers_list

if __name__ == "__main__":
 sorted_list = bubbleSort(create_random_list(min_value=-10, max_value=100, size=30))
 print(sorted_list)
