def decorator(f):
    def added_func():
        print("\nadded functionality")
        f()
    return added_func


@decorator
def normal_function():
    print("Normal function output\n")


normal_function()
