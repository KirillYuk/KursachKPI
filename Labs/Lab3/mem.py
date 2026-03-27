from functools import wraps

def memo():
    cache = {}

    def decorator(func):
        def wraper(*args):
            key = str(args)
            if key in cache:
                return cache[key]
            res = func(*args)
            cache[key] = res
            return res
        return wraper
    return decorator
