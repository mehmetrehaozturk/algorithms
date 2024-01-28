from convenience.utilities import evaluate_performance, create_random_list

@evaluate_performance
def selectionSort(numbers_list: list):
    for i in range(len(numbers_list)):
        min_index = i
        for j in range(i + 1, len(numbers_list)):
            if numbers_list[j] < numbers_list[min_index]:
                min_index = j

        numbers_list[i], numbers_list[min_index] = (
            numbers_list[min_index],
            numbers_list[i],
       )

    return numbers_list
    
if __name__ == "__main__":
 selectionSort(create_random_list(min_value=-10, max_value=100, size=30))