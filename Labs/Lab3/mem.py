from functools import wraps

def memo():
    cashe = {}

    def dec(func):
        def wraper(*args):
            key = str(args)
            if key in cashe:
                return cashe[key]
            res = func(*args)
            cashe[key] = res
            return res
        return wraper
    return dec
