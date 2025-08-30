from typing import List


def test(f):
    nums1 = [1, 2, 3, 0, 0, 0, 0]
    m = 3
    nums2 = [2, 2, 5, 6]
    n = 4
    f(nums1, m, nums2, n)
    print(nums1)


def test2(f):
    m = 0
    n = 1
    nums1 = [0]
    nums2 = [1]
    f(nums1, m, nums2, n)
    print(nums1)

    ss = [1, 2, 3, 4, 5]
    ss[2:4] = [0]
    print(ss)


@test2
def merge_new(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    to = len(nums1) - 1
    a = m - 1
    b = n - 1
    while a >= 0 and b >= 0:
        if nums1[a] < nums2[b]:
            nums1[to] = nums2[b]
            b -= 1
        else:
            nums1[to] = nums1[a]
            a -= 1
        to -= 1

    if a >= 0:
        print(f"a: {a}, b: {b}, to: {to}")
        # copy first array elements
        while a >= 0:
            nums1[to] = nums1[a]
            a -= 1
            to -= 1
    else:
        print(f"a: {a}, b: {b}, to: {to}")
        while b >= 0:
            nums1[to] = nums2[b]
            to -= 1
            b -= 1

# todo divide logic of moving and assigning(choosing appropriate massive)
