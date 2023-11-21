from collections.abc import Iterator, Iterable
from types import GeneratorType
print(issubclass(GeneratorType, Iterator)) #True
print(issubclass(Iterator, Iterable)) #True

#Thus generator is a type of iterator. All generators are iterators.
# They provide with an iterator without __iter__ and __next__ methods.
# They use yield in place of return and return one value at atime
# The control comes back to next line after yield.
# Usage : For e.g fetching 1000 rows from database to work on each row one by one
# No need to store al 1000 results in memory.
# So, generators are memory efficient.

def my_generator(n):

    # initialize counter
    value = 0

    # loop until counter is less than n
    while value < n:

        # produce the current value of the counter
        yield value

        # increment the counter
        value += 1

# iterate over the generator object produced by my_generator
for value in my_generator(3):

    # print each value produced by generator
    print(value)
