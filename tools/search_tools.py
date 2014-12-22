"""
A file implementing searching tools. Code is a mess right now, still under serious work.
"""
# bst split(func, space)


# Class that takes a desired result, a generator representing the search space (or a conditional?), and a next operator
def num_list(generator_of_things_to_check):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(generator_of_things_to_check, func(name))
        return func_wrapper
    return tags_decorator


@num_list("p")
def get_text(name):
    return "Hello "+name

print(get_text("John"))

# Outputs <p>Hello John</p>


def foo(*args):
    for a in args:
        print (a)

foo([i for i in range(10)])

