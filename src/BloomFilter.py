import mmh3
import random
import bitarray
import math


class BloomFilter():
    def __init__(self, max_items, expected_false_positive_rate):
        """
        Initialize the Bloom filter
        @max_items: the maximum number of possible items in this filter
        @expected_false_positive_rate: "maybe in the list" error rate, 0.99 = 99%
        """
        self.num_of_bit = math.log(max_items)
        # self.bit_array = bitarray(self.num_of_bit)
        self.hash_func = []  # todo: add more hash-function to this

    def add(self, item):
        print('added')

    def contains(self, item):
        """
        Check if this string is in the element
        """
        rand = random.randint(1, 2)
        print(rand)


filter = BloomFilter(2, 0.99)
filter.add('1')
filter.add('1')
filter.add('2')
filter.add('11')
filter.add('122')
filter.add('1')
