def productExceptSelf(nums):
    prefix = 1
    postfix = 1
    product = [1] * len(nums)
    for i in range(len(nums)):
        product[i] = prefix
        prefix *= nums[i]
    for i in reversed(range(0, len(nums))):
        product[i] *= postfix
        postfix *= nums[i]
    return product


if __name__ == '__main__':
    nums = [1, 2, 3, 4]
    print(productExceptSelf(nums))
