def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        posAndSpeed = {}
        for i in range(len(position)):
            posAndSpeed[position[i]] = speed[i]
        posAndSpeed = list(posAndSpeed.items())
        posAndSpeed = sorted(posAndSpeed, reverse=True)
        monotonicStack = []

        for p, s in posAndSpeed:
            duration = (target - p) / s
            monotonicStack.append(duration)
            if len(monotonicStack) >= 2:
                if monotonicStack[-1] <= monotonicStack[-2]:
                    monotonicStack.pop()

        return len(monotonicStack)
