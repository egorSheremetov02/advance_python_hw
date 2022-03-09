from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from datetime import datetime
import multiprocessing as mp
from functools import wraps
import logging
import math

logging.basicConfig(filename='./artifacts/medium.txt', level=logging.DEBUG, filemode='w')


def write_integration_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f'integrating function: {str(func.__name__)} with arguments {str(args)}')
        start = datetime.now()
        result = func(*args, **kwargs)
        duration = datetime.now() - start
        logging.info(f'time: {duration.microseconds} microseconds')
        return result

    return wrapper


def integrate_sequential(args):
    f, a, b, n_iter = args
    acc = 0
    step = (b - a) / n_iter
    for i in range(n_iter):
        acc += f(a + i * step) * step
    return acc


@write_integration_log
def integrate_via_pool_executor(pool_executor, func, l, r, parts_count, fragments_in_part_count):
    part_length = (r - l) / parts_count
    arguments = [(func, l + part_length * i, l + part_length * (i + 1), fragments_in_part_count // parts_count)
                 for i in range(parts_count)]
    with pool_executor(max_workers=parts_count) as pool:
        parts_results = pool.map(integrate_sequential, arguments)
    return sum(parts_results)


if __name__ == '__main__':
    executors = [ProcessPoolExecutor, ThreadPoolExecutor]
    for executor in executors:
        for iters in [10 ** i for i in range(6, 8)]:
            for jobs in range(1, mp.cpu_count() + 1):
                integrate_via_pool_executor(executor, math.sin, 0, math.pi / 2, jobs, iters)
