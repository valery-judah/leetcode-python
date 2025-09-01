# Solution Patterns

## Hash Map for Complements

**Use when**: You need to find two numbers in a collection that sum up to a target value.
**Idea**: Use a hash map to store the numbers you've seen and their indices. For each number, calculate its complement (target - number) and check if the complement is already in the hash map. This allows you to find a solution in a single pass.
**Template**:

```python
def find_sum_indices(nums: list[int], target: int) -> list[int]:
    num_map = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
    return []
```

**Pitfalls**: This approach assumes that each input has exactly one solution and that you cannot use the same element twice. If these constraints are different, the template will need to be modified.
