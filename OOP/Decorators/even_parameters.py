def even_parameters(func_ref):
    def wrapper(*args):
        for arg in args:
            if not isinstance(arg, int) or arg % 2 != 0:
                return "Please use only even numbers!"
        return func_ref(*args)
    return wrapper

