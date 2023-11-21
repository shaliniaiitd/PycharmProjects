# define a list
my_list = [4, 7, 0]

# create an iterator from the list
iterator = iter(my_list)

# get the first element of the iterator
print(next(iterator))  # prints 4

# get the second element of the iterator
print(next(iterator))  # prints 7

# get the third element of the iterator
print(next(iterator))  # prints 0

class PowTwo:
    """Class to implement an iterator
    of powers of two"""

    def __init__(self, max=0):
        self.max = max

    def __iter__(self):
        self.n = 0
        return self

    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration


# create an object
numbers = PowTwo(3)

# create an iterable from the object
i = iter(numbers)

# Using next to get to the next iterator element
print(next(i)) # prints 1
print(next(i)) # prints 2
print(next(i)) # prints 4
print(next(i)) # prints 8
print(next(i)) # raises StopIteration exception


# An ITERABLE is:
#
# anything that can be looped over (i.e. you can loop over a string or file) or
# anything that can appear on the right-side of a for-loop: for x in iterable: ... or
# anything you can call with iter() that will return an ITERATOR: iter(obj) or
# an object that defines __iter__ that returns a fresh ITERATOR, or it may have a __getitem__ method suitable for indexed lookup.
# An ITERATOR is an object:
#
# with state that remembers where it is during iteration,
# with a __next__ method that:
# returns the next value in the iteration
# updates the state to point at the next value
# signals when it is done by raising StopIteration
# and that is self-iterable (meaning that it has an __iter__ method that returns self).
# Notes:
#
# The __next__ method in Python 3 is spelt next in Python 2, and
# The builtin function next() calls that method on the object passed to it.
# For example:
#
# >>> s = 'cat'      # s is an ITERABLE
#                    # s is a str object that is immutable
#                    # s has no state
#                    # s has a __getitem__() method
#
# >>> t = iter(s)    # t is an ITERATOR
#                    # t has state (it starts by pointing at the "c"
#                    # t has a next() method and an __iter__() method
#
# >>> next(t)        # the next() function returns the next value and advances the state
# 'c'
# >>> next(t)        # the next() function returns the next value and advances
# 'a'
# >>> next(t)        # the next() function returns the next value and advances
# 't'
# >>> next(t)        # next() raises StopIteration to signal that iteration is complete
# Traceback (most recent call last):
# ...
# StopIteration
#
# >>> iter(t) is t   # the iterator is self-iterable