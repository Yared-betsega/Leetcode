class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        def make_set(letter):
            parent[letter] = letter
            
        def find_set(letter):
            if parent[letter] == letter:
                return letter
            parent[letter] = find_set(parent[letter])
            return parent[letter]
        
        def union_sets(letter1, letter2):
            parent1 = find_set(letter1)
            parent2 = find_set(letter2)
            if parent1 != parent2:
                if size[parent1] < size[parent2]:
                    parent1, parent2 = parent2, parent1
                
                parent[parent2] = parent1
                size[parent1] += size[parent2]
        
        parent, size = {}, defaultdict(int)
        for equation in equations:
            if equation[0] not in parent:
                make_set(equation[0])
            if equation[-1] not in parent:
                make_set(equation[-1])
            if equation[1] == "=":
                union_sets(equation[0], equation[-1])                
        
        for equation in equations:
            if equation[1] == "!":
                if find_set(equation[0]) == find_set(equation[-1]):
                    return False
        return True