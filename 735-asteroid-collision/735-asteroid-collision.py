class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if not stack:
                stack.append(ast)
            elif ast < 0:
                destroyed = False
                while stack and stack[-1] >= 0:
                    if abs(ast) > stack[-1]:
                        stack.pop()
                    elif abs(ast) == stack[-1]:
                        stack.pop()
                        destroyed = True
                        break
                    else:
                        destroyed = True
                        break
                if not destroyed:
                    stack.append(ast)
                
            else:
                stack.append(ast)
            
        return stack