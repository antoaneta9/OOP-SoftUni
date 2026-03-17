def logged(function):
    def wrapper(*args):
        result = function(*args)
        args_str = ", ".join(str(x) for x in args)
        return f"you called {function.__name__}({args_str})\nit returned {result}"
    return wrapper
@logged
def func(*args):
    return 3 + len(args)
print(func(4,4,4))
