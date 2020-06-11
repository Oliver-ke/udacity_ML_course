def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper


@my_decorator
def say_whee():
    print("Whee!")

# Decorator functions are simple functions that wraps another function to modify it state
# above, the say_whee function when executed will behave differently because of the decorator
# with it
# the my_decorator function specifies changes that should be made
# output


"""
  Something is happening before the function is called.
  Whee!
  Something is happening after the function is called.
"""

say_whee()


# with arguments
def do_twice(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
    return wrapper_do_twice


@do_twice
def greet(name):
    print(f"Hello {name}")

# *args and **kwargs is a way of acception any number of argument passed


# returning values
def do_twice_return(func):
    def wrapper_do_twice(*args, **kwargs):
        func(*args, **kwargs)
        return func(*args, **kwargs)
    return wrapper_do_twice


@do_twice_return
def return_greeting(name):
    print("Creating greeting")
    return f"Hi {name}"
