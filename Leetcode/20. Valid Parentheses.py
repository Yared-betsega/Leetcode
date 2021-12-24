def isValid(self, s: str) -> bool:
        par = {'(': ')', '[': ']', '{': '}'}
        lst = []
        for i in s:
            if i in par.keys():
                lst.append(i)
            else:
                if len(lst) == 0:
                    return False
                elif i == par[lst[-1]]:
                    lst.pop(-1)
                else:
                    return False
        if len(lst) == 0:
            return True
        else:
            return False
