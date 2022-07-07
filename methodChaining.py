def chaining(a):
    result = a
    def wrapper(b=None):
        nonlocal result
        if not b:
            return result
        result += b
        return wrapper
    return wrapper

        


print(chaining(5)(7)())