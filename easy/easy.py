import threading
import multiprocessing
from datetime import datetime
from functools import wraps
from itertools import repeat

argument_size = 150000


def fib(n):
    fs = []
    a, b = 0, 1
    for i in range(n):
        fs.append(a)
        a, b = b, a + b
    return fs


def measure_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = datetime.now()
        func(*args, **kwargs)
        return datetime.now() - start

    return wrapper


@measure_time
def sequential_executor(repetitions: int, func, args):
    for i in range(repetitions):
        func(*args)


@measure_time
def thread_executor(repetitions: int, func, args):
    thread_pool = [threading.Thread(target=func, args=args) for _ in range(repetitions)]
    for thread in thread_pool:
        thread.start()
    for thread in thread_pool:
        thread.join()


@measure_time
def process_executor(repetitions: int, func, args):
    with multiprocessing.Pool(repetitions) as proc_pool:
        proc_pool.map(func, repeat(*args, times=repetitions))


def main():
    executors = [
        (sequential_executor, 'sequential'),
        (process_executor, 'multiprocessing'),
        (thread_executor, 'multithreading'),
    ]
    with open('./artifacts/easy.txt', 'w') as file:
        for executor, name in executors:
            time_taken = executor(10, fib, args=(argument_size,))
            file.write(name + ' execution, time taken: ' + str(time_taken.microseconds) + ' microseconds\n')


if __name__ == '__main__':
    main()
