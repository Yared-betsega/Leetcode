def sortColors(nums):
    red =[]
    white = []
    blue = []
    ans = []
    for i in nums:
        if i == 0:
            red.append(i)
        elif i == 1:
            white.append(i)
        else:
            blue.append(i)
    ans.extend(red)
    ans.extend(white)
    ans.extend(blue)
    return ans
