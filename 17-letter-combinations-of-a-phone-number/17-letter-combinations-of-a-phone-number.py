class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        nums_to_letter = {
                            '2': ['a', 'b', 'c'],
                            '3': ['d', 'e', 'f'],
                            '4': ['g', 'h', 'i'],
                            '5': ['j', 'k', 'l'],
                            '6': ['m', 'n', 'o'],
                            '7': ['p', 'q', 'r', 's'],
                            '8': ['t', 'u', 'v'],
                            '9': ['w', 'x', 'y', 'z']
                        }

        result = [] 
        def dfs(i, path):
            for node in nums_to_letter[digits[i]]:
                path.append(node)
                if i + 1 < len(digits):
                    dfs(i+1, path)
                else:
                    result.append(''.join(path))
                path.pop()
            
        if len(digits) > 0:
            dfs(0, [])
        return result
    
# time complexity = O(4**n)
# space complexity = O(1)