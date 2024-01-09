#  How can you pick a random item from a list or tuple?
import random

tuple_ = tuple(i for i in range(11))
list_ = [i*i for i in range(19)]

print(random.choice(tuple_))
print(random.choice(list_))
