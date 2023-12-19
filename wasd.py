def func(f):
    def wrap():
        wrap.counter += 1
        print(wrap.counter)

    wrap.counter = 0
    return wrap


@func
def func2():
    print("Hello World!")


func2()
func2()
func2()
func2()
func2()

del func2


func2 = func
