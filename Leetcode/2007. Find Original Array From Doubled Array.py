changed = [1,2,3,2,4,6,2,4,6,4,8,12]
if changed == [0]*len(changed):
    print([0]*(len(changed)//2))
changed = sorted(changed, reverse=True)
ans = []
for i in changed:
    if i not in ans:
        if i %2==0:
            ans.append(i//2)
        else:
            ans.append(i)
newArr = []
for i in range(len(ans)):
    newArr.append(ans[i]*2)
for i in ans:
    newArr.append(i)
print(ans)
print(newArr)
print(changed)
print(sorted(newArr, reverse=True))
if sorted(newArr, reverse=True) != changed:
    print([])
else:
    print(ans)
