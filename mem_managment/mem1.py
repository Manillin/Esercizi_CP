import tracemalloc


def foo():
    f = [x for x in range(0, 100000000)]


tracemalloc.start()
foo()
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
print("Istananea ", current, " Picco ", peak)
