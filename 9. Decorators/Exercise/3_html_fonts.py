def make_bold(f):
    def wrapper(*args):
        result = f(*args)
        return f'<b>{result}</b>'
    return wrapper

def make_italic(f):
    def wrapper(*args):
        result = f(*args)
        return f'<i>{result}</i>'
    return wrapper

def make_underline(f):
    def wrapper(*args):
        result = f(*args)
        return f'<u>{result}</u>'
    return wrapper

@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))