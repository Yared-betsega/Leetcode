value = input()
lst = value.split(" ")
m = lst[0]
n =lst[1]
mult = int(m) * int(n)
maxDominoes = mult // 2
print(maxDominoes)
