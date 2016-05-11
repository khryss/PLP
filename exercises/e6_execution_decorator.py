import time


def execution_decorator(threshold = 0.05):
    def dummy_decorator(orig_func):
        def new_func(*args, **kwargs):
            start_time = time.time()
            orig_func(*args, **kwargs)
            execution_time = time.time() - start_time
            print orig_func.__name__ + "() execution time: " + str(execution_time)
            if execution_time > threshold:
                print "Funciton was slow!"
        return new_func
    return dummy_decorator


@execution_decorator(threshold = 0.02)
def function(*arg, **kwargs):
    for i in range(1000):
        for j in range(1000):
            pass


if __name__ == "__main__":
    function()
