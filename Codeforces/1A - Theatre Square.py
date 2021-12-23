import math
nums= input()
nums = nums.split(" ")
n = int(nums[0])
m = int(nums[1])
a = int(nums[2])
row = math.ceil(n / a)
col = math.ceil(m / a)
rowCover = row * a
colCover = col * a
answer = (rowCover * colCover) / (a * a)
print(int(answer))
