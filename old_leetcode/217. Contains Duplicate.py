import unittest

# Assuming the functions are in a file named 'contains_duplicate_217.py'
# in a 'leetcode' directory relative to the test file, or adjust the import path as needed.
# For this example, let's redefine the functions here for clarity,
# but in a real scenario, you would import them.


def contains_duplicate_brutforce(nums):
    for i, n in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if n == nums[j]:
                return True
    return False


def contains_duplicate_set(nums):
    seen_elements = set()
    for n in nums:
        if n in seen_elements:
            return True
        else:
            seen_elements.add(n)
    return False


def contains_duplicates_sorting_approach(nums):
    # Important: This function modifies the input list.
    nums_copy = nums[:]  # Create a copy to avoid modifying the original list passed to the test
    nums_copy.sort()
    return any(nums_copy[i] == nums_copy[i - 1] for i in range(1, len(nums_copy)))


class TestContainsDuplicate(unittest.TestCase):

    def test_bruteforce(self):
        print("\nTesting: contains_duplicate_brutforce")
        assert contains_duplicate_brutforce([1, 2, 3, 1])
        assert not contains_duplicate_brutforce([1, 2, 3, 4])
        assert contains_duplicate_brutforce([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        assert not contains_duplicate_brutforce([])
        assert not contains_duplicate_brutforce([5])
        assert contains_duplicate_brutforce([0, 0])
        assert contains_duplicate_brutforce([-1, -2, -1])

    def test_set(self):
        print("\nTesting: contains_duplicate_set")
        assert contains_duplicate_set([1, 2, 3, 1])
        assert not contains_duplicate_set([1, 2, 3, 4])
        assert contains_duplicate_set([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        assert not contains_duplicate_set([])
        assert not contains_duplicate_set([5])
        assert contains_duplicate_set([0, 0])
        assert contains_duplicate_set([-1, -2, -1])

    def test_sorting(self):
        print("\nTesting: contains_duplicates_sorting_approach")
        # Pass copies because the function sorts the list in place
        assert contains_duplicates_sorting_approach([1, 2, 3, 1])
        assert not contains_duplicates_sorting_approach([1, 2, 3, 4])
        assert contains_duplicates_sorting_approach([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
        assert not contains_duplicates_sorting_approach([])
        assert not contains_duplicates_sorting_approach([5])
        assert contains_duplicates_sorting_approach([0, 0])
        assert contains_duplicates_sorting_approach([-1, -2, -1])


# This allows running the tests from the command line
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
