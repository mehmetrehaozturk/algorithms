import random
import time
import traceback


    
def create_random_list(min_value: int = -100, max_value: int = 100, size: int = 20):

    random_numbers_list = [random.randint(min_value, max_value) for _ in range(size)]

    return random_numbers_list


def evaluate_performance(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()     
        
        try:
            result = func(*args, **kwargs)
        except Exception as e:
            traceback.print_exc(e)
            result = None
        
        end_time = time.time()   
        execution_time = end_time - start_time

        print(f"Execution Time: {execution_time} seconds")
    
        return result
    
    return wrapper
