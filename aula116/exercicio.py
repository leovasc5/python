nums = [10, 6, 9, 42, 14]
target = 8

soma_indices = 0
for i in nums:
    soma_indices += nums.index(i)

res = soma_indices + target
print(res)