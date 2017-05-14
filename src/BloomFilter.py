import mmh3
import random
import bitarray
import math


class BloomFilter():
    def __init__(self, max_items, false_positive_rate):
        """
        Initialize the Bloom filter
        max_items:
            the maximum number of possible items in this filter
        false_positive_rate:
            the expected error rate for positive set membership test
        """
        num_of_bit = math.log2(max_items)
        this.bit_array = bitarray()
        this.hash_func = []

    def add(self, item):
        print('added')

    def contains(self, item) -> bool:
        """
        Check if this string is in the element
        """
        rand = random.randint(1, 2)
        print(rand)


filter = BloomFilter()
filter.add('1')
filter.add('1')
filter.add('2')
filter.add('11')
filter.add('122')
filter.test('1')
