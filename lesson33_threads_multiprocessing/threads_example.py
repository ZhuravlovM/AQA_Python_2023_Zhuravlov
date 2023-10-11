import time
import concurrent.futures


def function_example(name):
    print(f'We are in {name} function')
    time.sleep(2)
    print(f'We are exiting {name} function')


with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor:
    executor.map(function_example, range(60))
