

def logged(func):
    def wrapper(*args, **kwargs):
        f = func(*args)
        return f"you called {func.__name__}{args}\nit returned {f}"

    return wrapper

