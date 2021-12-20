def sortColors(nums):
    red =[]
    white = []
    blue = []
    for i in nums:
        if i == 0:
            red.append(i)
        elif i == 1:
            white.append(i)
        else:
            blue.append(i)
    nums.clear()
    nums.extend(red)
    nums.extend(white)
    nums.extend(blue)

