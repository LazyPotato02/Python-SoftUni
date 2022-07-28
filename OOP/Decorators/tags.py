def tags(tag):
    def decorator(func_ref):
        def wrapper(*args):
            result = func_ref(*args)
            return f'<{tag}>{result}</{tag}>'

        return wrapper

    return decorator


@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))