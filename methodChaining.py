def chaining(a):
    def wrapper(b=None):
        if not b:
            return wrapper.result
        wrapper.result += b
        return wrapper
    wrapper.result = a
    return wrapper

        


print(chaining(5)(7)())