def repeat_me(count=1):

    def wrapper(func):

        def inner_wrapper(*args, **kwargs):
            for x in range(count):
                func(*args, **kwargs)

        return inner_wrapper

    return wrapper


@repeat_me(count=2)
def example(text):
    print(text)


example('print me')
