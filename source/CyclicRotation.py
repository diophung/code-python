# Rotate an array k-th time. For e.g:
# rotate([1,2,3], 2) -> [3,2,1]
# rotate([1,2,3,4,5], -1) -> [2,3,4,5,1]

#
# Algorithm 1:
#    create new array of size N
#        copy N(0,k) to New(k, N)
#        copy N(k,N) to New(0,N-k)
#    return array
#
# Space complexity: O(N)
# Time complexity: O(N)


class CyclicRotation:
    @staticmethod
    def rotate_extra_lists(arr: list, k: int) -> list:
        n = len(arr)
        k %= n
        pivot = n - k

        slice_left = arr[0:pivot]
        slice_right = arr[pivot:n]
        rotated_array = slice_right + slice_left
        return rotated_array


#
# Algorithm 2:
#    create output array with size n
#    for item i-th in array
#        copy to index (i + k) % n in output array
#    return output array
#
# Space complexity: O(N)
# Time complexity: O(N)
    @staticmethod
    def rotate_extra_array(arr: list, k: int) -> list:
        n = len(arr)
        rotated_array = [0] * n
        k %= n
        for i in range(n):
            rotated_array[(i + k) % n] = arr[i]
        return rotated_array


numbers = [1, 2, 3]
# expect [3,2,1]
print(CyclicRotation.rotate_extra_lists(numbers, 1))
print(CyclicRotation.rotate_extra_array(numbers, 1))
print(CyclicRotation.rotate_extra_lists(numbers, -1))
print(CyclicRotation.rotate_extra_array(numbers, -1))

numbers = [1, 2, 3, 4, 5]
# expect [4,5,1,2,3]
print(CyclicRotation.rotate_extra_array(numbers, 2))
print(CyclicRotation.rotate_extra_array(numbers, 2))
