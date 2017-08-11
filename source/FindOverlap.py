# find intersection between intervals


class FindOverlapping:
    @staticmethod
    def Solve(smaller, larger):
        # sort to ensure earlier intervals appear first
        if smaller[0] > larger[0]:
            temp = smaller
            smaller = larger
            larger = temp
        # no overlap
        if larger[0] > smaller[1]:
            return []
        # totally cover
        if smaller[0] <= larger[0] and larger[0] <= smaller[1] \
           and smaller[0] <= larger[1] and larger[1] <= smaller[1]:
            return [larger[0], larger[1]]
        # intersect
        if smaller[0] <= larger[0] and larger[0] <= smaller[1] \
           and larger[0] <= smaller[1] and smaller[1] <= larger[1]:
            return [larger[0], smaller[1]]


print(FindOverlapping.Solve([1, 5], [6, 10]))  # --> []
print(FindOverlapping.Solve([1, 5], [0, 10]))  # --> [1, 5]
print(FindOverlapping.Solve([1, 5], [3, 10]))  # --> [3, 5]
