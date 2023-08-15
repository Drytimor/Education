"""
input: nums = [2,7,11,15]
target = 9
output: [0,1]
Explanation: nums[0] = nums[1] == target
"""
"""
def twoSum(num: list, target: int):
    for i in range(len(num)):
        for j in range(i+1, len(num)):
            if num[j] == target - num[i]:
                return [i, j]

num = [2, 11, 7, 15]
target = 9
"""
"""
def twoSum(num: list, target: int):
    hashmap = {}
    for i in range(len(num)):
        hashmap[num[i]] = i
    print(hashmap)
    for i in range(len(num)):
        complement = target - num[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]]


num = [11, 7, 15, 2]
target = 9

print(twoSum(num, target))
"""
"""
Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
"""
#
# roman = {
#     'I': 1,
#     'V': 5,
#     'X': 10,
#     'L': 50,
#     'C': 100,
#     'D': 500,
#     'M': 1000,
# }
#
# def roman_too_int(s: str):
#     res = 0
#     for i, v in enumerate(s):
#         if roman[v]
#
#
# s = 'MCMXCIV'
# a = 'LVIII'
# print(roman_too_int(a))



