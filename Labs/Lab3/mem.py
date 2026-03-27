from functools import wraps

def memo():
    cache = {}

    def decorator(func):
        @wraps(func)

        def wraper(*args, **kwards):
            key = str(args) + str(kwards)

            if key in cache:
                return cache[key]
            
            res = func(*args, **kwards)
            cache[key] = res

            return res
        return wraper
    return decorator
