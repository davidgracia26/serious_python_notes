import multiprocessing
import random


def compute(n):
    return sum([random.randint(1, 100) for i in range(1_000_000)])


# Start 8 workers
pool = multiprocessing.Pool(processes=8)
print("Results: %s" % pool.map(compute, range(8)))