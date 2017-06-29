# find intersection between intervals


class FindOverlapping:
    @staticmethod
    def solve(this, that):
        # sort to ensure earlier intervals appear first
        if this[0] > that[0]:
            this, that = that, this
        # no overlap
        if that[0] > this[1]:
            return []
        # totally cover
        if this[0] <= that[0] and that[1] <= this[1]:
            return [that[0], that[1]]
        # intersect
        if this[0] <= that[0] and this[1] <= that[1]:
            return [that[0], this[1]]


print(FindOverlapping.solve([1, 2], [1, 2]))  # --> [1,2] 
print(FindOverlapping.solve([1, 5], [6, 10]))  # --> []
print(FindOverlapping.solve([1, 5], [0, 10]))  # --> [1, 5]
print(FindOverlapping.solve([1, 5], [3, 10]))  # --> [3, 5]
