def solution(nums):
    answer = 0
    num = len(nums) // 2
    nums = list(set(nums))

    return min(len(nums), num)